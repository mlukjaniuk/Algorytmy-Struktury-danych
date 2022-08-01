def znajdzWP(slowo1, slowo2, dlugosc1, dlugosc2):
    podciagi = []

    if dlugosc1 == 0 or dlugosc2 == 0:
        podciagi.append("")
        return podciagi

    # jeśli ostatnie litery słów są takie same:
    if slowo1[dlugosc1 - 1] == slowo2[dlugosc2 - 1]:

        # rekursywne wywołanie dla slowo1[0...dlugosc1-2] i slowo2[0...dlugosc2-2]:
        temp = znajdzWP(slowo1, slowo2, dlugosc1 - 1, dlugosc2 - 1)

        for string in temp:
            podciagi.append(string + slowo1[dlugosc1 - 1])

    # jeśli ostatnie litery nie są takie same:
    else:

        if L[dlugosc1 - 1][dlugosc2] >= L[dlugosc1][dlugosc2 - 1]:
            podciagi = znajdzWP(slowo1, slowo2, dlugosc1 - 1, dlugosc2)

        if L[dlugosc1][dlugosc2 - 1] >= L[dlugosc1 - 1][dlugosc2]:
            temp = znajdzWP(slowo1, slowo2, dlugosc1, dlugosc2 - 1)

            for i in temp:
                podciagi.append(i)
    return podciagi


def znajdzNWP(slowo1, slowo2):
    dlugosc1 = len(slowo1)
    dlugosc2 = len(slowo2)
    podciagi = znajdzWP(slowo1, slowo2, dlugosc1, dlugosc2)
    max_dlugosc = max([len(i) for i in podciagi])
    wynik = {i for i in podciagi if len(i) == max_dlugosc}
    return wynik


slowo1 = "POLITECHNIKA"
slowo2 = "TOALETA"

# wypełnienie tabeli zerami
N = 100
L = [[0 for i in range(N)]
     for j in range(N)]

najdluzsze_podciagi = znajdzNWP(slowo1, slowo2)
for i in najdluzsze_podciagi:
    print(i)
