def pound(kg):
    pounds=kg*2.20462
    return pounds


kg=float(input("enter a kg:"))
if kg>0:
    print(f"{pound(kg):.2f}")
else:
    print("Enter a positive KG")    