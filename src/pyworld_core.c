#include <Python.h>
#include <string.h>
#include <stdlib.h>

static PyObject* pyworld_init(PyObject* self, PyObject* args) {
    const char* version;
    if (!PyArg_ParseTuple(args, "s", &version))
        return NULL;
    
    return PyUnicode_FromFormat("PyWorld Core Module v%s initialized", version);
}

static PyObject* pyworld_process_text(PyObject* self, PyObject* args) {
    const char* text;
    if (!PyArg_ParseTuple(args, "s", &text))
        return NULL;
    
    char* result = (char*)malloc(strlen(text) * 2 + 1);
    strcpy(result, "Processed: ");
    strcat(result, text);
    
    PyObject* py_result = PyUnicode_FromString(result);
    free(result);
    return py_result;
}

static PyObject* pyworld_calculate(PyObject* self, PyObject* args) {
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b))
        return NULL;
    
    return PyLong_FromLong(a + b);
}

static PyMethodDef PyWorldMethods[] = {
    {"init", pyworld_init, METH_VARARGS, "Initialize PyWorld core module"},
    {"process_text", pyworld_process_text, METH_VARARGS, "Process text"},
    {"calculate", pyworld_calculate, METH_VARARGS, "Perform calculation"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef pyworld_core_module = {
    PyModuleDef_HEAD_INIT,
    "_pyworld_core",
    "PyWorld Core C Extension Module",
    -1,
    PyWorldMethods
};

PyMODINIT_FUNC PyInit__pyworld_core(void) {
    return PyModule_Create(&pyworld_core_module);
}