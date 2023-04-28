'''
yield作用
如果一个函数包含了yield，则这个函数就变成了生成器 generator


'''

'''1.包含yield的函数'''

# def h():
#     print('To be brave')
#     yield 5
#
#
# h()  # 发现print语句并没有执行，因为h函数里面包含yield表达式

'''2.yield是一个表达式'''

'''3.透过next()语句看原理
我们知道，我们上面的h()被调用后并没有执行，因为它有yield表达式，因此，我们通过next()语句让它执行。next()语句将恢复Generator执行，并直到下一个yield表达式处
在python3.0中，c.next() 变成了c.__next__(),或者next(c)
'''


def h():
    print('Wen Chuan')
    yield 5
    print('Fighting!')


c = h()
next(c)  # 调用next之后，h()开始执行，直到遇到了yield 5
next(c)  # 再次调用next，会继续执行，直到找到下一个yield。由于没有yield，会报异常



