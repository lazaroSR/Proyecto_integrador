# parte numero 3 - proyecto integrador 
"""
Iniciar con un número en 0, leer la tecla `n` del teclado en un bucle, 
por cada presionada, borrar la terminal e imprimir el nuevo número hasta el número 50.

La operación de borrar la terminal e imprimir el nuevo número debe estar en su propia función.
"""
import readchar
import os
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

n = 0
print("Presiona la tecla N para iniciar: ")
while n <= 50:
    tecla = readchar.readkey()
    if tecla == "n" or tecla == "N":
        clear()
        print(n)
        n = n + 1
        print("Presiona N para continuar")
print("FIN")