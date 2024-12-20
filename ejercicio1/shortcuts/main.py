def run(key1: str, key2: str, key3: str) -> str:
    # creamos una lista con las entradas
    lista = [key1, key2, key3]

    match lista:

        case ["CTRL", "ALT", "T"]:
            return "Open terminal"
        case ["CTRL", "ALT", "L"]:
            return "Lock screen"
        case ["CTRL", "ALT", "D"]:
            return "Show desktop"
        case ["ALT", "F2", ""]:
            return "Run console"
        case ["CTRL", "Q", ""]:
            return "Close window"
        case ["CTRL", "ALT", "DEL"]:
            return "Log out"
        case _:  # valor no encontrado
            return "Undefined"
    # para convervar la estructura de control de pypas asignamos undefined 
    # a su return
    action = "Undefined"
    return action


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
