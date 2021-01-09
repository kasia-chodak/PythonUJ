# szczerze mówiąc nie do końca wiem, czy dobrze zrozumiałam zadanie

class Bug:
    licznik = 0

    def __init__(self):
        self.__class__.licznik += 1
        self.id = self.__class__.licznik

    def __del__(self):
        self.__class__.licznik -= 1
        return f"Koniec, identyfikator: {self.id}, licznik: {self.__class__.licznik}"

    def __str__(self):
        return f"identyfikator: {self.id}, licznik: {self.__class__.licznik}"


bugs = []

for i in range(100):
    bugs.append(Bug())
    print(bugs[-1])
