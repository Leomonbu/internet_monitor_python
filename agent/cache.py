import time

CACHE_TIEMPO = 30  # segundos

dominios_cache = {}


def dominio_reciente(dominio):

    ahora = time.time()

    if dominio in dominios_cache:

        ultimo = dominios_cache[dominio]

        if ahora - ultimo < CACHE_TIEMPO:
            return True

    dominios_cache[dominio] = ahora

    return False