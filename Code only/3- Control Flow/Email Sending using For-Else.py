message = "attempt"
successful = False

for number in range(1, 6):
    print(message, number)
    if successful:
        print("Sent Successfully!")
        break
else:
    print("Tried 5 times and failed sucessfully!")
