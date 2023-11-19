def sort(list):
    marker = 1  #Marks the item which we want to sort

    while marker < len(list):   #Loop repeats until we check the last item
        add = []    #A list where we put the items that are lower than our marked number

        if list[marker] <= list[0]:
            """If the marked number is smaller than the first
            we remove it from the main list and add it to the temporary list add[]
            Then combining the 2 lists together we have sorted the marked number"""
            add.append(list[marker])
            list.remove(list[marker])
            list = add + list
        else:
            new_marker = marker     #Setting a new marker so that we dont mix them up

            while list[new_marker] >= list[0]:   
                """We remove the items before the marked number until we reach one that is higher
                Then we add the marked number and combine the lists"""
                add.append(list[0])
                list.remove(list[0])
                new_marker -= 1     #We need to lower the marker because the length of the list changes

            add.append(list[new_marker])
            list.remove(list[new_marker])
            list = add + list
        marker += 1     #Increasing the marker so that we check all the items

    return list