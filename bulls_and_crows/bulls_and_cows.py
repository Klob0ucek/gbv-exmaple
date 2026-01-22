# «Bulls and Cows» (v češtině někdy «Býci a krávy») je logická hra pro jednoho
# hráče, která spočívá v hádání tajného čtyřmístného čísla. Všechny cifry
# tajného čísla jsou různé.
#
# Po každém pokusu o uhádnutí hráč obdrží dvě informace:
# - Počet «býků» (bulls): Kolik číslic je na správné pozici
# - Počet «krav» (cows): Kolik číslic je správných, ale na špatné pozici
#
# Například: Pokud je tajné číslo ‹1234› a hráč hádá ‹1325›, odpověď je
# 2 býci (cifry 1 a 2 jsou na správných pozicích) a 1 kráva (cifra 3 je
# přítomna, ale na špatné pozici).
#
# Hra končí, když hráč uhádne správně všechny cifry na správných pozicích
# (tedy získá 4 býky).


# Implementujte funkci ‹generate_secret›, která vygeneruje náhodné tajné
# čtyřmístné číslo jako řetězec. Všechny cifry musí být různé a číslo nesmí
# začínat nulou.
#
# Hint: Použijte modul ‹random› a jeho funkci ‹random.sample›.

def generate_secret():
    pass


# Implementujte funkci ‹evaluate_guess›, která pro zadané tajné číslo ‹secret›
# a hráčův pokus ‹guess› (oba jsou řetězce) vrátí tuple ‹(bulls, cows)›, kde:
# - ‹bulls› je počet číslic na správných pozicích
# - ‹cows› je počet číslic, které jsou v tajném čísle, ale na špatných pozicích
#
# Předpokládejte, že oba parametry jsou validní čtyřciferné řetězce s různými
# ciframi.

def evaluate_guess(secret, guess):
    pass


# Implementujte funkci ‹is_valid_guess›, která zkontroluje, zda je hráčův
# pokus ‹guess› validní. Validní pokus musí splňovat:
# - Je to řetězec délky přesně 4
# - Obsahuje pouze cifry (0-9)
# - Všechny cifry jsou různé
#
# Funkce vrátí ‹True›, pokud je pokus validní, jinak ‹False›.

def is_valid_guess(guess):
    pass


# Implementujte proceduru ‹play_game›, která řídí průběh jedné hry.
# Procedura:
# 1. Vygeneruje tajné číslo pomocí ‹generate_secret›
# 2. Opakovaně žádá hráče o pokus, dokud neuhádne správně
# 3. Po každém pokusu vypíše počet býků a krav
# 4. Pokud pokus není validní, vypíše chybovou hlášku a žádá nový pokus
# 5. Na konci vypíše počet pokusů, které hráč potřeboval
#
# Pro testování můžete také přijmout volitelný parametr ‹secret›, který
# umožní nastavit konkrétní tajné číslo místo generování náhodného.

def play_game(secret=None):
    pass


def main():
    # Test evaluate_guess
    assert evaluate_guess('1234', '1234') == (4, 0)  # All correct
    assert evaluate_guess('1234', '1243') == (2, 2)  # 1,2 correct pos, 3,4 wrong pos
    assert evaluate_guess('1234', '5678') == (0, 0)  # Nothing correct
    assert evaluate_guess('1234', '4321') == (0, 4)  # All wrong positions
    assert evaluate_guess('1234', '1567') == (1, 0)  # Only 1 correct
    assert evaluate_guess('1234', '2345') == (1, 2)  # 3,4 correct pos, 2 wrong pos
    assert evaluate_guess('5678', '5819') == (1, 1)  # 5 correct pos, 8 wrong pos
    
    # Test is_valid_guess
    assert is_valid_guess('1234')
    assert is_valid_guess('5678')
    assert is_valid_guess('0123')
    assert not is_valid_guess('123')     # Too short
    assert not is_valid_guess('12345')   # Too long
    assert not is_valid_guess('1123')    # Duplicate digits
    assert not is_valid_guess('12a4')    # Contains non-digit
    assert not is_valid_guess('')        # Empty string
    assert not is_valid_guess('1111')    # All same digits
    
    # Test generate_secret
    for _ in range(10):
        secret = generate_secret()
        assert len(secret) == 4
        assert secret[0] != '0'  # Doesn't start with 0
        assert len(set(secret)) == 4  # All digits are unique
        assert all(c.isdigit() for c in secret)  # All are digits
    
    print("All tests passed!")


if __name__ == '__main__':
    main()
    # play_game()  # uncomment to play the game
