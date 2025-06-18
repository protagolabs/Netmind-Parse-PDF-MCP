import json
import os
import sys
from typing import Literal
from netmind import AsyncNetMind
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("parse-pdf")
NETMIND_API_TOKEN = os.environ.get("NETMIND_API_TOKEN")
NETMIND_BASE_URL = os.environ.get("NETMIND_BASE_URL", "https://api.netmind.ai")
client = AsyncNetMind(api_key=NETMIND_API_TOKEN, base_url=NETMIND_BASE_URL)


@mcp.tool()
async def parse_pdf(source: str, format: Literal["json", "markdown"] = "json"):
    """
    Parses a PDF file and returns the extracted content in the specified format.

    The function supports both local file paths and remote URLs as input sources. It extracts
    the content from the PDF and formats it either as structured JSON or as a Markdown string.

    :param source: The source of the PDF file to be parsed.
        - If it is a string starting with "http://" or "https://", it will be treated as a remote URL.
        - Otherwise, it will be treated as a local file path (absolute path recommended, e.g. "/Users/yourname/file.pdf").
    :param format: The desired format for the parsed output. Supports:
        - "json": Returns the extracted content as a dictionary.
        - "markdown": Returns the extracted content as a Markdown-formatted string.
    :return: The extracted content in the specified format (JSON dictionary or Markdown string).
    """
    if format not in ["json", "markdown"]:
        raise ValueError(f"Unsupported output format: {format}")

    res = await client.parse_pro.parse(
        source=source,
        format=format,
    )
    if not isinstance(res, str):
        res = json.dumps(res, ensure_ascii=False)
    return res


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
