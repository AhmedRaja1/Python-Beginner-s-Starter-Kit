try:
    file = open("Cleaning up.py")
    age = int(input("age>>>"))
    xfactor = 10/age

except (ValueError, ZeroDivisionError):
    print("Please enter a valid age")
finally:
    file.close()
