def check_even_odd(number):
    if (number % 2) == 0:
        return "even"
    else:
        return "odd"

def main():
    user_number = int(input("Please enter a number between 1 and 100: "))
    result = check_even_odd(user_number)
    print(f"\nYour number {user_number} is {result}.\n")

if __name__ == "__main__":
    main()