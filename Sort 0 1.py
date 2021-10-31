rom sys import stdin

def sortZeroesAndOne(arr, n) :
    j=-1
    for i in range(n):
        if arr[i]<1:
            j=j+1
            arr[i],arr[j]=arr[j],arr[i]
    for i in range(n):
        return arr[i]
    #Your code goes here 

























#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), 0

    
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = ' ')
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    sortZeroesAndOne(arr, n)
    printList(arr, n)
    print()

    t -= 1
