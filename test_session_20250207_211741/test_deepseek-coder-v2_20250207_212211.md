# Model Response: deepseek-coder-v2
Generated on: 2025-02-07 21:22:11


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
python pontoon game
```
</div>

## Model Solution
 A Pontoon (or Blackjack) game is a card game where the goal is to get as close to 21 points as possible without going over. The player competes against the dealer, and players are allowed to draw cards until they either choose to stand or bust (exceeding 21 points). In this implementation, we'll simulate a simplified version of Pontoon where only two players can play: the player and the dealer.

Here's a basic Python script for simulating a Pontoon game:

<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
import random

# Define card values
card_values = {
    'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10
}

# Function to calculate the score of a hand
def calculate_score(hand):
    score = sum([card_values[card] for card in hand])
    # Count Aces as 11 if they don't cause a bust; otherwise, count them as 1
    aces = [card for card in hand if card == 'A']
    while score > 21 and aces:
        score -= 10
        aces.remove('A')
    return score

# Function to deal cards from the deck
def deal_cards(deck, num):
    dealt_cards = []
    for _ in range(num):
        card = random.choice(deck)
        dealt_cards.append(card)
        deck.remove(card)
    return dealt_cards

# Function to check if the player or dealer busts
def is_bust(score):
    return score > 21

# Main game function
def play_pontoon():
    # Define the deck of cards
    suits = ['♠', '♥', '♦', '♣']
    ranks = list(card_values.keys()) + ['A'] * 4  # Include four Aces for flexibility
    deck = [rank + suit for suit in suits for rank in ranks]
    
    # Initial deal to the player and dealer
    player_hand = deal_cards(deck, 2)
    dealer_hand = deal_cards(deck, 2)
    
    print("Player's hand:", player_hand)
    print("Dealer's showing card:", dealer_hand[0])
    
    # Player's turn
    while True:
        choice = input("Do you want to hit or stand? (h/s): ").strip().lower()
        if choice == 'h':
            player_hand.extend(deal_cards(deck, 1))
            print("Player hits:", player_hand)
        elif choice == 's':
            break
        
        # Check if the player busts
        if is_bust(calculate_score(player_hand)):
            print("Player busts! Dealer wins.")
            return
    
    # Dealer's turn (auto-complete for simplicity)
    while calculate_score(dealer_hand) < 17:
        dealer_hand.extend(deal_cards(deck, 1))
    
    print("Dealer's hand:", dealer_hand)
    
    # Determine the winner
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    
    if is_bust(dealer_score):
        print("Dealer busts! Player wins.")
    elif player_score > dealer_score:
        print("Player wins!")
    elif player_score < dealer_score:
        print("Dealer wins.")
    else:
        print("It's a tie.")

# Start the game
play_pontoon()
```
</div>

This script includes basic functionality for dealing cards, calculating scores, and handling player choices. The player can choose to hit or stand based on their current hand. If the player busts, they lose immediately. Otherwise, both the player and dealer will draw cards until the conditions are met (either going over 21 or standing).

Please note that this script is a simplified version of Pontoon and does not include all the nuances of traditional Blackjack, such as splitting pairs or doubling down.

## Complete Code Summary
This section contains all the necessary code combined into a single, copyable block:

<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
# Complete implementation
# Generated by: deepseek-coder-v2
# Timestamp: 2025-02-07 21:22:11

import random

# Define card values
card_values = {
    'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10
}

# Function to calculate the score of a hand
def calculate_score(hand):
    score = sum([card_values[card] for card in hand])
    # Count Aces as 11 if they don't cause a bust; otherwise, count them as 1
    aces = [card for card in hand if card == 'A']
    while score > 21 and aces:
        score -= 10
        aces.remove('A')
    return score

# Function to deal cards from the deck
def deal_cards(deck, num):
    dealt_cards = []
    for _ in range(num):
        card = random.choice(deck)
        dealt_cards.append(card)
        deck.remove(card)
    return dealt_cards

# Function to check if the player or dealer busts
def is_bust(score):
    return score > 21

# Main game function
def play_pontoon():
    # Define the deck of cards
    suits = ['♠', '♥', '♦', '♣']
    ranks = list(card_values.keys()) + ['A'] * 4  # Include four Aces for flexibility
    deck = [rank + suit for suit in suits for rank in ranks]
    
    # Initial deal to the player and dealer
    player_hand = deal_cards(deck, 2)
    dealer_hand = deal_cards(deck, 2)
    
    print("Player's hand:", player_hand)
    print("Dealer's showing card:", dealer_hand[0])
    
    # Player's turn
    while True:
        choice = input("Do you want to hit or stand? (h/s): ").strip().lower()
        if choice == 'h':
            player_hand.extend(deal_cards(deck, 1))
            print("Player hits:", player_hand)
        elif choice == 's':
            break
        
        # Check if the player busts
        if is_bust(calculate_score(player_hand)):
            print("Player busts! Dealer wins.")
            return
    
    # Dealer's turn (auto-complete for simplicity)
    while calculate_score(dealer_hand) < 17:
        dealer_hand.extend(deal_cards(deck, 1))
    
    print("Dealer's hand:", dealer_hand)
    
    # Determine the winner
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    
    if is_bust(dealer_score):
        print("Dealer busts! Player wins.")
    elif player_score > dealer_score:
        print("Player wins!")
    elif player_score < dealer_score:
        print("Dealer wins.")
    else:
        print("It's a tie.")

# Start the game
play_pontoon()

```
</div>

## Usage Instructions
1. The code snippets above are wrapped in markdown code blocks with copy buttons
2. You can copy any code block by clicking the "Copy" button
3. The complete implementation is available in the "Complete Code Summary" section
4. Make sure to follow any setup instructions provided in the response

## Metadata
- Model: deepseek-coder-v2
- Timestamp: 2025-02-07 21:22:11
- File: test_deepseek-coder-v2_20250207_212211.md
