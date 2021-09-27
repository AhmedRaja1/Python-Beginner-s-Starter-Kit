import random
import string
password_list = string.ascii_letters + string.digits
password_generator = random.choices(password_list, k=8)
print(password_generator)
