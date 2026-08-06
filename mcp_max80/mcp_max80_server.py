#!/usr/bin/env python3
import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
import subprocess

app = Server("mcp-max80")

@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="dispatch_to_cmdr",
            description="Send a tactical order to CMDR_MAX80",
            inputSchema={
                "type": "object",
                "properties": {
                    "order": {"type": "string", "description": "The order for CMDR_MAX80"}
                },
                "required": ["order"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "dispatch_to_cmdr":
        order = arguments["order"]
        with open("../cmdr.in", "a") as f:
            f.write(f"CMDR_MAX80: {order}\n")
        try:
            result = subprocess.check_output(["tail", "-n", "5", "../logs/cmdr.out"], text=True)
            response = f"Order dispatched: {order}\n\nCMDR Response:\n{result}"
        except:
            response = f"Order dispatched: {order}\nCMDR_MAX80 processing..."
        return [TextContent(type="text", text=response)]

    return [TextContent(type="text", text=f"Unknown tool: {name}")]

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
