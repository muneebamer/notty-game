import pygame


def start_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    # Margins and colors
    margin = 40
    container_color = (19, 58, 17, 160)
    text_color = "#ffffff"
    font_path = pygame.font.match_font("arial")  # Default font

    # Fonts
    title_font = pygame.font.Font(font_path, 38)
    button_font = pygame.font.Font(font_path, 20)

    # Main container dimensions
    rect_x = margin
    rect_y = margin
    rect_width = SCREEN_WIDTH - 2 * margin
    rect_height = SCREEN_HEIGHT - 2 * margin

    # Transparent container
    container_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
    container_surface.fill(container_color)
    screen.blit(container_surface, (rect_x, rect_y))

    # border
    # for i in range(4):
    #     border_pos = pygame.Rect(rect_x - i, rect_y - i, rect_width, rect_height)
    #     pygame.draw.rect(screen, button_color, border_pos, 1, border_radius=20)

    # Title
    title_text = "Notty Game"
    title_surface = title_font.render(title_text, True, text_color)
    title_x = rect_x + (rect_width - title_surface.get_width()) // 2
    title_y = rect_y + 50
    screen.blit(title_surface, (title_x, title_y))

    # Buttons
    button_width = rect_width // 2
    button_height = 60
    button_x = rect_x + (rect_width - button_width) // 2
    button_gap = 40
    start_y = title_y + 100  # Space below the title

    button_texts = ["Play", "Game rules", "Credits", "Exit"]
    button_colors = ["#000000", "#000000", "#000000", "#bc4749"]
    for i, text in enumerate(button_texts):
        button_y = start_y + i * (button_height + button_gap)
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        pygame.draw.rect(screen, button_colors[i], button_rect, border_radius=10)

        # Button text
        button_surface = button_font.render(text, True, text_color)
        text_x = button_x + (button_width - button_surface.get_width()) // 2
        text_y = button_y + (button_height - button_surface.get_height()) // 2
        screen.blit(button_surface, (text_x, text_y))


def main():
    # Pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    SCREEN_WIDTH = screen.get_width()
    SCREEN_HEIGHT = screen.get_height()

    background_image = pygame.image.load("background.png")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Render background image
        screen.blit(background_image, (0, 0))

        # Render game screens
        start_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
