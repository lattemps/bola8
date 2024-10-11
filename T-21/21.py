from random import randint as random

def is_as (card: int) -> int:
    """
    Dada una carta verifica si es as, si lo es pregunta
    por el valor deseado
    (int) -> int
    """
    if card != 1: return card
    _as = -1
    while _as != 1 and _as != 10:
        _as = int(input("Usted ha obtenido un as, escoga un valor (1/10): "))
    return _as

def give_card () -> int:
    """
    Da cartas
    () -> int
    """
    return is_as(random(1, 11))

def ask_4_eating () -> int:
    """
    Pregunta si quiere seguir comiendo, dado el caso que si, reparte
    una carta, sino devuleve cero
    () -> int
    """
    eat = ''
    while eat != 's' and eat != 'n':
        eat = input("Quiere comer? (s/n): ")

    if eat == 's':
        return give_card()
    return 0

def game_for_1 () -> None:
    c1 = give_card()
    c2 = give_card()
    print(f"card 1: {c1}")
    print(f"card 2: {c2}")

    pts = c1 + c2

    while pts < 21:
        print(f"puntaje: {pts}")
        new = ask_4_eating()
        if new == 0: break;
        pts += new

    print(f"Puntaje final: {pts}")
    if pts == 21:
        print("Usted gana, felicidades!")

def game_for_2 () -> None:
    players = [0, 0]
    for i in range(2):
        a = give_card()
        b = give_card()
        print(f"cartas jugador {i + 1}: {a} {b}")
        players[i] = a + b

    nthp = 0
    while players[0] < 21 and players[1] < 21:
        print(f"jugador 1: {players[0]}")
        print(f"jugador 2: {players[1]}\n")

        print(f"Para jugador {nthp + 1}...")
        new = ask_4_eating()
        print()

        if new == 0: continue
        players[nthp] += new
        nthp = 1 - nthp

    print(f"Puntaje final jugador 1: {players[0]}")
    print(f"Puntaje final Pugador 2: {players[1]}")

    if players[0] == 21:
        print("jugador 2 gana!")
    elif players[1] == 21:
        print("jugador 1 gana!")
    elif players[1] == players[0] and players[0] == 21:
        print("ambos ganan!")

def ask_to_play_again () -> bool:
    print("* ----------------------------------------------------------- *")
    ans = ""
    while ans != 's' and ans != 'n':
        ans = input("\nSeguir jugando? (s/n): ").lower()

    if ans == 's':
        print("\n\n")
        return True
    return False

def main ():
    nplayers = int(input("Cuantos jugadores? (1/2): "))
    keeplaying = True
    while keeplaying:
        if nplayers == 1: game_for_1()
        else: game_for_2()
        keeplaying = ask_to_play_again()

main()
