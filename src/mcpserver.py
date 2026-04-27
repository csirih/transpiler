from fastapi import FastAPI
from pydantic import BaseModel
from jinja2 import Template
import os
from mcp.server.fastmcp import FastMCP

server= FastMCP("prompt-engine")

@server.prompt()
def generate_architecture(text: str) -> str:
    return f"""Please generate the architecture from the legacy code {code}, Thinking as "A".
           Q: How to modernise legacy archtecture?
           A: Please reference here : https://medium.com/cloud-journey-optimization/bridging-the-chasm-between-cloud-native-and-the-     	      mainframe-b87a2ed77742 """
if __name__="__main__":
   server.run()       
