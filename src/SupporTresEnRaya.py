import random
import pyfiglet
from colorama import init, Fore

def tablero_partida(tablero):
    # Crear una representación en forma de cadena del tablero
    tablero_str = f" {tablero[0]} | {tablero[1]} | {tablero[2]} \n"
    tablero_str += "---+---+---\n"
    tablero_str += f" {tablero[3]} | {tablero[4]} | {tablero[5]} \n"
    tablero_str += "---+---+---\n"
    tablero_str += f" {tablero[6]} | {tablero[7]} | {tablero[8]} \n"
    return tablero_str



def check_filas(tablero_actual):
    resultado_filas = ""
    if tablero_actual[0] == "O" and tablero_actual[1] == "O" and tablero_actual[2] == "O":
        resultado_filas = f"Has Ganado! Tres en ralla en fila 1!"
    
    elif tablero_actual[0] == "X" and tablero_actual[1] == "X" and tablero_actual[2] == "X":
        resultado_filas =f"Has Perdido, Tres en ralla en fila 1!"
   
    elif tablero_actual[3] == "O" and tablero_actual[4] == "O" and tablero_actual[5] == "O":
        resultado_filas = f"Has Ganado! Tres en ralla en fila 2!"
    
    elif tablero_actual[3] == "X" and tablero_actual[4] == "X" and tablero_actual[5] == "X":
        resultado_filas =f"Has Perdido, Tres en ralla en fila 2!"
    
    elif tablero_actual[6] == "O" and tablero_actual[7] == "O" and tablero_actual[8] == "O":
        resultado_filas = f"Has Ganado! Tres en ralla en fila 3!"
    
    elif tablero_actual[6] == "X" and tablero_actual[7] == "X" and tablero_actual[8] == "X":
        resultado_filas = f"Has Perdido, Tres en ralla en fila 3!"
    else:
        resultado_filas = f"No hay ganador en filas"
    
    return resultado_filas

def check_columnas(tablero_actual):
    resultado_filas = ""
    if tablero_actual[0] == "O" and tablero_actual[3] == "O" and tablero_actual[6] == "O":
        resultado_filas = f"Has Ganado! Tres en ralla en columna 1!"
    
    elif tablero_actual[0] == "X" and tablero_actual[3] == "X" and tablero_actual[6] == "X":
        resultado_filas =f"Has Perdido, Tres en ralla en columna 1!"
   
    elif tablero_actual[1] == "O" and tablero_actual[4] == "O" and tablero_actual[7] == "O":
        resultado_filas = f"Has Ganado! Tres en ralla en columna 2!"
    
    elif tablero_actual[1] == "X" and tablero_actual[4] == "X" and tablero_actual[7] == "X":
        resultado_filas =f"Has Perdido, Tres en ralla en columna 2!"
    
    elif tablero_actual[2] == "O" and tablero_actual[5] == "O" and tablero_actual[8] == "O":
        resultado_filas = f"Has Ganado! Tres en ralla en columna 3!"
    
    elif tablero_actual[2] == "X" and tablero_actual[5] == "X" and tablero_actual[8] == "X":
        resultado_filas = f"Has Perdido, Tres en ralla en columna 3!"
    else:
        resultado_filas = f"No hay ganador en columnas"
    
    return resultado_filas

def check_diagonales(tablero_actual):
    resultado_filas = ""
    if tablero_actual[0] == "O" and tablero_actual[4] == "O" and tablero_actual[8] == "O":
        resultado_filas = f"Has Ganado! Tres en ralla en diagonal 1!"
    
    elif tablero_actual[0] == "X" and tablero_actual[4] == "X" and tablero_actual[8] == "X":
        resultado_filas =f"Has Perdido, Tres en ralla en diagonal 1!"
   
    elif tablero_actual[2] == "O" and tablero_actual[4] == "O" and tablero_actual[6] == "O":
        resultado_filas = f"Has Ganado! Tres en ralla en diagonal 2!"
    
    elif tablero_actual[2] == "X" and tablero_actual[4] == "X" and tablero_actual[6] == "X":
        resultado_filas =f"Has Perdido, Tres en ralla en diagonal 2!"
    
    else:
        resultado_filas = f"No hay ganador en diagonal"
    
    return resultado_filas

def partida():
    tablero_inicial = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    startable=tablero_partida(tablero_inicial)
    user_tries = 0
    n_elegidos_user = []
    n_elegidos_maquina = []
    print(startable)
    try:
        while user_tries < 4: #son 4 de cada contrincante, si no es empate
            print("")
            check = 0
            while check == 0:
                try:
                    user_entrada = int(input("Introduce el número del tablero donde poner un O:"))
                    user_position = user_entrada - 1
                    if user_position < 0 or user_position > 8:
                        print(f"Introduce un valor de 1 a 9.")
                        check = 0
                    elif user_position in n_elegidos_maquina or user_position in n_elegidos_user:
                        print(f"Ya está escogido, pon otro.")
                        check = 0
                    else: 
                        n_elegidos_user.append(user_position)
                        check = 1
                except:
                    print(f"Valor inválido. Introduce Valores de 1 a 9")
            
            tablerotime = tablero_inicial
            tablerotime[user_position] = "O" #Esto es para almacenarlo en una lista
            modif_tablero = tablerotime #me guardo la lista modificada
            new_tablero = tablero_partida(tablerotime) #Esto es para pintarlo
            print(new_tablero)
            win_filas = check_filas(modif_tablero)
            win_columnas = check_columnas(modif_tablero)
            win_diagonal = check_diagonales(modif_tablero)
            
            if win_filas == "No hay ganador en filas":
                if win_columnas == "No hay ganador en columnas":
                    if win_diagonal == "No hay ganador en diagonal":
                        check = 0
                        while check == 0:
                            n_random = random.randrange(0,9,1)
                            if n_random in n_elegidos_user or n_random in n_elegidos_maquina:
                                check = 0
                            else:
                                n_elegidos_maquina.append(n_random)
                                check = 1
                        tablero_maquina = modif_tablero
                        tablero_maquina[n_random] = "X"
                        tablero_inicial = tablero_maquina #Guardo la lista modificada en inicial
                        tablero_maquina = tablero_partida(tablero_maquina)
                        print(tablero_maquina)
                        win_filas2 = check_filas(tablero_inicial)
                        win_columnas2 = check_columnas(tablero_inicial)
                        win_diagonal2 = check_diagonales(tablero_inicial)    
                        if win_filas2 == "No hay ganador en filas":
                            if win_columnas2 == "No hay ganador en columnas":
                                if win_diagonal2 == "No hay ganador en diagonal":
                                    user_tries += 1
                                else:
                                    print(win_filas2)
                                    break
                            else:
                                print(win_columnas2)
                                break
                        else:
                            print(win_diagonal2)
                            break
                    else:
                        print(win_diagonal)
                        break
                else:
                    print(win_columnas)
                    break
            else:
                print(win_filas)
                break
    except:
        print(f"EMPATE")


partida()
