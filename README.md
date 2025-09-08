# txt-mcp

`txt-mcp` is a minimal, fast, and extensible MCP (Model Context Protocol) server for reading, writing, and editing any text-based file. It is designed for seamless integration with Claude Desktop and other MCP-compatible clients.

## Features

- **Read any text file**: Supports reading UTF-8 encoded files of any type (.txt, .json, .md, .bat, etc.).
- **Write any text file**: Overwrite or create new text files with UTF-8 encoding.
- **Edit text in-place**: Perform search-and-replace operations on any readable file.
- **Simple API**: Exposes tools via MCP for easy automation and integration.
- **FastMCP-based**: Built on top of the FastMCP server for high performance.

## Installation

1. Clone this repository:
	```sh
	git clone https://github.com/kilgor/txt-mcp-server.git
	cd txt-mcp-server
	```
2. (Optional) Create and activate a Python 3.10+ virtual environment.
3. Install dependencies:
	```sh
	pip install -r requirements.txt
	# or, if using pyproject.toml:
	pip install .
	```

## Usage

You can run the server directly for use with Claude Desktop or other MCP clients:

```sh
python txt_mcp.py
```

### Available Tools

- `read_file(file_path: str) -> str`: Read any text file (UTF-8).
- `write_file(file_path: str, content: str) -> str`: Write (overwrite/create) any text file (UTF-8).
- `edit_text(file_path: str, search: str, replace: str) -> str`: Replace all occurrences of `search` with `replace` in the file.

## Project Structure

- `txt_mcp.py` — Main MCP server implementation.
- `main.py` — Simple hello-world entry point.
- `pyproject.toml` — Project metadata and dependencies.
- `.gitignore`, `.python-version`, `README.md` — Standard project files.

## License

MIT License. See [LICENSE](LICENSE) for details.

---
*Made with ❤️ for the Claude and MCP community.*
