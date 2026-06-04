def multi(x:int,y:int):
    return x,y
    
    
a,b=10,30
if isinstance(a,int) and isinstance(b,int):
    print(multi(a,b)) 
else:
    print("Enter a valid datatype")