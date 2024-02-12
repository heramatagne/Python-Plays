#This program converts body weight from from into kilogram according to the user input.

#define user input
body_weight_lbs = float(input("Please enter your body weight in pounds (lbs): "))

# Convert the weight from pounds to kilograms
body_weight_kg = body_weight_lbs / 2.204

#round the weight to 3 decimal places
rounded_weight_body_weight_kg = round(body_weight_kg, 3) 

# Display the weight in  pounds and kilograms with three decimal places
print(f"\nYour body weight is: {body_weight_lbs} lbs, and the equivalent in kgs is: {rounded_weight_body_weight_kg} kg.Thank you! \n")
