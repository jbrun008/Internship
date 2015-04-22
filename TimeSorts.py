import LinkedList
import time
import ShellSort
import BubbleSort
import InsertionSort
import SelectionSort
import random
#----------------------------------------------------------
# TimeSorts.py
#----------------------------------------------------------
# Create Data
#----------------------------------------------------------
dataList = []

def createData(m):
    f = open("Data.txt","w")
    for i in range(m):
        ran = random.randint(1,100)
        f.write(str(ran) + ",")
    f.close()


def readInData():
    dataList = []
    f = open("Data.txt","r")
    for line in f:
        dataList = (line.split(','))
    return(dataList)


def BubbleSortTime(m):
    aTime = 0.0
    createData(m)
    dataList = readInData()
    inputList = LinkedList.LinkedList(dataList)
    aStartTime = time.time()
    inputList = BubbleSort.BubbleSort(inputList)
    aEndTime = time.time()
    aTime = aEndTime-aStartTime
    print("BubbleSort         : " + str(aTime))
    

def ShellSortTime(m):
    bTime = 0.0
    createData(m)
    inputList = LinkedList.LinkedList(readInData())
    bStartTime = time.time()
    b = ShellSort.ShellSort(inputList)
    bEndTime = time.time()
    bTime = bEndTime-bStartTime
    print("ShellSort          : " + str(bTime))

def InsertionSortTime(m):
    cTime = 0.0
    createData(m)
    inputList = LinkedList.LinkedList(readInData())
    cStartTime = time.time()
    c = InsertionSort.InsertionSort(inputList)
    cEndTime = time.time()
    cTime = cEndTime-cStartTime
    print("InsertionSort      : " + str(cTime))

def SelectionSortTime(m):
    dTime = 0.0
    createData(m)
    inputList = LinkedList.LinkedList(readInData())
    dStartTime = time.time()
    d = SelectionSort.SelectionSort(inputList)
    dEndTime = time.time()
    dTime = dEndTime-dStartTime
    print("SelectionSort      : " + str(dTime))

def MergeSortTime(m):
    etime = 0.0
    createData(m)
    inputList = LinkedList.LinkedList(readInData())
    eStartTime = time.time()
    e = SelectionSort.SelectionSort(inputList)
    eEndTime = time.time()
    eTime = eEndTime-eStartTime
    print("Recursive MergeSort : " + str(eTime))


for i in range(100,450,50):
    print(str(i) + " Items:\n")
    BubbleSortTime(i)
    ShellSortTime(i)
    InsertionSortTime(i)
    SelectionSortTime(i)
    MergeSortTime(i)
    print("\n")




