def product(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


result = product(2, 3, 4, 5, 6)
print(result)
