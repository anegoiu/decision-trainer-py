from crewai.tools import BaseTool, tool
from typing import Type
from pydantic import BaseModel, Field
from exa_py import Exa
import os

exa_api_key = os.getenv("EXA_API_KEY")
print("exa_api_key: ", exa_api_key)

@tool("Exa search and get contents")
def search_and_get_contents_tool(question: str) -> str:
    """Tool using Exa's Python SDK to run semantic search and return result highlights."""

    exa = Exa(exa_api_key)

    response = exa.search_and_contents(
        question,
        type="neural",
        num_results=3,
        highlights=True
    )
    print("exa sresponse: ", response)

    parsedResult = ''.join([
      f'<Title id={idx}>{eachResult.title}</Title>
      f'<URL id={idx}>{eachResult.url}</URL>
      f'<Highlight id={idx}>{"".join(eachResult.highlights)}</Highlight>'
      for (idx, eachResult) in enumerate(response.results)
    ])

    return parsedResult


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."
