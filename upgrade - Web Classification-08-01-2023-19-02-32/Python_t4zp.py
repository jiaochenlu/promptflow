from promptflow import tool
from promptflow.connections import CustomConnection

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(input1: str, conn: CustomConnection) -> str:
  output1 = conn.AZURE_OPENAI_API_KEY
  return output1