'''
Liskov Substitution Principle (LSP)
Принцип подстановки лисков

Идея:
Если есть интерфейс принимающий какой-то базовый класс,
то должна быть возможность использовать любых его наследников.
'''


class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    def __str__(self):
        return f'Width: {self.width} height: {self.height}'

    @property
    def area(self):
        return self._width * self._height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rc):
    w = rc.width
    rc.height = 10
    '''Ожидаемая площадь'''
    expected = int(w * 10)

    print(f'Ожидаемая площадь {expected}, реальная {rc.area}')


if __name__ == '__main__':
    rc = Rectangle(2, 3)
    use_it(rc)

    '''
    Нарушается принцип подстановки лисков
    Функция use_it некорректно работает с наследником Square
    '''
    sq = Square(5)
    use_it(sq)

    '''
    Получается что класс Square не нужен.
    Вместо него лучше использовать фабричный метод или
    какое-то логическое свойство для прямоугольника,
    что он является квадратом.
    '''
