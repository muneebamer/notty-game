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

    # Return button variables for further use
    return button_x, start_y, button_width, button_height, button_gap

def game_rules_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    # Background
    screen.fill((0, 0, 0))  # Black background

    # Fonts and Colors
    font_path = pygame.font.match_font("arial")
    title_font = pygame.font.Font(font_path, 38)
    text_font = pygame.font.Font(font_path, 20)
    text_color = "#ffffff"
    back_button_color = "#bc4749"

    # Title
    title_text = "Game Rules"
    title_surface = title_font.render(title_text, True, text_color)
    title_x = (SCREEN_WIDTH - title_surface.get_width()) // 2
    title_y = 40
    screen.blit(title_surface, (title_x, title_y))

    # Rules Text
    rules_text = [
        "Overview:",
        "  - 2-3 players, 80-card deck (color + number).",
        "  - Cards: Red, Blue, Green, Yellow, numbered 1-10.",
        "",
        "Setup:",
        "  - Shuffle the deck, deal 5 cards face up to each player.",
        "  - Remaining deck stays face down.",
        "",
        "Gameplay (on your turn):",
        "  1. Draw up to 3 cards (once per turn).",
        "  2. Take 1 random card from another player.",
        "  3. Discard valid groups:",
        "     - Sequence: Same color, consecutive numbers.",
        "     - Set: Same number, different colors (no repeats).",
        "  4. Pass (do nothing).",
        "",
        "Goal: Empty your hand first to win!",
    ]
    line_height = 25  # Reduced spacing between lines
    center_x = SCREEN_WIDTH // 2  # Center alignment for text

    # Display each line of text, centered horizontally
    text_y = title_y + 60  # Start below the title
    for line in rules_text:
        text_surface = text_font.render(line, True, text_color)
        text_x = center_x - text_surface.get_width() // 2  # Center horizontally
        screen.blit(text_surface, (text_x, text_y))
        text_y += line_height

    # Back Button
    back_button_width = 200
    back_button_height = 50
    back_button_x = (SCREEN_WIDTH - back_button_width) // 2
    back_button_y = SCREEN_HEIGHT - 60  # Push the button closer to the bottom
    back_button_rect = pygame.Rect(back_button_x, back_button_y, back_button_width, back_button_height)
    pygame.draw.rect(screen, back_button_color, back_button_rect, border_radius=10)

    back_text = text_font.render("Back", True, text_color)
    back_text_x = back_button_x + (back_button_width - back_text.get_width()) // 2
    back_text_y = back_button_y + (back_button_height - back_text.get_height()) // 2
    screen.blit(back_text, (back_text_x, back_text_y))

    # Return the back button rectangle for interaction
    return back_button_rect



def main():
    # Pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    SCREEN_WIDTH = screen.get_width()
    SCREEN_HEIGHT = screen.get_height()
    
    # State variable to manage different screens
    state = "main"

    background_image = pygame.image.load("background.png")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if state == "main":
            # Render background image
            screen.blit(background_image, (0, 0))

            # Render game screens
            start_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

            # Render game screens and get button variables
            button_x, start_y, button_width, button_height, button_gap = start_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

            # Exit button functionality
            mouse_pos = pygame.mouse.get_pos()  # Get the current mouse position
            mouse_click = pygame.mouse.get_pressed()  # Check if a mouse button is pressed

            rules_button_rect = pygame.Rect(button_x, start_y + 1 * (button_height + button_gap), button_width, button_height)
            if rules_button_rect.collidepoint(mouse_pos) and mouse_click[0]:  # Check if "Game Rules" button is clicked
                state = "rules"  # Switch to rules screen

            exit_button_rect = pygame.Rect(button_x, start_y + 3 * (button_height + button_gap), button_width, button_height)
            if exit_button_rect.collidepoint(mouse_pos) and mouse_click[0]:  # If the left mouse button is pressed
                running = False  # Exit the game

        # Rules screen
        elif state == "rules":
            # Render the rules screen and get back button rectangle
            back_button_rect = game_rules_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

            # Handle Back button interaction
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()
            if back_button_rect.collidepoint(mouse_pos) and mouse_click[0]:  # Check if "Back" button is clicked
                state = "main"  # Return to main screen

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
