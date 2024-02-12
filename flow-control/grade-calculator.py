# Ask the student for their grades in 5 subjects
History = float(input("Enter your grade for History: "))
Mathematics = float(input("Enter your grade for mathematics: "))
Physics = float(input("Enter your grade for physics: "))
Chemestry = float(input("Enter your grade for chemestry: "))
Literature = float(input("Enter your grade for Literature: "))

# Calculate the average grade
average_grade = ( History+ Mathematics + Physics + Chemestry + Literature) / 5

# Determine the overall grade
if average_grade > 90:
    overall_grade = "A"
elif average_grade > 80:
    overall_grade = "B"
elif average_grade > 70:
    overall_grade = "C"
elif average_grade > 60:
    overall_grade = "D"
else:
    overall_grade = "E (Failed)"

# Display the overall grade
print(f"Your average grade is: {average_grade}")
print(f"Your overall grade is: {overall_grade}")
