class Employe(object):
    def __init__(self, id, name, sal):
        self.Id = id
        self.Name = name
        self.sal = sal
        self.HR = 0.20 * sal      # 20% House Rent Allowance
        self.DA = 0.10 * sal      # 10% Dearness Allowance
        self.Total = sal + self.HR + self.DA

    def show(self):
        print("\n---------------- Employee Details ----------------")
        print(f"{'ID':<10}{'Name':<15}{'Basic':<12}{'HR':<12}{'DA':<12}{'Total':<12}")
        print("---------------------------------------------------")
        print(f"{self.Id:<10}{self.Name:<15}{self.sal:<12.2f}{self.HR:<12.2f}{self.DA:<12.2f}{self.Total:<12.2f}")
        print("---------------------------------------------------")


print("Enter Employee Id:")
Id = int(input())

print("Enter Employee Name:")
name = input()

print("Enter Salary of Employee:")
sal = float(input())

d = Employe(Id, name, sal)
d.show()