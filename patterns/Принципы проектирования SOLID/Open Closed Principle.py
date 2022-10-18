'''
Open Closed Principle (OCP)
Принцип открытости-закрытости
Открытый для расширения, но закрытый для изменения.
Идея в том что не стоит менять код,
который протестирован и запущен в production.
'''

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    '''
    Нарушение принципа OCP
    Данный подход не масштабируется
    '''

    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.size == size and p.color == color:
                yield p


class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    print('Старый фильтр:')
    pf = ProductFilter()
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f' - {p.name} is green')

    print('Новый фильтр:')
    bf = BetterFilter()
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f' - {p.name} is green')

    print('Новый фильтр спецификация and:')
    bf = BetterFilter()
    large = SizeSpecification(Size.LARGE)
    # green_and_large = AndSpecification(green, large)
    green_and_large = green & large
    for p in bf.filter(products, green_and_large):
        print(f' - {p.name} is green and large')
