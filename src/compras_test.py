from compras import *

if __name__ == '__main__':
    compras = lee_compras('data/compras.csv')
    compras_huelva = compra_maxima_minima_provincia(compras, None)
    print(compras_huelva)