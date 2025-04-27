# parse-pdf-mcp

A Model Context Protocol (MCP) server that parses PDF files from a given URL into structured formats using
[netmind.ai](https://netmind.ai).

## Components

### Tools

- parse_pdf: Parse PDF files from a given URL and extract content in JSON or Markdown format.
    - url: required: A file url (string) pointing to a PDF file accessible via HTTP(S)
    - format: the desired format for the parsed output. Supports: "json", "markdown"
    - Returns the extracted content in the specified format (JSON dictionary or Markdown string).

## Installation

### Requires [UV](https://github.com/astral-sh/uv) (Fast Python package and project manager)

If uv isn't installed.

```bash
# Using Homebrew on macOS
brew install uv
```

or

```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Environment Variables

You can obtain an API key from [Netmind](https://www.netmind.ai/user/apiToken)

- `NETMIND_API_TOKEN`: Your Netmind API key

### Cursor & Claude Desktop Installation

Add this tool as a mcp server by editing the Cursor/Claude config file.

```json
"parse-pdf": {
  "env": {
    "NETMIND_API_TOKEN": "XXXXXXXXXXXXXXXXXXXX",
  },
  "command": "uvx",
  "args": [
    "netmind-parse-pdf-mcp"
  ]
}
```

#### Cursor

- On MacOS: `/Users/your-username/.cursor/mcp.json`
- On Windows: `C:\Users\your-username\.cursor\mcp.json`

#### Claude & Windsurf

- On MacOS: `~/Library/Application\ Support/Claude/claude_desktop_config.json`
- On Windows: `%APPDATA%/Claude/claude_desktop_config.json`
