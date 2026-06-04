def age(a):
    next_year=a+1
    return next_year

a=input("Enter your age:")
if a.isdigit():
    a=int(a)
    print(age(a))      
else:
    print("Enter a valid age")    