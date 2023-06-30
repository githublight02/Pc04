from pyfiglet import Figlet
import random
import math

figlet = Figlet()
fuentes_disponibles = figlet.getFonts()

num_columnas = 4  # Número de columnas para mostrar las fuentes
num_filas = math.ceil(len(fuentes_disponibles) / num_columnas)  # Cálculo del número de filas

print("Fuentes disponibles:")
for i in range(num_filas):
    fuentes_fila = fuentes_disponibles[i * num_columnas : (i + 1) * num_columnas]  # Obtener las fuentes de la fila actual
    print("  ".join(fuentes_fila))

while True:
    fuente_seleccionada = input("Ingrese el nombre de la fuente a utilizar (deje en blanco para seleccionar aleatoriamente): ")

    if not fuente_seleccionada:
        fuente_seleccionada = random.choice(fuentes_disponibles)
        print(f"Se seleccionó la fuente '{fuente_seleccionada}' aleatoriamente.")
    else:    
        if fuente_seleccionada not in fuentes_disponibles:
            print("La fuente ingresada no está disponible. Inténtelo de nuevo.")
            continue

    texto_imprimir = input("Ingrese el texto a imprimir: ")
    figlet.setFont(font=fuente_seleccionada)
    print(figlet.renderText(texto_imprimir))

    opcion = input("¿Desea imprimir otro texto? (s/n): ")
    if opcion.lower() != "s":
        break



