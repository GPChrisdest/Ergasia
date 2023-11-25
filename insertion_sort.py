def sort(list: list):
    max_height = max(map(lambda c: c.get_height(), list))
    i = 1  # Starting index
    while i < len(list):  # Loop through the whole list
        for j in range(i - 1, -1, -1):  # Loop through indices below current index
            """If the previous item of the list is smaller than the current one(i). If so, move the current
            item(i) just at index j.
            """
            if list[i].get_height() < list[j].get_height():
                # if j - 1 >= 0 and list[i].get_height() < list[j - 1].get_height():
                #     continue
                list[i].set_color("red")
                val = list.pop(i)
                val.set_position(j, max(map(lambda c: c.get_height(), list)))
                for k in range(j, i):
                    list[k].set_position(k + 1, max_height)
                list.insert(j, val)
                list[j].set_color("blue")
                i -= 1
            else:
                break
        i += 1  # Increment i and continue the loop
    return list
