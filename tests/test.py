import json

from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp import ClientSession
import asyncio


server = StdioServerParameters(
    command='uvx',
    args=['netmind-parse-pdf-mcp'],
    env={
        "NETMIND_API_TOKEN": "your_netmind_api_token"
    }
)


async def main():
    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            response = await session.list_tools()
            tools = [dict(t) for t in response.tools]
            print(json.dumps(tools, indent=4, ensure_ascii=False))
            res = await session.call_tool(
                'parse_pdf',
                {
                    'url': 'https://netmind-public-files.s3.us-west-2.amazonaws.com/tmp/output.pdf',
                    'format': 'json'
                }
            )
            print(res)
            res = await session.call_tool(
                'parse_pdf',
                {
                    'url': 'https://netmind-public-files.s3.us-west-2.amazonaws.com/tmp/output.pdf',
                    'format': 'markdown'
                }
            )
            print(res)


if __name__ == "__main__":
    asyncio.run(main())
