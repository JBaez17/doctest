# -*- coding:utf-8 -*-


def porcentaje(hombre, mujeres):
    """
>>> porcentaje(10, 10)
hombres: 50.0
mujeres: 50.0

"""

    total = hombre + mujeres
    porcentaje_h = (hombre / total) * 100
    porcentaje_m = (mujeres / total) * 100
    print ("hombres: " + str(porcentaje_h))
    print ("mujeres: " + str(porcentaje_m))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
