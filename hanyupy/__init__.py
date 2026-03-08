# -*- coding: utf-8 -*-
"""
汉py - 中文Python编程库
让用户可以用中文进行Python编程
"""

# 首先定义中文包装器类
class 中文列表(list):
    """支持中文方法的列表类"""
    def 添加(self, item):
        return self.append(item)

    def 移除(self, item):
        return self.remove(item)

    def 弹出(self, index=-1):
        return self.pop(index)

    def 排序(self, key=None, reverse=False):
        return self.sort(key=key, reverse=reverse)

    def 反转(self):
        return self.reverse()

    def 计数(self, value):
        return self.count(value)

    def 清除(self):
        return self.clear()

    def 拷贝(self):
        return self.copy()

    def 插入(self, index, object):
        return self.insert(index, object)

    def 索引(self, value, start=0, stop=None):
        if stop is None:
            return self.index(value, start)
        return self.index(value, start, stop)

class 中文字典(dict):
    """支持中文方法的字典类"""
    def 获取(self, key, default=None):
        return self.get(key, default)

    def 键们(self):
        return self.keys()

    def 值们(self):
        return self.values()

    def 项们(self):
        return self.items()

    def 更新(self, other=None, **kwargs):
        return self.update(other, **kwargs)

    def 设置(self, key, value):
        self[key] = value

    def 删除(self, key):
        del self[key]

class 中文字符串(str):
    """支持中文方法的字符串类"""
    def 大写(self):
        return self.upper()

    def 小写(self):
        return self.lower()

    def 去除两端空白(self):
        return self.strip()

    def 替换(self, old, new, count=-1):
        return self.replace(old, new, count)

    def 分割(self, sep=None, maxsplit=-1):
        return self.split(sep, maxsplit)

    def 加入(self, iterable):
        return self.join(iterable)

    def 查找(self, sub, start=0, end=None):
        if end is None:
            return self.find(sub, start)
        return self.find(sub, start, end)

    def 索引(self, sub, start=0, end=None):
        if end is None:
            return self.index(sub, start)
        return self.index(sub, start, end)

# 定义中文函数
def 列表(iterable=()):
    return 中文列表(iterable)

原始字典 = dict

def 字典(*args, **kwargs):
    return 中文字典(*args, **kwargs)

原始字符串 = str

def 字符串(object=''):
    return 中文字符串(object)

# 修改builtins，让中文关键字在全局可用
import builtins

# 基础函数映射
builtins.打印 = print
builtins.输入 = input
builtins.类型 = type
builtins.长度 = len
builtins.范围 = range
builtins.整数 = int
builtins.浮点数 = float
builtins.字符串 = 字符串  # 使用我们的字符串函数
builtins.列表 = 列表      # 使用我们的列表函数
builtins.元组 = tuple
builtins.字典 = 字典      # 使用我们的字典函数
builtins.集合 = set
builtins.布尔 = bool
builtins.打开 = open
builtins.求和 = sum
builtins.最大值 = max
builtins.最小值 = min
builtins.排序 = sorted
builtins.映射 = map
builtins.过滤 = filter
builtins.拉链 = zip
builtins.列举 = enumerate
builtins.求绝对值 = abs
builtins.幂 = pow
builtins.四舍五入 = round
builtins.切片 = slice

# 逻辑操作
builtins.真 = True
builtins.假 = False
builtins.空 = None

# 异常类
builtins.异常 = Exception
builtins.值错误 = ValueError
builtins.类型错误 = TypeError
builtins.索引错误 = IndexError
builtins.键错误 = KeyError
builtins.属性错误 = AttributeError
builtins.运行时错误 = RuntimeError
builtins.文件不存在错误 = FileNotFoundError
builtins.除零错误 = ZeroDivisionError

# 数学函数
import math
builtins.数学 = math
builtins.正弦 = math.sin
builtins.余弦 = math.cos
builtins.正切 = math.tan
builtins.对数 = math.log
builtins.自然对数 = math.log10
builtins.平方根 = math.sqrt
builtins.向下取整 = math.floor
builtins.向上取整 = math.ceil
builtins.常数 = math
builtins.圆周率 = math.pi
builtins.自然常数 = math.e

# 创建数学模块代理，支持中文方法调用
class 数学模块代理:
    def __init__(self):
        self._math = math

    @property
    def 平方根(self):
        return self._math.sqrt

    @property
    def 圆周率(self):
        return self._math.pi

    @property
    def 自然常数(self):
        return self._math.e

    def 正弦(self, x):
        return self._math.sin(x)

    def 余弦(self, x):
        return self._math.cos(x)

    def 正切(self, x):
        return self._math.tan(x)

    def 对数(self, x, base=None):
        if base is None:
            return self._math.log(x)
        return self._math.log(x, base)

    def 自然对数(self, x):
        return self._math.log10(x)

    def 向下取整(self, x):
        return self._math.floor(x)

    def 向上取整(self, x):
        return self._math.ceil(x)

    def 幂(self, x, y):
        return self._math.pow(x, y)

    def 绝对值(self, x):
        return self._math.fabs(x)

    def 最大值(self, *args):
        return max(args)

    def 最小值(self, *args):
        return min(args)

# 创建数学代理实例
数学代理 = 数学模块代理()

# 随机函数
import random
builtins.随机 = random
builtins.随机整数 = random.randint
builtins.随机浮点数 = random.random
builtins.随机选择 = random.choice
builtins.打乱 = random.shuffle
builtins.采样 = random.sample

# 时间函数
import time
builtins.时间 = time
builtins.睡眠 = time.sleep
builtins.当前时间戳 = time.time
builtins.获取当前时间 = time.localtime

# 路径和文件操作
import os
import os.path
builtins.操作系统 = os
builtins.路径 = os.path
builtins.路径存在 = os.path.exists
builtins.路径连接 = os.path.join
builtins.路径分割 = os.path.split
builtins.目录名 = os.path.dirname
builtins.文件名 = os.path.basename
builtins.创建目录 = os.makedirs
builtins.删除文件 = os.remove
builtins.删除目录 = os.rmdir
builtins.列出文件 = os.listdir
builtins.当前目录 = os.getcwd
builtins.改变目录 = os.chdir

# 欢迎信息
print("✨ 汉py 已加载！现在你可以用中文编写Python代码了！✨")

# 导入中文关键字执行器并添加到builtins
from hanpy.zh_decorator import 执行中文代码, 运行文件, 转换文件, 转换中文代码
builtins.执行中文代码 = 执行中文代码
builtins.运行文件 = 运行文件
builtins.转换文件 = 转换文件
builtins.转换中文代码 = 转换中文代码