def xfactor_cal(age):
    if age >= 10:
        raise ValueError("Age is not suitable")
    calculation = 10/age
    return calculation


xfactor_cal(20)
