import pygame

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    SCREEN_WIDTH = screen.get_width()
    SCREEN_HEIGHT = screen.get_height()

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("#2a513c")

        # RENDER YOUR GAME HERE
        pygame.draw.circle(screen, "red", player_pos, 80)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 600 * dt
        if keys[pygame.K_s]:
            player_pos.y += 600 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 600 * dt
        if keys[pygame.K_d]:
            player_pos.x += 600 * dt

        if player_pos.x >= SCREEN_WIDTH:
            player_pos.x = -80
        if player_pos.y >= SCREEN_HEIGHT:
            player_pos.y = -80

        pygame.display.flip()

        print("Position: ",player_pos)

        dt = clock.tick(60) / 1000

    pygame.quit()
if __name__ == '__main__':
    main()