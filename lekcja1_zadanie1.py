liczba = int(input("Wpisz nieparzystą liczbę gwiazdek na podstawie piramidy: "))


def poziom_piramidy(number, height):
    poziom = ''
    spaces = height - 1
    while spaces > 0:
        poziom += ' '
        spaces -= 1
    stars = number
    while stars > 0:
        poziom += '*'
        stars -= 1
    return poziom


# liczba poziomów piramidy to liczba / 2 + 1
final_heigth = liczba // 2 + 1
wysokosc = 1

if liczba % 2 == 0 or liczba <= 0:
    print("Zrestartuj program i wpisz inną liczbę - musi być dodatnia i nieparzysta.")
else:
    while liczba > 0 and wysokosc <= final_heigth:
        print(poziom_piramidy(liczba, wysokosc))
        liczba -= 2
        wysokosc += 1
