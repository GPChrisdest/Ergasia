import os
import random
from time import sleep

from insertion_sort_menu import sort


def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")


def list_options():
    list = []
    while True:
        clear_terminal()
        print("List Options:\n1. Generate random list\n2. Insert list\n3. View List")
        user_choice = input("Select an option: ")
        if user_choice == "":
            break  # Πρέπει να δούμε πώς θέλουμε να ελέγχουμε αν ήδη υπάρχει έγκυρη λίστα στην main
        elif not user_choice.isdigit() or int(user_choice) < 1 or int(user_choice) > 3:
            print("Invalid Choice!")
            continue
        user_choice = int(user_choice)
        if user_choice == 1:
            list = [random.randint(0, 100) for i in range(20)]
            print(f"List: {list}")
            sleep(2)
            break
        elif user_choice == 2:
            print("Insert each element one by one:")
            i = 0
            while i < 20:
                user_input = input(f"Element No.{i+1} ")
                if not user_input.isdigit():
                    print("Please input a number!")
                    continue
                list.append(int(user_input))
                i += 1
            print(f"List: {list}")
            sleep(2)
            break
        elif user_choice == 3:
            print(f"List: {list}")
            print("Press enter to return to previous menu")
            input()
            continue
    return list


def sort_menu(list):
    user_choice = 0
    while True:
        clear_terminal()
        print("Start Sorting:\n1. Plain sort\n2. Sort + Illustration")
        user_choice = input("Select an option: ")
        if user_choice == "":
            break
        elif not user_choice.isdigit() or int(user_choice) < 1 or int(user_choice) > 2:
            print("Invalid Choice!")
            continue
        user_choice = int(user_choice)
        break
    if user_choice == 1:
        print( f"\nSorted list: {sort(list)}")
        print("Press enter to return to main menu")
        input()
        return
    elif user_choice == 2:
        print("Work in progress!")
        sleep(1)
        return


def main():
    list = []
    while True:
        clear_terminal()
        print("1. List Options\n2. Start Sorting\n3. Exit")
        user_choice = input("Select and option: ")
        if not user_choice.isdigit or int(user_choice) < 1 or int(user_choice) > 3:
            print("Invalid Choice!")
            continue
        user_choice = int(user_choice)
        if user_choice == 1:
            list = list_options()
            continue
        elif user_choice == 2:
            sort_menu(list)
            continue
        elif user_choice == 3:
            break


if __name__ == "__main__":
    main()
