import importlib
import importlib.util
import debug

m = 'module.temp1'
c = 'MyClass'
_widget=(m,c)
if type(_widget) is tuple:
    try:
        importlib.import_module(_widget[0])
        if hasattr(importlib.import_module(_widget[0]),_widget[1]):
            t_class = getattr(importlib.import_module(_widget[0]),_widget[1])
        else: debug.cout(f'Class: {_widget[1]} not found in module: {_widget[0]}');
    except  ModuleNotFoundError:
        debug.cout(f'Module: {_widget[0]} not found');

#print('rt')
k=t_class(10)

k.display_value()