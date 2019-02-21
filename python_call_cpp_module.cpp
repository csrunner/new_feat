#include </System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7/Python.h>

int python_call_cpp_func(int a) {
    return a + 1;
}

static PyObject * _python_call_cpp_func(PyObject *self, PyObject *args)
{
    int _a;
    int res;

    if (!PyArg_ParseTuple(args, "i", &_a))
        return NULL;
    res = python_call_cpp_func(_a);
    return PyLong_FromLong(res);
}

static PyMethodDef PyCallCppModuleMethods[] = {
    {
        "python_call_cpp_func",
        _python_call_cpp_func,
        METH_VARARGS,
        ""
    },
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initpython_call_cpp_module(void) {
    (void) Py_InitModule("python_call_cpp_module", PyCallCppModuleMethods);
}