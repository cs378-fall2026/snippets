# Adds custom tool make_folder and resolve_in_cwd helper function
import asyncio
from pathlib import Path
from claude_agent_sdk import (
    query, ClaudeAgentOptions,
    AssistantMessage, UserMessage, ResultMessage,
    TextBlock, ToolUseBlock, ToolResultBlock, tool,
    create_sdk_mcp_server
)

PROMPT="""
You are a folder cleanup agent. What files do I currently have in my folder? Group them by what they're about.
You can list files, read them, and create subfolders. You cannot move, rename, or delete anything.
Don't ask for permission to create the folders.
"""

CWD = Path.cwd().resolve()

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
    if CWD not in target.parents:
        return None
    return target
    

# TO DO: implement make_folder tool

folder_server = create_sdk_mcp_server(
    name="folder",
    version="1.0.0",
    tools=[list_files], 
)

async def main():
    options = ClaudeAgentOptions(
        tools=["Read", "Grep"],
        mcp_servers={"folder": folder_server},
        allowed_tools=["mcp__folder__list_files", "Read", "Grep"],
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