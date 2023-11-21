import random
from time import sleep

from insertion_sort import sort


def list_options():
    list = []
    while True:
        print("List Options:\n1. Generate random list\n2. Insert list\n3. View List")
        user_choice = input("Select an option: ")
        if (
            (not user_choice.isdigit() and user_choice != "")
            or int(user_choice) < 1
            or int(user_choice) > 3
        ):
            print("Invalid Choice!")
            continue
        user_choice = int(user_choice)
        if user_choice == 1:
            list = [random.randint(0, 10000) for i in range(20)]
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
                    i -= 1
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
        else:
            break  # Πρέπει να δούμε πώς θέλουμε να ελέγχουμε αν ήδη υπάρχει έγκυρη λίστα στην main
    return list


def sort_menu(list):
    user_choice = 0
    while True:
        print("Start Sorting:\n1. Plain sort\n2. Sort + Illustration")
        user_choice = input("Select an option: ")
        if not user_choice.isdigit() or int(user_choice) < 1 or int(user_choice) > 2:
            print("Invalid Choice!")
            continue
        user_choice = int(user_choice)
        break
    if user_choice == 1:
        print(f"Sorted list: {sort(list)}")
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