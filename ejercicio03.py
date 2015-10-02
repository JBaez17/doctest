# -*- coding:utf-8 -*-


def calificacion(cali1, cali2, cali3):
    """
>>> calificacion(10,10,10)
10.0

"""

    suma = cali1 + cali2 + cali3
    promedio = suma / 3
    print(promedio)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
