import pandas as pd
import utilidades
import matplotlib.pyplot as plt
import numpy as np

opcion = 0
while opcion != 5:
    print("""Bienvenido.
    Indique a que sede pertenece:
    1. Sede 1
    2. Sede 2
    3. Sede 3
    4. Visualizar las ventas de las 3 sedes
    5. Salir del programa.
    """)
    opcion = int(input("seleccione una opcion:\n"))
    if opcion == 1:
        print("Ingrese el valor de las ventas\n")
        meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
        ventas_en_mes_sede1 = []
        gastos_en_mes_sede1 = []
        for mes in meses:
            validacion_numeros = False
            while validacion_numeros == False:
                ventas = input(f"ingresos del mes de {mes}:\n")
                validacion_numeros,mensaje = utilidades.validarNumeroEntero(ventas)
                if (mensaje != ""):
                    print(mensaje)
                ventas_en_mes_sede1.append(int(ventas))


        print("Ingrese el valor de los gastos:\n")
        for mes in meses:
            validacion_numeros = False
            while validacion_numeros == False:
                gastos = input(f"los gastos del mes de {mes}:\n")
                validacion_numeros, mensaje = utilidades.validarNumeroEntero(gastos)
                if (mensaje != ""):
                    print(mensaje)
                gastos_en_mes_sede1.append(int(gastos))
        datos1 = {
            "ventas": ventas_en_mes_sede1,
            "gastos": gastos_en_mes_sede1
        }
        dataFrame = pd.DataFrame(datos1)
        print(dataFrame)
        eje_x = meses
        serie1 = dataFrame["ventas"].values.tolist()
        serie2 = dataFrame["gastos"].values.tolist()
        lista_indices = np.arange(len(meses))
        ancho_columna = 0.35
        plt.bar(lista_indices, serie1,width=ancho_columna,label="ventas",color='green')
        plt.bar(lista_indices+ ancho_columna, serie2,width=ancho_columna,label="gastos",color="red")
        plt.legend(loc='best')
        plt.legend()
        plt.xticks(lista_indices, eje_x)
        plt.xlabel("ventas")
        plt.ylabel("gastos")
        plt.title("ventas y gastos")
        plt.show()

    if opcion == 2:
        print("Ingrese el valor de las ventas\n")
        meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre",
                 "noviembre", "diciembre"]
        ventas_en_mes_sede2 = []
        gastos_en_mes_sede2 = []
        for mes in meses:
            validacion_numeros = False
            while validacion_numeros == False:
                ventas = input(f"ingresos del mes de {mes}:\n")
                validacion_numeros, mensaje = utilidades.validarNumeroEntero(ventas)
                if (mensaje != ""):
                    print(mensaje)
                ventas_en_mes_sede2.append(int(ventas))

        for mes in meses:
            validacion_numeros = False
            while validacion_numeros == False:
                gastos = input(f"los gastos del mes de {mes}:\n")
                validacion_numeros, mensaje = utilidades.validarNumeroEntero(gastos)
                if (mensaje != ""):
                    print(mensaje)
                gastos_en_mes_sede2.append(int(gastos))
        datos2 = {"ventas": ventas_en_mes_sede2,
                  "gastos": gastos_en_mes_sede2}
        dataFrame = pd.DataFrame(datos2)
        print(dataFrame)
        eje_x = meses
        serie1 = dataFrame["ventas"].values.tolist()
        serie2 = dataFrame["gastos"].values.tolist()
        lista_indices = np.arange(len(meses))
        ancho_columna = 0.35
        plt.bar(lista_indices, serie1, width=ancho_columna, label="ventas", color='green')
        plt.bar(lista_indices + ancho_columna, serie2, width=ancho_columna, label="gastos", color="red")
        plt.legend(loc='best')
        plt.legend()
        plt.xticks(lista_indices, eje_x)
        plt.xlabel("ventas")
        plt.ylabel("gastos")
        plt.title("ventas y gastos")
        plt.show()

    if opcion == 3:
        print("Ingrese el valor de las ventas\n")
        meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre",
                 "noviembre", "diciembre"]
        ventas_en_mes_sede3 = []
        gastos_en_mes_sede3 = []
        for mes in meses:
            validacion_numeros = False
            while validacion_numeros == False:
                ventas = input(f"ingresos del mes de {mes}:\n")
                validacion_numeros, mensaje = utilidades.validarNumeroEntero(ventas)
                if (mensaje != ""):
                    print(mensaje)
                ventas_en_mes_sede3.append(int(ventas))

        for mes in meses:
            validacion_numeros = False
            while validacion_numeros == False:
                gastos = input(f"los gastos del mes de {mes}:\n")
                validacion_numeros, mensaje = utilidades.validarNumeroEntero(gastos)
                if (mensaje != ""):
                    print(mensaje)
                gastos_en_mes_sede3.append(int(gastos))
        datos3 = {
            "ventas": ventas_en_mes_sede3,
            "gastos": gastos_en_mes_sede3
        }
        dataFrame = pd.DataFrame(datos3)
        print(dataFrame)
        eje_x = meses
        serie1 = dataFrame["ventas"].values.tolist()
        serie2 = dataFrame["gastos"].values.tolist()
        lista_indices = np.arange(len(meses))
        ancho_columna = 0.35
        plt.bar(lista_indices, serie1, width=ancho_columna, label="ventas", color='green')
        plt.bar(lista_indices + ancho_columna, serie2, width=ancho_columna, label="gastos", color="red")
        plt.legend(loc='best')
        plt.legend()
        plt.xticks(lista_indices, eje_x)
        plt.xlabel("ventas")
        plt.ylabel("gastos")
        plt.title("ventas y gastos")
        plt.show()
    if opcion == 4:
        lista_ventas={
            "ventas":ventas_en_mes_sede1,
            "ventas":ventas_en_mes_sede2,
            "ventas":ventas_en_mes_sede3

        }
        dataFrame2 = pd.DataFrame(lista_ventas)
        eje_x = meses
        serie1 = dataFrame2["ventas"].values.tolist()
        plt.plot(eje_x,serie1,'g-',label="ventas")
        plt.xlabel("meses")
        plt.ylabel("ventas")
        plt.title("ventas de las sedes")
        plt.show()

    if opcion == 5:
        print("saliendo de la aplicacion")
    else:
        print("opcion no valida")