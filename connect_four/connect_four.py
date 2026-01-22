
# «Connect Four» je hra pro dva hráče, v češtině někdy nazývaná Cestovní nebo
# Padající piškvorky. Každý hráč má žetony v jedné barvě; vyhrává ten, kdo jako
# první vytvoří nepřerušenou řadu «přesně čtyř» svých žetonů (horizontální,
# vertikální, diagonální). Hrací deska je přitom postavena vertikálně tak, že
# žetony padají směrem dolů, dokud nenarazí na jiný žeton nebo spodní rám
# desky. Hráč si tedy při svém tahu volí pouze sloupec, do nějž žeton hodí.
# (Na rozdíl od klasických piškvorek, kde si hráč volí přesné souřadnice
# a nic nikam nepadá.)
#
# Pro reprezentaci žetonů hráčů budeme v tomto úkolu používat znaky ‹X› a ‹O›.
# Hrací desku bude představovat seznam seznamů žetonů – vnitřní seznamy jsou
# postupně jednotlivé sloupce desky seřazené zdola nahoru. Tedy např. seznam
# ‹[['X'], [], ['O', 'X'], [], ['X', 'O', 'O'], [], []]›
# popisuje následující situaci:
#
#  ┌───┬───┬───┬───┬───┬───┬───┐
#  │   │   │   │   │ O │   │   │
#  ├───┼───┼───┼───┼───┼───┼───┤
#  │   │   │ X │   │ O │   │   │
#  ├───┼───┼───┼───┼───┼───┼───┤
#  │ X │   │ O │   │ X │   │   │
#  └───┴───┴───┴───┴───┴───┴───┘
#    0   1   2   3   4   5   6
#
# V naší reprezentaci přitom nemáme žádnou maximální výšku. Do sloupce
# s indexem 4 tedy je možno přidat další žeton a celá herní deska se tak
# nadstaví o další řádek.
#
# Nejprve implementujte proceduru ‹draw›, která zadanou herní desku ‹grid›
# textově vykreslí podobně jako výše, přičemž čáry kreslete pomocí znaků ‹+›
# (pro křížení a rohy), ‹-› (pro vodorovné čáry), ‹|› (pro svislé čáry).
# Znaky pro žetony jsou od svislých čar odděleny z každé strany jednou
# mezerou, čísla jsou zarovnána na střed sloupců, pravostranné mezery se
# ignorují. Smíte přitom předpokládat, že sloupců nebude více než 10.
# Vykreslete vždy jen tolik řádků herní desky, kolik je potřeba (tedy žádné
# zcela prázdné řádky).
#
# Výše uvedenou situaci tedy vykreslete takto:
#     +---+---+---+---+---+---+---+
#     |   |   |   |   | O |   |   |
#     +---+---+---+---+---+---+---+
#     |   |   | X |   | O |   |   |
#     +---+---+---+---+---+---+---+
#     | X |   | O |   | X |   |   |
#     +---+---+---+---+---+---+---+
#       0   1   2   3   4   5   6

def draw(grid):
    pass


# Dále pak implementujte proceduru ‹play›, která provede do zadané herní desky
# ‹grid› vhození žetonu hráče ‹player› do sloupce ‹column›. Předpokládejte
# přitom, že herní deska je ve stavu, kdy ještě nikdo nevyhrál, ‹player› je
# buďto ‹'X'› nebo ‹'O'› a ‹column› je validní index sloupce. Procedura vrátí
# ‹True›, pokud tímto tahem hráč vyhrál; ‹False› jinak.
#
# Pro jistotu připomínáme, že za výhru považujeme pouze situaci, kdy má některý
# z hráčů nepřerušenou řadu «přesně čtyř» svých žetonů. Pokud tedy vhozením
# žetonu vznikne nepřerušená řada více než čtyř žetonů, o výhru se nejedná.

def play(grid, player, column):
    pass


# V zadání máte připravenu jednoduchou implementaci celé hry v proceduře
# ‹run_game›. Tuto proceduru můžete (poté, co implementujete ‹draw› a ‹play›)
# použít k jednoduchému testování, zda vaše implementace fungují správně.
# Parametr ‹size› je počet sloupců herní desky.


def main():
    grid = [['X'], [], ['O', 'X'], [], ['X', 'O', 'O'], [], []]

    assert not play(grid, 'X', 3)
    assert grid == [['X'], [], ['O', 'X'], ['X'], ['X', 'O', 'O'], [], []]

    assert not play(grid, 'O', 3)
    assert grid == [['X'], [], ['O', 'X'], ['X', 'O'], ['X', 'O', 'O'], [], []]

    assert not play(grid, 'X', 5)
    assert grid \
        == [['X'], [], ['O', 'X'], ['X', 'O'], ['X', 'O', 'O'], ['X'], []]

    assert not play(grid, 'O', 5)
    assert grid \
        == [['X'], [], ['O', 'X'], ['X', 'O'], ['X', 'O', 'O'], ['X', 'O'], []]

    assert not play(grid, 'X', 5)
    assert grid \
        == [['X'], [], ['O', 'X'], ['X', 'O'],
            ['X', 'O', 'O'], ['X', 'O', 'X'], []]

    assert play(grid, 'O', 5)
    assert grid \
        == [['X'], [], ['O', 'X'], ['X', 'O'],
            ['X', 'O', 'O'], ['X', 'O', 'X', 'O'], []]


def run_game(size):
    player = 'O'
    grid = [[] for _ in range(size)]
    draw(grid)
    over = False
    while not over:
        player = 'X' if player == 'O' else 'O'
        column = int(input("\nPlayer " + player + ": "))
        print()
        over = play(grid, player, column)
        draw(grid)
    print("\nGame over, player", player, "won.")


if __name__ == '__main__':
    main()
    # run_game(7)  # uncomment to play the game
