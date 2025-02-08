# Model Response: artifish/llama3.2-uncensored
Generated on: 2025-02-08 10:39:01


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
python tic tac toe game

```
</div>

## Model Solution
**Tic Tac Toe Game in Python**
=====================================

This is a simple implementation of the classic Tic Tac Toe game in Python.

**Game Rules:**
- Two players, X and O, take turns marking a square.
- The first player to get three in a row (horizontally, vertically, or diagonally) wins the game.
- If all squares are filled and no player has won, the game is a draw.

**Code:**
<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
# Tic Tac Toe Game in Python

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    def print_board(self):
        row1 = '| {} | {} | {} |'.format(self.board[0], self.board[1], self.board[2])
        row2 = '| {} | {} | {} |'.format(self.board[3], self.board[4], self.board[5])
        row3 = '| {} | {} | {} |'.format(self.board[6], self.board[7], self.board[8])

        print()
        print(row1)
        print(row2)
        print(row3)
        print()

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_cells(self):
        return ' ' in self.board

    def num_empty_cells(self):
        return self.board.count(' ')


    def make_move(self, letter, pos):
        if self.board[pos] != '':
            print("You can't go there!")

        elif self.board[pos] == "X":
            print("Invalid move. You're playing as X.")

        else:
            self.board[pos] = letter

    def check_winner(self, let):
        win_condition = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for condition in win_condition:
            if self.board[condition[0]] == let and self.board[condition[1]] == let and self.board[condition[2]] == let:
                return True

    def restart(self):
        self.board = [' ' for _ in range(9)}


# Initialize the game
game = TicTacToe()
game.print_board()


# Game loop
while True:

    move = input("Please select a position to place an X (1-9): ")

    # Validate input
    try:
        num = int(move)
        if 1 <= num <= 9:
            if game.board[num - 1] != ' ':
                print('Position already occupied!')
            else:
                game.make_move('X', num - 1)
                game.print_board()
                if game.check_winner('X'):
                    print("X wins!")
                    break
        else:
            print("Invalid move. Please enter a number between 1 and 9.")

    except:

        print("Invalid input. Please try again.")

    # Check for draw
    if not game.empty_cells():
        print("It's a draw!")
        break


    # Switch player
    if game.check_winner('O'):

        game.print_board()
        print("O wins!")
        break

    move = input("Please select a position to place an O (1-9): ")

    try:
        num = int(move)
        if 1 <= num <= 9:
            if game.board[num - 1] != 'O':
                game.make_move('O', num - 1)
                game.print_board()
                if game.check_winner('O'):
                    print("O wins!")

                    break
            else:
                print('Position already occupied!')

        else:
            print("Invalid move. Please enter a number between 1 and 9.")

    except:

        print("Invalid input. Please try again.")

    # Check for draw
    if not game.empty_cells():
        game.print_board()
        print("It's a draw!")

        break

# Ask to restart the game
ask = input('Would you like to play again? (yes/no): ')

if ask.lower() == "yes":
    game.restart()
    game.print_board()
else:
    print('Thanks for playing!')
```
</div>

**How to Run:**
1. Save this code in a file named `tic_tac_toe.py`.
2. Open your terminal and navigate to the directory where you saved the file.
3. Type `python tic_tac_toe.py` to run the game.

**Gameplay Instructions:**
1. The game is played on a 3x3 grid, with positions numbered 1-9.
2. Player X makes the first move, followed by player O.
3. To make a move, type the number of the position where you'd like to place your mark (X or O).
4. If the position is already occupied, an error message will be displayed.
5. If all squares are filled and no player has won, the game ends in a draw.
6. The game continues until either player wins or it's a draw.

## Complete Code Summary
This section contains all the necessary code combined into a single, copyable block:

<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
# Complete implementation
# Generated by: artifish/llama3.2-uncensored
# Timestamp: 2025-02-08 10:39:01

# Tic Tac Toe Game in Python

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    def print_board(self):
        row1 = '| {} | {} | {} |'.format(self.board[0], self.board[1], self.board[2])
        row2 = '| {} | {} | {} |'.format(self.board[3], self.board[4], self.board[5])
        row3 = '| {} | {} | {} |'.format(self.board[6], self.board[7], self.board[8])

        print()
        print(row1)
        print(row2)
        print(row3)
        print()

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_cells(self):
        return ' ' in self.board

    def num_empty_cells(self):
        return self.board.count(' ')


    def make_move(self, letter, pos):
        if self.board[pos] != '':
            print("You can't go there!")

        elif self.board[pos] == "X":
            print("Invalid move. You're playing as X.")

        else:
            self.board[pos] = letter

    def check_winner(self, let):
        win_condition = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for condition in win_condition:
            if self.board[condition[0]] == let and self.board[condition[1]] == let and self.board[condition[2]] == let:
                return True

    def restart(self):
        self.board = [' ' for _ in range(9)}


# Initialize the game
game = TicTacToe()
game.print_board()


# Game loop
while True:

    move = input("Please select a position to place an X (1-9): ")

    # Validate input
    try:
        num = int(move)
        if 1 <= num <= 9:
            if game.board[num - 1] != ' ':
                print('Position already occupied!')
            else:
                game.make_move('X', num - 1)
                game.print_board()
                if game.check_winner('X'):
                    print("X wins!")
                    break
        else:
            print("Invalid move. Please enter a number between 1 and 9.")

    except:

        print("Invalid input. Please try again.")

    # Check for draw
    if not game.empty_cells():
        print("It's a draw!")
        break


    # Switch player
    if game.check_winner('O'):

        game.print_board()
        print("O wins!")
        break

    move = input("Please select a position to place an O (1-9): ")

    try:
        num = int(move)
        if 1 <= num <= 9:
            if game.board[num - 1] != 'O':
                game.make_move('O', num - 1)
                game.print_board()
                if game.check_winner('O'):
                    print("O wins!")

                    break
            else:
                print('Position already occupied!')

        else:
            print("Invalid move. Please enter a number between 1 and 9.")

    except:

        print("Invalid input. Please try again.")

    # Check for draw
    if not game.empty_cells():
        game.print_board()
        print("It's a draw!")

        break

# Ask to restart the game
ask = input('Would you like to play again? (yes/no): ')

if ask.lower() == "yes":
    game.restart()
    game.print_board()
else:
    print('Thanks for playing!')

```
</div>

## Usage Instructions
1. The code snippets above are wrapped in markdown code blocks with copy buttons
2. You can copy any code block by clicking the "Copy" button
3. The complete implementation is available in the "Complete Code Summary" section
4. Make sure to follow any setup instructions provided in the response

## Metadata
- Model: artifish/llama3.2-uncensored
- Timestamp: 2025-02-08 10:39:01
- File: test_artifish_llama3.2-uncensored_20250208_103901.md
