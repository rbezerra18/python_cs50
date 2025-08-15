def main():
    print_column(3)
    print()
    print_row(4)
    print()
    print_square(3)

def print_column(height):
    for _ in range(height):
        print("#")

def print_row(width):
    print("#" * width)

def print_square(size):
    for i in range(size):
        print_row(size)
        
main()