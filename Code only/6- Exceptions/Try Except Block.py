try:
    age = int(input("age>>>"))
except ValueError as error:
    print("Please enter a valid age")
    print(error)
    print(type(error))
else:
    print("No Exceptions thrown")

print("Execution continues, try some valid age")
