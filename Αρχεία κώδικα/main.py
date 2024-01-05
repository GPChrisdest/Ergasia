import os
import random
from time import sleep

from insertion_sort_menu import sort
from turtle1 import turtle1

def clear_terminal(): 
    '''Clears terminal baised on the system'''
    if os.name == "nt": #check if the os is windows and runs the equivalent command to clear the terminal, in this case its "cls"
        os.system("cls")
    elif os.name == "posix": #if the os isn't windows the command "clear" runs instead
        os.system("clear")

def list_options(list):
    '''Creats a mini menu in which the user can creat the list that he wants,or a random list and then see it '''
    list = list
    while True:
        clear_terminal()
        print("List Options:\n1. Generate random list\n2. Insert list\n3. View List")
        user_choice = input("Select an option: ")
        if user_choice == "":
            break  
        elif not user_choice.isdigit() or int(user_choice) < 1 or int(user_choice) > 3:
            print("Invalid Choice!")
            continue
        user_choice = int(user_choice)
        if user_choice == 1:
            clear_terminal()
            user_range = input("Give range of numbers(min-max):") 
            try:
                user_am = int(input("Give length of the ramdom list:"))
                start, end = user_range.split("-" )  
                start = int(start)
                end = int(end)
                if (start >= end): 
                    y = int("k") # in this way the code informs the user that the input has something wrong
            except ValueError:
                print("Wrong input!")
                sleep(3)
                list_options()
            list = [random.randint(start, end) for i in range(user_am)]
            print(f"List: {list}")
            sleep(2)
            break
        elif user_choice == 2:
            print("Insert each element one by one:")
            i = 0
            while True:
                user_input = input(f"Element No.{i+1} ")
                if user_input == "":
                    clear_terminal()
                    sleep(0.5)
                    break
                elif not user_input.isdigit():
                    print("Please input a number!")
                    continue
                list.append(int(user_input))
                i += 1
            print("The given list is:")
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
    '''This function creats a sorting menu which compins with the other code files'''
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
        print(f"\nSorted list: {sort(list)}")
        print("Press enter to return to main menu")
        input()
        return
    elif user_choice == 2:
        print("Work in progress!")
        turtle1(list)
        sleep(1)
        return

def main():  
    '''It cpmpins all the function into a new menu '''
    list = []
    while True: 
        clear_terminal()
        print("1. List Options\n2. Start Sorting\n3. Exit")
        user_choice = input("Select and option: ")
        if not user_choice.isdigit() or int(user_choice) < 1 or int(user_choice) > 3:
            print("Invalid Choice!")
            continue
        user_choice = int(user_choice)
        if user_choice == 1:
            list = list_options(list)
            continue
        elif user_choice == 2:
            if list == []:
                list = list_options()
            else:
                sort_menu(list)
                continue
        elif user_choice == 3:
            break

if __name__ == "__main__":  
    main()