# coding: utf-8
import random

print(chr(27) + "[3;34m" + "##########################################################")
print(chr(27) + "[3;37m" + "#        🎲Bienvenido a El juego de dos o tres🎲        #")
print(chr(27) + "[3;34m" + "##########################################################")

############################  Primera Ronda  ############################
reglasvar = int(input(chr(27) + "[3;37m" + "\nPor favor, digite 1 para leer las reglas "
                                           "o digite 2 para comenzar el juego: "))

if reglasvar == 1:
    print(chr(27) + "[3;37m" + "Las reglas de la primera ronda son: "
        "\n1) El primer jugador lanza los 3 dados. Si los tres dados fueran iguales el jugador suma 6 puntos. "
        "\nPor ejemplo, si el jugador obtiene 5, 5 y 5, sumara 6 puntos."
        "\n2) Si el jugador tuviera dos dados iguales y uno distinto (por ejemplo 4 ,4 y 3), entonces el jugador vuelve a tirar, "
        "\npero unicamente el dado distinto (en este caso 3). "
        "\nSi al volver a lanzar ese dado logra que los tres dados sean iguales ( por ejemplo que se obtenga un 4 en el caso descripto), "
        "\nentonces sumar los 6 puntos en esa ronda. Si el dado relanzado sigue siendo distinto a los dos que eran iguales,"
        "\nel jugador sumara 3 puntos en esa ronda."
        "\n3) Si los tres dados fueran todos distintos, entonces obtiene 0 puntos y no puede volver a tirar ningún dado en esa ronda."
        "\npor ejemplo 1,3 y 4. ")
    input("\nPresiona enter para comenzar ")

############################  DESIGNACION DE JUGADORES  ############################
jug1 = input(chr(27) + "[1;31m" + "\nJugador 1 escriba su nombre: ")
jug2 = input(chr(27) + "[1;32m" + "Jugador 2 escriba su nombre: ")

############################ TIRAR LOS DADOS ############################
print(chr(27) + "[3;34m" + "\n##########################################################")
print(chr(27) + "[3;37m" + "#                     ·Primera ronda·                      #")
print(chr(27) + "[3;34m" + "############################################################")

############################ Primer jugador ############################
print(chr(27) + "[1;31m" + f"\n{jug1} presiona enter para tirar los dados")
input()
d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
d3 = random.randint(1, 6)

print(chr(27) + "[1;31m" + "Tus dados fueron: ", d1, ",", d2, ",", d3)
PtsJug1 = 0

if d1 == d2 == d3:
    print(chr(27) + "[1;31m" + "\nExcelente, sumaste 6 puntos al tener los 3 dados iguales")
    PtsJug1 = 6

elif d2 == d3:
    print(chr(27) + "[1;31m" + "\nObtuviste 2 dados iguales, vuele a tirar el primer dado")
    print(chr(27) + "[1;31m" + "Presiona Enter para voler a tirar el dado desigual")
    input()
    d1 = random.randint(1, 6)
    print(chr(27) + "[1;31m" + "su nuevo resultado del dado 1 es: ", d1)
    if d2 == d1:
        print(chr(27) + "[1;31m" + "Excelente, sumaste 6 puntos al tener los 3 dados iguales")
        PtsJug1 = 6
    else:
        print(chr(27) + "[1;31m" + f"\n{jug1} Ha salido un dado diferente a {d2}, sumas solo 3 puntos")
        PtsJug1 = 3
elif d2 == d1:
    print(chr(27) + "[1;31m" + "\nObtuviste 2 dados iguales, vuelve a tirar el tercer dado")
    print(chr(27) + "[1;31m" + "Presiona Enter para voler a tirar el dado desigual")
    input()
    d3 = random.randint(1, 6)
    print(chr(27) + "[1;31m" + "su nuevo resultado del dado 3 es: ", d3)
    if d2 == d3:
        print(chr(27) + "[1;31m" + "Excelente, sumaste 6 puntos al tener los 3 dados iguales")
        PtsJug1 = 6
    else:
        print(chr(27) + "[1;31m" + f"\n{jug1} Ha salido un dado diferente a {d2}, sumas solo 3 puntos")
        PtsJug1 = 3
elif d3 == d1:
    print(chr(27) + "[1;31m" + "\nObtuviste 2 dados iguales, vuelve a tirar el segundo dado")
    print(chr(27) + "[1;31m" + "Presiona Enter para voler a tirar el dado desigual")
    input()
    d2 = random.randint(1, 6)
    print(chr(27) + "[1;31m" + "su nuevo resultado del dado 2 es: ", d2)
    if d3 == d2:
        print(chr(27) + "[1;31m" + "Excelente, sumaste 6 puntos al tener los 3 dados iguales")
        PtsJug1 = 6
    else:
        print(chr(27) + "[1;31m" + f"\n{jug1} Ha salido un dado diferente a {d3}, sumas solo 3 puntos")
        PtsJug1 = 3

else:
    print(chr(27) + "[1;31m" + f"\nLo siento {jug1} has sacado 3 dados diferentes, no ganas puntos ")
    PtsJug1 = 0

print()
print(chr(27) + "[1;31m" + jug1, "tus puntos actuales son: ", PtsJug1)

print("\n------------------------------------------------------------")

############################ Le toca al segundo jugador ############################
print(chr(27) + "[1;32m" + f"\n{jug2} Presiona enter para tirar los dados")
input()

d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
d3 = random.randint(1, 6)

print(chr(27) + "[1;32m" + "Tus dados fueron: ", d1, ",", d2, ",", d3)
PtsJug2 = 0

if d1 == d2 == d3:
    print(chr(27) + "[1;32m" + "\nExcelente, sumaste 6 puntos al tener los 3 dados iguales")
    PtsJug2 = 6

elif d2 == d3:
    print(chr(27) + "[1;32m" + "\nObtuviste 2 dados iguales, vuelve a tirar el primer dado")
    print(chr(27) + "[1;32m" + "Presiona una tecla para voler a tirar el dado desigual")
    input()
    d1 = random.randint(1, 6)
    print(chr(27) + "[1;32m" + "su nuevo resultado del dado 1 es: ", d1)
    if d2 == d1:
        print(chr(27) + "[1;32m" + "Excelente, sumaste 6 puntos al tener los 3 dados iguales")
        PtsJug2 = 6
    else:
        print(chr(27) + "[1;32m" + f"\n{jug2} Ha salido un dado diferente a {d2}, sumas solo 3 puntos")
        PtsJug2 = 3
elif d2 == d1:
    print(chr(27) + "[1;32m" + "\nObtuviste 2 dados iguales, vuelve a tirar el tercer dado")
    print(chr(27) + "[1;32m" + "Presiona una tecla para volver a tirar: ")
    input()
    d3 = random.randint(1, 6)
    print(chr(27) + "[1;32m" + "su nuevo resultado del dado 3 es: ", d3)
    if d2 == d3:
        print(chr(27) + "[1;32m" + "Excelente, sumaste 6 puntos al tener los 3 dados iguales")
        PtsJug2 = 6
    else:
        print(chr(27) + "[1;32m" + f"\n{jug2} Ha salido un dado diferente a {d2}, sumas solo 3 puntos")
        PtsJug2 = 3
elif d3 == d1:
    print(chr(27) + "[1;32m" + "\nObtuviste 2 dados iguales, vuelve a tirar el segundo dado")
    d2 = random.randint(1, 6)
    print(chr(27) + "[1;32m" + "Presiona una tecla para volver a tirar: ")
    input()
    print(chr(27) + "[1;32m" + "su nuevo resultado del dado 2 es: ", d2)
    if d3 == d2:
        print(chr(27) + "[1;32m" + "Excelente, sumaste 6 puntos al tener los 3 dados iguales")
        PtsJug2 = 6
    else:
        print(chr(27) + "[1;32m" + f"\n{jug2} Ha salido un dado diferente a {d3}, sumas solo 3 puntos")
        PtsJug2 = 3

else:
    print(chr(27) + "[1;32m" + f"\nLo siento {jug2} has sacado 3 dados diferentes, no ganas puntos ")
print()
print(chr(27) + "[1;32m" + jug2, "tus puntos actuales son: ", PtsJug2)

print("\n------------------------------------------------------------")
############################ Segunda Ronda ############################
print('\nPresione enter para continuar a la Segunda Ronda')

reglasvar = int(input("\nPor favor, digite 1 para leer las reglas "
                      "o digite 2 para comenzar el juego: "))

if reglasvar == 1:
    print(chr(27) + "[3;37m" + "Continuemos con las reglas de la Segunda Ronda "
        "\n1) El primer jugador vuelve a lanzar los 3 dados, teniendo en cuenta que se apuesta todo "
        "\nel puntaje de la ronda anterior a par/impar. "
        "\n2) Si la suma de los tres dados en esta segunda jugada es de la paridad elegida, entonces suma "
        "\nel dado de mayor valor a su puntaje de la ronda anterior; "
        "\nen caso contrario, resta el dado de menor valor a su puntaje anterior. "
        "\n3) Si efectivamente la suma en la segunda jugada es de la paridad elegida, se duplica el puntaje total. "
        "\nSe repite la jugada para el segundo jugador con las mismas reglas que el primero."
        "\nAl finalizar el juego gana el que mas puntaje haya obtenido.")
    input("\nPresiona enter para comenzar ")

print(chr(27) + "[3;34m" + "##########################################################")
print(chr(27) + "[3;37m" + "#                    ·Segunda Ronda·                     #")
print(chr(27) + "[3;34m" + "##########################################################")

############################ Primer jugador ############################
print("\nA continuacion vamos a tirar 3 dados nuevamente y vamos a sumarlos")
print(chr(27) + "[1;31m" + jug1, "Apuesta por par o impar? \nNumero par: 2\nNumero impar: 1")
cond = int(input("\nIngrese una opcion: "))
print(chr(27) + "[1;31m" + jug1, "presiona enter para tirar los dados")
input()

d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
d3 = random.randint(1, 6)

print(chr(27) + "[1;31m" + "Tus dados fueron: ", d1, ",", d2, ",", d3)
tiro = d1 + d2 + d3

if cond == 2:
    if (d1 % 2) == 0 and (d2 % 2) == 0 and (d3 % 2) == 0:
        print(chr(27) + "[1;31m" + "Ganaste la apuesta! sacaste:", tiro, "es un numero par")
        PtsJug1 = (PtsJug1 + max(d1, d2, d3)) * 2
    elif (tiro % 2) == 0:
        print(chr(27) + "[1;31m" + "Ganaste la apuesta! sacaste:", tiro, "es un numero par")
        PtsJug1 = PtsJug1 + max(d1, d2, d3)
    else:
        PtsJug1 = PtsJug1 - min(d1, d2, d3)
        print(chr(27) + "[1;31m" + "Perdiste la apuesta sacaste:", tiro, "es un numero impar")
else:
    if (d1 % 2) == 1 and (d2 % 2) == 1 and (d3 % 2) == 1:
        print(chr(27) + "[1;31m" + "Ganaste la apuesta! sacaste:", tiro, "es un numero impar")
        PtsJug1 = (PtsJug1 + max(d1, d2, d3)) * 2
    elif (tiro % 2) == 1:
        print(chr(27) + "[1;31m" + "Ganaste la apuesta! sacaste:", tiro, "es un numero impar")
        PtsJug1 = PtsJug1 + max(d1, d2, d3)
    else:
        PtsJug1 = PtsJug1 - min(d1, d2, d3)
        print(chr(27) + "[1;31m" + "Perdiste la apuesta! sacaste:", tiro, "es un numero par")

print()
print(chr(27) + "[1;31m" + jug1, "tus puntos actuales son: ", PtsJug1)

print("\n----------------------------------------------------")

############################ Le toca al segundo jugador ############################
print(chr(27) + "[1;32m" + f"\n{jug2} presione Enter para continuar:")
input()
print(chr(27) + "[1;32m" + jug2, "Apuesta por par o impar? :\nNumero par: 2\nNumero impar: 1")
cond = int(input(chr(27) + "[1;32m" + "\nIngrese una opcion: "))
print(chr(27) + "[1;32m" + jug2, "presiona enter para tirar los dados")
input()

d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
d3 = random.randint(1, 6)

print(chr(27) + "[1;32m" + "Tus dados fueron: ", d1, ",", d2, ",", d3)
tiro = d1 + d2 + d3

if cond == 2:
    if (d1 % 2) == 0 and (d2 % 2) == 0 and (d3 % 2) == 0:
        print(chr(27) + "[1;32m" + "Ganaste la apuesta! sacaste:", tiro, "salio un numero par")
        PtsJug2 = (PtsJug2 + max(d1, d2, d3)) * 2
    elif (tiro % 2) == 0:
        print(chr(27) + "[1;32m" + "Ganaste la apuesta! sacaste:", tiro, "Ganaste la apuesta!, salio un numero par")
        PtsJug2 = PtsJug2 + max(d1, d2, d3)
    else:
        PtsJug2 = PtsJug2 - min(d1, d2, d3)
        print(chr(27) + "[1;32m" + "Perdiste la apuesta sacaste:", tiro, "es un numero impar")
else:
    if (d1 % 2) == 1 and (d2 % 2) == 1 and (d3 % 2) == 1:
        print(chr(27) + "[1;32m" + "Ganaste la apuesta!", tiro, "salio un numero impar")
        PtsJug2 = (PtsJug2 + max(d1, d2, d3)) * 2
    elif (tiro % 2) == 1:
        print(chr(27) + "[1;32m" + "Ganaste la apuesta!", tiro, "salio un numero impar")
        PtsJug2 = PtsJug2 + max(d1, d2, d3)
    else:
        PtsJug2 = PtsJug2 - min(d1, d2, d3)
        print(chr(27) + "[1;32m" + "Perdiste la apuesta! sacaste:", tiro, "es un numero par")

print()
print(chr(27) + "[1;32m" + jug2, "tus puntos actuales son: ", PtsJug2)

############################ Resultados ############################
print(chr(27) + "[1;32m" + '\nPresione enter para confirmar los resultados')
input()

if PtsJug1 > PtsJug2:
    ganador = "Ganaste", jug1
elif PtsJug1 == PtsJug2:
    ganador = "Empataron"
else:
    ganador = "Ganaste", jug2

print(chr(27) + "[1;35m" + "###########################################################")
print(chr(27) + "[1;35m" + "                      Felicidades                          ")
print(chr(27) + "[1;35m" + "###########################################################")
print("\n----------------------------------------------------------")
print(chr(27) + "[1;31m" + f"\n{jug1} termino con:", PtsJug1)
print(chr(27) + "[1;32m" + jug2, "termino con:", PtsJug2)
input("\033" + "[1;35m" +"\nPresione enter para finalizar el juego")
print("\033" + "[1;35m" + " gracias por jugar ")
