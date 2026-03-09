DOMINIOS_BLOQUEADOS = [
    ".io"
]


def dominio_permitido(dominio):

    for bloqueado in DOMINIOS_BLOQUEADOS:

        if dominio.endswith(bloqueado):
            return False

    return True