# ============================================
# BMI Calculator
# Beginner Tier - Oasis Infobyte SIP
# ============================================

print("===================================")
print("        BMI CALCULATOR")
print("===================================")

try:
    # Get user input
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    # Validate input
    if weight <= 0 or height <= 0:
        print("\nError: Weight and height must be greater than zero.")

    else:
        # Calculate BMI
        bmi = weight / (height ** 2)

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        # Display results
        print("\n========== RESULT ==========")
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")
        print("============================")

except ValueError:
    print("\nError: Please enter numeric values only.")