# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 16:45:33 2021

@author: Toshiba
"""

print("|---------------------------Calculadora--------------------------|")
def suma(a,b):
    return f"Suma: {a + b}"

def resta(a,b):
    return f"Resta: {a - b}"

def multiplicacion(a,b):
    return f"Multiplicacion: {a * b}"

def division_entera(a,b):
    return f"Division Entera: {a // b}"

def division(a,b):
    return f"Division: {a / b}"

def potencia(a,b):
    return f"Potencia: {a ** b}"

def potencia_cubica(a,b):
    return f"Potencia Cubica: {(a+b)**3}"

def potencia_cero(a,b):
    return f"Todo numero elevado a la 0 da: {(a+b)**0}"

def raiz_cuadrada(a,b):
    return f"Raiz Cuadrada: {(a+b)**1/2}"

a = 3
b = 2
print(suma(a,b))
print(resta(a,b))
print(multiplicacion(a,b))
print(division_entera(a,b))
print(division(a,b))
print(potencia(a,b))
print(potencia_cubica(a,b))
print(potencia_cero(a,b))
print(raiz_cuadrada(a,b))
print("|------------------------Fin del calculo--------------------------|")