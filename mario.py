def main():
    print_square(int(input()))
   


def print_square(size):
    for i in range (size):
        print_row(size)

def print_row(size):
    print("#"* size)
main()