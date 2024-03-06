# assign value to variable number
numbers = [1, 123, 3456, 1111, 2662]

# Iterate over each number in the list of test cases
for number in numbers:
    # Check if the number has only one digit
    if number < 10:
        # If the number has only one digit, print it
        print(number)
    else:
        # If the number has more than one digit, iterate through its digits
        while number > 0:
            # Extract the last digit of the number using modulus operator
            print(number % 10, end="")
            # Remove the last digit from the number
            number //= 10
        # Print a newline after printing all the digits of the number
        print("")
