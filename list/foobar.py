# Request a number from the user
num = int(input("Enter a number between 0 and 50: "))

# Check if the number is within the specified range
if 0 <= num <= 50:
    # Check for multiples of both 5 and 7
    if num % 5 == 0 and num % 7 == 0:
        print("FooBar")
    # Check for multiples of 5
    elif num % 5 == 0:
        print("Foo")
    # Check for multiples of 7
    elif num % 7 == 0:
        print("Bar")
    # Print the number itself if not a multiple of 5 or 7
    else:
        print(num)
else:
    print("Number out of range!")
