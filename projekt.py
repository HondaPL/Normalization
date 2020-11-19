from itertools import combinations

x = True
atrybutyKluczowe = []
atrybutyNieKluczowe = []
danePoczatkowe = []
domknieciePoczatkowe = []
klucze = []
zaPierwszymRazem = True
atrybuty = []
atrybuty2 = []
zaleznosci = []


def czyZawieraKlucz(x):
    global klucze
    for z in klucze:
        if set(z).issubset(x):
            return False
    return True


def domkniecia(atrybut, zaleznosci):
    kandydatNaKlucz = list(atrybut)
    global atrybuty
    global x
    global atrybutyKluczowe
    global danePoczatkowe
    global zaPierwszymRazem
    global klucze
    danePoczatkowe = []
    for qwe in atrybut:
        danePoczatkowe.append(qwe)
    wynik = "{"
    for i in range(len(atrybut)):
        if (i == len(atrybut) - 1):
            wynik += atrybut[i] + '}+ = '
        else:
            wynik += atrybut[i] + ', '
    powtorka = True
    while powtorka:
        powtorka = False
        for j in zaleznosci:
            wymagania = j[0].split(',')
            prawda = True
            for g in wymagania:
                if g not in atrybut:
                    prawda = False
                    break
            if prawda and j[1] not in atrybut:
                atrybut.append(j[1])
                powtorka = True
    dane = sorted(set(atrybut))
    wynik += str(dane)
    if len(dane) == len(atrybuty):
        if x or czyZawieraKlucz(set(danePoczatkowe)):
            wynik += " <- Minimalny klucz kandydujacy"
            x = False
            for q in danePoczatkowe:
                atrybutyKluczowe.append(q)
            if zaPierwszymRazem:
                klucze.append(kandydatNaKlucz)
        else:
            wynik += " <- Nadklucz"
    odp = wynik.replace('\'', '').replace('[', '{').replace(']', '}')
    return odp


def bazaMinilana(zaleznosc):
    global x
    x = True
    global atrybuty
    sprawdzenie = []
    global atrybutyKluczowe
    atrybutyKluczowe = []
    global klucze
    klucze = []
    # Sprawdzamy czy domknięcia się pokrywają
    for i in range(1, len(atrybuty) + 1):
        comb = combinations(atrybuty, i)
        for j in list(comb):
            sprawdzenie.append(domkniecia(list(j), zaleznosc))
    if sprawdzenie == domknieciePoczatkowe:
        return True
    else:
        return False


def usuwanie(zaleznosc):
    pomoc = len(zaleznosc)
    for x in range(pomoc):
        powtorka2 = True
        while powtorka2:
            global klucze
            klucze = []
            global zaPierwszymRazem
            zaPierwszymRazem = True
            powtorka2 = False
            zaleznosc2 = []
            for y in zaleznosc:
                zaleznosc2.append(y)
            if len(zaleznosc[x][0]) > 1:
                bufor2 = zaleznosc[x][0]
                gie = zaleznosc[x][0].split(',')
                ha = zaleznosc[x][0].split(',')
                for k in range(len(gie)):
                    kopiaHa = list(ha)
                    ha.remove(gie[k])
                    bufor = ""
                    for de in range(len(ha)):
                        if de != len(ha) - 1:
                            bufor += ha[de] + ","
                        else:
                            bufor += ha[de]
                    zaleznosc2[x][0] = bufor
                    if bazaMinilana(zaleznosc2):
                        if k == len(gie) - 1:
                            k += 1
                        powtorka2 = True
                        break
                    else:
                        ha = kopiaHa
                if k != len(gie) - 1:
                    if k == len(gie):
                        k -= 1
                    zaleznosc[x][0] = bufor
                else:
                    zaleznosc[x][0] = bufor2


def usuwanie2(zaleznosc):
    g = 0
    pomoc = len(zaleznosc)
    for g in range(pomoc):
        zaleznosci2 = []
        for y in zaleznosc:
            zaleznosci2.append(y)
        del (zaleznosci2[g])
        if bazaMinilana(zaleznosci2):
            if g == pomoc - 1:
                g += 1
            break
    if g == pomoc - 1:
        return zaleznosc
    else:
        if g == pomoc:
            g -= 1
        del (zaleznosc[g])
        if len(zaleznosc):
            return usuwanie2(zaleznosc)

def subset(givenSet):
    listaa = []
    for i in range(1, len(givenSet)):
        comb = combinations(givenSet, i)
        for j in list(comb):
            listaa.append(list(j))
    return listaa


def czy2PN(zaleznosc):
    """
    # Sprawdzamy czy wszystkie argumenty niekluczowe są w pełni zależne od klucza
    for x in zaleznosc:
        print(x)
        print(set(x[0].split(',')))
        print(set(atrybutyKluczowe))
        # x[0] in atrybutyKluczowe ???
        if set(x[0].split(',')).issubset(set(atrybutyKluczowe)) and x[1] not in atrybutyKluczowe:
            return "nie, bo " + x[0] + " -> " + x[1] + " narusza 2PN"
    return "tak"

    """
    # Sprawdzamy czy istnieje co najmniej jeden atrybut niekluczowy zależny od części klucza

    global klucze
    wynik = ""
    for x in klucze:
        for y in subset(x):
            podzbior = ""
            for d in range(len(y)):
                if d != len(y) - 1:
                    podzbior += y[d] + ", "
                else:
                    podzbior += y[d]
            z = domkniecia(y, zaleznosc)
            for v in atrybutyNieKluczowe:
                if v in z:
                    if "Bo " + v + " jest funkcyjnie zależny od " + podzbior + " narusza 2PN" + "\n" not in wynik:
                        wynik += "Bo " + v + " jest funkcyjnie zależny od " + podzbior + " narusza 2PN" + "\n"
    if wynik:
        return wynik
    return "tak"


def czy3PN(zaleznosc):
    # Sprawdzamy czy każda zależność funkcyjna X -> Y ma jedną z 3 własności:
    # (1) jest trywialna (Y zawiera się w X) lub
    # (2) X jest nadkluczem lub
    # (3) Y jest atrybutem kluczowym
    wynik = ""
    global atrybutyKluczowe
    for x in zaleznosc:
        if x[1] not in x[0] and x[1] not in atrybutyKluczowe and "klucz" not in domkniecia(x[0].split(','), zaleznosc):
            if "Bo " + x[0] + " -> " + x[1] + " narusza 3PN" + "\n" not in wynik:
                wynik += "Bo " + x[0] + " -> " + x[1] + " narusza 3PN" + "\n"
    if wynik:
        return wynik
    return "tak"


def sprowadzanieDo3PN(zaleznosc):
    i = 1
    zbior = set()
    listyZbiorowArgumentow = []
    listyZbiorowZaleznosci = []
    for x in zaleznosc:
        zbior.add(x[0])
    for x in zbior:
        zaleznosciOgraniczone = []
        for z in zaleznosc:
            if z[0] == x:
                zaleznosciOgraniczone.append(z)
        argumentyOgraniczone = []
        for z in x.split(','):
            argumentyOgraniczone.append(z)
        for z in zaleznosciOgraniczone:
            argumentyOgraniczone.append(z[1])
        listyZbiorowArgumentow.append(set(argumentyOgraniczone))
        listyZbiorowZaleznosci.append(zaleznosciOgraniczone)
        i += 1

    #Sprawdzamy czy ktorys U zawiera dowolny klucz
    kluczeZbiorowe = []
    for x in klucze:
        kluczeZbiorowe.append(set(x))
    zawieraKlucz = False
    dodanyKlucz = kluczeZbiorowe[0]
    for x in kluczeZbiorowe:
        for z in listyZbiorowArgumentow:
            if x.issubset(z):
                zawieraKlucz = True
                break
        if zawieraKlucz:
            break
    if not zawieraKlucz:
        listyZbiorowArgumentow.append(dodanyKlucz)
        listyZbiorowZaleznosci.append([])

    # Sprawdzamy czy jakies U zawieraja sie miedzy soba
    for x in range(len(listyZbiorowArgumentow)):
        for y in range(len(listyZbiorowArgumentow)):
            if listyZbiorowArgumentow[x].issubset(listyZbiorowArgumentow[y]) and x != y:
                for z in listyZbiorowZaleznosci[x]:
                    listyZbiorowZaleznosci[y].append(z)
                listyZbiorowZaleznosci[x] = set()
                listyZbiorowArgumentow[x] = set()
            if listyZbiorowArgumentow[y].issubset(listyZbiorowArgumentow[x]) and x != y:
                for z in listyZbiorowZaleznosci[y]:
                    listyZbiorowZaleznosci[x].append(z)
                listyZbiorowZaleznosci[y] = set()
                listyZbiorowArgumentow[y] = set()

    # Dodajemy dodatkowe zaleznosci, jeżeli dla zaleznosci X -> Y istnieje zaleznosc Y -> X, to ja dodajemy
    for i in range(len(listyZbiorowZaleznosci)):
        dlugosc = len(listyZbiorowZaleznosci[i])
        teraz = 0
        for j in listyZbiorowZaleznosci[i]:
            teraz += 1
            rozbiteAtrybuty = j[0].split(',')
            for l in zaleznosc:
                if l[0] == j[1] and l[1] in rozbiteAtrybuty:
                    rozbiteAtrybuty.remove(l[1])
            if not rozbiteAtrybuty:
                rozbiteAtrybuty = j[0].split(',')
                for s in rozbiteAtrybuty:
                    a = []
                    a.append(j[1])
                    a.append(s)
                    if a not in listyZbiorowZaleznosci[i]:
                        listyZbiorowZaleznosci[i].append(a)
            if teraz == dlugosc:
                break

    #Wypisywanie syntezy
    for i in range(len(listyZbiorowArgumentow)):
        if listyZbiorowArgumentow[i]:
            print("R" + str(i) + "(", end="")
            d = 0
            for k in sorted(listyZbiorowArgumentow[i]):
                if d != len(listyZbiorowArgumentow[i]) - 1:
                    print(k, end=",")
                else:
                    print(k, end=") : ")
                d += 1
            if listyZbiorowZaleznosci[i]:
                d = 0
                for k in listyZbiorowZaleznosci[i]:
                    print(k[0], end=" -> ")
                    if d != len(listyZbiorowZaleznosci[i]) - 1:
                        print(k[1], end="; ")
                    else:
                        print(k[1], end="")
                    d += 1
            else:
                print("(brak)")
            #print(listyZbiorowZaleznosci[i])
            print()


def weryfikacja(atrybuty, atrybutyZaleznosci):
    return sorted(atrybuty) == sorted(atrybutyZaleznosci)


# Główny program

print("Witaj w programie do normalizacji!")
print("Jeżeli chcesz obejrzeć skrypt prezentujący możliwości algorytmu wpisz 1, a jeżeli chcesz przejść dalej wpisz inną liczbę")
odpowiedz = int(input())

jeszczeRaz = True
while jeszczeRaz:
    atrybuty = []
    atrybuty2 = []
    zaleznosci = []
    atrybutyKluczowe = []
    atrybutyNieKluczowe = []
    danePoczatkowe = []
    domknieciePoczatkowe = []
    klucze = []
    zaPierwszymRazem = True
    x = True
    if odpowiedz != 1:
        jeszczeRaz = False
        print("Wpisz 1, żeby pobrać dane z pliku, lub 2, aby pobrać dane ze standradowego wyjścia")
        decyzja = 0
        while(decyzja != 1 and decyzja != 2):
            decyzja = int(input())

            # 2a Pobieranie z pliku
            if decyzja == 1:
                print("Podaj numer testu w zapiscie dwucyfrowym np. 01, 10")
                numerTestu = input()
                blad = True
                while blad:
                    try:
                        blad = False
                        plik = open("/Users/adam/Desktop/testy/test-" + numerTestu + ".txt")
                    except FileNotFoundError:
                        blad = True
                        print("Podaj numer testu w zapiscie dwucyfrowym np. 01, 10")
                        numerTestu = input()
                lista = []
                for linia in plik:
                    lista.append(linia.strip())
                atrybuty = lista[0].replace(' ', '').split(',')
                lista.pop(0)
                print()
                print("Atrybuty")
                print()
                for zmienna in atrybuty:
                    print(zmienna, end=" ")
                print()
                print()
                print("Zaleznosci")
                print()
                for zmienna in lista:
                    print(zmienna)
                print()
                for a in lista:
                    wejscie = a.replace(';', '').replace(' ', '').replace(';', '').split('->')
                    naKanoniczna = wejscie[1].split(',')
                    for x in wejscie[0].split(','):
                        if x not in atrybuty2:
                            atrybuty2.append(x)
                    for d in naKanoniczna:
                        lista = [wejscie[0], d]
                        zaleznosci.append(lista)
                        if d not in atrybuty2:
                            atrybuty2.append(d)

            # 2b Pobieranie danych ze standardowego wejścia
            elif decyzja == 2:
                atrybuty = input().replace(' ', '').split(',')
                zaleznosci = []
                a = input()
                lista = []
                atrybuty2 = []
                string = ""
                # 4 Zmiana na postać kakoniczną
                while a:
                    string += "\n" + a
                    wejscie = a.replace(';', '').replace(' ', '').replace(';', '').split('->')
                    naKanoniczna = wejscie[1].split(',')
                    for x in wejscie[0].split(','):
                        if x not in atrybuty2:
                            atrybuty2.append(x)
                    for d in naKanoniczna:
                        lista = [wejscie[0], d]
                        zaleznosci.append(lista)
                        if d not in atrybuty2:
                            atrybuty2.append(d)
                    a = input()
                print("Atrybuty:")
                print()
                for b in atrybuty:
                    print(b, end=" ")
                print()
                print()
                print("Zaleznosci:")
                print(string)
                print()
            else:
                print("Podaj poprawny numer sposobu")

    # 1 Przykładowy skrypt
    else:
        atrybuty = "A,B,C,QX".replace(' ', '').split(',')
        zaleznosci = []
        lista = ["A -> B;", "QX -> C;", "B,C -> A"]
        atrybuty2 = []
        print()
        print("Atrybuty")
        print()
        for zmienna in atrybuty:
            print(zmienna, end=" ")
        print()
        print()
        print("Zaleznosci")
        print()
        for zmienna in lista:
            print(zmienna)
        print()
        # 4 Zmiana na postać kakoniczną
        for a in lista:
            wejscie = a.replace(';', '').replace(' ', '').replace(';', '').split('->')
            naKanoniczna = wejscie[1].split(',')
            for x in wejscie[0].split(','):
                if x not in atrybuty2:
                    atrybuty2.append(x)
            for d in naKanoniczna:
                lista = [wejscie[0], d]
                zaleznosci.append(lista)
                if d not in atrybuty2:
                    atrybuty2.append(d)


    # 3 Weryfikacja czy wszystkie atrybuty z 𝓕 znajdują się w 𝓤 i vice versa
    print("Weryfikacja: " + str(weryfikacja(atrybuty, atrybuty2)))
    print()

    # 4 Wypisanie postaci kanonicznej
    print("Postac kanoniczna:")
    print()
    for x in zaleznosci:
        print(str(x[0] + " -> " + str(x[1])))
    print()

    # 5 Obliczenie 𝓕+
    print("Domkniecia: ")
    print()
    for i in range(1, len(atrybuty) + 1):
        comb = combinations(atrybuty, i)
        for j in list(comb):
            odp = domkniecia(list(j), zaleznosci)
            domknieciePoczatkowe.append(odp)
            print(odp)
    zaPierwszymRazem = False
    print()

    # 6 Wyznaczenie kluczy kandydujących, nadkluczy, atrybutów kluczowych i niekluczowych
    atrybutyKluczowe = sorted(set(atrybutyKluczowe))
    print("Atrybuty kluczowe: ")
    print()
    for x in atrybutyKluczowe:
        print(x, end=" ")
    print()
    print()

    print("Atrybuty niekluczowe: ")
    print()
    atrybutyNieKluczowe = sorted(set(atrybuty).difference(atrybutyKluczowe))
    if len(atrybutyNieKluczowe) > 0:
        for x in atrybutyNieKluczowe:
            print(x, end=" ")
        print()
    else:
        print("brak")
    print()

    schowek = list(klucze)
    schowek2 = list(atrybutyKluczowe)

    # 7 Obliczenie 𝓕min
    usuwanie(zaleznosci)
    usuwanie2(zaleznosci)
    print("Fmin: ")
    print()
    if len(zaleznosci) >= 1:
        for x in zaleznosci:
            print(str(x[0] + " -> " + str(x[1])))
    else:
        print("brak")
    print()

    # Wracam do poprzednich kluczy i atrybutw kluczowych
    # (były one zmianane przy sprowadzaniu do bazy minimalnej)
    klucze = schowek
    atrybutyKluczowe = schowek2

    # 8 Test na 2PN
    pn2 = czy2PN(zaleznosci)
    if pn2 != "tak":
        print("2PN: nie")
        print(pn2)
    else:
        print("2PN: " + pn2)
        print()


    schowek3 = list(schowek)

    # 9 Test na 3PN
    pn3 = czy3PN(zaleznosci)
    if pn3 != "tak":
        print("3PN: nie")
        print(pn3)
    else:
        print("3PN: " + pn3)


    # 10 Obliczenie 3PN przy pomocy algorytmu syntezy
    if pn3 != "tak":
        print("Synteza do 3PN:")
        print()
        sprowadzanieDo3PN(zaleznosci)
    klucze = schowek3

    #print("Klucze")
    #print(klucze)

    if odpowiedz != 1:
        print("Czy chcesz jeszcze raz wywołać? Wpisz Y, jeżeli tak lub cokolwiek innego, jeżeli nie")
        odpowiedz2 = input()
        if odpowiedz2 == "Y":
            jeszczeRaz = True
    else:
        jeszczeRaz = True
        odpowiedz = 0
    print()