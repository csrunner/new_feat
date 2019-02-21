def cpp_call_python_func(a):
    return a + 1

from python_call_cpp_module import python_call_cpp_func
print(python_call_cpp_func(2)) 