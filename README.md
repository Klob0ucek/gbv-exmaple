# GBV Example - Python Games for Students

Repository for students of GBV to test their Git skills and practice Python programming through simple game implementations.

## 📖 About

This repository contains three classic games designed as programming exercises for students. Each game is provided with:
- Detailed Czech documentation explaining the game rules
- Function stubs to implement
- Test cases to verify correctness
- A playable version once implementation is complete

## 🎮 Games

### Connect Four (Piškvorky Padající)
**Location:** [`connect_four/connect_four.py`](connect_four/connect_four.py)

Connect Four is a two-player game where players take turns dropping tokens into columns of a vertical board. The tokens fall down until they hit the bottom or another token. The goal is to create a line of exactly four tokens (horizontally, vertically, or diagonally).

**Tasks to implement:**
- `draw()` - Display the game board
- `play()` - Drop a token and check for winner

### Tic-Tac-Toe (Piškvorky)
**Location:** [`tic_tac_toe/tic_tac_toe.py`](tic_tac_toe/tic_tac_toe.py)

Classic 3×3 grid game where two players take turns placing X's and O's. The first player to get three symbols in a row (horizontally, vertically, or diagonally) wins.

**Tasks to implement:**
- `draw()` - Display the board
- `check_winner()` - Detect if someone won
- `play()` - Make a move
- `is_full()` - Check if board is full

### Bulls and Cows (Býci a Krávy)
**Location:** [`bulls_and_cows/bulls_and_cows.py`](bulls_and_cows/bulls_and_cows.py)

A logic puzzle game where players try to guess a secret 4-digit number with unique digits. After each guess, the game reveals:
- **Bulls**: Digits in the correct position
- **Cows**: Correct digits in wrong positions

**Tasks to implement:**
- `generate_secret()` - Create random 4-digit number
- `evaluate_guess()` - Calculate bulls and cows
- `is_valid_guess()` - Validate user input
- `play_game()` - Game loop

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher

### Running the Games

1. Clone this repository:
```bash
git clone https://github.com/yourusername/gbv-exmaple.git
cd gbv-exmaple
```

2. Navigate to any game directory:
```bash
cd connect_four
```

3. Run the tests:
```bash
python connect_four.py
```

4. Once implemented, uncomment the `run_game()` line to play:
```bash
python connect_four.py
```

## 🎯 Learning Objectives

Through these exercises, students will practice:
- List and matrix manipulation in Python
- Control flow and conditional logic
- Function design and implementation
- Input validation
- Game state management
- Testing and debugging

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍🏫 Author

Jan Poláček

## 🤝 Contributing

This repository is primarily for educational purposes. Students are encouraged to:
- Clone the repository
- Implement the games
- Experiment with additional features
- Share improvements via pull requests

---

**Note:** Keep an eye on commit history - there might be hidden surprises! 👀
