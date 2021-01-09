import roman

wybrana_liczba = str(input("Wpisz dużymi literami liczbę w systemie rzymskim: "))


def roman2int(roman_liczba):
    int_liczba = 0
    length = len(roman_liczba)
    for i in range(length):
        if i > 0 and roman.fromRoman(roman_liczba[i]) > roman.fromRoman(roman_liczba[i - 1]):
            # gdy pojawiają się "wyjątki" w stosunku do zwykłego sumowania jak np. 4
            int_liczba += roman.fromRoman(roman_liczba[i]) - roman.fromRoman(roman_liczba[i - 1]) - roman.fromRoman(roman_liczba[i - 1])
            # odejmuję wcześniej "błędnie" dodaną liczbę i dodaję właściwą, czyli większą pomniejszoną o mniejszą
        else:
            int_liczba += roman.fromRoman(roman_liczba[i])
    return int_liczba


print(roman2int(wybrana_liczba))
