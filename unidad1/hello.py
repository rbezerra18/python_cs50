"""
# Ask user for their name, remove whitespace and capitalize user's name
name = input("What's your name? ").strip().title()

# Split user's name into first and last name
first_name, last_name = name.split(" ")

# Say hello to user
print(f"Hello, {first_name}!")
print(f"Hello, Mr. {last_name}!")
"""

# Refactor the code above into functions
def main():
    hello()
    name = input("What's your name? ").strip().title()
    hello(name)

def hello(to = "World"):
    print("Hello,", to)

main()