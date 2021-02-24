width = int(input("Wpisz pożądaną długość miarki: "))

podzialka = '|'
miarka = '0'
dlugosc_1 = width

while dlugosc_1 > 0:
    podzialka += ' . . . . |'
    dlugosc_1 -= 1

odliczanie = 1
while odliczanie <= width:
    ile_spacji = 10 - len(str(odliczanie))
    while ile_spacji > 0:
        miarka += ' '
        ile_spacji -= 1
    miarka += (str(odliczanie))
    odliczanie += 1


if width <= 0:
    print("Miarka nie istnieje.")
else:
    print(podzialka)
    print(miarka)
