import os
import sys
import httpx
from typing import Literal
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("parse-pdf")
NETMIND_API_TOKEN = os.getenv("NETMIND_API_TOKEN")
API_URL = "https://api.netmind.ai/inference-api/agent/v1/parse-pdf"


@mcp.tool(description="Parse PDF files from a given URL and extract content in JSON or Markdown format. ")
async def parse_pdf(url: str, format: Literal["json", "markdown"] = "json"):
    """
    Parses a PDF file and returns the extracted content in the specified format.

    :param url: A file url (string) pointing to a PDF file accessible via HTTP(S).
    :param format: The desired format for the parsed output. Supports:
        - "json": Returns the extracted content as a dictionary.
        - "markdown": Returns the extracted content as a Markdown-formatted string.
    :return: The extracted content in the specified format (JSON dictionary or Markdown string).
    """
    if format not in ["json", "markdown"]:
        raise ValueError(f"Unsupported output format: {format}")

    payload = {'url': url, 'format': format}
    headers = {"Authorization": f"Bearer {NETMIND_API_TOKEN}"}

    async with httpx.AsyncClient() as client:
        response = await client.post(API_URL, json=payload, headers=headers, timeout=5 * 60)

    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code} - {response.text}")
    return response.text


def main():
    if not NETMIND_API_TOKEN:
        print(
            "Error: NETMIND_API_TOKEN environment variable is required",
            file=sys.stderr,
        )
        sys.exit(1)
    mcp.run(transport='stdio')


if __name__ == "__main__":
    main()
