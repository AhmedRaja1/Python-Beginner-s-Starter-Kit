try:
    with open("Cleaning up.py") as file:
        print("Good Job")
    age = int(input("age>>>"))
    xfactor = 10/age

except (ValueError, ZeroDivisionError):
    print("Please enter a valid age")
