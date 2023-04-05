from art import logo
import random
print(logo)
print("I'm guessing between 1 to 100.")


def check_guess(guess, generated_number):
    """returns the string based on the comparision."""
    if guess > generated_number:
        return "high"
    elif guess < generated_number:
        return "low"
    else:
        return "right"


def play_game():

    generated_number = random.randint(1, 100)
    difficulty = input("choose difficulty level : high or low >")
    number_of_attemps = 0
    if difficulty == "high":
        number_of_attemps = 5
    elif difficulty == "low":
        number_of_attemps = 10
    else:
        print(
            f"you have typed wrong input {difficulty}, which is not the option available. ")

    while number_of_attemps > 0:
        print(f"number of attemps {number_of_attemps}")
        guess = int(input("guess number: "))
        check = check_guess(guess, generated_number)
        if (check == "right"):
            number_of_attemps = -1
            print("you have guess right")

        elif check == "high":
            print("too high")
            number_of_attemps -= 1
        elif check == "low":
            print("too low")
            number_of_attemps -= 1
    if (number_of_attemps == 0):
        print(f"you are out of guess.")
        if (input("do you want to continue, type y for yes. ") == "y"):
            play_game()


play_game()
