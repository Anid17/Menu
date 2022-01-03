print("Welcome to Slastičarna 'Specijal' Jelah")
print(56*"-")
print("Menu")
print(56*"-")

def menu():
    print("[1] Ice Cream")
    print("[2] Waffle")
    print("[3] Cookies")
    print("[4] Kaffezeit")
    print("[5] Tea")
    print("[6] Natural Juice")
    print("[7] Pie")
    print("[8] Cups")
    print("[9] Exit")

while True:
    menu()
    print(56*"-")
    Choice =(int(input("Enter your choice")))
    if Choice == 1:
        print("[1] Vanilla ")
        print("[2] Chocolate ")
        print("[3] Hazelnut ")
        print("[4] Malaga ")
        print("[5] Yogurt ")
        print("[6] Strawberries ")
        print("[7] Cookies ")
        print("[8] Stracciatella ")
        print("[9] Azzuro ")
        print("[10] Kivi ")
        print("[11] Exit ")
        select=int(input("Enter a number "))
        if select == 11:
            break
        else:
            print("The ice cream is 1.00 BAM")
            more = input("Do you want something else? ")
            if more =="NO":
                break


    elif Choice == 2:
        print("[1] Waffles with Ice Cream")
        print("[2] Waffles with Nutella")
        print("[3] Waffles with Caramel")
        print("[4] Waffles with Fruits")
        print("[5] Waffles with Honey")
        print("[6] Exit")
        select=int(input("Enter a number "))
        if select == 6:
            break
        else:
            print("Waffles are 5.00 BAM")
        more = input("Do you want something else")
        if more =="NO":
            break
    elif Choice == 3:
        print("[1] Krempita ")
        print("[2] Šampita")
        print("[3] Tulumba ")
        print("[4] Baklava ")
        print("[5] Fruit ")
        print("[6] Trileqe ")
        print("[7] Figaro ")
        print("[8] Rolat ")
        print("[9] Bohem ")
        print("[10] Exit ")
        select=int(input("Enter a number "))
        if select == 10:
            break
        else:
            print("Cookies are 1.00 BAM")
        more = input("Do you want something else? ")
        if more =="NO":
            break

    elif Choice == 4:
        print("[1] Turskish coffe ")
        print("[2] Esspresso ")
        print("[3] Cappuccino ")
        print("[4] Macchiato ")
        print("[5] Eis coffe ")
        print("[6] Exit ")
        select=int(input("Enter a number "))
        if select == 6:
            break
        else:
            print("Coffes are 1.50 BAM")
            more = input("Do you want something else")
            if more == "NO":
                break

    elif Choice == 5:
        print("[1] Chamomile ")
        print("[2] Turkish ")
        print("[3] Menthol ")
        print("[4] Vanilla and Apple ")
        print("[5] Fruit ")
        print("[6] Blueberry")
        print("[7] Exit ")
        select=int(input("Enter a number "))
        if select == 7:
            break
        else:
            print("Tees are 1.50 BAM")
        more = input("Do you want something else?")
        if more == "NO":
            break

    elif Choice == 6:
        print("[1] Lemonade ")
        print("[2] Blueberry ")
        print("[3] Orange ")
        print("[4] Red orange ")
        print("[5] Peach ")
        print("[6] Exit")
        select=int(input("Enter a number "))
        if select == 6:
            break
        else:
            print("Juices are 2.00 BAM")
        more = input("Do you want something else?")
        if more =="NO":
            break

    elif Choice == 7:
        print("[1] Burek ")
        print("[2] Sirnica ")
        print("[3] Maslanica ")
        print("[4] Zeljanica ")
        print("[5] Krompiruša ")
        print("[6] Exit")
        select=int(input("Enter a number "))
        if select == 6:
            break
        else:
            print("Pie is 2.00 BAM")
        if select =="NO":
            break

    elif Choice == 8:
        print("[1] Banana split ")
        print("[2] Tutti Frutti ")
        print("[3] Royal Cup ")
        print("[4] Specijal Cup")
        print("[5] Kokos Cup ")
        print("[6] Exit")
        select=int(input("Enter a number "))
        if select == 6:
            break
        else:
            print("Cups are 5.00 BAM")
            more=input("Do you want something else")
            if more == "NO":
                break
