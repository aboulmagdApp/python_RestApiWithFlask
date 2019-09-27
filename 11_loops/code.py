# Using while
# number = 7

# while True:
#     user_input = input("would you like to play? (Y/n)")

#     if user_input == "n":
#         break

#     user_number = int(input("Guess our number: "))
#     if user_number == number:
#         print("you guessed correctly")
#     elif abs(number - user_number) == 1:
#         print("you were off by one.")
#     else:
#         print("sorry, it's wrong!")
#---------------------------------------------------
# Using For loop
# friends = ["Rolf","Jen","Bob","Anne"]

# for friend in friends:
#     print(f"{friend} is my friend.")
#------------------------------------
grades = [35, 67, 98, 100, 100]
total = sum(grades)
amount = len(grades)

print(total / amount)