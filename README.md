# NetMind ParsePro

> - **MCP Certified** – Verified by [MCP Review](https://mcpreview.com/mcp-servers/protagolabs/netmind-parse-pdf-mcp)


The PDF Parser AI service, built and customized by the [NetMind](https://netmind.ai) team, is a high-quality, robust,
and cost-efficient solution for converting PDF files from a given URL into specified output formats such as JSON and Markdown.
It is fully MCP server–ready, allowing seamless integration with AI agents.

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

### Cursor & Claude Desktop && Windsurf Installation

Add this tool as a mcp server by editing the Cursor/Claude/Windsurf config file.

```json
{
  "mcpServers": {
    "parse-pdf": {
      "env": {
        "NETMIND_API_TOKEN": "XXXXXXXXXXXXXXXXXXXX"
      },
      "command": "uvx",
      "args": [
        "netmind-parse-pdf-mcp"
      ]
    }
  }
}
```

#### Cursor

- On MacOS: `/Users/your-username/.cursor/mcp.json`
- On Windows: `C:\Users\your-username\.cursor\mcp.json`

#### Claude

- On MacOS: `~/Library/Application\ Support/Claude/claude_desktop_config.json`
- On Windows: `%APPDATA%/Claude/claude_desktop_config.json`


### Windsurf

- On MacOS: `/Users/your-username/.codeium/windsurf/mcp_config.json`
- On Windows: `C:\Users\your-username\.codeium\windsurf\mcp_config.json`