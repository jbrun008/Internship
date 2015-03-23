

# LinkedList.py


NULL = None


#----------------------------------------------------------------------------
# Node Class
#----------------------------------------------------------------------------
class _Node(object):

    def __init__(self, previous, data, next):
        self.next = next
        self.previous = previous
        self.data = data
        
    def getData(self):
        return (self.data)
    def getNext(self):
        return (self.next)
    def getPrevious(self):
        return (self.previous)
    def setData(self, newData):
        self.data = newData
    def setNext(self, newNext):
        self.next = newNext
    def setPrevious(self, newPrevious):
        self.previous = newPrevious
    def hasNext(self):
        if self.next != NULL:
            return(True)
#----------------------------------------------------------------------------
# Linked List Class
#--------------------------------------------------------------------

class LinkedList(object):
    # Doubly linked list.
    # Constructed with dummy nodes at the begining and at the end.
    # The list object stores references to the dummy nodes
    # and stores list's length.

    def __init__(self, list):

        self.node1 = _Node(NULL,NULL,NULL)
        self.node2 = _Node(NULL,NULL,NULL)
        self.node1.setNext(self.node2)
        self.node2.setPrevious(self.node1)
        self._Length = 0
        
        for i in list:
            self.insertItemAtTheEnd(i)


    def __len__(self):
        
        return self._Length

    def _nodeBeforeIndex(self, index):
        
        tempNode = self.node1
        if index <= self._Length:
            i = 0
            while i <= index:
                tempNode = tempNode.getNext()
                i+= 1
        return(tempNode.getPrevious().getData())

        

    def __getitem__(self, index):
        
        tempNode = self.node1
        if index <= self._Length:
            i = 0
            while i <= index:
                tempNode = tempNode.getNext()
                i = i + 1
            return (tempNode.getData())

    def __setitem__(self, index, item):
        
        tempNode = self.node1
        if index <= self._Length:
            i = 0
            while i <= index:
                tempNode = tempNode.getNext()
                i = i + 1
            tempNode.setData(item)

        

    def _insertItemAfterNode(self, item, aNode):
        
        i = 0
        tempNode = self.node1
        if aNode <= self._Length:
            while i <=aNode:
                tempNode = tempNode.getNext()
                i +=1
            newNode = _Node(tempNode, item, tempNode.getNext())
            tempNode.getNext().setPrevious(newNode)
            tempNode.setNext(newNode)
        self._Length +=1

       

    def insertItemAtTheFront(self, item):
        
        tempNode = _Node(self.node1, item, self.node1.getNext())
        self.node1.setNext(tempNode)
        self.node1.getNext().setPrevious(tempNode)
        self._Length +=1

        

    def insertItemAtTheEnd(self, item):
        
        tempNode = _Node(self.node2.getPrevious(), item, self.node2)
        self.node2.getPrevious().setNext(tempNode)
        self.node2.setPrevious(tempNode)
        self._Length +=1
        

    def insertItemAtIndex(self, index, item):
        
        i = 0
        tempNode = self.node1
        if index <= self._Length:
            while i <= index:
                tempNode = tempNode.getNext()
                i +=1
            newNode = _Node(tempNode.getPrevious(), item, tempNode)
            tempNode.getPrevious().setNext(newNode)
            tempNode.setPrevious(newNode)
            self._Length +=1
        

    def _deleteItemAfterNode(self, aNode):
        
        i = 0
        tempNode = self.node1
        if aNode <= self._Length-1:
            while i <=aNode:
                tempNode = tempNode.getNext()
                i +=1
            tempNode.getNext().getNext().setPrevious(tempNode)
            anode =  tempNode.getNext().getNext()
            tempNode.setNext(anode)
            self._Length -= 1

        

    def deleteItemAtTheFront(self):
        
        tempNode = self.node1.getNext().getNext()
        self.node1.setNext(tempNode)
        tempNode.setPrevious(self.node1)
        self._Length -= 1
       

    def deleteItemAtTheEnd(self):
        
        tempNode = self.node2.getPrevious().getPrevious()
        self.node2.setPrevious(tempNode)
        tempNode.setNext(self.node2)
        self._Length -= 1

        

    def deleteItemAtIndex(self, index):
        
        i = 0
        tempNode = self.node1
        if index <= self._Length:
            while i <= index:
                tempNode = tempNode.getNext()
                i +=1
            tempNode.getPrevious().setNext(tempNode.getNext())
            tempNode.getNext().setPrevious(tempNode.getPrevious())
            self._Length -= 1

        

    def deleteAll(self):
        
        self.node1.setNext(self.node2)
        self.node2.setPrevious(self.node1)
        self._Length = 0
        

    def __iter__(self):
        
        return(_LinkedListIterator(self))


        

    def __repr__(self):

        tempNode = self.node1.getNext()
        stringL = "LinkedList(["
        while tempNode.hasNext():
            stringL = stringL + str(tempNode.getData())
            if tempNode.getNext() != self.node2:
                stringL += ", "
            tempNode = tempNode.getNext()
        stringL = stringL + "])"
        return(stringL)







    def __eq__(self, otherLinkedList):
        
        if self._Length == len(otherLinkedList):
            counter = 0
            it = iter(otherLinkedList)
            tempNode = self.node1.getNext()
            while counter <= self._Length and next(it) != StopIteration:
                if tempNode.getData() != next(it):
                    return(False)
                counter += 1
                tempNode = tempNode.getNext()
            return(True)


        

    def copy(self):
        
        c = self
        return (c)

        

#----------------------------------------------------------------------------
class _LinkedListIterator(object):

    def __init__(self, aLinkedList):

        self.list = aLinkedList
        self.counter = 0
       

    def __iter__(self):

        return(self)
        
        

    def __next__(self):
        
        if self.counter < len(self.list):
            tempNode = self.list[self.counter]
            self.counter += 1
            return(tempNode)
        else:
            raise StopIteration



#----------------------------------------------------------------------------









