def add(x, y):
    result = x + y
    print(result)


add(2, 3)  # 5

def say_hello(name,surname):
    print(f"Hello, {name} {surname}")

#say_hello("Mohamed","aboulmagd")

say_hello(surname="aboulmagd",name="Mohamed")

def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")

divide(15,2)
divide(dividend=15, divisor=3)