import random
import pyfiglet
from colorama import init, Fore

class TresEnRaya:
    def __init__(self) -> None:
        pass


    def tablero_partida(self,tablero):
        """
        Crea una representación visual del tablero de juego.

        Este método toma el estado actual del tablero y lo convierte en una 
        representación en forma de cadena, que se puede imprimir en la consola. 
        Se utiliza principalmente para mostrar el estado del juego en 
        juegos de mesa como el Tres en Raya.

        Args:
            tablero (list): Una lista que contiene los elementos del tablero, 
                            donde cada elemento representa una celda (por ejemplo, 
                            "X", "O" o un espacio vacío).

        Returns:
            str: Una cadena que representa el tablero en un formato legible, 
                con líneas y separaciones que indican las celdas del juego.
        """ 
        # Crear una representación en forma de cadena del tablero
        tablero_str = f" {tablero[0]} | {tablero[1]} | {tablero[2]} \n"
        tablero_str += "---+---+---\n"
        tablero_str += f" {tablero[3]} | {tablero[4]} | {tablero[5]} \n"
        tablero_str += "---+---+---\n"
        tablero_str += f" {tablero[6]} | {tablero[7]} | {tablero[8]} \n"
        return tablero_str

    def check_filas(self,tablero_actual):
        """
        Verifica si hay un ganador en las filas del tablero de Tres en Raya.

        Este método comprueba las filas del tablero actual para determinar si 
        algún jugador ha conseguido alinear tres de sus símbolos ("O" o "X") en 
        una fila. Devuelve un mensaje indicando el resultado de la verificación.

        Args:
            tablero_actual (list): Una lista que representa el estado actual 
                                del tablero, donde cada elemento es un 
                                símbolo del jugador ("O" o "X") o un espacio vacío.

        Returns:
            str: Un mensaje que indica si el jugador ha ganado, ha perdido 
                o si no hay ganador en las filas.
        """
        resultado_filas = ""
        if tablero_actual[0] == "O" and tablero_actual[1] == "O" and tablero_actual[2] == "O":
            resultado_filas = f"Has Ganado! Tres en raya en fila 1!"
        
        elif tablero_actual[0] == "X" and tablero_actual[1] == "X" and tablero_actual[2] == "X":
            resultado_filas =f"Has Perdido, Tres en raya en fila 1!"
    
        elif tablero_actual[3] == "O" and tablero_actual[4] == "O" and tablero_actual[5] == "O":
            resultado_filas = f"Has Ganado! Tres en raya en fila 2!"
        
        elif tablero_actual[3] == "X" and tablero_actual[4] == "X" and tablero_actual[5] == "X":
            resultado_filas =f"Has Perdido, Tres en raya en fila 2!"
        
        elif tablero_actual[6] == "O" and tablero_actual[7] == "O" and tablero_actual[8] == "O":
            resultado_filas = f"Has Ganado! Tres en raya en fila 3!"
        
        elif tablero_actual[6] == "X" and tablero_actual[7] == "X" and tablero_actual[8] == "X":
            resultado_filas = f"Has Perdido, Tres en raya en fila 3!"
        else:
            resultado_filas = f"No hay ganador en filas"
        
        return resultado_filas

    def check_columnas(self,tablero_actual):
        """
        Verifica si hay un ganador en las columnas del tablero de Tres en Raya.

        Este método comprueba las columnas del tablero actual para determinar si 
        algún jugador ha conseguido alinear tres de sus símbolos ("O" o "X") en 
        una columna. Devuelve un mensaje indicando el resultado de la verificación.

        Args:
            tablero_actual (list): Una lista que representa el estado actual 
                                del tablero, donde cada elemento es un 
                                símbolo del jugador ("O" o "X") o un espacio vacío.

        Returns:
            str: Un mensaje que indica si el jugador ha ganado, ha perdido 
                o si no hay ganador en las columnas.
        """
        resultado_filas = ""
        if tablero_actual[0] == "O" and tablero_actual[3] == "O" and tablero_actual[6] == "O":
            resultado_filas = f"Has Ganado! Tres en raya en columna 1!"
        
        elif tablero_actual[0] == "X" and tablero_actual[3] == "X" and tablero_actual[6] == "X":
            resultado_filas =f"Has Perdido, Tres en raya en columna 1!"
    
        elif tablero_actual[1] == "O" and tablero_actual[4] == "O" and tablero_actual[7] == "O":
            resultado_filas = f"Has Ganado! Tres en raya en columna 2!"
        
        elif tablero_actual[1] == "X" and tablero_actual[4] == "X" and tablero_actual[7] == "X":
            resultado_filas =f"Has Perdido, Tres en raya en columna 2!"
        
        elif tablero_actual[2] == "O" and tablero_actual[5] == "O" and tablero_actual[8] == "O":
            resultado_filas = f"Has Ganado! Tres en raya en columna 3!"
        
        elif tablero_actual[2] == "X" and tablero_actual[5] == "X" and tablero_actual[8] == "X":
            resultado_filas = f"Has Perdido, Tres en raya en columna 3!"
        else:
            resultado_filas = f"No hay ganador en columnas"
        
        return resultado_filas

    def check_diagonales(self,tablero_actual):
        """
        Verifica si hay un ganador en las diagonales del tablero de Tres en Raya.

        Este método comprueba las dos diagonales del tablero actual para 
        determinar si algún jugador ha conseguido alinear tres de sus 
        símbolos ("O" o "X") en una diagonal. Devuelve un mensaje indicando 
        el resultado de la verificación.

        Args:
            tablero_actual (list): Una lista que representa el estado actual 
                                del tablero, donde cada elemento es un 
                                símbolo del jugador ("O" o "X") o un espacio vacío.

        Returns:
            str: Un mensaje que indica si el jugador ha ganado, ha perdido 
                o si no hay ganador en las diagonales.
        """
        resultado_filas = ""
        if tablero_actual[0] == "O" and tablero_actual[4] == "O" and tablero_actual[8] == "O":
            resultado_filas = f"Has Ganado! Tres en raya en diagonal 1!"
        
        elif tablero_actual[0] == "X" and tablero_actual[4] == "X" and tablero_actual[8] == "X":
            resultado_filas =f"Has Perdido, Tres en raya en diagonal 1!"
    
        elif tablero_actual[2] == "O" and tablero_actual[4] == "O" and tablero_actual[6] == "O":
            resultado_filas = f"Has Ganado! Tres en raya en diagonal 2!"
        
        elif tablero_actual[2] == "X" and tablero_actual[4] == "X" and tablero_actual[6] == "X":
            resultado_filas =f"Has Perdido, Tres en raya en diagonal 2!"
        
        else:
            resultado_filas = f"No hay ganador en diagonal"
        
        return resultado_filas

    def partida(self):
        """
        Inicia una partida de Tres en Raya entre un jugador humano y una IA.

        Este método configura el tablero inicial y permite al jugador humano 
        introducir sus movimientos. Después de cada movimiento del jugador, 
        la IA realiza su propio movimiento aleatorio. La partida continúa 
        hasta que un jugador gane, se produzca un empate o el jugador 
        decida terminar la partida.

        El flujo de la partida incluye la visualización del tablero, 
        la validación de entradas del usuario y la verificación de condiciones 
        de victoria en filas, columnas y diagonales.

        Returns:
            None: Este método no devuelve un valor. En su lugar, imprime el 
                estado de la partida y los mensajes correspondientes en 
                función del resultado de la partida.
        """
        tablero_inicial = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        startable=self.tablero_partida(tablero_inicial)
        user_tries = 0
        n_elegidos_user = []
        n_elegidos_maquina = []
        print("")
        print(startable)
        try:
            while user_tries < 5: #son 4 de cada contrincante, si no es empate
                if user_tries == 4:
                    textostop = pyfiglet.figlet_format(f"EMPATE")
                    print(Fore.YELLOW + textostop + Fore.RESET)
                    print(Fore.MAGENTA + f"En esta ocasión no hay ganadores!"+Fore.RESET)
                    print("")
                    repetir = input(Fore.YELLOW + f"¿Quieres Jugar otra vez? Si / No: "+ Fore.RESET)
                    if repetir.lower() == "si":
                        self.partida()
                    else:
                        break
                
                print("")
                check = 0
                
                while check == 0:
                    try:
                        user_entrada = int(input("Introduce el número del tablero donde poner un O: "))
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
                new_tablero = self.tablero_partida(tablerotime) #Esto es para pintarlo
                print(Fore.YELLOW + f"Tu turno:"+Fore.RESET)
                print("")
                print(new_tablero)
                win_filas = self.check_filas(modif_tablero)
                win_columnas = self.check_columnas(modif_tablero)
                win_diagonal = self.check_diagonales(modif_tablero)
            
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
                            tablero_maquina = self.tablero_partida(tablero_maquina)
                            print(Fore.YELLOW + f"Turno de la IA:"+Fore.RESET)
                            print("")
                            print(tablero_maquina)
                            win_filas2 = self.check_filas(tablero_inicial)
                            win_columnas2 = self.check_columnas(tablero_inicial)
                            win_diagonal2 = self.check_diagonales(tablero_inicial)    
                            if win_filas2 == "No hay ganador en filas":
                                if win_columnas2 == "No hay ganador en columnas":
                                    if win_diagonal2 == "No hay ganador en diagonal":
                                        user_tries += 1
                                    else:
                                        textostop = pyfiglet.figlet_format(f"PIERDES")
                                        print(Fore.RED + textostop + Fore.RESET)
                                        print(tablero_maquina)
                                        print("")
                                        print(Fore.YELLOW + win_diagonal2)
                                        repetir = input(Fore.YELLOW + f"¿Quieres Jugar otra vez? Si / No: "+ Fore.RESET)
                                        print("")
                                        if repetir.lower() == "si":
                                            self.partida()
                                        else:
                                            print("Hasta Pronto!")
                                            print("Presiona Cualquier tecla para continuar")
                                            break 
                                        break                                  
                                else:
                                    textostop = pyfiglet.figlet_format(f"PIERDES")
                                    print(Fore.RED + textostop + Fore.RESET)
                                    print(tablero_maquina)
                                    print("")
                                    print(Fore.YELLOW + win_columnas2)
                                    repetir = input(Fore.YELLOW + f"¿Quieres Jugar otra vez? Si / No: "+ Fore.RESET)
                                    print("")
                                    if repetir.lower() == "si":
                                        self.partida()
                                    else:
                                        print("Hasta Pronto!")
                                        print("Presiona Cualquier tecla para continuar")
                                        break
                                    break
                            else:
                                textostop = pyfiglet.figlet_format(f"PIERDES")
                                print(Fore.RED + textostop + Fore.RESET)
                                print(tablero_maquina)
                                print("")
                                print(Fore.YELLOW + win_filas2)
                                print("")
                                repetir = input(Fore.YELLOW + f"¿Quieres Jugar otra vez? Si / No: "+ Fore.RESET)
                                
                                if repetir.lower() == "si":
                                    self.partida()
                                else:
                                    print("Hasta Pronto!")
                                    print("Presiona Cualquier tecla para continuar")
                                    break
                                break
                        else:
                            textostop = pyfiglet.figlet_format(f"GANAS")
                            print(Fore.GREEN + textostop + Fore.RESET)
                            print(new_tablero)
                            print("")
                            print(Fore.YELLOW + win_diagonal)
                            print("")
                            repetir = input(Fore.YELLOW + f"¿Quieres Jugar otra vez? Si / No: "+ Fore.RESET)
                            if repetir.lower() == "si":
                                self.partida()
                            else:
                                print("Hasta Pronto!")
                                print("Presiona Cualquier tecla para continuar")
                                break
                            break
                    else:
                        textostop = pyfiglet.figlet_format(f"GANAS")
                        print(Fore.GREEN + textostop + Fore.RESET)
                        print(new_tablero)
                        print("")                    
                        print(Fore.YELLOW + win_columnas)
                        print("")
                        repetir = input(Fore.YELLOW + f"¿Quieres Jugar otra vez? Si / No: "+ Fore.RESET)
                        if repetir.lower() == "si":
                            self.partida()
                        else:
                            print("Hasta Pronto!")
                            print("Presiona Cualquier tecla para continuar")
                            break
                        break
                else:
                    textostop = pyfiglet.figlet_format(f"GANAS")
                    print(Fore.GREEN + textostop + Fore.RESET)
                    print(new_tablero)
                    print("")
                    print(Fore.YELLOW + win_filas)
                    print("")
                    repetir = input(Fore.YELLOW + f"¿Quieres Jugar otra vez? Si / No: "+ Fore.RESET)
                    if repetir.lower() == "si":
                        self.partida()
                    else:
                        print("Hasta Pronto!")
                        print("Presiona Cualquier tecla para continuar")
                        break
                    break
                    
        except:
            print(f"Error Fatal")

    def iniciarTTT(self):
        """
        Inicia el juego de Tres en Raya.

        Este método imprime un mensaje de bienvenida y las instrucciones del juego 
        para el jugador. Se utiliza la biblioteca `pyfiglet` para mostrar el 
        título del juego en un formato artístico y se utilizan colores para 
        mejorar la experiencia visual.

        Después de mostrar las reglas del juego, el método espera que el jugador 
        pulse una tecla para comenzar la partida, llamando a la función `partida`.

        Returns:
            None: Este método no devuelve un valor. En su lugar, inicia la 
                partida de Tres en Raya.
        """
        textostop = pyfiglet.figlet_format(f"TRES EN RAYA")
        print(Fore.MAGENTA + textostop)
        print(Fore.YELLOW + f"Bienvenido al Tres en Raya!")
        print(Fore.RESET + f"Las reglas son sencillas:")
        print(f"1º Pon el número donde quieras colocarte")
        print(f"2º Haz tres en raya, ya sea en columna, fila o diagonal")
        input(Fore.YELLOW + f"Estás listo? pulsa cualquier tecla para empezar"+Fore.RESET)
        self.partida()
        return