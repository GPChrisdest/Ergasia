def sort(list: list):
    max_height = max(map(lambda c: c.get_height(), list))
    for i in range(1, len(list)):
        val= list[i]
        val_height = val.get_height()
        j =i-1
        while j >= 0 and val_height < list[j].get_height():
            list[j+1] = list[j]
            list[j].set_position(j+1, max_height)
            j-= 1
        list[j+1] = val
        val.set_position(j+1, max_height)
        
    return list
