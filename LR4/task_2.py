import json

aeroport = {}.fromkeys(["full_name", "flight", "class", "place", "price"])

aeroport_list = list()

ex = False


def add():
    aeroport_list.append(aeroport.copy())
    while True:
        full_name = input("Введіть повне ім'я: ")
        if full_name.replace(" ", "").isalpha() and len(full_name) > 0:
            aeroport_list[-1]["full_name"] = full_name
            break
        else:
            print("Введіть нове або минуле повне ім'я.")
    aeroport_list[-1]["flight"] = input("Введіть рейс:\t")
    aeroport_list[-1]["class"] = input("Введіть клас:\t")
    while True:
        place = input("Введіть місце:\t")
        if place.isdigit() and len(place) > 0:
            aeroport_list[-1]["place"] = place
            break
        else:
            print("Введіть лише числа.")
    while True:
        price = input("Введіть вартість:\t")
        if price.isdigit() and len(price) > 0:
            aeroport_list[-1]["price"] = price
            break
        else:
            print("Введіть лише числа.")
    print("Запис успішно додано")

def delete():
    index = int(input("Введіть індекс запису:\t"))
    if index >= 0 and index < len(aeroport_list):
        aeroport_list.pop(index)
        print("Запис успішно видалено")
    else:
        print("Невірно вказаний індекс")

def edit():
    index = int(input("Введіть індекс запису:\t"))
    if index >= 0 and index < len(aeroport_list):
        while True:
            full_name = input("Введіть нове або минуле повне ім'я: ")
            if full_name.replace(" ", "").isalpha() and len(full_name) > 0:
                aeroport_list[index]["full_name"] = full_name
                break
            else:
                print("Введіть тільки літери або пробіл.")
        aeroport_list[index]["flight"] = input("Введіть новий або минулий рейс:\t")
        aeroport_list[index]["class"] = input("Введіть новий або минулий клас:\t")
        while True:
            place = input("Введіть нове або минуле місце:\t")
            if place.isdigit() and len(place) > 0:
                aeroport_list[index]["place"] = place
                break
            else:
                print("Введіть лише числа.")
        while True:
            price = input("Введіть нову або минулу вартість:\t")
            if price.isdigit() and len(price) > 0:
                aeroport_list[index]["price"] = price
                break
            else:
                print("Введіть лише числа.")
        print("Запис успішно змінено")
    else:
        print("Невірно вказаний індекс")


def show_all():
    for i in aeroport_list:
        info = f"Повне ім'я: {i['full_name']}, Рейс: {i['flight']}, Клас: {i['class']}, Місце: {i['place']}, Вартість: {i['price']}\n"
        print(info)


def calculation_func():
    sum = 0
    for i in aeroport_list:
        sum += int(i['price'])

    if len(aeroport_list) > 0:
        avg = sum / len(aeroport_list)

    for i in aeroport_list:
        if float(i['price']) <= avg:
            info = f"Повне ім'я: {i['full_name']}, Рейс: {i['flight']}, Клас: {i['class']}, Місце: {i['place']}, Вартість: {i['price']}\n"
            print(info)


def load_from_file():
    global aeroport_list
    try:
        with open("save_data.txt", "r") as file:
            aeroport_list = json.load(file)
    except Exception:
        print("Файл збережень відсутній")


def save_in_file():
    with open("save_data.txt", "w", encoding="UTF-8") as file:
        json.dump(aeroport_list, file)

load_from_file()

while not ex:
    choice = -1
    print("\nОберіть один варіант")
    print("1. Додати")
    print("2. Видалити")
    print("3. Змінити")
    print("4. Показати всі записи")
    print("5. Показати результат розрахункової функції")
    print("6. Вихід")

    try:
        choice = int(input("Обраний варіант:\t"))

        if choice == 1:
            add()
        elif choice == 2:
            delete()
        elif choice == 3:
            edit()
        elif choice == 4:
            show_all()
        elif choice == 5:
            calculation_func()
        elif choice == 6:
            ex = True
            save_in_file()
        else:
            print("Невірне число!")
    except ValueError:
        print("Невірний тип даних")

