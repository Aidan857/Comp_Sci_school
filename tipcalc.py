
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollars = d.removeprefix("$")
    dollars = float(dollars)
    return dollars


def percent_to_float(p):
    percent = p.removeprefix("%")
    percent = float(percent)
    percent = percent/100
    return percent
main()


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d.removeprefix("$"))


def percent_to_float(p):
    return float (p.removeprefix("%"))/ 100


main()
