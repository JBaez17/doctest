# -*- coding:utf-8 -*-


def total(precio):
    """
>>> total(100)
85.0

"""

    subtot = precio * .15
    total = precio - subtot
    print (total)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
