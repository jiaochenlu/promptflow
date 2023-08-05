from promptflow import tool
import numpy as np

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(input1: str) -> dict:
  np_arr = np.array([1,2,3])
  return_dict = {"name": input1, "age": {"gap":1,"akjdnf":23, "ree":"adf"}, "np_array":np_arr}
  return return_dict