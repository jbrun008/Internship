import NonDestructiveList

#----------------------------------------------------------
# MergeSort.py
#----------------------------------------------------------

  
def merge(a, b):
    if len(a) == 0:
        return b
    elif len(b) == 0:
        return a
    elif a.first() <= b.first():
        return merge(a.rest(), b).cons(a.first())
    else:
        return merge(b.rest(), a).cons(b.first())


def MergeSort(NonDestructiveList):
    n =  len(NonDestructiveList)
    if n<=1:
        return(NonDestructiveList)
    mid = n/ 2
    left = NonDestructiveList.FSlice(mid)
    right = NonDestructiveList.LSlice(mid)
    return(merge(MergeSort(left),MergeSort(right)))
    
