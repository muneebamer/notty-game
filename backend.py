import random


# Define the Card class
class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __str__(self):
        return f"{self.color} {self.number}"

    def __repr__(self):
        return f"Card({self.color}, {self.number})"


# Define the Deck class
class Deck:
    def __init__(self):
        self.cards = [
            Card(color, number) for color in ["red", "blue", "green", "yellow"] for number in range(1, 11)
        ] * 2  # Two of each card
        random.shuffle(self.cards)
        self.discards = []  # Discard pile

    def draw(self, num_cards):
        """
        Draws the requested number of cards from the deck.
        If the deck is empty, reshuffles the discard pile back into the deck.
        """
        if len(self.cards) < num_cards:
            self._reshuffle_discard_pile()

        return [self.cards.pop() for _ in range(min(num_cards, len(self.cards)))]

    def _reshuffle_discard_pile(self):
        """
        Shuffles the discard pile back into the main deck.
        """
        if self.discards:
            self.cards.extend(self.discards)
            random.shuffle(self.cards)
            self.discards.clear()

    def add_to_discard(self, cards):
        """
        Adds discarded cards to the discard pile.
        """
        self.discards.extend(cards)


# Define the Player class
class Player:
    def __init__(self, name, is_human=True):
        self.name = name
        self.is_human = is_human
        self.cards = []

    def add_cards(self, cards):
        self.cards.extend(cards)

    def remove_cards(self, cards):
        for card in cards:
            self.cards.remove(card)

    def is_valid_group(self, collection):
        """Checks if the collection of cards is a valid group."""
        if len(collection) < 3:
            return False

        colors = {card.color for card in collection}
        numbers = sorted(card.number for card in collection)

        # Case 1: All cards have the same color and consecutive numbers
        if len(colors) == 1 and all(numbers[i] + 1 == numbers[i + 1] for i in range(len(numbers) - 1)):
            return True

        # Case 2: All cards have the same number and different colors
        if len(set(numbers)) == 1 and len(colors) == len(collection):
            return True

        return False

    def find_valid_group(self):
        """Finds a valid group in the player's collection."""
        if len(self.cards) < 3:
            return None

        colors = [card.color for card in self.cards]
        numbers = [card.number for card in self.cards]

        # Case 1: Group with the same number and different colors
        for num in set(numbers):
            same_number_cards = [card for card in self.cards if card.number == num]
            if len(same_number_cards) >= 3 and len({card.color for card in same_number_cards}) == len(same_number_cards):
                return same_number_cards

        # Case 2: Group with the same color and consecutive numbers
        for color in set(colors):
            same_color_cards = sorted((card for card in self.cards if card.color == color), key=lambda x: x.number)
            for i in range(len(same_color_cards) - 2):
                if (same_color_cards[i].number + 1 == same_color_cards[i + 1].number and
                        same_color_cards[i + 1].number + 1 == same_color_cards[i + 2].number):
                    return same_color_cards[i:i + 3]

        return None

    def find_largest_valid_group(self):
        """Finds the largest valid group in the player's collection."""
        largest_group = []
        while True:
            valid_group = self.find_valid_group()
            if valid_group and len(valid_group) > len(largest_group):
                largest_group = valid_group
                for card in valid_group:
                    self.cards.remove(card)
            else:
                break
        return largest_group or None

    def steal_card(self, target_player):
        """Steals a random card from another player."""
        if target_player.cards:
            stolen_card = random.choice(target_player.cards)
            target_player.remove_cards([stolen_card])
            return stolen_card
        return None



# Define the Game class
class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = [Player("Player 1", True), Player("Computer 1", False), Player("Computer 2", False)]
        self.current_player_idx = 0
        self.message = ""

    def next_player(self):
        self.current_player_idx = (self.current_player_idx + 1) % len(self.players)

    def check_winner(self):
        for player in self.players:
            if not player.cards:
                return player
        return None

    def draw_cards(self, player, num_cards):
        """Draw cards for a player."""
        if num_cards <= 3:
            drawn_cards = self.deck.draw(num_cards)
            player.add_cards(drawn_cards)
            self.message = f"{player.name} drew {num_cards} card(s)"
        else:
            self.message = "You can draw up to 3 cards"

    def take_card_from_another_player(self, current_player, target_player):
        """Steal a random card from another player."""
        stolen_card = current_player.steal_card(target_player)
        if stolen_card:
            self.message = f"{current_player.name} stole {stolen_card} from {target_player.name}"

    def discard_largest_valid_group(self, player):
        """Discard the largest valid group."""
        largest_group = player.find_largest_valid_group()
        if largest_group:
            self.deck.add_to_discard(largest_group)
            self.message = f"{player.name} discarded the largest valid group: {largest_group}"
        else:
            self.message = f"{player.name} has no valid group to discard"


# Function to print the current game state
def print_game_state(game):
    print("\nCurrent Game State:")
    for i, player in enumerate(game.players):
        print(f"\n{player.name}'s cards:")
        for card in player.cards:
            print(card)
    print(f"\nMessage: {game.message}")


# Function to prompt the human player for input
def human_player_turn(game, current_player):
    print(f"\n{current_player.name}'s turn!")
    
    # Draw cards
    draw_choice = input("How many cards do you want to draw? (1, 2, 3): ")
    if draw_choice in ["1", "2", "3"]:
        game.draw_cards(current_player, int(draw_choice))
    else:
        print("Invalid choice. You can only draw up to 3 cards.")
        return

    # Option to steal a card
    steal_choice = input("Do you want to steal a card from another player? (y = yes, n = no): ")
    if steal_choice == "y":
        target_player = choose_target_player(game, current_player)
        game.take_card_from_another_player(current_player, target_player)

    # Discard the largest valid group or skip
    action_choice = input("Do you want to discard the largest valid group or skip your turn? (d = discard, s = skip): ")
    if action_choice == "d":
        game.discard_largest_valid_group(current_player)
    elif action_choice == "s":
        print(f"{current_player.name} skipped their turn.")
    else:
        print("Invalid action. You can only choose to discard or skip.")


def choose_target_player(game, current_player):
    """Helper function for the human player to select a target player for stealing."""
    print("\nChoose a player to steal from:")
    available_targets = [player for player in game.players if player != current_player]
    for idx, target in enumerate(available_targets):
        print(f"{idx + 1}. {target.name}")
    target_choice = int(input("Enter the number of the player you want to steal from: ")) - 1
    return available_targets[target_choice]


# Main game loop
def main():
    game = Game()
    running = True

    # Initial card distribution
    for player in game.players:
        player.add_cards(game.deck.draw(5))

    while running:
        current_player = game.players[game.current_player_idx]

        # Print the current game state
        print_game_state(game)

        if current_player.is_human:
            human_player_turn(game, current_player)
        else:
            print(f"\n{current_player.name}'s turn (Computer)!")
            # Simulate computer player actions
            action = random.choice([1, 2, 3, 4, 5])  # Random action
            if action == 1:
                game.draw_cards(current_player, random.randint(1, 3))
            elif action == 2:
                target_player = random.choice([player for player in game.players if player != current_player])
                game.take_card_from_another_player(current_player, target_player)
            elif action == 3:
                game.discard_largest_valid_group(current_player)

        # Check for winner
        winner = game.check_winner()
        if winner:
            print(f"\n{winner.name} wins!")
            running = False
        else:
            game.next_player()


# Run the game
if __name__ == "__main__":
    main()
