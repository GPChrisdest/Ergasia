def sort(list: list):
    '''This function compers two elements, if the n+1 digit is lower than the n digit it swaps them,else it's move one element ahead.This method goes throw the whole list and ends when everything is set.
    Generally the sort function is the core of the project'''
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