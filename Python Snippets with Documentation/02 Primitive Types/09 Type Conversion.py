# 09 Type Conversion
x = input("x: ")  # Even if the input is a number it will be read as a string
print(type(x))

y = int(x) + 5
print(f"x: {x} ; y: {y}")

# type converters
# int() converts to an interger
# str() converts to string
# float() converts to float

# bool() converts to boolean
# Falsy values - values that return False
print(bool(""))  # Double quotations returns False
print(bool(0))  # 0 returns False
print(bool(None))
# Other values return True
print(bool(2))

