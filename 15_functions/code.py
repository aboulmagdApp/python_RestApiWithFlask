def Hello():
    print('Hello!')

Hello()

print("Welcome to the age in seconds program!")

def user_age_in_seconds():
    user_age = int(input("Enter your age here: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")


#user_age_in_seconds()

print("Goodbye!")

friends = ["Rolf", "Bob"]


def add_friend():
    friend_name = input("Enter your friend name: ")
    friends.append(friend_name)


add_friend()
print(friends)