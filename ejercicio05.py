# -*- coding:utf-8 -*-


def cambio_moneda(peso, dolar):
    """
>>> cambio_moneda(10, 17)
Total de 10 pesos = 170 dolar

"""
    total = peso * dolar
    print("Total de " + str(peso) + " pesos = " + str(total) + " dolar")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
