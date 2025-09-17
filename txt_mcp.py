#!/usr/bin/env python3

# Import the FastMCP class from the fastmcp module
from mcp.server.fastmcp import FastMCP

# Prompt that asks for confirmation before proceeding
from mcp.server.fastmcp.prompts import base

# Initialize the FastMCP server with the name 'txt-mcp'
mcp = FastMCP("txt-mcp")


@mcp.prompt(title="Confirmation Before Action")
def confirm_action(action_description: str = "an operation") -> list[base.Message]:
    """
    Before you initiate order from user, explain what you will do and ask for confirmation and if user confirms, proceed process, if user does not confirms wait for further information
    """
    return [
        base.UserMessage(f"You are about to: {action_description}"),
        base.AssistantMessage(
            "Before I begin, please confirm: Should I proceed with this action?\n"
            "If you confirm, I will continue. If not, I will wait for further instructions."
        ),
    ]



# Tool to read a UTF-8 encoded text file
@mcp.tool()
async def read_file(file_path: str) -> str:
    """Read any text file (UTF-8)."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# Tool to write (overwrite or create) a text file with UTF-8 encoding
@mcp.tool()
async def write_file(file_path: str, content: str) -> str:
    """Write (overwrite/create) any text file (UTF-8)."""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Wrote {file_path}"

# Tool to perform search-and-replace in a file's content
@mcp.tool()
async def edit_text(file_path: str, search: str, replace: str) -> str:
    """
    Edit any readable file by replacing all occurrences of 'search' with 'replace'.
    """
    try:
        # Read the original file content
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Replace all occurrences of 'search' with 'replace'
        new_content = content.replace(search, replace)

        # Write the modified content back to the file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        return f"Replaced all occurrences of '{search}' with '{replace}' in {file_path}."
    except Exception as e:
        # Return the error message if editing fails
        return f"Error editing file: {e}"

# Entry point with selectable transports (matching provided screenshot)
if __name__ == "__main__":
    # Start the MCP server without specifying a transport (defaults to WebSocket)
    mcp.run()
