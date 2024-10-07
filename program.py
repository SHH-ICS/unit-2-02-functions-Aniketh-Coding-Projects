    

def hello_world():
    print("Hello World!")

def hello_user(name):
    return f"Hello, {name}!"

def hello_world():
    print("Hello World!")

def hello_user(name):
    return f"Hello, {name}!"


hello_world()  
print(hello_user("Aniketh")) 


def calculate_birth_year(name, age, had_birthday):
    current_year = 2024  
    if had_birthday.lower() == 'yes':
        birth_year = current_year - age
    else:
        birth_year = current_year - age - 1
    return f"{name}, you were born in {birth_year}."


name = input("What's your name? ")
age = int(input("How old are you? "))
had_birthday = input("Have you had a birthday this year? (yes/no) ")


print(calculate_birth_year(name, age, had_birthday))


for i in range(1, 33):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
