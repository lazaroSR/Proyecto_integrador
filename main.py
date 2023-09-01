print("Bienvenido, Ingresa tu nombre")
nombre_del_jugador = input()
print(f"Hola {nombre_del_jugador}, inicias un nuevo reto")

# parte numero 2 - proyecto integrador 

import keyboard as kb
print("Comienza un bucle infinito, detenlo presionando la flecha hacia arriba")
n = int(input("Ingresa un numero POSITIVO: "))

while n > 0:
  print("Ejecutando..." + str(n))
  n = n+1
  if kb.is_pressed("up"):
    break
print("FIN")

# parte numero 3 - proyecto integrador 

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


        
    #tecla = readchar.readkey()
    #if tecla:
        #break
#print("Presionaste la tecla: UP")









    
