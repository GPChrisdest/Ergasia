def sort(li: list):
    i=1
    n=1
    while True:
        try:
            if li[i]<li[i-1]:   
                li[i-1],li[i]=li[i],li[i-1]
                print('step {}:{}'.format(n,li))
                n+=1
                i=1   
            else:
                i+=1
        except IndexError:
            break
    return li
sort(li=[9, 5, 4, 6, 7, 3, 10, 2, 8])