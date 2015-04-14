import NonDestructiveList

#----------------------------------------------------------
# MergeSort.py
#----------------------------------------------------------

  

def test():
    c = NonDestructiveList.NonDestructiveList([1,3,5,1,5,3,7,5,8,6,9,2,5,4,7,1,3,2,4,9,7,8,5,3,4,2,5,6,7,1])
    print(MergeSort(c))

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
    if len(NonDestructiveList) <= 1:
        return(NonDestructiveList)

    mid = len(NonDestructiveList) // 2
    left = NonDestructiveList.FSlice(mid)
    right = NonDestructiveList.LSlice(mid)
    left = MergeSort(left)
    right = MergeSort(right)
    return(merge(left,right))
    
