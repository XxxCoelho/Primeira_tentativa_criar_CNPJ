from random import randint


def achar_digito(lista, digito):
    Lista_de_numeros = [int(valor) for valor in lista]
    lista_multiplicadores = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    if digito == 1:
        lista_multi = lista_multiplicadores[1:]
    elif digito == 2:
        lista_multi = lista_multiplicadores
    else:
        return None

    uniao = zip(Lista_de_numeros, lista_multi)
    total = sum([valor[0] * valor[1] for valor in uniao])

    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0
    return str(digito)


def verificador_repetidos(numeros):
    sequencia = numeros[0] * len(numeros)
    if sequencia == numeros:
        return True


def organizador(numeros):
    organizado = ''
    for indices, valor in enumerate(str(numeros)):
        if indices == 1 or indices == 4:
            organizado += valor
            organizado += '.'
        elif indices == 7:
            organizado += valor
            organizado += '/'
        elif indices == 11:
            organizado += valor
            organizado += '-'
        else:
            organizado += valor
    return organizado


def retirar_residuos(CNPJ):
    CNPJ = CNPJ.strip().replace('.', '').replace(',', '').replace('/', '').replace('-', '')
    return CNPJ


def separador_numeros(numeros):
    Lista_de_numeros = [int(valor) for valor in numeros]
    return Lista_de_numeros


def soma_digito(lista, digito):
    Lista_de_numeros = [int(valor) for valor in lista]
    lista_multiplicadores = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    if digito == 1:
        lista_multi = lista_multiplicadores[1:]
    elif digito == 2:
        lista_multi = lista_multiplicadores
    else:
        return None

    uniao = zip(Lista_de_numeros, lista_multi)
    total = sum([valor[0] * valor[1] for valor in uniao])
    return total


def gerador_CNPJ():
    CNPJ = str(randint(10000000, 99999999)) + '0001'
    return CNPJ
