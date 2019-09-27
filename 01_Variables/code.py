x = 15

price = 9.99

discount = 0.2

print(x)

name = 'aboulmagd'

greeting = f"Hello, {name}"

print(greeting)

longer_phrase = "Hello, {}. Today is {}."

formatted = longer_phrase.format("Rolf","Monday")
print(formatted)

size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_metres = square_feet / 10.8
print(f"{square_feet} square feet is {square_metres:.2f} square metres")