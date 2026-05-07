import random;
import math;

def password_generator(length:int)->str:
    new_password=[]
    for i in range(length):
        random_ord=math.floor(random.random()*(126-33)+33)
        new_password.append(chr(random_ord))
    return ''.join(new_password)

def init():
    print("**** Welcome to my password generator ****")
    length=input("Please enter password length:")
    print(password_generator(10),end="\nThank you!!")

init()