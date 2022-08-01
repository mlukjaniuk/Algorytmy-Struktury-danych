Sortowanie szybkie (Quick-sort)

Komentarz do zadań: do zaprogramowania należy wybrać tylko jedno zadanie spośród z3.2, z3.3, z3.4, z3.5. Punkty będą przyznane tylko za jedno zadanie. Na przykład zadanie z3.4 jest za 5 punktów i nie jest szczególnie skomplikowane. z3.2 jest najmniej pracochłonne, ale mniej punktowane. Zadanie z3.1 jest przydatne do zrozumienia szczegółów algorytmu - tego typu zadanie będzie na sprawdzianie jak zajęcia zaczną odbywać się normalnie.

Zadanie z3.1 Tablicę A = [23, 6, 11, 12, 17, 19, 7, 18, 12, 14, 15] sortujemy sortowaniem szybkim (quickSort). W jaki sposób będzie zmieniała się ta tablica w czasie pierwszego przebiegu funkcji partition dokonującej podziału? Wskaż kolejne elementy, które są ze sobą zamieniane, oraz zaznacz, jak ostatecznie zostanie podzielona tablica.

Zadanie z3.2 (4 pkt.)

Zaimplementuj algorytm sortowania szybkiego omówiony na wykładzie. (3 pkt.)

Zmierz i porównaj czasy działania sortowania dla dwóch rodzajów danych: dane losowe oraz dane skrajnie niekorzystne (np. liczby uprządkowane rosnąco lub malejąco). (1 pkt)

Testy (pomiary czasu) powinny być wykonane dla różnych wielkości tablicy, np. 1000 elementów, 5000 elementów, 10000 elementów i 15000 elementów. Sugerowany sposób prezentacji wyników testów:

rozmiar tablicy	czas - dane losowe	czas - dane niekorzystne
1000		
5000		
itd.		
Zadanie z3.3 (4.5 pkt.) Zaimplementuj i przetestuj (3.5 pkt.) oraz porównaj czasy działaniaj (1 pkt.) podstawową i zmodyfikowane wersje sortowania szybkiego, gdzie element wyznaczający podział jest:

skrajnie prawym elementem A[r] (pod)tablicy (wersja podstawowa);

wybranym pseudolosowo (randomizedQuickSort);

medianą (czyli elementem środkowym co do wartości) z trzech następujących elementów tablicy: skrajnie lewego (A[p]), środkowego (A[p + (r−p)/2]), skrajnie prawego (A[r]).

Podobnie jak w zadaniu z3.2, testy powinny być wykonane dla danych losowych i niekorzystnych, dla różnych wielkości tablicy (np. 1000,5000,10000 i 15000). Dla tego samego rodzaju danych należy zestawić czasy działania trzech wersji algorytmów. Sugerowany sposób prezentacji wyników testów:

DANE LOSOWE
rozmiar tablicy | czas - algorytm 1 | czas - algorytm 2 | czas - algorytm 3
1000		|		    |			|
5000		|		    |			|
itd.			
DANE NIEKORZYSTNE
rozmiar	tablicy	| czas - algorytm 1 | czas - algorytm 2 | czas - algorytm 3
1000		|		    |			|
5000		|		    |			|
itd.			
Zadanie z3.4 (5 pkt.)

Zaimplementuj algorytm sortowania szybkiego omówiony na wykładzie. (3 pkt.)

Następnie zmodyfikuj ten algorytm tak, aby dla tablic o rozmiarze mniejszym od pewnej stałej c ≥ 1 (tj. kiedy r−p+1 < c) nie była wykonywana procedura partition i rekursywne wywołania, a tablice te pozostawały nieposortowane. Dopiero po zakończeniu tak „zepsutego” sortowania szybkiego, cała tablica ma być dodatkowo sortowana algorytmem sortowania przez wstawianie (insertion-sort, omawiany na pierwszym wykładzie). Przetestuj czy zmodyfikowany algorytm poprawnie sortuje.(1 pkt.)

Porównaj czasy działania algorytmu podstawowego oraz jego modyfikacji dla dwóch rodzajów danych dane losowe oraz dane skrajnie niekorzystne (ciąg rosnący). Podobnie jak w zadaniu z3.3, dla tego samego rodzaju danych należy zestawić czasy działania dwóch wersji algorytmów. (1 pkt.)

Zadanie z3.5 (5 pkt.)

Zaimplementuj algorytm sortowania szybkiego omówiony na wykładzie. (3 pkt.)

Następnie zmodyfikuj ten algorytm tak, aby dla podtablic o rozmiarze mniejszym od pewnej stałej c ≥ 1 (tj. kiedy r−p+1 < c) nie była wykonywana procedura partition i rekursywne wywołania, tylko stosowane było jakieś proste sortowanie, np. bąbelkowe czy przez wstawianie (ale tylko dla tej podtablicy, nie dla całej tablicy). (Sortowanie przez wstawianie insertion-sort było omawiane na pierwszym wykładzie.) Przetestuj czy zmodyfikowany algorytm poprawnie sortuje.(1 pkt.)

Porównaj czasy działania algorytmu podstawowego oraz jego modyfikacji dla dwóch rodzajów danych: dane losowe oraz dane skrajnie niekorzystne (ciąg rosnący). Podobnie jak w zadaniu z3.3, dla tego samego rodzaju danych należy zestawić czasy działania dwóch wersji algorytmów. (1 pkt)