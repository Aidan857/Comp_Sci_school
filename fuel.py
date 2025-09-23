
# # def main():
# #     userX = get_frac("Enter X: ")
# #     userY = get_frac("Enter Y: ")
# #     result = 1 * userX/userY
# #     print(f"You have {result}available")

# #     if result >= 1:
# #         print("input an available fraction")
# #     else:
# #         main()


# # def get_int(prompt):
# #     while True:
# #         try:
# #             x = int(input(prompt))        
# #         except (ValueError, ZeroDivisionError):
# #             print("give me two actual numbers ")
# #         else:
# #             return x
        

# # if __name__ == "__main__":
# #     main()


# def main():
#     user = input("Enter a fraction: ")
    
#     while True:
        
#         try:
#             x_str, y_str =user.split("/")
#             x = int(x_str)
#             y = int(y_str)
#             if y == 0:
#                 print("Y cannot be zero")
#                 continue
                
#             if (x < 0 or y < 0):
#                 print("numbers cant be negative")
#                 continue
#             if x > y:
#                 print ('second number should be bigger try again')
#                 continue
#             break
#         except(ValueError, ZeroDivisionError):
#             print("enter a number")
    
    

#     percent = round(100 * (x / y))

#     if 99 <= 100*x/y:
#         print("F")
#     if 1 >= 100*x/y:
#         print("E")

#     else:
#         print(f"you have {percent}% ")
#     # print(f"you have {user} available")



    
    
# if __name__ == "__main__":
#      main()

def main():
    while True:
        user = input("Enter a fraction (X/Y): ").strip()
        try:
            x_str, y_str = user.split("/")
            x = int(x_str)
            y = int(y_str)

            if y == 0:
                print("Y cannot be zero. Try again.")
            elif x < 0 or y < 0:
                print("Numbers cannot be negative. Try again.")   
            elif x > y:
                print("X cannot be greater than Y. Try again.")     
            break
        except EOFError:
            break
        except (ValueError, ZeroDivisionError):
            print("Invalid input. Enter a fraction like X/Y with integers.")

    # Compute percentage
    percent = round(100 * x / y)

    # Print result
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")

if __name__ == "__main__":
    main()
