import pygame, sys
pygame.init()

BALL_ACCELERATION = 1

def main() :
    clock = pygame.time.Clock()
    #aesthetics - tło, ikonka, nazwa

    pygame.display.set_caption('The beginnings')
    icon = pygame.image.load(r'C:\Users\Kasia\Documents\ślimaczek.jpg') #r - ścieżka
    pygame.display.set_icon(icon)

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    image = pygame.image.load(r'C:\Users\Kasia\Documents\piasek na marsie.png')
    image = pygame.transform.scale(image, size) #skalowanie obrazu do size

    surf_center = (
        (width - image.get_width()) / 2,
        (height - image.get_height()) / 2
        ) #tupla wyliczjaąca środek

    ball_size = [75, 100]

    ball = pygame.image.load(r'C:\Users\Kasia\Documents\School\Studia\pythonProject\lekcja4\tennisball.gif')
    ball = pygame.transform.scale(ball, ball_size)
    #ballrect = ball.get_rect(center=(width / 2, height / 2)) #gdybym chciała uzyskać wymiary prostokąta - zdjęcia piłki
    ballPosition = ballPositionX, ballPositionY = (width / 2, height / 2)
    ball_speed = [0, 0]


    while True :
        pygame.time.delay(50)
        clock.tick(60)

        for event in pygame.event.get() :
            if event.type == pygame.QUIT : sys.exit()

        screen.blit(image, surf_center)  # narysowanie tła na środku okienka

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] : sys.exit()

        if keys[pygame.K_UP] :
            ball_speed[1] -= BALL_ACCELERATION
        elif keys[pygame.K_DOWN] :
            ball_speed[1] += BALL_ACCELERATION
        elif keys[pygame.K_LEFT] :
            ball_speed[0] -= BALL_ACCELERATION
        elif keys[pygame.K_RIGHT] :
            ball_speed[0] += BALL_ACCELERATION
        ballPosition = ballPositionX, ballPositionY = ballPositionX + ball_speed[0], ballPositionY + ball_speed[1]
        screen.blit(ball, ballPosition)

        if ballPositionX < 0 or ballPositionX > (width - ball_size[0]):
            ball_speed[0] *= -1

        if ballPositionY < 0 or ballPositionY > (height - ball_size[1]):
            ball_speed[1] *= -1

        #speed = [1, 2]
        #ballrect = ballrect.move(speed)
        #if ballrect.left < 0 or ballrect.right > width :
        #    speed[0] = -speed[0]
        #if ballrect.top < 0 or ballrect.bottom > height :
        #    speed[1] = -speed[1]

        pygame.display.flip()  # odświeżanie wszystkiego

if __name__ == '__main__' :
    main()
    pygame.quit()
    sys.exit()