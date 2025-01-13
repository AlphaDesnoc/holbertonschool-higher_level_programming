#!/usr/bin/python3
import marshal
import types

if __name__ == "__main__":
    pyc_file_path = '/tmp/hidden_4.pyc'
    with open(pyc_file_path, 'rb') as pyc_file:
        pyc_file.seek(16)
        code = marshal.load(pyc_file)
    module = types.ModuleType("hidden_4")
    exec(code, module.__dict__)
    names = [name for name in dir(module) if not name.startswith("__")]
    names.sort()
    for name in names:
        print(name)
