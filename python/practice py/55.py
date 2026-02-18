print("enter a basic salary")
sal = float(input())
da,hra=0,0
if sal>=5000:
    da=sal*0.3
    hra=sal*0.2
total=sal+da+hra
print("basic sal=",sal)
print("da=",da)
print("hra=",hra)
print("total sal=",total)