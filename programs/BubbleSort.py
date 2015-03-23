import LinkedList

#----------------------------------------------------------
# BubbleSort.py
#----------------------------------------------------------

def BubbleSort(k):
    for passes in range(len(k)-1,0,-1):
        for switches in range(passes):
            if k[switches]>k[switches+1]:
                temp = k[switches]
                k[switches] = k[switches+1]
                k[switches+1] = temp
    return(k)




