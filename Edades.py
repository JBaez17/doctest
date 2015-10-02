# -*- coding:utf-8 -*-


def edades(edad):
    """
    >>> edades(-1)
    No existes

    >>> edades(12)
    Eres un niño

    >>> edades(17)
    Eres adolescente

    >>> edades(64)
    Eres adulto

    >>> edades(119)
    Adulto mayor

    >>> edades(123)
    Eres Mumm-Ra

    """
    if edad < 0:
        print ("No existes")
    elif edad <= 13:
        print ("Eres un niño")
    elif edad <= 18:
        print ("Eres adolescente")
    elif edad <= 65:
        print ("Eres adulto")
    elif edad <= 120:
        print ("Adulto mayor")
    else:
        print ("Eres Mumm-Ra")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
