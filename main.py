from random import randint
import cmd, sys


# Returns a random integer in the given boundaries
def get_random_num(low_bound, upp_bound):
    return randint(low_bound, upp_bound)


# Returns 0 if the number is correctly guessed.
# Returns 1 if the number is lower than expected.
# Returns 2 if the number is greater than expected.
def guess(num_to_guess, num_input):
    if num_input == num_to_guess:
        return 0
    elif num_input < num_to_guess:
        return 1
    else:
        return 2


def get_boundary_input():
    global low_bound
    global upp_bound

    try:
        low_bound = int(input("Enter the lower boundary:"))
        upp_bound = int(input("Enter the upper boundary:"))
    except ValueError:
        print("This is not a whole number!")

    if low_bound > upp_bound:
        print("Lower boundary cannot be greater than the upper boundary!")
        print("Please enter new values again:")
        get_boundary_input()
        return
    else:
        return {"low_bound": low_bound, "upp_bound": upp_bound}


def check_boundary_input():
    check = input("Is this correct? (y/n):")

    if check == "y":
        print("Continuing game")
        return
    elif check == "n":
        print("Please enter new boundaries:")
        get_boundary_input()
    else:
        print("Not the answer we were looking for!\nExiting game!")
        return


def main_game_loop(rand_num, boundaries):
    while True:
        num_input = 0
        try:
            num_input = int(input("Please enter a guess number:"))
        except ValueError:
            print("This is not a whole integer number!")
            continue
        gues_res = guess(rand_num, num_input)

        if gues_res == 0:
            print("You guessed correctly! %d was the answer!" % num_input)
            break
        elif gues_res == 1:
            print("Too low! Try again!")
        else:
            print("Too High! Try again!")


# Main function used for running the code
def run():
    print("Welcome! Please input a range to beginn the game!")

    boundaries = get_boundary_input()

    print(boundaries["low_bound"])

    print(
        "You entered: \nlower boundary: %s \nupper boundary: %s \n" % (boundaries["low_bound"], boundaries["upp_bound"])
    )

    check_boundary_input()

    main_game_loop(get_random_num(boundaries["low_bound"], boundaries["upp_bound"]), boundaries)


run()
