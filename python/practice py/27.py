print("enter principle, rate of intrest, time")
p = float(input("enter principle amount"))
r = float(input("enter rate of intrest"))
t = float(input("enter time in year"))
ci = p*(1+r/100)**t
print("principle amount=",p)
print("rate of intrest=",r)
print("time in year=",t)
print("compound intrest=",ci)