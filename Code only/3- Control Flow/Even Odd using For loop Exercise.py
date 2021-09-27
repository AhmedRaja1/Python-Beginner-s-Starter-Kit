even_number_counter = 0

for number in range(1, 30):
    if number % 2 == 0:
        print(number)
        even_number_counter += 1
print(f"We have {even_number_counter} Even Numbers")
