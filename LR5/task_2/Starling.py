from Bird import Bird


class Starling(Bird):
    variety = ''
    area = ''

    def __init__(self, name=None, variety=None, area=None):
        if name is None and variety is None and area is None:
            pass
        else:
            self.name = name
            self.variety = variety
            self.area = area
            self.fly = True

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
        while True:
            area = input("Введіть ареал існування:\t")
            if area.replace(" ", "").isalpha() and len(area) > 0:
                self.area = area
                break
            else:
                print("Невірно введені данні")
        self.fly = True

    def info(self):
        print(
            f" Кличка: {self.name}\n Вид: {self.variety}\n Ареал існування: {self.area}\n Птах літаючий: {'Taк' if self.fly else 'Ні'}\n")

    def __str__(self):
        return f" Кличка: {self.name}\n Вид: {self.variety}\n Ареал існування: {self.area}\n Птах літаючий: {'Taк' if self.fly else 'Ні'}\n"