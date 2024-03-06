# Loop through numbers from 1 to 15
for i in range(1, 16):
    # Check if the number is a multiple of both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print("FooBar")
    # Check if the number is a multiple of 3 only
    elif i % 3 == 0:
        print("Foo")
    # Check if the number is a multiple of 5 only
    elif i % 5 == 0:
        print("Bar")
    # If none of the above conditions are met, print the number itself
    else:
        print(i)
