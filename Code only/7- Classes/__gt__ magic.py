class Numbers:
    def number1(self):
        print("14")

    def number2(self):
        print("5")

    def __gt__(self, other):
        return num1 == num2


num1 = Numbers()
num2 = Numbers()
print(num1 > num2)
