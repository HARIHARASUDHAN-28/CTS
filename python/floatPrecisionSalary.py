def float_salary(salary:float,tax_rate:float)->float:
    if salary<0 :return 0
    if tax_rate<0 or tax_rate>1: return 0
    tax=salary*tax_rate
    net_salary=salary-tax
    return net_salary
salary=75000.5
tax_rate=0.18
result=float_salary(salary,tax_rate)
print(f"{result:.2f}")