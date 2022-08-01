from tabulate import tabulate


class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def wstaw(self, key):
        x = Node(key)
        if self.head is None:
            self.head = x
            return 0
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = x
            return 1

    def drukuj(self):
        temp = self.head
        while temp:
            print(f"{temp.key}")
            temp = temp.next

    def sumuj(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count


class HashTable:
    def __init__(self, capacity=None, option=None):
        self.length = 0
        self.capacity = capacity
        self.option = option
        self.buckets = [LinkedList() for i in range(0, self.capacity)]

    def hashuj(self, key):
        if self.option == 'W':
            return hash(key) % self.capacity
        elif self.option == 'D':
            a = len(key)
            counter = 0
            for i in range(0, a - 1):
                counter = counter + ord(key[i]) * 111
            counter = counter * 111 + ord(key[a - 1])
            return counter % self.capacity
        else:
            a = len(key)
            counter = 0
            for i in range(0, a):
                counter = counter + ord(key[i])
            return counter % self.capacity

    def drukuj(self):
        for i in range(0, self.capacity):
            print('Index:', i)
            self.buckets[i].drukuj()
            print('-----')

    def wstaw(self, key):
        index = self.hashuj(key)
        add = self.buckets[index].wstaw(key)
        if add == 0:
            self.length += 1

    def ilepustych(self):
        return self.capacity - self.length

    def srdlugosc(self):
        a = self.length
        counter = 0
        for i in range(0, self.capacity):
            counter = counter + self.buckets[i].sumuj()
        return counter/a

    def maxdlugosc(self):
        max = 0
        for i in range(0, self.capacity):
            if self.buckets[i].sumuj() > max:
                max = self.buckets[i].sumuj()
        return max


arr = []
arr2 = []
f = open('3700.txt', 'r')
for line in f:
    line = line.strip()
    arr.append(line)
for i in arr:
    arr2.append(i)


w17 = HashTable(17, 'W')
for i in range(0, 2*17):
    w17.wstaw(arr2[i])
print('\nWydruk tablicy W17:\n')
w17.drukuj()

w1031 = HashTable(1031, 'W')
for j in range(0, 2*1031):
    w1031.wstaw(arr2[j])

w1024 = HashTable(1024, 'W')
for j in range(0, 2*1024):
    w1024.wstaw(arr2[j])


d17 = HashTable(17, 'D')
for i in range(0, 2*17):
    d17.wstaw(arr2[i])
print('\nWydruk tablicy D17:\n')
d17.drukuj()

d1031 = HashTable(1031, 'D')
for j in range(0, 2*1031):
    d1031.wstaw(arr2[j])

d1024 = HashTable(1024, 'D')
for j in range(0, 2*1024):
    d1024.wstaw(arr2[j])


s17 = HashTable(17, 'S')
for i in range(0, 2*17):
    s17.wstaw(arr2[i])
print('\nWydruk tablicy S17:\n')
s17.drukuj()

s1031 = HashTable(1031, 'S')
for j in range(0, 2*1031):
    s1031.wstaw(arr2[j])

s1024 = HashTable(1024, 'S')
for j in range(0, 2*1024):
    s1024.wstaw(arr2[j])


rozmiary = [17, 1031, 1024]
dane = [['W17', w17.ilepustych(), w17.maxdlugosc(), w17.srdlugosc()], ['D17', d17.ilepustych(), d17.maxdlugosc(),
        d17.srdlugosc()], ['S17', s17.ilepustych(), s17.maxdlugosc(), s17.srdlugosc()], ['W1031', w1031.ilepustych(),
        w1031.maxdlugosc(), w1031.srdlugosc()], ['D1031', d1031.ilepustych(), d1031.maxdlugosc(), d1031.srdlugosc()],
        ['S1031', s1031.ilepustych(), s1031.maxdlugosc(), s1031.srdlugosc()], ['W1024', w1024.ilepustych(),
        w1024.maxdlugosc(), w1024.srdlugosc()], ['D1024', d1024.ilepustych(), d1024.maxdlugosc(), d1024.srdlugosc()],
        ['S1024', s1024.ilepustych(), s1024.maxdlugosc(), s1024.srdlugosc()]]
print(tabulate(dane, headers=['Tablica haszująca', 'Liczba pustych list', 'Maksymalna długość listy',
                              'Średnia długość niepustych list'], tablefmt='fancy_grid'))
