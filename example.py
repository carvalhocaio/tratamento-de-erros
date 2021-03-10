def dividir(dividendo, divisor):
    if not (isinstance(dividendo, int) and isinstance(divisor, int)):
        raise ValueError('dividir() deve receber apenas argumentos inteiros')

    try:
        aux = dividendo / divisor
    except:
        print(f'Não foi possível dividir {dividendo} por {divisor}')
        raise
    return aux


def testa_divisao(divisor):
    resultado = dividir(10, divisor)
    print(f'O resultado da divisão de 10 por {divisor} é {resultado}')

# try:
#     testa_divisao(2.5)
# except ZeroDivisionError as e:
#     print('Erro de divisão por zero')
# # except Exception as e:
# #     print('tratamento genérico')

# print('Programa encerrado')


try:
    print('o fluxo está aqui')
    raise ValueError
except Exception:
    print('Agora ele foi pra cá')
print('E enfim ele continua...')
