try:
    age = int(input("age>>>"))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("Please enter a valid age")

# except ZeroDivisionError:
    #print("Please enter a valid age")
