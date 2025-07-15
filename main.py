import asyncio
from mirascope.mcp.client import stdio_client
from mcp.client.stdio import StdioServerParameters
from mirascope.core import openai
from dotenv import load_dotenv

load_dotenv()
import os


server_params = StdioServerParameters(
    command="python",
    args=["/Users/charan/Desktop/MCP/server.py"],  # update if needed
)

async def main():
    async with stdio_client(server_params) as client:
        print("✅ Connected to MCP server.")
        
        tools = await client.list_tools()

        @openai.call("gpt-4o", tools=tools)
        def chat(prompt: str) -> str:
            return prompt

        while True:
            user_input = input("\n💬 Enter a message (or 'q' to quit): ")
            if user_input.lower() == "q":
                break

            result = chat(user_input)

            if result.tool:
                print(f"🔧 Calling tool: {type(result.tool).__name__}")
                tool_result = await result.tool.call()
                if isinstance(tool_result, list):
                   print("✅ Tool Result:\n" + "\n".join(tool_result))
                else:
                    print(f"✅ Tool Result:\n{tool_result}")
            else:
                print(f"🧠 LLM Response:\n{result.content}")

if __name__ == "__main__":
    asyncio.run(main())
