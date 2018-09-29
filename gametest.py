import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)


size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("ASCII")

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User asked to quit.")
            done = True
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for x in range(0, 100, 20):
                pygame.draw.line(screen, GREEN, [x, 0], [x, 100], 5)
            print("User pressed a mouse button.")

        pygame.display.flip()
    clock.tick(60)



