from ApeMan import ApeMan


class Human(ApeMan):
    nationality = ''

    def __init__(self, name = None, nationality = None):
        if name is None and nationality is None:
            pass
        else:
            self.name = name
            self.nationality = nationality


    def add(self):
        while True:
            name = input("Введіть ім'я:\t")
            if name.replace(" ", "").isalpha() and len(name) > 0:
                self.name = name
                break
            else:
                print("Невірно введені данні")
        while True:
            nationality = input("Введіть національність\t")
            if nationality.replace(" ", "").isalpha() and len(nationality) > 0:
                self.nationality = nationality
                break
            else:
                print("Невірно введені данні")

    def info(self):
        print(f" Ім'я: {self.name}\n Національність: {self.nationality}\n Раціон: {self.ration}\n")

    def __str__(self):
        return f" Ім'я: {self.name}\n Національність: {self.nationality}\n Раціон: {self.ration}\n"