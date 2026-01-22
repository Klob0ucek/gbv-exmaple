# «Tic-Tac-Toe» neboli «Piškvorky» je klasická hra pro dva hráče na hrací
# desce 3×3. Hráči střídavě umisťují své symboly (‹X› nebo ‹O›) na volná pole.
# Vyhrává hráč, který jako první vytvoří nepřerušenou řadu tří svých symbolů
# v horizontálním, vertikálním nebo diagonálním směru.
#
# Hrací desku budeme reprezentovat jako seznam tří řádků, přičemž každý řádek
# je seznam tří políček. Prázdné políčko je reprezentováno prázdným řetězcem
# ‹''›, obsazená políčka obsahují ‹'X'› nebo ‹'O'›.
#
# Například následující deska:
#
#   X | O | X
#  -----------
#     | X | O
#  -----------
#   O |   |
#
# bude reprezentována jako:
# ‹[['X', 'O', 'X'], ['', 'X', 'O'], ['O', '', '']]›


# Implementujte proceduru ‹draw›, která zadanou herní desku ‹board› textově
# vykreslí podobně jako výše. Použijte znaky ‹|› pro svislé čáry a ‹-› pro
# vodorovné čáry. Symboly hráčů jsou od svislých čar odděleny z každé strany
# jednou mezerou. Prázdná políčka vykreslete jako mezeru.
#
# Výše uvedenou situaci tedy vykreslete takto:
#   X | O | X
#  -----------
#     | X | O
#  -----------
#   O |   |

def draw(board):
    pass


# Implementujte funkci ‹check_winner›, která pro zadanou herní desku ‹board›
# vrátí symbol vítěze (‹'X'› nebo ‹'O'›), pokud některý hráč vyhrál.
# Pokud nikdo nevyhrál, vrátí prázdný řetězec ‹''›.
#
# Hráč vyhrává, pokud má nepřerušenou řadu tří svých symbolů horizontálně,
# vertikálně, nebo diagonálně.

def check_winner(board):
    pass


# Implementujte proceduru ‹play›, která provede tah hráče ‹player› (‹'X'› nebo
# ‹'O'›) na pozici zadanou souřadnicemi ‹row› (řádek) a ‹col› (sloupec).
# Indexy jsou číslovány od 0.
#
# Funkce vrátí ‹True›, pokud byl tah úspěšně proveden (políčko bylo prázdné),
# jinak vrátí ‹False› (políčko už bylo obsazené).
#
# Předpokládejte, že ‹row› a ‹col› jsou validní indexy (0, 1, nebo 2).

def play(board, player, row, col):
    pass


# Implementujte funkci ‹is_full›, která vrátí ‹True›, pokud jsou všechna
# políčka herní desky obsazená, jinak vrátí ‹False›.

def is_full(board):
    pass


# V zadání máte připravenu jednoduchou implementaci celé hry v proceduře
# ‹run_game›. Tuto proceduru můžete (poté, co implementujete všechny funkce)
# použít k jednoduchému testování.


def main():
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    
    assert play(board, 'X', 0, 0)
    assert board == [['X', '', ''], ['', '', ''], ['', '', '']]
    assert check_winner(board) == ''
    assert not is_full(board)
    
    assert play(board, 'O', 1, 1)
    assert board == [['X', '', ''], ['', 'O', ''], ['', '', '']]
    assert check_winner(board) == ''
    
    assert play(board, 'X', 0, 1)
    assert board == [['X', 'X', ''], ['', 'O', ''], ['', '', '']]
    
    assert play(board, 'O', 2, 0)
    assert board == [['X', 'X', ''], ['', 'O', ''], ['O', '', '']]
    
    assert play(board, 'X', 0, 2)
    assert board == [['X', 'X', 'X'], ['', 'O', ''], ['O', '', '']]
    assert check_winner(board) == 'X'  # X wins horizontally
    
    # Test vertical win
    board2 = [['X', 'O', ''], ['X', 'O', ''], ['', '', '']]
    assert play(board2, 'X', 2, 0)
    assert check_winner(board2) == 'X'  # X wins vertically
    
    # Test diagonal win
    board3 = [['O', 'X', ''], ['X', 'O', ''], ['', '', '']]
    assert play(board3, 'O', 2, 2)
    assert check_winner(board3) == 'O'  # O wins diagonally
    
    # Test occupied position
    board4 = [['X', '', ''], ['', '', ''], ['', '', '']]
    assert not play(board4, 'O', 0, 0)  # Position already occupied
    assert board4 == [['X', '', ''], ['', '', ''], ['', '', '']]
    
    # Test full board
    board5 = [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']]
    assert is_full(board5)
    assert check_winner(board5) == ''  # No winner, draw


def run_game():
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    player = 'O'
    draw(board)
    
    while check_winner(board) == '' and not is_full(board):
        player = 'X' if player == 'O' else 'O'
        print(f"\nPlayer {player}'s turn")
        row = int(input("Row (0-2): "))
        col = int(input("Column (0-2): "))
        print()
        
        if play(board, player, row, col):
            draw(board)
        else:
            print("Position already occupied! Try again.")
            player = 'O' if player == 'X' else 'X'  # Switch back
    
    winner = check_winner(board)
    if winner:
        print(f"\nGame over! Player {winner} won.")
    else:
        print("\nGame over! It's a draw.")


if __name__ == '__main__':
    main()
    # run_game()  # uncomment to play the game
