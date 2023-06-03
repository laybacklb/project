import ctypes
import suibian
import zaisuibian
# 通过ctypes.CDLL()函数加载lib文件
# 这里lib的名字叫ps4000a
ps4000a = ctypes.CDLL("D:\PycharmProjects\pythonProjects\lib_pico\ps4000a.dll")

# 设置Picotech SDK函数的参数和返回类型
ps4000a.function_name.argtypes = [arg_type1, arg_type2, ...]  # 设置函数的参数类型
ps4000a.function_name.restype = return_type  # 设置函数的返回类型

# 调用Picotech SDK函数
result = ps4000a.function_name(arg1, arg2, ...)  # 替换为实际的函数名和参数


import ctypes
import numpy as np
from picosdk.ps4000a import ps4000a as ps
import matplotlib.pyplot as plt  #file-settings-右边有个+号，可以下载matplotlib库
from picosdk.functions import adc2mV, assert_pico_ok
