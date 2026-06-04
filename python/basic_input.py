def basic(name:str)->str:
    greet=name+" welcome "
    return greet

name=str(input("Enter your name:"))
if name.strip():
    print("Enter a valid input")
    
print(basic(name))