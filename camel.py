def main():
    user = input("Give me a name: ")
    snake = ""
    for i in user:
        if i.isupper:
            snake += "_" +i.lower()
        else:
            snake +=i
        print (f"snake_case: ",{snake})









main()