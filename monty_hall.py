import random


def set_prize():
    doors = [0,0,0]
    index = random.randint(0,2)
    doors[index] = 1
    return doors


def initial_choice():
    return 0


def reveal_bad_door(initial_choice, doors):
    if doors[initial_choice] == 1:
        doors[initial_choice+2] = -1

    elif doors[initial_choice+1] == 1:
        doors[initial_choice+2] = -1

    else:
        doors[initial_choice+1] = -1

    return doors


def change_doors_or_not(change_value, initial_choice, doors):
    if change_value == 0:
        return initial_choice, doors

    elif change_value == 1:
        for index in range(len(doors)):
            if index != initial_choice and doors[index] != -1:
                return index, doors

    else:
        return 'broken', doors


def win_or_lose(final_choice, doors):

    if doors[final_choice] == 1:
        return 1

    if doors[final_choice] == 0:
        return 0

    else:
        return 'broken'


def main():
    print("Welcome to the Monty Hall Monte Carlo simulator")
    user_input = int(input('Choose 0 for always keep and 1 for always change: '))
    counter = 1
    win_total = 0
    while counter <= 1000:
        doors = set_prize()
        choice = initial_choice()
        doors = reveal_bad_door(choice, doors)
        choice, doors = change_doors_or_not(user_input, choice, doors)
        win_total += win_or_lose(choice, doors)
        counter += 1

    print("Win percentage: {}".format(win_total/counter))

if __name__ == '__main__':
    main()
