import logo2
logo = logo2.logo
print(logo)
def cal():
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
num1 = int(input("Enter the first operand\n"))
op = input("Enter your operation\n+\n-\n*\n/\n")
num2 = int(input("Enter the second operand\n"))
a = cal()
print(f'{num1}{op}{num2} = {a}')
n = input("if you want to continue press y else n").lower()
while n != "n":
    num1 = a
    op = input("Enter your operation\n")
    num2 = int(input("Enter the number\n"))
    b = cal()
    a = b
    print(f'{num1}{op}{num2} = {a}')
    n = input("if you want to continue press y else n").lower()
print(f"Your Final Answer is {a}")




