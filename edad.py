def edad_buena(valor):
    try:
        v = int(valor)
        if v < 1:
            return False
        return True

    except ValueError