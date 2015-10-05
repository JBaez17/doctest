# -*- coding:utf-8 -*-


def sueldo_commision(sueldo_base, v1, v2, v3):
    """
    >>> sueldo_commision(100, 11, 12, 11)
    3.4000000000000004
    103.4

    """

    comision_1 = v1 + v2 + v3
    subtotal = comision_1 * .10
    total = subtotal + sueldo_base
    print (subtotal)
    print (total)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
