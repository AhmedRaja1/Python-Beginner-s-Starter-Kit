def product(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


result = product(1, 2, 3)
print(result)
