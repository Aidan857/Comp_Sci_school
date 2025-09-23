
user = str(input('Greetings! ')).lower()
user = user.lstrip()



if "hello" == user:
    print ("0$")
else:
    # print("h")
    if user[0] == "h":
        print("20$")
    else:
        print("100$")
