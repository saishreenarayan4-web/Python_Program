for no in range(1, 21,1):
    if no == 0 or no == 1:
        continue
    c = 0
    for d in range(2, no // 2 + 1,1):
        if no % d == 0:
            c = c + 1
    if c == 0:
        print(no, "is prime number")
   