def floordiv(total_bill,people) ->int:
    share=total_bill//people
    return share

total_bill = "1250"
people = 4
if(isinstance(total_bill,int) and isinstance(people,int)):
    if total_bill>=0 and people>0:
        print(floordiv(total_bill,people))
else:
    print("Enter a valid number")    