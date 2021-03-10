def dividir(dividendo, divisor):
    return dividendo / divisor


def testa_divisao(divisor):
    resultado = dividir(10, divisor)
    print(f'O resultado da divisão de 10 por {divisor} é {resultado}')

try:
    testa_divisao(0)
except ZeroDivisionError as e:
    print(f'Não é possível realizar a divisão por zero: {e}')