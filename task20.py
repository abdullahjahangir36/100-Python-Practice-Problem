# Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%), and 
# tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),(20< _   – 30%)(0-1lakh print k).
def calculate_in_hand_salary(gross_salary):
    # Deduction percentages
    HRA = 0.10  # 10%
    DA = 0.05   # 5%
    PF = 0.03   # 3%

    # Calculate deductions
    hra_deduction = gross_salary * HRA
    da_deduction = gross_salary * DA
    pf_deduction = gross_salary * PF

    # Calculate taxable salary after deductions
    taxable_salary = gross_salary - (hra_deduction + da_deduction + pf_deduction)

    # Calculate tax based on salary range
    if 500000 <= taxable_salary <= 1000000:
        tax = taxable_salary * 0.10  # 10%
    elif 1000001 <= taxable_salary <= 2000000:
        tax = taxable_salary * 0.20  # 20%
    elif taxable_salary > 2000000:
        tax = taxable_salary * 0.30  # 30%
    else:
        tax = 0
        print("No tax applicable, salary is less than 5 lakh.")

    # Calculate in-hand salary
    in_hand_salary = taxable_salary - tax

    return in_hand_salary

try:
    # Input from the user
    gross_salary = float(input("Enter your gross salary: "))

    if gross_salary >= 100000:
        # Calculate in-hand salary
        in_hand_salary = calculate_in_hand_salary(gross_salary)
        print(f"Your in-hand salary after all deductions is: {in_hand_salary:.2f}")
    else:
        print("Salary is less than 1 lakh. No deductions applied.")

except ValueError:
    print("Please enter a valid numeric value for the salary.")
