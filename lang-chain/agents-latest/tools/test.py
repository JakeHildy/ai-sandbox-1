from langchain.tools import Tool

def test_tool(str):
    return f"{str}"

tool = Tool(
    name="test_tool",
    description="A test tool",
    func=test_tool,
)

