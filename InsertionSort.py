import LinkedList

#----------------------------------------------------------
# InsertionSort.py
#----------------------------------------------------------

def InsertionSort(LinkedList):

    for index in range(1,len(LinkedList)):

        cv = LinkedList[index]
        pos = index

        while pos>0 and LinkedList[pos-1]>cv:
         
            LinkedList[pos] = LinkedList[pos-1]
            pos = pos-1
            LinkedList[pos]=cv
    return(LinkedList)
