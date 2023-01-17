from CNPJ import modulos

cnpj_usuario = ''
cnpj_validando = ''
while True:
    if cnpj_usuario == '':
        cnpj_usuario = input('Informe seu CNPJ: ').strip().replace('.', '').replace('/', '').replace('-', '')
        if not cnpj_usuario.isnumeric():
            print('Digite apenas números!')
            continue
        if len(cnpj_usuario) > 14:
            print(f'Seu CNPJ: {cnpj_usuario} tem mais de 14 digitos!')
            continue
        if modulos.verificador_repetidos(cnpj_usuario):
            print(f'Seus numeros estão se repetindo {cnpj_usuario}')
            continue

    if cnpj_validando:
        cnpj_separada = modulos.separador_numeros(cnpj_validando)
        Soma = modulos.soma_digito(cnpj_separada, 2)
    else:
        cnpj_separada = modulos.separador_numeros(cnpj_usuario[:-2])
        Soma = modulos.soma_digito(cnpj_separada, 1)
        for valor in cnpj_separada:
            valor = str(valor)
            cnpj_validando += valor

    digito = 11 - (Soma % 11)
    digito = digito if digito <= 9 else 0

    cnpj_validando += str(digito)

    if len(cnpj_validando) == len(cnpj_usuario):
        if cnpj_validando == cnpj_usuario:
            print(f' Seu CNPJ: {modulos.organizador(cnpj_validando)} é valido!')
            break
        else:
            print(f'Seu CNPJ : {modulos.organizador(cnpj_usuario)} não é valido! ')
            print(f'CNPJ validado: {modulos.organizador(cnpj_validando)}')
            break
