class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


n = input("Enter name: ")
s = input("Enter surname")
p = input("Enter position: ")
w = int(input("Enter wage"))
b = int(input("Enter bonus"))
a = Position(n, s, p, w, b)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())
