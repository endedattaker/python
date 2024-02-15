gross_salary = float(input("Enter your gross salary: "))
deductions = float(input("Enter deductions: "))


tax_rate = 0.2  

taxable_income = gross_salary - deductions

tax_amount = taxable_income * tax_rate

  
net_salary = gross_salary - tax_amount

print(f"Net Salary: ${net_salary:.2f}")

if net_salary>50000:
    print("high")
else:
    print("ok")

