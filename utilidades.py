import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def validarNumeroEntero(numero):
    if not numero.isnumeric():
        return (False, "El valor debe ser un número entero")
    elif int(numero) < 0 :
        return (False, "El valor debe ser un número positivo")
    else:
        return (True, "")

