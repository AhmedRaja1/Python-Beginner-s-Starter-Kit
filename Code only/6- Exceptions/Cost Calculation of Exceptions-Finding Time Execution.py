from timeit import timeit

code1 = '''
def xfactor_cal(age):
    if age >= 10:
        raise ValueError("Age is not suitable")
    calculation = 10/age
    return calculation
'''

code2 = ''' 
def xfactor_cal(age):
    if age >= 10:
        return None
    calculation = 10/age
    return calculation
'''

print("first=", timeit(code1, number=10000))
print("second=", timeit(code2, number=10000))
