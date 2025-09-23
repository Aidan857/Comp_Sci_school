
menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
total = 0
for i in menu:
    print(f"These are the items available: {i}")
while True:
    try:
        item = input("Item: ")
        item_cap = item.title()
        if item_cap in menu:
            total = total + (menu[item_cap])
            print(f"Total: ${total:.2f}")
        elif item_cap != menu:
            print("gimme a valid item")
    except EOFError:
        break
    

