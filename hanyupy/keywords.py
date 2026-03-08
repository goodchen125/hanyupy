# -*- coding: utf-8 -*-
"""
中文关键字和符号定义
"""

# 中文符号映射
中文符号 = {
    # 逻辑符号
    "且": lambda x, y: x and y,
    "或": lambda x, y: x or y,
    "非": lambda x: not x,
    "等于": lambda x, y: x == y,
    "不等于": lambda x, y: x != y,
    "大于": lambda x, y: x > y,
    "小于": lambda x, y: x < y,
    "大于等于": lambda x, y: x >= y,
    "小于等于": lambda x, y: x <= y,
    
    # 算术符号
    "加": lambda x, y: x + y,
    "减": lambda x, y: x - y,
    "乘": lambda x, y: x * y,
    "除": lambda x, y: x / y,
    "整除": lambda x, y: x // y,
    "取余": lambda x, y: x % y,
    "幂运算": lambda x, y: x ** y,
    
    # 位运算
    "位与": lambda x, y: x & y,
    "位或": lambda x, y: x | y,
    "位异或": lambda x, y: x ^ y,
    "位取反": lambda x: ~x,
    "左移": lambda x, y: x << y,
    "右移": lambda x, y: x >> y,
    
    # 中文标点符号（用于代码编写）
    "，": ",",
    "。": ".",
    "：": ":",
    "；": ";",
    "（": "(",
    "）": ")",
    "【": "[",
    "】": "]",
    "｛": "{",
    "｝": "}",
    "《": "<",
    "》": ">",
    "《＝": "<=",
    "》＝": ">=",
    "《》": "!=",
    "《＝》": "==",
    "？": "?",
    "！": "!",
    "｜": "|",
    "＆": "&",
    "％": "%",
    "＊": "*",
    "／": "/",
    "＋": "+",
    "－": "-",
    "＝": "=",
    "＠": "@",
    "＃": "#",
    "￥": "$",
    "＿": "_",
    "．": ".",
    "，": ",",
}

# 中文关键字映射（用于代码转换）
中文关键字映射 = {
    # 基础关键字
    "如果": "if",
    "否则如果": "elif",
    "否则": "else",
    "当": "while",
    "循环": "for",
    "在": "in",
    "范围": "range",
    "定义": "def",
    "类": "class",
    "返回": "return",
    "中断": "break",
    "继续": "continue",
    "通过": "pass",
    "尝试": "try",
    "除了": "except",
    "最终": "finally",
    "抛出": "raise",
    "导入": "import",
    "从": "from",
    "作为": "as",
    "且": "and",
    "或": "or",
    "非": "not",
    "是": "is",
    "不是": "is not",
    "包含": "in",
    "不包含": "not in",
    "等于": "==",
    "不等于": "!=",
    "大于": ">",
    "小于": "<",
    "大于等于": ">=",
    "小于等于": "<=",
    "全局": "global",
    "非局部": "nonlocal",
    "断言": "assert",
    "异步": "async",
    "等待": "await",
    "与": "with",
    "生成器": "yield",
    "从生成器": "yield from",
    "拉姆达": "lambda",
    "删除": "del",
}

# 中文函数映射
中文函数映射 = {
    "打印": "print",
    "输入": "input",
    "类型": "type",
    "长度": "len",
    "范围": "range",
    "整数": "int",
    "浮点数": "float",
    "字符串": "str",
    "列表": "list",
    "元组": "tuple",
    "字典": "dict",
    "集合": "set",
    "布尔": "bool",
    "打开": "open",
    "求和": "sum",
    "最大值": "max",
    "最小值": "min",
    "排序": "sorted",
    "映射": "map",
    "过滤": "filter",
    "拉链": "zip",
    "列举": "enumerate",
    "求绝对值": "abs",
    "幂": "pow",
    "四舍五入": "round",
    "切片": "slice",
}

# 中文类映射
中文类映射 = {
    "列表": "list",
    "元组": "tuple",
    "字典": "dict",
    "集合": "set",
    "字符串": "str",
    "整数": "int",
    "浮点数": "float",
    "布尔": "bool",
    "异常": "Exception",
    "值错误": "ValueError",
    "类型错误": "TypeError",
    "索引错误": "IndexError",
    "键错误": "KeyError",
    "属性错误": "AttributeError",
}

# 中文常量
中文常量 = {
    "真": "True",
    "假": "False",
    "空": "None",
}

def 转换中文代码(代码):
    """
    将包含中文关键字的代码转换为英文Python代码
    """
    for 中文, 英文 in 中文关键字映射.items():
        代码 = 代码.replace(中文, 英文)
    
    for 中文, 英文 in 中文函数映射.items():
        代码 = 代码.replace(中文, 英文)
    
    for 中文, 英文 in 中文类映射.items():
        代码 = 代码.replace(中文, 英文)
    
    for 中文, 英文 in 中文常量.items():
        代码 = 代码.replace(中文, 英文)
    
    # 处理中文符号
    代码 = 代码.replace("（", "(")
    代码 = 代码.replace("）", ")")
    代码 = 代码.replace("【", "[")
    代码 = 代码.replace("】", "]")
    代码 = 代码.replace("｛", "{")
    代码 = 代码.replace("｝", "}")
    代码 = 代码.replace("：", ":")
    代码 = 代码.replace("，", ",")
    代码 = 代码.replace("《", "<")
    代码 = 代码.replace("》", ">")
    
    return 代码