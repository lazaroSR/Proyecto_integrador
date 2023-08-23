print("Bienvenido, Ingresa tu nombre")
nombre_del_jugador = input()
print(f"Hola {nombre_del_jugador}, inicias un nuevo reto")

# parte numero 2 - proyecto integrador 
import keyboard as kb

n = int(input("Ingresa un numero: "))
print("Comienza un bucle infinito, detenlo presionando la flecha hacia arriba")

while n > 0:
  print("Ejecutando..." + str(n))
  n = n+1
  if kb.is_pressed("up"):
    break
print("FIN")










    
