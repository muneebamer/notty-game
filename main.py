import pygame
import sys


def start_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    # Margins and colors
    margin = 40
    container_color = (35, 64, 41, 120)
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
    global button_rects  # Store button rects for click detection
    button_rects = []
    for i, text in enumerate(button_texts):
        button_y = start_y + i * (button_height + button_gap)
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        pygame.draw.rect(screen, button_colors[i], button_rect, border_radius=10)
        button_rects.append(button_rect)  # Save rect for click detection

        # Button text
        button_surface = button_font.render(text, True, text_color)
        text_x = button_x + (button_width - button_surface.get_width()) // 2
        text_y = button_y + (button_height - button_surface.get_height()) // 2
        screen.blit(button_surface, (text_x, text_y))


def play_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    """Render the main game screen with Game Settings."""
    # Margins and colors
    container_color = (35, 64, 41, 120)
    text_color = "#ffffff"
    font_path = pygame.font.match_font("arial")  # Default font
    title_font = pygame.font.Font(font_path, 32)
    paragraph_font = pygame.font.Font(font_path, 18)
    button_font = pygame.font.Font(font_path, 18)

    # Load and scale the background image
    main_bg_image = pygame.image.load("main-bg.jpg")
    main_bg_image = pygame.transform.scale(main_bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Render background image
    screen.blit(main_bg_image, (0, 0))

    # Game Settings Container Dimensions
    container_width = SCREEN_WIDTH // 2
    container_height = SCREEN_HEIGHT
    container_x = (SCREEN_WIDTH - container_width) // 2
    container_y = (SCREEN_HEIGHT - container_height) // 2

    # Transparent container for settings
    container_surface = pygame.Surface(
        (container_width, container_height), pygame.SRCALPHA
    )
    container_surface.fill(container_color)
    screen.blit(container_surface, (container_x, container_y))

    # Title: Game Settings
    title_text = "Game Settings"
    title_surface = title_font.render(title_text, True, text_color)
    title_x = container_x + (container_width - title_surface.get_width()) // 2
    title_y = container_y + 44
    screen.blit(title_surface, (title_x, title_y))

    # Body

    para_text = "Select how many players you want to play with"
    para_surface = paragraph_font.render(para_text, True, text_color)
    para_x = container_x + (container_width - para_surface.get_width()) // 2
    para_y = title_y + 84
    screen.blit(para_surface, (para_x, para_y))

    # Options and Start Game Button
    option_width = container_width // 2
    option_height = 50
    option_gap = 20
    option_x = container_x + (container_width - option_width) // 2
    option_y_start = para_y + 100

    global option_1_rect, option_2_rect, start_button_rect, home_button_rect

    # Option 1: 1 Computer Player
    option_1_rect = pygame.Rect(option_x, option_y_start, option_width, option_height)
    pygame.draw.rect(screen, "#000000", option_1_rect, border_radius=10)
    option_1_text = button_font.render("1 Computer Player", True, text_color)
    screen.blit(
        option_1_text,
        (
            option_x + (option_width - option_1_text.get_width()) // 2,
            option_y_start + (option_height - option_1_text.get_height()) // 2,
        ),
    )

    # Option 2: 2 Computer Players
    option_2_rect = pygame.Rect(
        option_x,
        option_y_start + option_height + option_gap,
        option_width,
        option_height,
    )
    pygame.draw.rect(screen, "#000000", option_2_rect, border_radius=10)
    option_2_text = button_font.render("2 Computer Players", True, text_color)
    screen.blit(
        option_2_text,
        (
            option_x + (option_width - option_2_text.get_width()) // 2,
            option_y_start
            + option_height
            + option_gap
            + (option_height - option_2_text.get_height()) // 2,
        ),
    )

    # Start Game Button
    start_button_y = option_y_start + 2 * (option_height + option_gap)
    start_button_rect = pygame.Rect(
        option_x, start_button_y, option_width, option_height
    )
    pygame.draw.rect(screen, "#6A994E", start_button_rect, border_radius=10)
    start_button_text = button_font.render("Start Game", True, text_color)
    screen.blit(
        start_button_text,
        (
            option_x + (option_width - start_button_text.get_width()) // 2,
            start_button_y + (option_height - start_button_text.get_height()) // 2,
        ),
    )

    # Back to Home Button
    home_button_y = SCREEN_HEIGHT - 100
    home_button_rect = pygame.Rect(
        option_x, home_button_y, option_width, option_height
    )
    pygame.draw.rect(screen, "#bc4749", home_button_rect, border_radius=10)
    home_button_text = button_font.render("Back to Home", True, text_color)
    screen.blit(
        home_button_text,
        (
            option_x + (option_width - home_button_text.get_width()) // 2,
            home_button_y + (option_height - home_button_text.get_height()) // 2,
        ),
    )

def main_board_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    """Render the main game screen."""
    font_path = pygame.font.match_font('arial')
    title_font = pygame.font.Font(font_path, 38)

    # Load and scale the background image
    main_bg_image = pygame.image.load("start-game-bg.jpg")
    main_bg_image = pygame.transform.scale(main_bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Render background image
    screen.blit(main_bg_image, (0, 0))

    # Title for the game screen
    title_text = "Welcome to the Game!"
    title_surface = title_font.render(title_text, True, (255, 255, 255))
    title_x = (SCREEN_WIDTH - title_surface.get_width()) // 2
    title_y = (SCREEN_HEIGHT - title_surface.get_height()) // 2
    screen.blit(title_surface, (title_x, title_y))


def handle_button_click(mouse_pos):
    """Handle button clicks and return the action."""
    if button_rects[0].collidepoint(mouse_pos):  # Play button
        return "play"
    elif button_rects[3].collidepoint(mouse_pos):  # Exit button
        return "exit"
    return None


def handle_play_screen_click(mouse_pos):
    """Handle clicks in the play screen."""
    if option_1_rect.collidepoint(mouse_pos):
        print("Selected 1 Computer Player")
    elif option_2_rect.collidepoint(mouse_pos):
        print("Selected 2 Computer Players")
    elif start_button_rect.collidepoint(mouse_pos):
        return "board"
    elif home_button_rect.collidepoint(mouse_pos):
        return "start"


def main():
    # Pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    SCREEN_WIDTH = screen.get_width()
    SCREEN_HEIGHT = screen.get_height()

    # Load and scale the background image
    background_image = pygame.image.load("main-bg.jpg")
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    current_screen = "start"  # Track current screen

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle button clicks
            if (
                event.type == pygame.MOUSEBUTTONDOWN and event.button == 1
            ):  # Left mouse button
                mouse_pos = pygame.mouse.get_pos()
                if current_screen == "start":
                    action = handle_button_click(mouse_pos)
                    if action == "play":
                        current_screen = "play"
                    elif action == "exit":
                        running = False
                elif current_screen == "play":
                    action = handle_play_screen_click(mouse_pos)
                    if action == "start":
                        current_screen = "start"
                    elif action == "board":
                        current_screen = "board"

        # Render background image
        screen.blit(background_image, (0, 0))

        # Render the current screen
        if current_screen == "start":
            start_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
        elif current_screen == "play":
            play_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
        elif current_screen == "board":
            main_board_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
