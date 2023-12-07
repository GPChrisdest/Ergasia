def sort(list: list):
    max_height = max(map(lambda c: c.get_height(), list))
    for i in range(1, len(list)):
        val= list[i]
        val_height = val.get_height()
        j =i-1
        while j >= 0 and val_height < list[j].get_height():
            try:
                list[j+2].set_color('green')
            except:
                pass
            list[j].set_color("red")  
            list[j+1].set_color("red")
            list[j+1].set_color("white") 
            list[j+1] = list[j]
            list[j].set_position(j+1, max_height)
            j-= 1
            list[j+1].set_color("white")  
        list[j+1] = val
        val.set_position(j+1, max_height)
        list[-1].set_color('white')
    i=1
    n=1
    while True:
        try:
            if list[i]<list[i-1]:   
                list[i-1],list[i]=list[i],list[i-1]
                n+=1
                i=1   
            else:
                i+=1
        except IndexError:
            break
    return list