def is_happy(n):
    seen = set()
    
    while n != 1 and n not in seen:
        seen.add(n)
        s = 0
        
        while n > 0:
            digit = n % 10
            s += digit * digit
            n = n // 10
        
        n = s
    
    return n == 1

num = int(input("Enter number: "))
if is_happy(num):
    print("Happy Number")
else:
    print("Not a Happy Number")
