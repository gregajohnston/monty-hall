import random


def initialize_strat():
    print("Welcome to the Monty Hall Monte Carlo simulator!")
    while True:
        user_input_strat = input("Choose 0 for always-keep-strategy and 1 for always-change-strategy: ")
        if user_input_strat in ['0', '1']:
            return int(user_input_strat)
        print("Please type 0 or 1.")


def initialize_runs():
    while True:
        user_input_runs = input("And choose the number of runs you want to test: ")
        try:
            user_input_runs = int(user_input_runs)
        except:
            print("Please type an integer.")

        if user_input_runs > 0:
            return user_input_runs
        else:
            print("Please type a number greater than 0.")


def set_doors(door_count=3):
    doors = [0] * door_count
    index = random.randint(0,len(doors)-1)
    doors[index] = 1
    return doors


def reveal_bad_door(choice, doors):
    doors_choice = []
    for index in range(len(doors)):
        if doors[index] == 0 and index != choice:
            doors_choice.append(index)

    doors[random.choice(doors_choice)] = -1

    return doors


def change_doors_or_not(change_value, initial_choice, doors):
    if change_value == 1:
        for index in range(len(doors)):
            if index != initial_choice and doors[index] != -1:
                return index, doors

    return initial_choice, doors



def win_or_lose(final_choice, doors):
    return doors[final_choice]


def main():
    user_input_strat = initialize_strat()
    user_input_runs = initialize_runs()

    counter, win_total = 1, 0
    initial_door, total_doors = 0, 3
    choice = random.randint(0,2)
    while counter <= user_input_runs:
        doors = set_doors(total_doors)
        doors = reveal_bad_door(choice, doors)
        choice, doors = change_doors_or_not(user_input_strat, choice, doors)
        win_total += win_or_lose(choice, doors)
        counter += 1

    print("Win percentage: {0:.1f}%".format(win_total/(counter-1)*100))


if __name__ == '__main__':
    main()
