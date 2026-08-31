# Adds hooks write_log and log_attempt 
# Implements move_file tool with helper function deny
import asyncio, json
from datetime import datetime
from pathlib import Path
from claude_agent_sdk import (
    query, ClaudeAgentOptions,
    AssistantMessage, UserMessage, ResultMessage,
    TextBlock, ToolUseBlock, ToolResultBlock, tool,
    create_sdk_mcp_server, HookMatcher
)

PROMPT="""
You are a folder cleanup agent. What files do I currently have in my folder? Group them by what they're about.
You can list files, read them, and create subfolders. You can also move files into subfolders, but you can't rename or delete anything.
Ask for permission to create the subfolders or move the files into them.
"""

CWD = Path.cwd().resolve()

LOG_PATH = CWD / "folder_cleanup_agent.log"
WATCHED = "mcp__folder__(make_folder)"


# hook functions

def write_log(kind: str, data: dict):
    line = {"time": datetime.now().isoformat(timespec="seconds"), "kind": kind, **data}
    with LOG_PATH.open("a") as f:
        f.write(json.dumps(line) + "\n")

async def log_attempt(input_data, tool_use_id, context):
    """Runs before the tool. Records what the agent asked for."""
    try:
        write_log("attempted", {
            "id": tool_use_id,
            "tool": input_data["tool_name"],
            "args": input_data["tool_input"],
        })
    except Exception as e:
        print(f"[log error] {e}")
    return {}   

async def log_outcome(input_data, tool_use_id, context):
    """Runs after the tool. Records what actually happened."""
    try:
        write_log("finished", {
            "id": tool_use_id,
            "tool": input_data["tool_name"],
            "args": input_data["tool_input"],
            "response": str(input_data.get("tool_response"))[:300],
        })
    except Exception as e:
        print(f"[log error] {e}")
    return {}


# tool functions

@tool("list_files", "List files in the current folder", {})
async def list_files(args):
    
    files = []
    
    for f in CWD.iterdir():
        if (f.is_file() and f.suffix.lower() != ".py" and f.name not in (".gitignore", ".DS_Store")):
            files.append(f.name)
            
    files = sorted(files)
    return {"content": [{"type": "text", "text": "\n".join(files)}]}


def resolve_in_cwd(name: str) -> Path | None:
    """Resolve name under CWD, or return None if it escapes."""
    if not name or not name.strip():
        return None
    target = (CWD / name).resolve()
    if target CWD not in target.parents:
        return None
    return target
    

@tool("make_folder", "Make a subfolder in the current folder", {"folder_name": str})
async def make_folder(args):
    folder_path = resolve_in_cwd(args["folder_name"])
    if folder_path is None:
        return {
            "content": [{"type": "text",
                         "text": f"DENIED: '{args['folder_name']}' is outside the folder."}],
            "isError": True,
        }
    folder_path.mkdir(parents=True, exist_ok=True)
    return {"content": [{"type": "text", "text": f"Created {folder_path.name}/"}]}    


def deny(reason: str):
    return {"content": [{"type": "text", "text": f"DENIED: {reason}"}], "isError": True}

# TO DO: Implement the move_file tool

folder_server = create_sdk_mcp_server(
    name="folder",
    version="1.0.0",
    tools=[list_files, make_folder], 
)

async def main():
    options = ClaudeAgentOptions(
        tools=["Read", "Grep"],
        mcp_servers={"folder": folder_server},
        allowed_tools=["mcp__folder__list_files", "mcp__folder__make_folder", "Read", "Grep"],
        disallowed_tools=["Read(.env)", "Read(*.pem)", "Read(*.key)", "Read(folder_cleanup_agent.log)"],
        hooks={"PreToolUse":  [HookMatcher(matcher=WATCHED, hooks=[log_attempt])],
               "PostToolUse": [HookMatcher(matcher=WATCHED, hooks=[log_outcome])],},
        setting_sources=[],
        max_turns=10,
    )
    async for message in query(prompt=PROMPT, options=options):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, ToolUseBlock):
                    print(f"[tool_use] {block.name}({block.input})")

        elif isinstance(message, UserMessage):
            if isinstance(message.content, list):
                for block in message.content:
                    if isinstance(block, ToolResultBlock):
                        print(f"[tool_result] {str(block.content)[:200]}")

        elif isinstance(message, ResultMessage):
            print(f"\n[result] {message.result}")
            
asyncio.run(main())