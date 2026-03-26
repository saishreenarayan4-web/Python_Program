no = int(input("Enter a number: "))

while no > 9:
    s = 0
    while no > 0:
        digit = no % 10
        s = s + digit
        no = no // 10
    no = s

print("Single digit:", no)
