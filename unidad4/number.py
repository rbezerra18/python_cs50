def main():
    x = get_int("Enter a number integer (x): ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("x is not an integer. Please try again.")
        
main()