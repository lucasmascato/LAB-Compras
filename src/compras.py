from datetime import datetime 
from typing import NamedTuple
import csv

Compra = NamedTuple('Compra',
                    [('dni', str),
                     ('supermercado', str),
                     ('provincia', str),
                     ('fecha_llegada', datetime),
                     ('fecha_salida', datetime),
                     ('total_compra', float)])

def parsea_fecha_hora(cadena:str)-> datetime:
    return datetime.strptime(cadena, '%d/%m/%Y %H:%M')

def lee_compras(ruta_fichero):
    compras = []
    with open(ruta_fichero, encoding="utf-8")as f:
        lector = csv.reader(f)
        next(lector)
        for linea in lector:
            dni = str(linea[0])
            supermercado = str(linea[1])
            provincia = str(linea[2])
            fecha_llegada = parsea_fecha_hora(linea[3])
            fecha_salida = parsea_fecha_hora(linea[4])
            total_compra = float(linea[5])
            compra_individual = Compra(dni, supermercado, provincia, fecha_llegada, fecha_salida, total_compra)
            compras.append(compra_individual)
    return compras

def compra_maxima_minima_provincia(list, provincia):
    gastos = []
    if provincia == None:
        for compra in list:
            if len(gastos) < 2:
                gastos.append(compra.total_compra)
            elif len(gastos) == 2:
                if compra.total_compra > gastos[0]:
                    gastos[0] = compra.total_compra
                elif compra.total_compra < gastos[1]:
                    gastos[1] = compra.total_compra
                else:
                    pass
    else:
        for compra in list:
            if compra.provincia == provincia:
                if len(gastos) < 2:
                    gastos.append(compra.total_compra)
                elif len(gastos) == 2:
                    if compra.total_compra > gastos[0]:
                        gastos[0] = compra.total_compra
                    elif compra.total_compra < gastos[1]:
                        gastos[1] = compra.total_compra
            else:
                pass
    return (f'Importe máximo de la provincia de {provincia}: {gastos[0]}. Importe mínimo: {gastos[1]}')

def num_compras_por_hora(compras:list[Compra])->dict[int, int]:
    horas_llegadas= {}
    for compra in compras:
        if compra.fecha_llegada.hour not in horas_llegadas:
            horas_llegadas[compra.fecha_llegada.hour] = 1
        else:
            horas_llegadas[compra.fecha_llegada.hour] += 1
    return horas_llegadas

def hora_menos_afluencia(list):
    horas_llegadas = num_compras_por_hora(list)
    hora_menor = min(horas_llegadas, key=horas_llegadas.get)
    return (f'La hora con menos afluencia es: {hora_menor} h. con {horas_llegadas[hora_menor]} llegadas de clientes')