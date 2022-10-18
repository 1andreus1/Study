'''
Interface Segregation Principle (ISP)
Принцип разделения интерфейса

Идея:
Не стоит добавлять слишком много методов в интерфейс.
'''
from abc import ABC, abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError()

    def fax(self, document):
        raise NotImplementedError()

    def scan(self, document):
        raise NotImplementedError()


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):
    def print(self, document):
        '''ок'''
        pass

    '''
    Пользователь будет видеть эти методы,
    но они не будут работать.
    '''

    def fax(self, document):
        '''Вариант оставить так и ничего не делать'''
        pass

    def scan(self, document):
        '''Не поддерживается!'''
        raise NotImplementedError()


'''Рекомендуется разделить интерфейс следующим образом'''


class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass


'''Абстрактный класс-интерфейс'''


class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


'''Декоратор'''


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.scanner = scanner
        self.printer = printer

    @abstractmethod
    def print(self, document):
        self.printer.print(document)

    @abstractmethod
    def scan(self, document):
        self.scanner.scan(document)
