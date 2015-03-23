import LinkedList

#----------------------------------------------------------
# ShellSort.py
#----------------------------------------------------------





def ShellSort(LinkedList):
    sublist = len(LinkedList)//2
    while sublist> 0:

      for pos in range(sublist):
        gapInsertionSort(LinkedList,pos,sublist)

      sublist= sublist // 2
    return(LinkedList)

def gapInsertionSort(LinkedList,start,gap):
    for i in range(start+gap,len(LinkedList),gap):

        cv = LinkedList[i]
        pos= i

        while pos>=gap and LinkedList[pos-gap]>cv:
            LinkedList[pos]=LinkedList[pos-gap]
            pos = pos-gap

        LinkedList[pos]=cv

    
