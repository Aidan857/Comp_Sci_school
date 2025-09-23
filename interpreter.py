x = float(input("give me your first number"))
y = input (" Give me one of these math operators+, -, *, or, /")
z = float(input("give me your second number"))
answer = 0


if (x and y).isdigit:
    if y == "-":
        answer = x - z
    elif y == "*":
        answer = x * z
    elif y == "+":
        answer = x + z
    elif y == "/":
        answer = x / z
    print(answer)
else:
    print("give me valid numbers")



