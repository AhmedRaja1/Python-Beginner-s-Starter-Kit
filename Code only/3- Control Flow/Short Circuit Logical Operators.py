high_income = True
good_credit = True
defaulter = True

if high_income or good_credit and not defaulter:
    print("Eligible")
else:
    print("Not Eligible")
