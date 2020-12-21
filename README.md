# Normalization

PL

Zadanie polegało na napisaniu programu, który miał konwertował wejściowy schemat relacji do schematu w 3 postaci normalnej:

- parsuje wejściowy schemat relacji jako zbiór atrybutów oraz zbiór zależności funkcyjnych,
- oblicza domknięcie dla każdego podzbioru zbioru atrybutów,
- oblicza minimalny zbiór kluczy oraz nadklucze,
- oblicza bazę minimalną dla wejściowego zbioru zależności funkcyjnych,
- sprawdza czy podany schemat relacji jest w 2 oraz 3 postaci normalnej (zakładamy na wejściu co najmniej 1 postać normalną),
- jeżeli schemat nie jest w 3 postaci normalnej, to normalizuje go przy pomocy algorytmu syntezy.

ENG

This program will normalize relation scheme to 3NF.

It will:

- parse input into set of atributes and functional dependences
- calculate closure of sets
- calculate minimal set of keys and extra keys
- calculate minimal base
- check if scheme is in 2NF or 3NF
- if scheme is not in 3NF, it'll transfer it into 3NF

Project created by Adam Hącia 2020
