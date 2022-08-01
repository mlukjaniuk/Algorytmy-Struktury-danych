arr = []
arr2 = []
f = open('readme.txt', 'r')
for line in f:
    line = line.strip()
    arr.append(line)
for i in arr:
    i = int(i)
    arr2.append(i)


#1
def heapify(arr, heapSize, i):
    l = (2*i)+1
    r = (2*i)+2
    if l < heapSize and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r < heapSize and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, heapSize, largest)
        return arr


def buildHeap(arr):
    heapSize = len(arr)
    k = int((len(arr)-2)/2)
    for i in range(k, -1, -1):
        heapify(arr, heapSize, i)
    return arr


def heapSort(arr):
    arr = buildHeap(arr)
    heapSize = len(arr)
    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[heapSize-1] = arr[heapSize-1], arr[0]
        heapSize -= 1
        heapify(arr, heapSize, 0)
    return arr


print(arr2)
print(heapSort(arr2))
with open('output.txt', 'w') as filehandle:
    for k in heapSort(arr2):
        filehandle.write('%s\n' % k)


#2
def iterative_heapify(arr, heapSize, i):
    done = False
    while not done:
        l = (2*i)+1
        r = (2*i)+2
        if l < heapSize and arr[l] > arr[i]:
            largest = l
        else:
            largest = i
        if r < heapSize and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest
        else:
            done = True
    return arr

