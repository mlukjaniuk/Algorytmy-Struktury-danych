from tabulate import tabulate


class HashObject:
    def __init__(self, lastname=None, amount=None):
        self.key = lastname
        self.amount = amount

    def drukuj(self):
        print([self.key, self.amount])


class HashTable:
    def __init__(self, capacity=None, option=None):
        self.length = 0
        self.capacity = capacity
        self.option = option
        self.buckets = [None for i in range(0, self.capacity)]

    def IntUni(self, key):
        a = len(key)
        counter = 0
        for i in range(0, a - 1):
            counter = counter + ord(key[i]) * 111
        counter = counter * 111 + ord(key[a - 1])
        return counter

    def wstaw(self, key, amount):
        m = self.capacity
        k = self.IntUni(key)
        x = HashObject(key, amount)
        if self.option == "OL":
            i = 0
            while True:
                result = ((k % m) + i) % m
                if self.buckets[result] is not None:
                    i += 1
                else:
                    self.buckets[result] = x
                    return i
        elif self.option == "OK":
            i = 0
            while i < self.capacity*10:
                result = ((k % m) + i * i) % m
                if self.buckets[result] is not None:
                    i += 1
                else:
                    self.buckets[result] = x
                    return i
            return i
        else:
            i = 0
            while True:
                result = ((k % m) + i * (1 + (k % (m - 2)))) % m
                if self.buckets[result] is not None:
                    i += 1
                else:
                    self.buckets[result] = x
                    return i

    def drukuj(self):
        for i in range(0, self.capacity):
            print('Index:', i)
            if self.buckets[i] is not None:
                self.buckets[i].drukuj()
            else:
                print("[]")
            print('-----')


list = []
with open('nazwiskaASCII.txt') as f:
    for line in f:
        x = [i for i in line.split()]
        list.append(x)

testol11 = HashTable(11, 'OL')
testsumaol11 = 0
print("\nTest OL m = 11")
for i in range(0, 11):
    k = testol11.wstaw(list[i][1], int(list[i][0])) + 1
    testsumaol11 += k
    print(list[i][1], "udana próba nr", k)
testsredniaol11 = testsumaol11/11
print("\nWydruk tablicy testowej OL 11:\n")
testol11.drukuj()
print("Średnia liczba wszystkich prób wstawienia:", testsredniaol11)

testok11 = HashTable(11, 'OK')
testsumaok11 = 0
print("\nTest OK m = 11")
for i in range(0, 11):
    k = testok11.wstaw(list[i][1], int(list[i][0])) + 1
    testsumaok11 += k
    print(list[i][1], "udana próba nr", k)
testsredniaok11 = testsumaok11/11
print("\nWydruk tablicy testowej OK 11:\n")
testok11.drukuj()
print("Średnia liczba wszystkich prób wstawienia przy ograniczeniu do 10*m:", testsredniaok11)

testod11 = HashTable(11, 'OD')
testsumaod11 = 0
print("\nTest OD m = 11")
for i in range(0, 11):
    k = testod11.wstaw(list[i][1], int(list[i][0])) + 1
    testsumaod11 += k
    print(list[i][1], "udana próba nr", k)
testsredniaod11 = testsumaod11/11
print("\nWydruk tablicy testowej OD 11:\n")
testod11.drukuj()
print("Średnia liczba wszystkich prób wstawienia:", testsredniaod11)
print("\n-----")


# Tablica 50%
print("\nTablica z adresowaniem OL wypełniona w 50%")
ol50 = HashTable(5003, 'OL')
for i in range(0, 2502):
    ol50.wstaw(list[i][1], int(list[i][0]))
sumaol50 = 0
for i in range(2503, 5003):
    k = ol50.wstaw(list[i][1], int(list[i][0])) + 1
    sumaol50 += k
sredniaol50 = sumaol50 / 2501
print("Średnia liczba wszystkich prób wstawienia:", sredniaol50)

print("\nTablica z adresowaniem OK wypełniona w 50%")
ok50 = HashTable(5003, 'OK')
for i in range(0, 2502):
    ok50.wstaw(list[i][1], int(list[i][0]))
sumaok50 = 0
for i in range(2503, 5003):
    k = ok50.wstaw(list[i][1], int(list[i][0])) + 1
    sumaok50 += k
sredniaok50 = sumaok50 / 2501
print("Średnia liczba wszystkich prób wstawienia:", sredniaok50)

print("\nTablica z adresowaniem OD wypełniona w 50%")
od50 = HashTable(5003, 'OD')
for i in range(0, 2502):
    od50.wstaw(list[i][1], int(list[i][0]))
sumaod50 = 0
for i in range(2503, 5003):
    k = od50.wstaw(list[i][1], int(list[i][0])) + 1
    sumaod50 += k
sredniaod50 = sumaod50 / 2501
print("Średnia liczba wszystkich prób wstawienia:", sredniaod50)

# Tablica 70%
print("\nTablica z adresowaniem OL wypełniona w 70%")
ol70 = HashTable(5003, 'OL')
for i in range(0, 3502):
    ol70.wstaw(list[i][1], int(list[i][0]))
sumaol70 = 0
for i in range(3503, 5003):
    k = ol70.wstaw(list[i][1], int(list[i][0])) + 1
    sumaol70 += k
sredniaol70 = sumaol70 / 1501
print("Średnia liczba wszystkich prób wstawienia:", sredniaol70)

print("\nTablica z adresowaniem OK wypełniona w 70%")
ok70 = HashTable(5003, 'OK')
for i in range(0, 3502):
    ok70.wstaw(list[i][1], int(list[i][0]))
sumaok70 = 0
for i in range(3503, 5003):
    k = ok70.wstaw(list[i][1], int(list[i][0])) + 1
    sumaok70 += k
sredniaok70 = sumaok70 / 1501
print("Średnia liczba wszystkich prób wstawienia:", sredniaok70)

print("\nTablica z adresowaniem OD wypełniona w 70%")
od70 = HashTable(5003, 'OD')
for i in range(0, 3502):
    od70.wstaw(list[i][1], int(list[i][0]))
sumaod70 = 0
for i in range(3503, 5003):
    k = od70.wstaw(list[i][1], int(list[i][0])) + 1
    sumaod70 += k
sredniaod70 = sumaod70 / 2501
print("Średnia liczba wszystkich prób wstawienia:", sredniaod70)

# Tablica 90%
print("\nTablica z adresowaniem OL wypełniona w 90%")
ol90 = HashTable(5003, 'OL')
for i in range(0, 4503):
    ol90.wstaw(list[i][1], int(list[i][0]))
sumaol90 = 0
for i in range(4504, 5003):
    k = ol90.wstaw(list[i][1], int(list[i][0])) + 1
    sumaol90 += k
sredniaol90 = sumaol90 / 499
print("Średnia liczba wszystkich prób wstawienia:", sredniaol90)

print("\nTablica z adresowaniem OK wypełniona w 90%")
ok90 = HashTable(5003, 'OK')
for i in range(0, 4503):
    ok90.wstaw(list[i][1], int(list[i][0]))
sumaok90 = 0
for i in range(4504, 5003):
    k = ok90.wstaw(list[i][1], int(list[i][0])) + 1
    sumaok90 += k
sredniaok90 = sumaok90 / 499
print("Średnia liczba wszystkich prób wstawienia:", sredniaok90)

print("\nTablica z adresowaniem OD wypełniona w 90%")
od90 = HashTable(5003, 'OD')
for i in range(0, 4503):
    od90.wstaw(list[i][1], int(list[i][0]))
sumaod90 = 0
for i in range(4504, 5003):
    k = od90.wstaw(list[i][1], int(list[i][0])) + 1
    sumaod90 += k
sredniaod90 = sumaod90 / 499
print("Średnia liczba wszystkich prób wstawienia:", sredniaod90, "\n")

dane = [['OL', sredniaol50, sredniaol70, sredniaol90],
        ['OK', sredniaok50, sredniaok70, sredniaok90],
        ['OD', sredniaod50, sredniaod70, sredniaod90]]
print(tabulate(dane, headers=['', '50%', '70%', '90%'], tablefmt='fancy_grid'))
