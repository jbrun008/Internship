import LinkedList

#----------------------------------------------------------
# MergeSort.py
#----------------------------------------------------------

class _Node:

    def __init__(self, data, next):
        self._data = data
        self._next = next

    def __repr__(self):
        return str(self._data)

class NonDestructiveList:

    def __init__(self, pythonList = []):
        self._length = len(pythonList)
        self._first = None
        for index in range(1, len(pythonList)+1):
            rest = self._first
            self._first = _Node(pythonList[-index], rest)

    def __len__(self):
        return self._length

    def first(self):
        return self._first._data

    def rest(self):
        r = NonDestructiveList()
        r._length = self._length - 1
        r._first = self._first._next
        return r

    def cons(self, item):
        newNode = _Node(item,self._first)
        r = NonDestructiveList()
        r._length = self._length + 1
        r._first = newNode
        return r

    def __repr__(self):
        tempNode = self._first
        stringN = ("LinkedList[" + repr(tempNode))
        for item in range(self._length - 1):
            tempNode = tempNode._next
            stringN = stringN + ", " + repr(tempNode)
        stringN = str(stringN + "]")
        return(stringN)

    def __getitem__(self, index):
        if index >= self._length or index < 0:
            raise IndexError
        tempNode = self._first
        if index < self._length:
            for item in range(int(index)):
                tempNode = tempNode._next
        return(tempNode._data)

    def FSlice(self, index):
        if index >= self._length or index < 0: 
            raise IndexError
        a = []
        tempNode = self._first
        if index < self._length:
            for item in range(int(index)):
                a.append(tempNode._data)
                tempNode = tempNode._next
        b = NonDestructiveList(a)
        return(b)

    def LSlice(self, index):
        if index >= self._length or index < 0: 
            raise IndexError
        a = []
        tempNode = self._first
        if index < self._length:
            for item in range(self._length):
                if item <= index:
                    tempNode = tempNode._next
                else:
                    a.append(tempNode._data)
                    tempNode = tempNode._next
        b = NonDestructiveList(a)
        return(b)
 
        













        


