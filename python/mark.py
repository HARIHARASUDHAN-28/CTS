def std_mark(mark):
    if mark<40:
        return "fail"
    else:
        return "Pass"

mark=75
if   0<=mark<=100:
    print(std_mark(mark))
else:
    print("enter a valid mark")    