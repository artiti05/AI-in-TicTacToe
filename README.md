# Tic-Tac-Toe with AI

This project is a simple implementation of the Tic-Tac-Toe game using Python and the Pygame library. It features a user interface for playing the game, where you can either play against another player or against an AI. The AI uses the Minimax algorithm to make decisions.

## Features

- **Two-player mode**: Play Tic-Tac-Toe with another player on the same machine.
- **Single-player mode**: Play against an AI powered by the Minimax algorithm.
- **Graphical User Interface (GUI)**: Built using Pygame to render the board, moves, and game status.

## Files

### `runner.py`

This is the main script that runs the game. It initializes the Pygame window and handles user input for choosing player type (X or O), interacting with the game board, and displaying the game state (e.g., whose turn it is, whether the game is over, etc.). The script also manages the logic for player and AI moves.

#### Key Features of `runner.py`:
- Initializes a 3x3 Tic-Tac-Toe grid and renders it.
- Allows the user to choose to play as 'X' or 'O'.
- Handles the game loop, user inputs, and displays game messages.
- Handles the AI's move if playing against the computer.
- Allows restarting the game after it ends.

### `tictactoe.py`

This file contains the core logic for the Tic-Tac-Toe game. It defines the game state, checks for win conditions, and uses the Minimax algorithm to calculate the best moves for the AI.

#### Key Functions in `tictactoe.py`:
- `initial_state()`: Initializes an empty Tic-Tac-Toe board.
- `player(board)`: Determines whose turn it is based on the current board state.
- `actions(board)`: Returns a set of available actions (empty spaces) on the board.
- `result(board, action)`: Returns a new board state after a player makes a move.
- `winner(board)`: Checks if there is a winner (either 'X' or 'O') based on the current board state.
- `terminal(board)`: Checks if the game is over (either due to a win or a tie).
- `utility(board)`: Returns the utility of a board state: `1` for 'X' win, `-1` for 'O' win, and `0` for a tie.
- `minimax(board)`: Implements the Minimax algorithm for the AI to determine the best move.
- `max_value(board)`: Recursively calculates the best move for the 'X' player.
- `min_value(board)`: Recursively calculates the best move for the 'O' player.

## Requirements

- Python 3.x
- Pygame (You can install it via `pip install pygame`)

## Running the Game

To run the game, simply execute the `runner.py` script:

```bash
python runner.py
