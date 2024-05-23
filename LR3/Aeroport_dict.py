aeroport = {}.fromkeys(["full_name", "flight", "class", "place", "price"])

aeroport_list = list()

ex = False


def add():
    aeroport_list.append(aeroport.copy())
    while True:
        full_name = input("Enter full name: ")
        if full_name.replace(" ", "").isalpha() and len(full_name) > 0:
            aeroport_list[-1]["full_name"] = full_name
            break
        else:
            print("Please enter only letters and spaces.")
    aeroport_list[-1]["flight"] = input("Enter flight:\t")
    aeroport_list[-1]["class"] = input("Enter class:\t")
    while True:
        place = input("Enter place:\t")
        if place.isdigit() and len(place) > 0:
            aeroport_list[-1]["place"] = place
            break
        else:
            print("Please enter only numbers.")
    while True:
        price = input("Enter price:\t")
        if price.isdigit() and len(price) > 0:
            aeroport_list[-1]["price"] = price
            break
        else:
            print("Please enter only numbers.")


def delete():
    index = int(input("Enter some index:\t"))
    if index >= 0 and index < len(aeroport_list):
        aeroport_list.pop(index)


def edit():
    index = int(input("Enter some index:\t"))
    if index >= 0 and index < len(aeroport_list):
        while True:
            full_name = input("Enter new or previous full name: ")
            if full_name.replace(" ", "").isalpha() and len(full_name) > 0:
                aeroport_list[index]["full_name"] = full_name
                break
            else:
                print("Please enter only letters and spaces.")
        aeroport_list[index]["flight"] = input("Enter new or previous flight:\t")
        aeroport_list[index]["class"] = input("Enter new or previous class:\t")
        while True:
            place = input("Enter new or previous place:\t")
            if place.isdigit() and len(place) > 0:
                aeroport_list[index]["place"] = place
                break
            else:
                print("Please enter only numbers.")
        while True:
            price = input("Enter new or previous price:\t")
            if price.isdigit() and len(price) > 0:
                aeroport_list[index]["price"] = price
                break
            else:
                print("Please enter only numbers.")



def show_all():
    for i in aeroport_list:
        info = f"Full name: {i['full_name']}, flight: {i['flight']}, class: {i['class']}, place: {i['place']}, price: {i['price']}\n"
        print(info)


def calculation_func():
    sum = 0
    for i in aeroport_list:
        sum += int(i['price'])

    if len(aeroport_list) > 0:
        avg = sum / len(aeroport_list)

    for i in aeroport_list:
        if float(i['price']) <= avg:
            info = f"Full name: {i['full_name']}, flight: {i['flight']}, class: {i['class']}, place: {i['place']}, price: {i['price']}\n"
            print(info)


while not ex:
    choice = -1
    print("\nChange some point")
    print("1. Add")
    print("2. Delete")
    print("3. Edit")
    print("4. Show All")
    print("5. Show calculation")
    print("6. Exit")

    choice = int(input("Your choise:\t"))

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
    else:
        print("Incorrect type or invalid number entered!")

