Drzewa poszukiwań binarnych

Zadanie z7.1. Narysuj drzewo poszukiwań binarnych, które powstanie po:
wstawieniu elementów 18, 11, 6, 30, 21, 19, 8, 22, 23, 5, 20, 26, 17 do pustego drzewa;
a następnie usunięciu elementów 8, 30, 18, 11.

Uwaga Należy zrobić i przysłać tylko jedno (dowolnie wybrane) zadanie spośród 7.2, 7.3, i 7.4

Zadanie z7.2. (3 pkt.) Zaimplementuj i przetestuj operacje WSTAW, SZUKAJ, USUŃ, DRUKUJ na drzewie poszukiwań binarnych, którego kluczami/elementami są słowa (można przyjąć że zbudowane tylko ze znaków ASCII). Przyjąć, że do drzewa wstawiane są klucze o różnych wartościach, a wypisanie (DRUKUJ) wartości węzłów odbywa się np. w porządku in-order (najlepiej z zaznaczaniem przez odstępy zagłębienia węzłów w drzewie, lub jakiś inny sposób pozwalający zrozumieć strukturę drzewa).

Zadanie AL7.3. (4 pkt.) Zaimplementuj i przetestuj operacje WSTAW, SZUKAJ, USUŃ, DRUKUJ jak w zadaniu 7.2, ale tym razem dopuszczamy wielokrotne wstawienie takiego samego klucza (napisu), z tym, że w przypadku wielokrotnego wstawiania tego samego klucza, nie tworzymy nowych węzłów o tej samej zawartości tylko w węźle zawierającym powtarzający się klucz zliczamy ilość powtórzeń tego samego klucza. Analogicznie, "fizyczne" usuwanie węzła o danym kluczu ma miejsce dopiero wtedy, gdy ilość powtórzeń tego klucza wynosi 1.

Zadanie AL7.4. (5 pkt.) Wykorzystać funkcje WSTAW (i ewentualnie SZUKAJ, żeby unikać powtórzeń kluczy) z zadania 7.2 do przeprowadzenia następującego eksperymentu. Zmierzyć i wypisać wysokość drzewa poszukiwań binarnych uzyskanego w wyniku wstawienia pewnej ilości słów (500, 1000, 2000) do początkowo pustego drzewa. Słowa do wstawienia można brać z dowolnego pliku tekstowego, najlepiej angielskiego, żeby nie było problemów z kodowaniem, np. można wziąć stronę manuala unixowego man python albo man less i wyciągać z takiego pliku słowa, czyli ciągi liter a pominąć pozostałe znaki. Ponadto, w celu sprawdzenia czy drzewa są poprawnie tworzone, wydrukować fragment uworzonego drzewa podobnie jak w zadaniu 7.2, ale tylko do pewnej wysokości.