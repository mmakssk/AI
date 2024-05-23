from EvenToed import EvenToed


class Cow(EvenToed):
    variety = ''

    def __init__(self, name = None, variety = None):
        if name is None and variety is None:
            pass
        else:
            self.name = name
            self.variety = variety

    def add(self):
        while True:
            name = input("Введіть кличку тврини:\t")
            if name.replace(" ", "").isalpha() and len(name) > 0:
                self.name = name
                break
            else:
                print("Невірно введені данні")
        while True:
            variety = input("Введіть вид тварини:\t")
            if variety.replace(" ", "").isalpha() and len(variety) > 0:
                self.variety = variety
                break
            else:
                print("Невірно введені данні")

    def info(self):
        print(f" Кличка: {self.name}\n Вид: {self.variety}\n  Раціон: {self.ration}\n")

    def __str__(self):
        return f" Кличка: {self.name}\n Вид: {self.variety}\n  Раціон: {self.ration}\n"