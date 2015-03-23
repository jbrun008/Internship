import LinkedList

#----------------------------------------------------------
# SelectionSort.py
#----------------------------------------------------------

def SelectionSort(LinkedList):
    
    for index in range(0,len(LinkedList)):

        pos = index
        currentMinPos = pos
        
        while pos < len(LinkedList):
            
            if LinkedList[pos] < LinkedList[currentMinPos]:
                
                currentMinPos = pos
                
            pos = pos+1
            
        temp = LinkedList[index]
        LinkedList[index] = LinkedList[currentMinPos]
        LinkedList[currentMinPos] = temp

    return(LinkedList)
