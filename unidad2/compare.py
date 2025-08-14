def compare1(x, y):
    if x < y:
        print("x is less than y")
    elif x > y:
        print("x is greater than y")
    else:
        print("x is equal to y")

def compare2(x, y):
    if x == y:
        print("x is equal to y")
    else:
        print("x is not equal to y")

def main():
    print("Starting comparison...")
    x = int(input("What's x? "))
    y = int(input("What's y? "))

    compare1(x, y)
    compare2(x, y)
    print("Comparison complete.")

main()