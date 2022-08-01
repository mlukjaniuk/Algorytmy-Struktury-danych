import math
from timeit import default_timer as timer
import matplotlib.pyplot as plt


nn = [2000, 4000, 8000, 16000, 32000]
wartosci1 = []
wartosci2 = []
wartosci3 = []
wartosci4 = []
wartosci5 = []


def f1(n):
    s = 0
    for j in range(1, n):
        s = s + 1 / j
    return s


def pomiarf1(tablica):
    for n in tablica:
        start = timer()
        f1(n)
        stop = timer()
        Tn = stop - start
        Fn = n
        print(n, Tn, Fn / Tn)
        wartosci1.append(Tn)


#pomiarf1(nn)
# wyniki: n, Tn, Fn/Tn
# 2000, 0.0001257999999779713, 15898251.195152763
# 4000, 0.0002448999999842272, 16333197.224408414
# 8000, 0.00048620000006849295, 16454134.098874964
# 16000, 0.0009853999999904772, 16237061.092099272
# 32000, 0.0019462000000203261, 16442297.810947381


def f2(n):
    s = 0
    for j in range(1, n):
        for k in range(1, n):
            s = s + k / j
    return s


def pomiarf2(tablica):
    for n in tablica:
        start = timer()
        f2(n)
        stop = timer()
        Tn = stop - start
        Fn = n * n
        print(n, Tn, Fn / Tn)
        wartosci2.append(Tn)


#pomiarf2(nn)
# wyniki: n, Tn, Fn/Tn
# 2000, 0.2735449999998991, 14622822.57033203
# 4000, 1.1089428999999882, 14428154.957302283
# 8000, 3.9097709000000123, 16369245.573954167
# 16000, 16.07364819999998, 15926689.250297286
# 32000, 63.99838980000004, 16000402.56012815


def f3(n):
    s = 0
    for j in range(1, n):
        for k in range(j, n):
            s = s + k / j
    return s


def pomiarf3(tablica):
    for n in tablica:
        start = timer()
        f3(n)
        stop = timer()
        Tn = stop - start
        Fn = (n * n)/2
        print(n, Tn, Fn / Tn)
        wartosci3.append(Tn)


#pomiarf3(nn)
# wyniki: n, Tn, Fn/Tn
# 2000, 0.13770030000000588, 14524296.606470099
# 4000, 0.5859224000000722, 13653685.197901657
# 8000, 1.9013471000000663, 16830172.670733757
# 16000, 7.49338570000009, 17081731.159254014
# 32000, 30.690891100000044, 16682474.234187331


def f4(n):
    s = 0
    for j in range(1, n):
        k = 2
        while k <= n:
            s = s + k / j
            k = k * 2
    return s


def pomiarf4(tablica):
    for n in tablica:
        start = timer()
        f4(n)
        stop = timer()
        Tn = stop - start
        Fn = n * math.log(n, 2)
        print(n, Tn, Fn / Tn)
        wartosci4.append(Tn)


#pomiarf4(nn)
# wyniki: n, Tn, Fn/Tn
# 2000, 0.0019433999996181228, 11285154.149240362
# 4000, 0.005897699999877659, 8115559.818173393
# 8000, 0.010522300000047835, 9857756.790513972
# 16000, 0.025587699999960023, 8732811.020722555
# 32000, 0.0395435999998881, 12110811.790290767


def f5(n):
    s = 0
    k = 2
    while k <= n:
        s = s + 1 / k
        k = k * 2
    return s


def pomiarf5(tablica):
    for n in tablica:
        start = timer()
        f5(n)
        stop = timer()
        Tn = stop - start
        Fn = math.log(n, 2)
        print(n, Tn, Fn / Tn)
        wartosci5.append(Tn)


#pomiarf5(nn)
# 2000, 3.099999958067201e-06, 3537349.8170945374
# 4000, 1.8999999156221747e-06, 6297781.482134311
# 8000, 1.4999986888142303e-06, 8643863.74558215
# 16000, 1.3999997463542968e-06, 9975562.01065752
# 32000, 1.5000005078036338e-06, 9977186.145473804


# inne funkcje czasu:
# Fn=math.log(n,2)
# Fn=n
# Fn=100*n
# Fn=n*math.log(n,2)
# Fn=n*n


# Rysowanie wykresów:
# plt.plot(nn, wartosci1)
# plt.plot(nn, wartosci2)
# plt.plot(nn, wartosci3)
# plt.plot(nn, wartosci4)
# plt.plot(nn, wartosci5)
# plt.ylabel('Czas wykonania Tn')
# plt.xlabel('Rozmiar wejścia n')
# plt.legend(['f1', 'f2', 'f3', 'f4', 'f5'])
# plt.show()
