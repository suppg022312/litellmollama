# Model Response: llama3.2-3b-instruct-fp16
Generated on: 2025-02-07 21:10:36


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
Cribbage is a popular two-player card game that involves counting points for pairs, runs, and combinations of cards. Here's a simplified implementation of the game in Python:

<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
import random

# Define suits and ranks
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Define card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

# Define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def draw(self, deck):
        self.cards.append(deck.pop())

    def discard(self, card):
        if card in self.cards:
            self.cards.remove(card)

    def sort_cards(self):
        self.cards.sort(key=lambda x: ranks.index(x.rank))

# Define deck class
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def draw(self, num_draws=1):
        return [self.cards.pop() for _ in range(num_draws)]

# Define cribbage game class
class Cribbage:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def deal_cards(self, num_cards=6):
        player_hand.draw(self.deck, num_cards)
        dealer_hand.draw(self.deck, num_cards)

    def show_hands(self):
        print("Player's hand:")
        for card in self.player_hand.cards:
            print(card)
        print("\nDealer's hand:")
        for card in self.dealer_hand.cards:
            print(card)

    def calculate_score(self, hand):
        score = 0
        pairs = 0

        # Count pairs
        for i in range(len(hand.cards) - 1):
            if hand.cards[i].rank == hand.cards[i+1].rank:
                pairs += 1
                score += 2 + (i * 10)

        # Count runs
        current_run = [hand.cards[0]]
        for card in hand.cards[1:]:
            if ranks.index(card.rank) == ranks.index(current_run[-1].rank) + 1:
                current_run.append(card)
            else:
                run_points = sum([ranks.index(card.rank) for card in current_run])
                score += run_points
                current_run = [card]

        # Count combinations
        for i in range(len(hand.cards)):
            for j in range(i+1, len(hand.cards)):
                if ranks.index(hand.cards[i].rank) + 5 == ranks.index(hand.cards[j].rank):
                    score += 2

        return score, pairs

    def play_game(self):
        self.deal_cards()
        print("\nShow hands:")
        self.show_hands()

        # Calculate scores
        player_score, player_pairs = self.calculate_score(self.player_hand)
        dealer_score, dealer_pairs = self.calculate_score(self.dealer_hand)

        print(f"\nPlayer's score: {player_score} pairs: {player_pairs}")
        print(f"Dealer's score: {dealer_score} pairs: {dealer_pairs}")

        # Determine winner
        if player_score > dealer_score:
            print("You win!")
        elif dealer_score > player_score:
            print("Dealer wins!")
        else:
            print("It's a tie!")

# Create and play game
game = Cribbage()
game.play_game()
```
</div>

This implementation provides basic functionality for playing cribbage. The `Card`, `Hand`, and `Deck` classes define the structure of the cards, hands, and decks used in the game. The `Cribbage` class manages the gameplay logic, including dealing cards, calculating scores, and determining the winner.

You can extend this implementation by adding additional features such as:

* Implementing the "cribbage" rule, where the player sets aside a subset of their cards to be held by the dealer
* Allowing players to discard cards from their hand
* Implementing rules for scoring pairs, runs, and combinations
* Providing options for multiple hands or games

## Complete Code Summary
This section contains all the necessary code combined into a single, copyable block:

<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
# Complete implementation
# Generated by: llama3.2-3b-instruct-fp16
# Timestamp: 2025-02-07 21:10:36

import random

# Define suits and ranks
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Define card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

# Define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def draw(self, deck):
        self.cards.append(deck.pop())

    def discard(self, card):
        if card in self.cards:
            self.cards.remove(card)

    def sort_cards(self):
        self.cards.sort(key=lambda x: ranks.index(x.rank))

# Define deck class
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def draw(self, num_draws=1):
        return [self.cards.pop() for _ in range(num_draws)]

# Define cribbage game class
class Cribbage:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def deal_cards(self, num_cards=6):
        player_hand.draw(self.deck, num_cards)
        dealer_hand.draw(self.deck, num_cards)

    def show_hands(self):
        print("Player's hand:")
        for card in self.player_hand.cards:
            print(card)
        print("\nDealer's hand:")
        for card in self.dealer_hand.cards:
            print(card)

    def calculate_score(self, hand):
        score = 0
        pairs = 0

        # Count pairs
        for i in range(len(hand.cards) - 1):
            if hand.cards[i].rank == hand.cards[i+1].rank:
                pairs += 1
                score += 2 + (i * 10)

        # Count runs
        current_run = [hand.cards[0]]
        for card in hand.cards[1:]:
            if ranks.index(card.rank) == ranks.index(current_run[-1].rank) + 1:
                current_run.append(card)
            else:
                run_points = sum([ranks.index(card.rank) for card in current_run])
                score += run_points
                current_run = [card]

        # Count combinations
        for i in range(len(hand.cards)):
            for j in range(i+1, len(hand.cards)):
                if ranks.index(hand.cards[i].rank) + 5 == ranks.index(hand.cards[j].rank):
                    score += 2

        return score, pairs

    def play_game(self):
        self.deal_cards()
        print("\nShow hands:")
        self.show_hands()

        # Calculate scores
        player_score, player_pairs = self.calculate_score(self.player_hand)
        dealer_score, dealer_pairs = self.calculate_score(self.dealer_hand)

        print(f"\nPlayer's score: {player_score} pairs: {player_pairs}")
        print(f"Dealer's score: {dealer_score} pairs: {dealer_pairs}")

        # Determine winner
        if player_score > dealer_score:
            print("You win!")
        elif dealer_score > player_score:
            print("Dealer wins!")
        else:
            print("It's a tie!")

# Create and play game
game = Cribbage()
game.play_game()

```
</div>

## Usage Instructions
1. The code snippets above are wrapped in markdown code blocks with copy buttons
2. You can copy any code block by clicking the "Copy" button
3. The complete implementation is available in the "Complete Code Summary" section
4. Make sure to follow any setup instructions provided in the response

## Metadata
- Model: llama3.2-3b-instruct-fp16
- Timestamp: 2025-02-07 21:10:36
- File: test_llama3.2-3b-instruct-fp16_20250207_211036.md
