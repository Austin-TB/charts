# Chart Generator MCP server

An MCP server that generates charts based on input data.

## Status
🚧 **In Development** 🚧

## Features
- Generates charts dynamically based on provided input data (natural language).
- Built using MCP Python SDK.

## Usage
- Install `uv`
- inside the directory run `uv venv`
- activate this virtual environment
- run `uv add fastapi "mcp[cli]" quickchart.io`
- in the mcp client,
    - add this to the mcp servers list
    ```
            "charts": {
            "command": "uv",
            "args": [
                "--directory",
                ABSOLUTE_PATH_TO/charts",
                "run",
                "charts.py"
            ]
    ```

---
Stay tuned for updates!
