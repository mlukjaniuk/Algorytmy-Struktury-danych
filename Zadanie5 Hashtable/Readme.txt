Haszowanie

Zadanie z5 (2 pkt.) Celem zadania jest sprawdzenie różnych wariantów funkcji haszującej: będziemy badać wynik haszowania ciągu kluczy, które są napisami, z użyciem łańcuchowej metody usuwania kolizji. W tym celu należy zdefiniować listę T rozmiaru m , gdzie każde T[i] będzie listą tych kluczy (napisów) k, dla których h(k)=i.

Zatem najpierw trzeba wypełnić tablicę T, pustymi listami a potem dla kolejnych kluczy k wyliczać h(k) i dodawać k do odpowiedniej listy: T[h(k)].apend(k).

Klucze-napisy do testowania są w pliku 3700.txt.

Haszowanie modularne: h(k) = liczba(k)% m. gdzie liczba() to zdefiniowana przez nas funkcja robiąca pseudolosową konwersję napisu na liczbę.

Przykładowe schematy konwersji napisu na liczbę:

"abc...x" -> (...((111*ord(a)+ord(b))*111+ord(c))*111+ ... )*111 +ord(x)

"abcdef..." -> ((256*ord(a)+ord(b)) XOR (256*ord(c)+ord(d)) XOR (256*ord(e)+ord(f)) ...

W pierwszym schemacie "111" to przykładowa stała (nie będąca potęgą 2).

Warianty funkcji haszującej:

(W) wbudowana w Pythonie funkcja hash
(D) własna dobra funkcja haszująca h według jednego ze schematów powyżej
(S) własna słaba funkcja haszująca, np. tylko według pierwszej litery lub według sumy kodów liter klucza
Warianty rozmiaru tablicy:

(17) to znaczy m = 17, z wydrukiem całej tablicy
(1031) to znaczy m = 1031, liczba pierwsza
(1024) to znaczy m = 1024, potęga 2 (lub m = 1026, czyli 19 * 3 * 3 * 3 * 2)
Do tablicy T wstawiamy około 2*m kluczy, po czym wypisujemy jaka jest:
– ilość pustych list w tablicy T;
– maksymalna długość listy w T;
– średnia długość niepustych list.
Mamy następujące warianty do sprawdzenia:

W17, D17, S17, W1031, D1031, S1031, W1024, D1024, S1024

Jako rozwiązanie przesłać kod programu wykonującego pomiary z dołączonymi wynikami wygenerowanymi przez ten program dla wszyskich dziewięciu wariantów powyżej. Wyniki te można dołączyć np. jako komentarz na końcu kodu programu. Proszę też wpisać odpowiedź na pytania:
- który z rozmiarów tablicy (1031 lub 1024) dawał lepsze wyniki
- czy wybór rodzaju funkcji hszującej (W, D, S) wpływał na jakość wyniku
Lepszy wynik to taki, że maksymalna i średnia długość listy są mniejsze.

Uwaga: treść zadania może odstraszać swoim rozmiarem, ale jak już się zrozumie o co chodzi, to sam program do napisania jest raczej prosty i krótki.