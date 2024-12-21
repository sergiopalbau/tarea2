def run(player1: str, player2: str) -> int:
    p1 = player1.lower()
    p2 = player2.lower()

    # caso que ambos tenga el mismo elemento
    if p1 == p2:
        return 0
    # distintos casos de juego
    if p1 == "rock" and p2 != "paper":
        return 1
    elif p1 == "paper" and p2 != "scissors":
        return 1
    elif p1 == "scissors" and p2 != "rock":
        return 1

    # en este juego si no gana p1 y no hay empate significa que 
    # gano el jugador 2.
    return 2

# DO NOT TOUCH THE CODE BELOW


if __name__ == '__main__':
    import vendor

    vendor.launch(run)
