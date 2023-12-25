def sort(list: list):
    i=1
    n=1
    while True:
        try:
            if list[i]<list[i-1]:   
                list[i-1],list[i]=list[i],list[i-1] #swap list elements if the previous number is lower 
                print('step {}:{}'.format(n,list))
                n+=1
                i=1   
            else:
                i+=1
        except IndexError:
            break
    return list