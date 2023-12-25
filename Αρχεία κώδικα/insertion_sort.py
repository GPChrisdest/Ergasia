import time
import threading 

def sort(list: list):
    '''This def gets,from main.py,a random list given by the user and graphicly(with insertion sort algo) trys to sort every single number step by step.
    The user see the compering coloumns with red and with green the coloumn that the algo gona compare after the while loop ends.
    When the list is sorted the coloumns become purple'''
    from turtle1 import turtle1
    max_height = max(map(lambda c: c.get_height(), list)) #geting the max number of the list as the max height 
    for i in range(1, len(list)):
        val= list[i]
        val_height = val.get_height() #transleting list's number i into height
        j =i-1
        while j >= 0 and val_height < list[j].get_height(): #compare i and i-1 elements height
            try:
                list[j+2].set_color('green')
            except:
                pass 
            list[j].set_color("red")  
            list[j+1].set_color("white") 
            list[j+1] = list[j] #swaping the two elements
            list[j].set_position(j+1, max_height) #creating the "coloumn"
            j-= 1
            list[j+1].set_color("white")  
        list[j+1] = val 
        val.set_position(j+1, max_height)
        list[-1].set_color('white')
    
    def new_color():
        for i in range(len(list)):
            list[i].set_color('purple')
    
    action=threading.Timer(1.1,new_color)
    action.start()

    return list