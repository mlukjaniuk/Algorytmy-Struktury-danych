import numpy as np
from timeit import default_timer as timer
from tabulate import tabulate
import random
import sys
import threading
def sortowanie_szybkie():

    # Podstawowy QuickSort
    def partition(arr, left, right):
        pivot = arr[right]
        i = left - 1
        for j in range(left, right + 1):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        if i < right:
            return i
        else:
            return i - 1


    def quickSort(arr, left, right):
        if left < right:
            q = partition(arr, left, right)
            quickSort(arr, left, q)
            quickSort(arr, q + 1, right)


    # Randomized QuickSort
    def randomizedPartition(arr, left, right):
        k = random.randint(left, right)
        arr[k], arr[right] = arr[right], arr[k]
        return partition(arr, left, right)

    def randomizedQuickSort(arr, left, right):
        if left < right:
            q = randomizedPartition(arr, left, right)
            randomizedQuickSort(arr, left, q)
            randomizedQuickSort(arr, q + 1, right)


    # QuickSort z pivotem jako medianą
    def medianaPartition(arr, left, right):
        dlugosc = right - left
        if dlugosc % 2 == 0:
            mid = dlugosc // 2
        else:
            mid = dlugosc // 2 + 1
        tablica = [arr[left], arr[right], arr[mid]]
        tablica.remove(max(tablica))
        tablica.remove(min(tablica))
        pivot = tablica[0]
        i = left - 1
        for j in range(left, right + 1):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        if i < right:
            return i
        else:
            return i - 1


    def medianaQuickSort(arr, left, right):
        if left < right:
            q = medianaPartition(arr, left, right)
            medianaQuickSort(arr, left, q)
            medianaQuickSort(arr, q + 1, right)


    rozmiary = [1000, 5000, 10000, 15000]
    tab1 = np.random.randint(500, size=1000)
    tab2 = np.random.randint(500, size=5000)
    tab3 = np.random.randint(500, size=10000)
    tab4 = np.random.randint(500, size=15000)
    tabs = [tab1, tab2, tab3, tab4]
    x = 20
    tab5 = []
    tab6 = []
    tab7 = []
    tab8 = []
    for i in range(0, 1000):
        x += 2
        tab5.append(x)
    for i in range(0, 5000):
        x += 2
        tab6.append(x)
    for i in range(0, 10000):
        x += 2
        tab7.append(x)
    for i in range(0, 15000):
        x += 2
        tab8.append(x)
    tabs2 = [tab5, tab6, tab7, tab8]
    czas1 = []
    czas2 = []
    czas3 = []
    czas4 = []
    czas5 = []
    czas6 = []
    for tab in tabs:
        start = timer()
        quickSort(tab, 0, len(tab) - 1)
        stop = timer()
        Tn = stop - start
        czas1.append(Tn)

    for tab in tabs:
        start = timer()
        randomizedQuickSort(tab, 0, len(tab) - 1)
        stop = timer()
        Tn = stop - start
        czas2.append(Tn)

    for tab in tabs:
        start = timer()
        medianaQuickSort(tab, 0, len(tab) - 1)
        stop = timer()
        Tn = stop - start
        czas3.append(Tn)

    for tab in tabs2:
        start = timer()
        quickSort(tab, 0, len(tab) - 1)
        stop = timer()
        Tn = stop - start
        czas4.append(Tn)

    for tab in tabs2:
        start = timer()
        randomizedQuickSort(tab, 0, len(tab) - 1)
        stop = timer()
        Tn = stop - start
        czas5.append(Tn)

    for tab in tabs2:
        start = timer()
        medianaQuickSort(tab, 0, len(tab) - 1)
        stop = timer()
        Tn = stop - start
        czas6.append(Tn)

    dane_losowe = {'Rozmiar tablicy': rozmiary, 'Czas - algorytm 1': czas1,
                   'Czas - algorytm 2': czas2, 'Czas - algorytm 3': czas3}
    dane_niekorzystne = {'Rozmiar tablicy': rozmiary, 'Czas - algorytm 1': czas4,
                   'Czas - algorytm 2': czas5, 'Czas - algorytm 3': czas6}
    print('\nDANE LOSOWE:')
    print(tabulate(dane_losowe, headers='keys', tablefmt='fancy_grid'))
    print('\nDANE NIEKORZYSTNE:')
    print(tabulate(dane_niekorzystne, headers='keys', tablefmt='fancy_grid'))


sys.setrecursionlimit(150000)
threading.stack_size(0x2000000)
sortowanie = threading.Thread(target=sortowanie_szybkie)
sortowanie.start()
