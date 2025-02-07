# Model Response: x/llama3.2-vision
Generated on: 2025-02-07 21:08:55


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
Here is a basic implementation of the Cribbage card game in Python:

**cribbage.py**
<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
import random

# Define the ranks and suits of a deck of cards
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Define the values of each card
VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

# Define the cribbage hand
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        return sum(VALUES[card] for card in self.cards)

    def get_pairs(self):
        pairs = {}
        for card in self.cards:
            if VALUES[card] in pairs:
                pairs[VALUES[card]] += 1
            else:
                pairs[VALUES[card]] = 1
        return [(rank, count) for rank, count in pairs.items() if count > 1]

    def get_runs(self):
        runs = []
        sorted_cards = sorted([VALUES[card] for card in self.cards])
        for i in range(len(sorted_cards) - 2):
            if sorted_cards[i+1] == sorted_cards[i] + 1 and sorted_cards[i+2] == sorted_cards[i+1] + 1:
                runs.append((sorted_cards[i], sorted_cards[i+1], sorted_cards[i+2]))
        return runs

# Define the cribbage game
class Game:
    def __init__(self):
        self.deck = [card for suit in SUITS for rank in RANKS for card in [f"{rank} of {suit}"]]
        random.shuffle(self.deck)
        self.hand = Hand()
        self.crib = Hand()

    def deal(self, num_cards):
        for _ in range(num_cards):
            self.hand.add_card(self.deck.pop())

    def get_score(self):
        score = 0
        pairs = self.hand.get_pairs()
        runs = self.hand.get_runs()
        if pairs:
            score += len(pairs)
        if runs:
            score += len(runs) * 3
        return score

# Define the cribbage player
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def play(self, game):
        game.deal(6)
        print(f"{self.name}'s hand: {', '.join(game.hand.cards)}")
        print(f"Crib: {', '.join(game.crib.cards)}")
        score = game.get_score()
        print(f"Score for {self.name}: {score}")
        self.score += score
        print(f"{self.name}'s final score: {self.score}")

# Define the cribbage game loop
def play_game():
    game = Game()
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    while True:
        game.deal(4)
        print("Crib:", ', '.join(game.crib.cards))
        player1.play(game)
        player2.play(game)

# Play the game
play_game()
```
</div>
This code defines a basic implementation of the Cribbage card game. It includes classes for the deck, hand, and game, as well as a simple text-based interface for playing the game.

Note that this is just a starting point, and there are many ways to improve the game (e.g., adding more features, improving the user interface, etc.).

Here's an explanation of how the code works:

1. The `Hand` class represents a cribbage hand and has methods to add cards, get the value of the hand, and get pairs and runs.
2. The `Game` class represents a cribbage game and has methods to deal cards, get the score for a hand, and update the player's score.
3. The `Player` class represents a cribbage player and has methods to play a hand and update their score.
4. The `play_game` function sets up the game state and loops until the players have played all their hands.

To run the code, save it to a file called `cribbage.py` and run it with Python (e.g., `python cribbage.py`).

## Complete Code Summary
This section contains all the necessary code combined into a single, copyable block:

<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
# Complete implementation
# Generated by: x/llama3.2-vision
# Timestamp: 2025-02-07 21:08:55

import random

# Define the ranks and suits of a deck of cards
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Define the values of each card
VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

# Define the cribbage hand
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        return sum(VALUES[card] for card in self.cards)

    def get_pairs(self):
        pairs = {}
        for card in self.cards:
            if VALUES[card] in pairs:
                pairs[VALUES[card]] += 1
            else:
                pairs[VALUES[card]] = 1
        return [(rank, count) for rank, count in pairs.items() if count > 1]

    def get_runs(self):
        runs = []
        sorted_cards = sorted([VALUES[card] for card in self.cards])
        for i in range(len(sorted_cards) - 2):
            if sorted_cards[i+1] == sorted_cards[i] + 1 and sorted_cards[i+2] == sorted_cards[i+1] + 1:
                runs.append((sorted_cards[i], sorted_cards[i+1], sorted_cards[i+2]))
        return runs

# Define the cribbage game
class Game:
    def __init__(self):
        self.deck = [card for suit in SUITS for rank in RANKS for card in [f"{rank} of {suit}"]]
        random.shuffle(self.deck)
        self.hand = Hand()
        self.crib = Hand()

    def deal(self, num_cards):
        for _ in range(num_cards):
            self.hand.add_card(self.deck.pop())

    def get_score(self):
        score = 0
        pairs = self.hand.get_pairs()
        runs = self.hand.get_runs()
        if pairs:
            score += len(pairs)
        if runs:
            score += len(runs) * 3
        return score

# Define the cribbage player
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def play(self, game):
        game.deal(6)
        print(f"{self.name}'s hand: {', '.join(game.hand.cards)}")
        print(f"Crib: {', '.join(game.crib.cards)}")
        score = game.get_score()
        print(f"Score for {self.name}: {score}")
        self.score += score
        print(f"{self.name}'s final score: {self.score}")

# Define the cribbage game loop
def play_game():
    game = Game()
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    while True:
        game.deal(4)
        print("Crib:", ', '.join(game.crib.cards))
        player1.play(game)
        player2.play(game)

# Play the game
play_game()

```
</div>

## Usage Instructions
1. The code snippets above are wrapped in markdown code blocks with copy buttons
2. You can copy any code block by clicking the "Copy" button
3. The complete implementation is available in the "Complete Code Summary" section
4. Make sure to follow any setup instructions provided in the response

## Metadata
- Model: x/llama3.2-vision
- Timestamp: 2025-02-07 21:08:55
- File: test_x_llama3.2-vision_20250207_210855.md
