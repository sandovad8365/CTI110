# Darrin Sandoval
# April 19, 2026
# P4HW2
# This program calculates gross pay for multiple employees using a sentinel loop.
# It tracks overtime pay, regular pay, gross pay totals, and the number of employees.

# Pseudocode:
# 1. Initialize variables: overtime_total = 0, regular_total = 0, gross_total = 0, employee_count = 0
# 2. Ask for employee name
# 3. While employee name is not "Done":
#       a. Ask for hours worked and pay rate
#       b. Calculate overtime hours and pay (if hours > 40)
#       c. Calculate regular pay
#       d. Calculate gross pay
#       e. Add to running totals (overtime_total, regular_total, gross_total)
#       f. Increment employee_count
#       g. Ask for next employee name (or "Done" to stop)
# 4. After the loop ends, display:
#       - Total number of employees entered
#       - Total overtime pay
#       - Total regular pay
#       - Total gross pay

print("Welcome to the Employee Payroll Calculator\n")

overtime_total = 0.0
regular_total = 0.0
gross_total = 0.0
employee_count = 0

while True:
    name = input("Enter employee's name or \"Done\" to terminate: ")
    
    if name.lower() == "done":
        break
    
    hours = float(input(f"How many hours did {name} work? "))
    rate = float(input(f"What is {name}'s pay rate? "))
    
    # Calculate pay
    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * rate * 1.5
        regular_pay = 40 * rate
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours * rate
    
    gross_pay = regular_pay + overtime_pay
    
    # Add to totals
    overtime_total += overtime_pay
    regular_total += regular_pay
    gross_total += gross_pay
    employee_count += 1
    
    print("-" * 40)

# Final Results
print("\n" + "=" * 50)
print("Total Employees Entered   :", employee_count)
print(f"Total Overtime Pay        : ${overtime_total:,.2f}")
print(f"Total Regular Pay         : ${regular_total:,.2f}")
print(f"Total Gross Pay           : ${gross_total:,.2f}")
print("=" * 50)