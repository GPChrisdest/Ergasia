def sort(list: list):
    i = 1  # Starting index
    while i < len(list):  # Loop through the whole list
        for j in range(i - 1, -1, -1):  # Loop through indices below current index
            """If the previous item of the list is smaller than the current one(i), check if the one before that(j-1)
            is lower as well. If so, continue so that the check is run again with j = j-1. Otherwise, move the current
            item(i) just before j.
            """
            if list[i] < list[j]:
                if j - 1 >= 0 and list[i] < list[j - 1]:
                    continue
                val = list.pop(i)
                list.insert(j, val)
                i -= 1  # Decrement i to account for the insertion before current i, thus ensuring that all items are checked
                break
        i += 1  # Increment i and continue the loop
    return list
