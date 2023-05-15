import random

game_choices = ["1", "2", "3", "4", "5", "6"]
user_runs, computer_runs = 0, 0


def valid_usr_choice(choice):
    while choice not in game_choices:
        choice = input("Kindly choose a number between 1 to 6: ")

    return int(choice)


def even_odd(num):
    if num % 2 == 0:
        return "EVEN"
    else:
        return "ODD"


def check_winner(user_score, computer_score):
    if user_score == computer_score:
        print("It was a TIE 🙂")
    elif user_score > computer_score:
        print("You WON the game 🥳")
    else:
        print("You LOST the game ☹️")


def user_is_bat():
    user_counter, computer_counter = 0, 0
    print()
    print("User is the bat".center(29, "-"))

    usr = input("Choose a number between 1 to 6: ")
    usr = valid_usr_choice(usr)
    comp = int(random.choice(game_choices))

    while usr != comp:
        user_counter += usr
        usr = input("Choose a number between 1 to 6: ")
        usr = valid_usr_choice(usr)
        comp = int(random.choice(game_choices))

    else:
        print()
        print("Computer is the bat".center(29, "-"))
        comp = int(random.choice(game_choices))
        usr = input("Choose a number between 1 to 6: ")
        usr = valid_usr_choice(usr)

        while comp != usr:
            computer_counter += comp
            comp = int(random.choice(game_choices))
            usr = input("Choose a number between 1 to 6: ")
            usr = valid_usr_choice(usr)
    return user_counter, computer_counter


def computer_is_bat():
    print()
    print("Computer is the bat".center(29, "-"))
    user_counter, computer_counter = 0, 0

    comp = int(random.choice(game_choices))
    usr = input("Choose a number between 1 to 6: ")
    usr = valid_usr_choice(usr)

    while comp != usr:
        computer_counter += comp
        comp = int(random.choice(game_choices))
        usr = input("Choose a number between 1 to 6: ")
        usr = valid_usr_choice(usr)
    else:
        print()
        print("User is the bat".center(29, "-"))
        usr = input("Choose a number between 1 to 6: ")
        usr = valid_usr_choice(usr)
        comp = int(random.choice(game_choices))

        while usr != comp:
            user_counter += usr
            usr = input("Choose a number between 1 to 6: ")
            usr = valid_usr_choice(usr)
            comp = int(random.choice(game_choices))

    return user_counter, computer_counter


print("ODD/EVEN GAME".center(28, "*"))
user_input = input("    Choose(1 or 2)    \n1.EVEN  2.ODD  : ")

while user_input != "1" and user_input != "2":
    user_input = input("    Ensure choose is either 1 or 2    \n1.EVEN  2.ODD  : ")
else:
    user_input = int(user_input)
    if user_input == 1:
        user, computer = "EVEN", "ODD"
    else:
        user, computer = "ODD", "EVEN"

    user_choice_number = input("Choose a number between 1 to 6: ")
    user_choice_number = valid_usr_choice(user_choice_number)

    computer_choice_number = random.choice(game_choices)
    toss = int(user_choice_number) + int(computer_choice_number)

    if user == even_odd(toss):
        user_position, computer_position = "Bat", "Ball"
    else:
        user_position, computer_position = "Ball", "Bat"

    print()
    print(f" Toss = {toss}({even_odd(toss)}) User:{user}  computer:{computer}\nTherefore...  User:{user_position}\
     Computer:{computer_position}")

    if user_position == "Bat":
        user_runs, computer_runs = user_is_bat()
        print(f"User runs:{user_runs} - Computer_runs:{computer_runs}")
    else:
        user_runs, computer_runs = computer_is_bat()
        print(f"User runs:{user_runs} - Computer_runs:{computer_runs}")

check_winner(user_score=user_runs, computer_score=computer_runs)
