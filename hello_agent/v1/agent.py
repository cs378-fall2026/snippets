import asyncio
from claude_agent_sdk import (
    query, ClaudeAgentOptions,
    AssistantMessage, UserMessage, ResultMessage,
    TextBlock, ToolUseBlock, ToolResultBlock,
)

PROMPT="You are a folder cleanup agent. What files do I currently have in my folder?"

async def main():
    options = ClaudeAgentOptions(
        tools=[],
        setting_sources=[],
        max_turns=1,
    )
    async for message in query(prompt=PROMPT, options=options):
        
        # TO DO: AssistantMessage
        # TO DO: UserMessage
        
        if isinstance(message, ResultMessage):
            print(f"\n[result] {message.result}")
            
asyncio.run(main())