def maxmin(salary:list)->tuple[int,int]:
    maxi=float('-inf')
    mini=float('inf')
    for i in range(len(salary)):
        if( not isinstance(salary[i],int) ) :
            return "Enter valid datatype"    
        else:
            
            if maxi<salary[i]:
                maxi=salary[i]
            if mini>salary[i]:
                mini=salary[i] 
    return maxi,mini        

salary=[50000, 75000, 62000, 95000]

print(maxmin(salary))
