# Dictionary containing information about employees and owners
d = {
    "employees": [
        {"firstName": "John", "lastName": "Doe"},
        {"firstName": "Anna", "lastName": "Smith"},
        {"firstName": "Peter", "lastName": "Jones"}
    ],
    "owners": [
        {"firstName": "Jack", "lastName": "Petter"},
        {"firstName": "Jessy", "lastName": "Petter"}
    ]
}

# Print out the last name of the second employee (Anna Smith)
print(d["employees"][1]["lastName"])
