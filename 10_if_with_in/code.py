# movies_watched = {"the Matrix", "Green Book", "Her"}
# user_movie = input("Enter sonthing you've watched recently: ")

# if user_movie in movies_watched:
#     print(f"I've watched {user_movie} too!")
# else:
#     print("I haven't watched that yet.")

number = 7
user_input = input("Enter 'y' if you would like to play: ").lower()

if user_input == "y":
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("you guessed correctly")
    elif abs(number - user_number) == 1:
        print("you were off by one.")
    else:
        print("sorry, it's wrong!")
