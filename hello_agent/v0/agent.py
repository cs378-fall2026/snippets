import asyncio
from claude_agent_sdk import query, ResultMessage

# query() returns an async iterator
async def main():
    async for message in query(prompt="Hello World"):
        if isinstance(message, ResultMessage):
            print(message.result)

asyncio.run(main()) 