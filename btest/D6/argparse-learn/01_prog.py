import argparse

# 第一步：创建一个 ArgumentParser对象
'''
description - 在参数帮助之前显示的文本（默认情况下，没有文本）
'''
parser = argparse.ArgumentParser(description='Process some integers.')


# 添加参数。在命令行上获取字符串并转化成对象
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

# 解析参数。
# 返回一个具有两个属性的对象，integers和accumulate。属性integers将是一个或多个整数的列表，accumulate属性将是sum()函数
args = parser.parse_args()

print(args.accumulate(args.integers))
