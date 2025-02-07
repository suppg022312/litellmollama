# Model Response: llama3.2-vision
Generated on: 2025-02-07 21:11:14


<style>
.copy-button {
    position: absolute;
    top: 5px;
    right: 5px;
    padding: 5px 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 3px;
    cursor: pointer;
    z-index: 1;
}
.code-container {
    position: relative;
    margin: 10px 0;
}
.copy-button:hover {
    background-color: #45a049;
}
.copy-button:active {
    background-color: #3d8b40;
}
</style>

<script>
function copyCode(buttonElement) {
    const codeBlock = buttonElement.parentElement.querySelector('code');
    const range = document.createRange();
    range.selectNode(codeBlock);
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    try {
        document.execCommand('copy');
        buttonElement.textContent = 'Copied!';
        setTimeout(() => {
            buttonElement.textContent = 'Copy';
        }, 2000);
    } catch(e) {
        console.error('Failed to copy text:', e);
        buttonElement.textContent = 'Failed to copy';
    }
    window.getSelection().removeAllRanges();
}
</script>


## Original Task
<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```
python cribbage card game
```
</div>

## Model Solution
Cribbage is a classic card game that involves counting points for pairs, runs, and combinations of cards. Here's a simple implementation of the Cribbage game in Python:

**cribbage.py**
<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
import random

# Define the ranks and suits of a deck of cards
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Define the card values
VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}

# Define the cribbage hand
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def count_points(self):
        points = 0
        for i in range(len(self.cards)):
            for j in range(i+1, len(self.cards)):
                if RANKS.index(self.cards[i][0]) == RANKS.index(self.cards[j][0]):
                    points += VALUES[self.cards[i][0]]
                elif (RANKS.index(self.cards[i][0]) + 1) % 13 == RANKS.index(self.cards[j][0]):
                    points += VALUES[self.cards[i][0]] + VALUES[self.cards[j][0]]
        return points

# Define the cribbage game
class Game:
    def __init__(self):
        self.deck = [card for suit in SUITS for rank in RANKS for card in [(rank, suit)]]
        random.shuffle(self.deck)

    def deal_cards(self, num_players):
        hands = []
        for i in range(num_players):
            hand = Hand()
            for j in range(6):
                hand.add_card(self.deck.pop())
            hands.append(hand)
        return hands

    def play_round(self, player_hand, dealer_hand):
        print("Your hand:")
        for card in player_hand.cards:
            print(f"{card[0]} of {card[1]}")
        print("\nDealer's hand:")
        for card in dealer_hand.cards:
            print(f"{card[0]} of {card[1]}")

        # Determine the starter
        starter = random.choice(player_hand.cards)
        print(f"\nStarter: {starter[0]} of {starter[1]}\n")

        # Deal the crib
        crib = Hand()
        for card in dealer_hand.cards:
            if card == starter:
                continue
            crib.add_card(card)

        # Count points for your hand
        player_points = player_hand.count_points()
        print(f"\nYour hand: {player_points} points")

        # Count points for the crib
        crib_points = crib.count_points()
        print(f"Crib: {crib_points} points")

    def play_game(self, num_players):
        hands = self.deal_cards(num_players)
        dealer_hand = hands[0]

        while True:
            self.play_round(hands[1], dealer_hand)
            # Ask the player if they want to continue
            response = input("\nDo you want to continue playing? (y/n): ")
            if response.lower() != 'y':
                break

# Play the game
game = Game()
game.play_game(2)
```
</div>
This code defines a `Hand` class to represent a cribbage hand, which has methods for adding cards and counting points. The `Game` class represents the game itself, with methods for dealing cards, playing rounds, and determining the starter.

To play the game, run the script and follow the prompts. You will be dealt six cards and asked to play against the dealer's hand. After each round, you will be prompted to continue playing or quit.

Note that this is a very basic implementation of Cribbage, and there are many variations and rules that can be added to make it more realistic.

## Complete Code Summary
This section contains all the necessary code combined into a single, copyable block:

<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
# Complete implementation
# Generated by: llama3.2-vision
# Timestamp: 2025-02-07 21:11:14

import random

# Define the ranks and suits of a deck of cards
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Define the card values
VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}

# Define the cribbage hand
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def count_points(self):
        points = 0
        for i in range(len(self.cards)):
            for j in range(i+1, len(self.cards)):
                if RANKS.index(self.cards[i][0]) == RANKS.index(self.cards[j][0]):
                    points += VALUES[self.cards[i][0]]
                elif (RANKS.index(self.cards[i][0]) + 1) % 13 == RANKS.index(self.cards[j][0]):
                    points += VALUES[self.cards[i][0]] + VALUES[self.cards[j][0]]
        return points

# Define the cribbage game
class Game:
    def __init__(self):
        self.deck = [card for suit in SUITS for rank in RANKS for card in [(rank, suit)]]
        random.shuffle(self.deck)

    def deal_cards(self, num_players):
        hands = []
        for i in range(num_players):
            hand = Hand()
            for j in range(6):
                hand.add_card(self.deck.pop())
            hands.append(hand)
        return hands

    def play_round(self, player_hand, dealer_hand):
        print("Your hand:")
        for card in player_hand.cards:
            print(f"{card[0]} of {card[1]}")
        print("\nDealer's hand:")
        for card in dealer_hand.cards:
            print(f"{card[0]} of {card[1]}")

        # Determine the starter
        starter = random.choice(player_hand.cards)
        print(f"\nStarter: {starter[0]} of {starter[1]}\n")

        # Deal the crib
        crib = Hand()
        for card in dealer_hand.cards:
            if card == starter:
                continue
            crib.add_card(card)

        # Count points for your hand
        player_points = player_hand.count_points()
        print(f"\nYour hand: {player_points} points")

        # Count points for the crib
        crib_points = crib.count_points()
        print(f"Crib: {crib_points} points")

    def play_game(self, num_players):
        hands = self.deal_cards(num_players)
        dealer_hand = hands[0]

        while True:
            self.play_round(hands[1], dealer_hand)
            # Ask the player if they want to continue
            response = input("\nDo you want to continue playing? (y/n): ")
            if response.lower() != 'y':
                break

# Play the game
game = Game()
game.play_game(2)

```
</div>

## Usage Instructions
1. The code snippets above are wrapped in markdown code blocks with copy buttons
2. You can copy any code block by clicking the "Copy" button
3. The complete implementation is available in the "Complete Code Summary" section
4. Make sure to follow any setup instructions provided in the response

## Metadata
- Model: llama3.2-vision
- Timestamp: 2025-02-07 21:11:14
- File: test_llama3.2-vision_20250207_211114.md
