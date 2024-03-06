user_number = int(input("Please enter a number between 1 and 100: "))

# Check if the number is even or odd
if (user_number % 2) == 0:
    result = "even"
else:
    result = "odd"

# Display the result
print(f"\n Your number {user_number} is {result}.\n")