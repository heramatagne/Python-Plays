# Define the first name
first_name = "Hera"

# Convert the first name to a list of characters
name_list = list(first_name)

# Iterate through the list of characters in reverse order
for i in range(len(name_list) - 1, -1, -1):
    # Print each character on a new line
    print(name_list[i])
