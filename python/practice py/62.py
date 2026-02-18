print("enter basic sal ")
sal = float(input())

if sal >= 5000:
    da = sal * 0.3
    hra = sal * 0.2
else:
    da = sal * 0.2
    hra = sal * 0.1
print("basic sal=",sal)
print("da=",da)
print("hra=",hra)