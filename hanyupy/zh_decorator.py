# -*- coding: utf-8 -*-
"""
中文关键字执行器
允许在Python代码中使用中文关键字（如 如果、否则、循环 等）
"""

import re

# 中文关键字到英文关键字的映射（按长度降序排列，避免部分匹配）
中文关键字映射 = {
    # 控制流关键字
    "否则如果": "elif",
    "如果": "if",
    "否则": "else",
    "当": "while",
    "循环": "for",
    "在": "in",
    "范围": "range",
    "枚举": "enumerate",
    "中断": "break",
    "继续": "continue",
    "通过": "pass",

    # 函数和类定义
    "定义": "def",
    "类": "class",
    "返回": "return",
    "从返回": "yield",
    "从返回...到": "yield from",

    # 异常处理
    "尝试": "try",
    "除了": "except",
    "最终": "finally",
    "抛出": "raise",

    # 逻辑运算符
    "且": "and",
    "或": "or",
    "非": "not",
    "是": "is",
    "不是": "is not",
    "包含": "in",
    "不包含": "not in",

    # 比较运算符
    "等于": "==",
    "不等于": "!=",
    "大于": ">",
    "小于": "<",
    "大于等于": ">=",
    "小于等于": "<=",

    # 其他关键字
    "导入": "import",
    "从": "from",
    "作为": "as",
    "全局": "global",
    "非局部": "nonlocal",
    "断言": "assert",
    "异步": "async",
    "等待": "await",
    "与": "with",
    "拉姆达": "lambda",
    "删除": "del",
}

# 模块名称映射
模块名称映射 = {
    "数学": "math",
    "随机": "random",
    "时间": "time",
    "操作系统": "os",
    "操作系统路径": "os.path",
    "系统": "sys",
    "json": "json",
    "正则": "re",
    "日期时间": "datetime",
    "集合库": "collections",
    "迭代工具": "itertools",
    " functools": "functools",
}

# 中文符号到英文符号的映射
中文符号映射 = {
    "（": "(",
    "）": ")",
    "【": "[",
    "】": "]",
    "｛": "{",
    "｝": "}",
    "：": ":",
    "，": ",",
    "《": "<",
    "》": ">",
    "《＝": "<=",
    "》＝": ">=",
    "《》": "!=",
    "《＝》": "==",
    "＝": "=",
    "＋": "+",
    "－": "-",
    "＊": "*",
    "／": "/",
    "％": "%",
    "＆": "&",
    "｜": "|",
    "？": "?",
    "！": "!",
}

def 转换中文代码(代码):
    """
    将包含中文关键字的代码转换为英文Python代码
    """
    # 首先处理中文符号
    for 中文, 英文 in 中文符号映射.items():
        代码 = 代码.replace(中文, 英文)

    # 处理模块名称
    for 中文, 英文 in 模块名称映射.items():
        # 匹配导入语句中的模块名
        代码 = re.sub(r'导入\s+' + re.escape(中文), r'import ' + 英文, 代码)
        代码 = re.sub(r'从\s+' + re.escape(中文), r'from ' + 英文, 代码)

    # 处理中文关键字（按长度降序，确保长关键字优先匹配）
    # 对关键字按长度排序，长的先替换
    排序后的关键字 = sorted(中文关键字映射.items(), key=lambda x: -len(x[0]))

    for 中文, 英文 in 排序后的关键字:
        # 使用正则表达式确保只匹配独立的关键字
        # 前后是空格、冒号、换行、制表符等
        pattern = r'(?<![\w])' + re.escape(中文) + r'(?![\w])'
        代码 = re.sub(pattern, 英文, 代码)

    return 代码

def 执行中文代码(代码字符串, 全局变量=None, 局部变量=None):
    """
    直接执行包含中文关键字的代码字符串

    参数:
        代码字符串: 包含中文关键字的Python代码
        全局变量: 执行时的全局变量字典
        局部变量: 执行时的局部变量字典

    返回:
        执行后的局部变量字典
    """
    转换后的代码 = 转换中文代码(代码字符串)

    if 全局变量 is None:
        # 使用当前的全局变量，确保包含hanpy定义的中文函数
        全局变量 = globals().copy()
    if 局部变量 is None:
        局部变量 = {}

    # 添加数学代理，支持中文方法调用
    try:
        from hanpy import 数学代理
        全局变量['数学'] = 数学代理
    except:
        pass

    # 确保内置函数可用
    import builtins
    内置函数 = ['enumerate', 'range', 'len', 'str', 'int', 'float', 'list', 'dict', 'set', 'bool']
    for 函数名 in 内置函数:
        if 函数名 not in 全局变量:
            全局变量[函数名] = getattr(builtins, 函数名)

    exec(转换后的代码, 全局变量, 局部变量)
    return 局部变量

def 运行文件(文件路径):
    """
    运行包含中文关键字的Python文件

    参数:
        文件路径: Python文件路径
    """
    with open(文件路径, 'r', encoding='utf-8') as f:
        代码 = f.read()

    转换后的代码 = 转换中文代码(代码)
    exec(转换后的代码, globals())

def 转换文件(输入文件路径, 输出文件路径=None):
    """
    将包含中文关键字的Python文件转换为英文Python文件

    参数:
        输入文件路径: 输入的Python文件路径
        输出文件路径: 输出的Python文件路径（如果为None，则覆盖原文件）
    """
    with open(输入文件路径, 'r', encoding='utf-8') as f:
        代码 = f.read()

    转换后的代码 = 转换中文代码(代码)

    if 输出文件路径:
        with open(输出文件路径, 'w', encoding='utf-8') as f:
            f.write(转换后的代码)
    else:
        # 覆盖原文件
        with open(输入文件路径, 'w', encoding='utf-8') as f:
            f.write(转换后的代码)

# 别名
zh_code = 执行中文代码
convert = 转换中文代码
convert_file = 转换文件
run_file = 运行文件