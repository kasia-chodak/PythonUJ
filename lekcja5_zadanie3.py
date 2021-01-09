import pygame
from random import randint

pygame.init()

# kolory
CZARNY = (0, 0, 0)
BIALY = (255, 255, 255)

class Rakietka(pygame.sprite.Sprite):
    # klasa Rakietka dziedziczy z klasy "Sprite" w Pygame.

    def __init__(self, color, width, height):
        # wołamy najpierw konstruktor klasy bazowej (Sprite)
        # dzięki metodzie super() dziedziczymy wszystkie elementy klasy bazowej
        super().__init__()

        # przekazanie koloru Rakietka oraz szerokości i wysokości, kolor tła i ustawienie go na przezroczyste
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)

        # rysuję Rakietka jako prostokąt
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # pobieramy prostokąt (jego rozmiary) z obiektu image
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # sprawdzanie położenia brzegowego
        if self.rect.x < 0:
           self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        # sprawdzanie położenia brzegowego
        if self.rect.x > 600:
           self.rect.x = 600



class Pilka(pygame.sprite.Sprite):
    # klasa Pilka dziedziczy ze "Sprite" w Pygame.

    def __init__(self, color, width, height):
        # wołamy konstruktor klasy bazowej
        super().__init__()

        # przekazujemy rozmiary, kolor, przezroczystość
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)

        # rysowanie piłki (jako prostokącika)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # losowanie prędkości
        self.velocity = [randint(4, 6), randint(-7, 7)]

        # pobieramy prostokąt (jego rozmiary) z obiektu image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[1] = -self.velocity[1]
        self.velocity[0] = randint(-8,8)



# definiujemy rozmiary i otwieramy nowe okno
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

rakietkaA = Rakietka(BIALY, 100, 10)
rakietkaA.rect.x = 200
rakietkaA.rect.y = 450

pileczka = Pilka(BIALY,10,10)
pileczka.rect.x = 345
pileczka.rect.y = 10

# lista wszystkich widzalnych obiektów potomnych z klasy Sprite
all_sprites_list = pygame.sprite.Group()

# dodanie rakietki i piłeczki do listy
all_sprites_list.add(rakietkaA)
all_sprites_list.add(pileczka)

# zaczynamy właściwy blok programu
kontynuuj = True

# służy do kontroli liczby klatek na sekudnę (fps)
clock = pygame.time.Clock()

# Początkowe wyniki graczy
score = 0
scores = []

# -------- GLÓWNA PĘTLA PROGRAMU -----------
while kontynuuj:

    in_game = True  # aktywna gra
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # zamknięcie okienka
            kontynuuj = False

    font = pygame.font.Font(None, 50)
    smaller_font = pygame.font.Font(None, 20)

    # ruchy obiektu Rakietka klawisze strzałka lewo prawo
    if keys[pygame.K_LEFT]:
        rakietkaA.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        rakietkaA.moveRight(5)

    # aktualizacja listy duszków
    all_sprites_list.update()

    # sprawdzenie czy piłeczka nie uderza w którąś ścianę
    if pileczka.rect.y<=0:
        pileczka.velocity[1] = -pileczka.velocity[1]
    if pileczka.rect.x>700:
        pileczka.velocity[0] = -pileczka.velocity[0]
    if pileczka.rect.x<0:
        pileczka.velocity[0] = -pileczka.velocity[0]

    # sprawdzenie kolizji piłeczki z obiektem rakietka
    if pygame.sprite.collide_mask(pileczka, rakietkaA):
        pileczka.bounce()
        score += 1

    # RYSOWANIE
    # czarny ekran
    screen.fill(CZARNY)

    # narysowanie obiektów
    all_sprites_list.draw(screen)

    # wyświetlanie wyników
    text = font.render(str(f"Obecny wynik: {score}"), True, BIALY)
    screen.blit(text, (200,10))

    scores.append(score)
    naj_wynik = max(scores)

    if pileczka.rect.y == 500 or pileczka.rect.y > 500:  # przegrana
        in_game = False
        screen.fill(CZARNY)
        text = font.render(str(f"Koniec gry. Twój wynik to {score}."), True, BIALY)
        another_text = smaller_font.render(str(f"Twój najwyższy wynik to {naj_wynik}. Wciśnij klawisz r, aby zagrać ponownie."), True, BIALY)
        screen.blit(text, (140,10))
        screen.blit(another_text, (150, 60))
        pileczka.velocity = [0, 0]
        all_sprites_list.draw(screen)

    if keys[pygame.K_r] and not in_game:  # ponowne uruchomienie gry
        score = 0
        screen.fill(CZARNY)
        rakietkaA.rect.x = 200
        rakietkaA.rect.y = 450
        pileczka.rect.x = 345
        pileczka.rect.y = 10
        pileczka.velocity = [randint(4, 6), randint(-7, 7)]
        all_sprites_list.update()
        text = font.render(str(f"Obecny wynik: {score}"), True, BIALY)
        screen.blit(text, (200, 10))
        all_sprites_list.draw(screen)
        pygame.display.flip()
        in_game = True


    # odświeżenie / przerysowanie całego ekranu
    pygame.display.flip()

    # 60 klatek na sekundę
    clock.tick(60)

# koniec
pygame.quit()