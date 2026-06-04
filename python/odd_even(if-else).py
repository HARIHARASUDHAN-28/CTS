def oddoreven(n:int):
    if n%2==0:
        return "even"
    else:
        return "odd"


num=8
if isinstance(num,int):
    print(oddoreven(num))
else:
    print("enter valid number")