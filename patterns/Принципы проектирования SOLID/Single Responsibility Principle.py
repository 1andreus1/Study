'''
Single Responsibility Principle (SRP, SOC)
Принцип единственной ответственности
У класса должна быть своя основная ответственность.
И он не должен брать на себя другие ответственности.
'''


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    def save(self, filename):
        '''
        Эта функция нарушает принцип SRP

        Помимо журнала могут быть другие классы,
        у которых могут быть свои методы сохранения.
        Которые возможно потребуется централизованно изменить.
        '''
        with open(filename, 'w') as file:
            file.write(str(self))


class PersistenceManager:
    '''Поэтому ответственность сохранения лучше выделить в отдельный класс.'''

    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, 'w') as file:
            file.write(str(journal))


if __name__ == '__main__':
    j = Journal()

    j.add_entry('Hello!')
    print(f'Journal:\n{j}')

    file = 'Journal.txt'
    PersistenceManager.save_to_file(j, file)
