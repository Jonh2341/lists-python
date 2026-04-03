import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('My first minigame!')
clock = pygame.time.Clock()
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            player_pos.x = screen.get_width() / 2
            player_pos.y = screen.get_height() / 2

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, "red", (player_pos.x, player_pos.y, 40, 40))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    elif keys[pygame.K_s]:
        player_pos.y += 300 * dt
    elif keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    elif keys[pygame.K_d]:
        player_pos.x += 300 * dt
    else:
        print('no key')

        
    pygame.display.flip()

    dt = clock.tick(60) / 1000



pygame.quit()