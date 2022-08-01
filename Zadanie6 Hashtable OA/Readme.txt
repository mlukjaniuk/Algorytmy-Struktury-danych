Haszowanie z adresowaniem otwartym

Zadanie z6.1. Niech m=13. Zdefiniujmy następujące funkcje haszujące:
h1(k) = k mod m
h2(k) = 1+ (k mod (m-2)).
(A) Prześledź działanie haszowania z adresowaniem otwartym, wariant z adresowaniem liniowym, z funkcją haszującą h(k,i)=(h1(k)+i) mod m w sytuacji, gdy do początkowo pustej (m-elementowej) tablicy T wstawiamy liczby 6, 19, 28, 41, 54, a następnie usuwamy 41 i szukamy potem 54 oraz 32. "Prześledź działanie" oznacza, że dla każdej wstawianej liczby należy wyliczyć pozycje, na jakich były próby wstawienia i pozycję na której ostatecznie było wstawienie.

(B) Prześledź działanie haszowania z adresowaniem otwartym, wariant z adresowaniem kwadratowym, z funkcją haszującą h(k,i)=(h1(k)+i2) mod m w sytuacji, gdy do początkowo pustej (m-elementowej) tablicy T wstawiamy liczby 6, 19, 28, 41, 54, 67, a następnie usuwamy 54 i szukamy potem 67.

(C) Prześledź działanie haszowania z adresowaniem otwartym, wariant z haszowaniem dwukrotnym, z funkcją haszującą h(k,i)=(h1(k)+i*h2(k)) mod m w sytuacji, gdy do (m-elementowej) tablicy T zawierającej elementy 50 (pozycja 11), 69 (pozycja 4), 72 (pozycja 7), 79 (pozycja 1), oraz 98 (pozycja 5), wstawiamy liczbę 14, a następnie usuwamy 98 i szukamy potem 14.

Zadanie z6.2. (4 pkt.) Zaprogramować JEDEN wybrany wariant operacji ( W,U,S, patrz niżej) na tablicy z haszowaniem z adresowaniem otwartym oraz przeprowadzić testy i pomiary:

Operacje przetestować osobno na małej tablicy, z wydrukiem kontrolnym,
testy/pomiary przeprowadzić na tablicy większego rozmiaru, np. rzędu kilku tysięcy.
W tablicy haszowań mają być obiekty zawierające dwa pola:

ilosc – typu int
nazwisko – ciąg znaków

Kluczami mają być nazwiska (schematy zamiany na liczbę, do haszowania, jak w zadaniu z5). W pliku nazwiskaASCII (ściągniętym z nieistniejącej już chyba strony www.futrega.org/etc/nazwiska.html) znajduje się wykaz zapisów postaci: [liczba typu int] [nazwisko], które można wykorzystać.

Wykaz liczb pierwszych (przydatnych przy doborze rozmiaru tablicy): pierwsze.txt.

Warianty operacji i pomiarów

[W] Operacja WSTAW. Pomiar: średnia ilość prób wykonanych przy wstawianiu elementu (średnia ze wszystkich wstawień) przy różnych wypełnieniach tablicy: 50%, 70% i 90%.
[S] Operacje WSTAW i SZUKAJ. Pomiar: wypełnienie tablicy do 80% i wykonanie pewnej ilości operacji szukaj (np. ostatnich 20) ze zliczaniem i wydrukiem ilości prób przy szukaniu każdego klucza.
[U] Operacje WSTAW i USUŃ. Pomiar: wstawiać elementy aż do wypełnienia tablicy w 80%, potem usunąć połowę wstawionych elementów i następnie znowu dopełnić tablicę innymi elementami do 80%. Po tych operacjach zliczyć i wypisać, ile pozycji w tablicy jest wypełnionych znacznikiem DEL (miejsce po usuniętym elemencie)
Warianty techniki rozwiązywania kolizji
[OL] adresowanie otwarte liniowe
[OK] adresowanie otwarte kwadratowe
[OD] adresowanie otwarte, dwukrotne haszowanie
Możliwe kombinacje wariantów: [W+OL], [W+OK], [W+OD], [S+OL], [S+OK], [S+OD], [U+OL], [U+OK], [U+OD].