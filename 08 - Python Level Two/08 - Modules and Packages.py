'''
import mymodule

mymodule.func_in_module()

# __pycacge__ é lixo
'''

'''
import mymodule as mm 

mm.func_in_module()
'''

'''
from mymodule import func_in_module

func_in_module()
'''

#não fazer isso, gasta memória
from mymodule import *
func_in_module()