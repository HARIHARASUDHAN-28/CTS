def std_mark(mark):
    if mark<50:
        return "fail"
    elif 50<=mark<75:
        return "C"
    elif 75<=mark<90:
        return "B"
    else:
        return "A"

mark=88
if   0<=mark<=100:
    print(std_mark(mark))
else:
    print("enter a valid mark")    