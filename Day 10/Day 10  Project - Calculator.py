import logo2
logo = logo2.logo
print(logo)
def cal(num1 = int(input("Enter the first operand")), op = input("Enter your operation\n+\n-\n*\n/\n"),num2 = int(input("Enter the second operand"))):
    def add():
        return num1 + num2
    def sub():
        return num1 - num2
    def mul():
        return num1 * num2
    def div():
        return num1 / num2
    calculator = {
        "+" : add(),
        "-" : sub(),
        "*" : mul(),
        "/" : div()
    }
    return calculator[op]

a = cal()
n = input("if you want to continue press y else n").lower()
while n != "n":
    b = cal(num1 = a,op = input("Enter your operation\n+\n-\n*\n/\n"),num2 = int(input("Enter the number")))
    a = b
    n = input("if you want to continue press y else n").lower()
print(f'The answer is {a}')




