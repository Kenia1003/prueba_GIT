import pytest
# from src.math_operations 
def suma(valor1: int, valor2: int):
    if valor1 < 0 or valor2 < 0:
        return "error"
    return valor1 + valor2

valor1 = int(input("Introduce el primer número: "))
valor2 = int(input("Introduce el segundo número: "))

print(suma(valor1, valor2))

    