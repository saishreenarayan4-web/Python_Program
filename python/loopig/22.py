'''   no=22

        while no !=1 and no !=4:
            s = 0
            while no != 0:
                digit = no % 10
                s = s + digit
                no =  no // 10
            no = s

        if no == 1:
            print("happy number")
        else:
            print("not happy number")'''



for num in range(1, 1001,1):
    no = num

    while no != 1 and no != 4:
        s = 0
        while no != 0:
            digit = no % 10
            s = s + digit * digit   # FIXED (square)
            no = no // 10
        no = s

    if no == 1:
        print(num, "is a happy number") 
        if another w

