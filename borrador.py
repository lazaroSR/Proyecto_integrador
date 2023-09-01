# parte numero 3 - proyecto integrador 
"""

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

#segunda forma de solucion
import os
import readchar
def clear_terminal():
    os.system('cls' if os.name=='nt' else 'clear')
print("para iniciar preciona la tecla n")
def main():
    numero = 0
    while numero <= 50:
        k = readchar.readkey()
        if k == "n" or k == "N":
            clear_terminal()
            print(numero)
            print("Presiona la tecla N para continuar... ")
            numero += 1
if __name__ == "__main__":
    main()