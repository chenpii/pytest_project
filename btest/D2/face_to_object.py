"""
面向对象断言
"""
from dataclasses import dataclass, asdict, astuple, replace


@dataclass
class Person:
    # 节省了init函数
    name: str
    age: int
    height: int = 170  # cm
    weight: int = 60  # kg

    @classmethod
    def from_dict(cls, d):
        return Person(**d)

    def to_dict(self):
        return asdict(self)

    def to_tuple(self):
        return astuple(self)

    def update(self, **changes):
        return replace(self, **changes)

    # 待完成
    def cook(self):
        pass

    def eat(self, food):
        pass


if __name__ == '__main__':
    # 把字典转换成类对象
    ym_dict = {'name': 'ym', 'age': 18, 'height': 170, 'weight': 68}
    ym = Person.from_dict(ym_dict)
    print('我是类对象型ym', ym)

    # 把类对象转化成字典
    ym_dict = ym.to_dict()
    print('我是字典型ym', ym_dict)

    # 把类对象转化成元组
    ym_tuple = ym.to_tuple()
    print('我是元组型ym', ym_tuple)

    # 修改类对象姓名
    lyf = ym.update(name='lyf', age=22)
    print('我是lyf', lyf)
