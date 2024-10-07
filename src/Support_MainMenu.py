import pyfiglet
from colorama import init, Fore
import time
import os
import threading
from src.Support_Preguntados import Preguntados
from src.Support_PiedraPapelTijeraLagartoSpock import PiedraPapelTijeraLagartoSpock
from src.Support_Ahorcado import Ahorcado
from src.SupportTresEnRaya import TresEnRaya

class MenuPrincipal: 
    def __init__(self) -> None:
        self.hola = 0
        self.animacion_activa = True
        self.input_detectado = False
        self.frames = [
            Fore.MAGENTA + r'''
    O       O      ██████   █████  ███    ███ ███████     ███████  ██████  ███    ██ ███████      O       O
   /|\     /|\    ██       ██   ██ ████  ████ ██             ███  ██    ██ ████   ██ ██          /|\     /|\
   / \     / \    ██   ███ ███████ ██ ████ ██ █████         ███   ██    ██ ██ ██  ██ █████       / \     / \
                  ██    ██ ██   ██ ██  ██  ██ ██           ███    ██    ██ ██  ██ ██ ██         - - -   - - -
                   ██████  ██   ██ ██      ██ ███████     ███████  ██████  ██   ████ ███████
            ''',
            Fore.GREEN + r'''
    O       O      ██████   █████  ███    ███ ███████     ███████  ██████  ███    ██ ███████      O       O
   /|\     /|\    ██       ██   ██ ████  ████ ██             ███  ██    ██ ████   ██ ██          /|\     /|\
   //      //     ██   ███ ███████ ██ ████ ██ █████         ███   ██    ██ ██ ██  ██ █████       //      //
                  ██    ██ ██   ██ ██  ██  ██ ██           ███    ██    ██ ██  ██ ██ ██        - - -   - - -
                   ██████  ██   ██ ██      ██ ███████     ███████  ██████  ██   ████ ███████ 
            ''',
          Fore.YELLOW + r'''
    O       O      ██████   █████  ███    ███ ███████     ███████  ██████  ███    ██ ███████      O       O
   /|\     /|\    ██       ██   ██ ████  ████ ██             ███  ██    ██ ████   ██ ██          /|\     /|\
    \\      \\    ██   ███ ███████ ██ ████ ██ █████         ███   ██    ██ ██ ██  ██ █████        \\      \\
                  ██    ██ ██   ██ ██  ██  ██ ██           ███    ██    ██ ██  ██ ██ ██         - - -   - - -
                   ██████  ██   ██ ██      ██ ███████     ███████  ██████  ██   ████ ███████  
            ''',
            Fore.RED + r'''
    O       O      ██████   █████  ███    ███ ███████     ███████  ██████  ███    ██ ███████      O       O
   /|\     /|\    ██       ██   ██ ████  ████ ██             ███  ██    ██ ████   ██ ██          /|\     /|\
   / \     / \    ██   ███ ███████ ██ ████ ██ █████         ███   ██    ██ ██ ██  ██ █████       / \     / \
                  ██    ██ ██   ██ ██  ██  ██ ██           ███    ██    ██ ██  ██ ██ ██          - - -   - - -
                   ██████  ██   ██ ██      ██ ███████     ███████  ██████  ██   ████ ███████  
            ''',
           Fore.GREEN + r'''
    O       O      ██████   █████  ███    ███ ███████     ███████  ██████  ███    ██ ███████      O       O
   \|/     \|/    ██       ██   ██ ████  ████ ██             ███  ██    ██ ████   ██ ██          \|/     \|/
    \\      \\    ██   ███ ███████ ██ ████ ██ █████         ███   ██    ██ ██ ██  ██ █████        \\      \\
                  ██    ██ ██   ██ ██  ██  ██ ██           ███    ██    ██ ██  ██ ██ ██         - - -   - - -
                   ██████  ██   ██ ██      ██ ███████     ███████  ██████  ██   ████ ███████  
            ''',
            Fore.MAGENTA + r'''
    O       O      ██████   █████  ███    ███ ███████     ███████  ██████  ███    ██ ███████      O       O
   \|/     \|/    ██       ██   ██ ████  ████ ██             ███  ██    ██ ████   ██ ██          \|/     \|/
   //      //     ██   ███ ███████ ██ ████ ██ █████         ███   ██    ██ ██ ██  ██ █████       //      //
                  ██    ██ ██   ██ ██  ██  ██ ██           ███    ██    ██ ██  ██ ██ ██        - - -   - - -
                   ██████  ██   ██ ██      ██ ███████     ███████  ██████  ██   ████ ███████  
            ''',
            Fore.BLUE + r'''
    O       O      ██████   █████  ███    ███ ███████     ███████  ██████  ███    ██ ███████      O       O
   \|/     \|/    ██       ██   ██ ████  ████ ██             ███  ██    ██ ████   ██ ██          \|/     \|/
   / \     / \    ██   ███ ███████ ██ ████ ██ █████         ███   ██    ██ ██ ██  ██ █████       / \     / \
                  ██    ██ ██   ██ ██  ██  ██ ██           ███    ██    ██ ██  ██ ██ ██         - - -   - - -
                   ██████  ██   ██ ██      ██ ███████     ███████  ██████  ██   ████ ███████  
            '''
        ]

    def limpiar_pantalla(self):
        """
        Limpia la pantalla de la consola, compatible con sistemas Windows y Unix.

        En sistemas Windows, utiliza el comando `cls`, y en sistemas Unix (Linux/macOS), utiliza el comando `clear`.
        Esto asegura que la pantalla de la consola quede vacía para mostrar nueva información.

        Args:
            None

        Returns:
            None: Este método no devuelve ningún valor, solo ejecuta un comando del sistema para limpiar la pantalla.
        """
        # Limpiar la pantalla (compatible con Windows y Unix)
        os.system('cls' if os.name == 'nt' else 'clear')

    def reproducir_animacion(self):
        """
        Reproduce una animación en bucle mientras `animacion_activa` es verdadero.

        La animación consiste en mostrar una serie de frames uno tras otro, limpiando la pantalla entre cada frame para 
        crear un efecto visual. Durante la animación, también se muestra un mensaje de bienvenida al jugador. La animación 
        se detiene si `animacion_activa` se establece en falso.

        Args:
            None

        Returns:
            None: Este método no devuelve ningún valor, solo ejecuta un bucle que muestra la animación en la consola.
        """
        while self.animacion_activa:
            for frame in self.frames:
                if not self.animacion_activa:
                    break  # Salir del bucle si se desactiva la animación
                self.limpiar_pantalla()
                print(frame)
                # Mostrar el texto del menú
                print(Fore.YELLOW + "Bienvenido a la" + Fore.MAGENTA + " GAME" + Fore.CYAN + " ZONE" + Fore.YELLOW + " Pulsa Enter para comenzar.")
                time.sleep(0.35)  # Controla la velocidad de la animación

    def esperar_input(self):
        """
        Espera a que el usuario pulse Enter y detiene la animación en curso.

        Este método se utiliza para pausar la ejecución hasta que el usuario realiza una entrada. 
        Al detectar la pulsación de Enter, se establece el atributo `input_detectado` en verdadero y se 
        llama al método `detener_animacion()` para parar cualquier animación que esté activa.

        Args:
            None

        Returns:
            None: Este método no devuelve ningún valor, solo espera la entrada del usuario y 
            realiza acciones en consecuencia.
        """
        input("")  # Espera la pulsación de Enter
        self.input_detectado = True
        self.detener_animacion()  # Detiene la animación cuando el usuario pulsa Enter

    def detener_animacion(self):
        """
        Detiene la animación activa.

        Este método establece el atributo `animacion_activa` en falso, lo que provoca que cualquier animación en curso se detenga 
        inmediatamente. Esto puede ser utilizado para interrumpir una animación en respuesta a eventos de entrada del usuario o 
        en otras circunstancias que requieran la finalización de la animación.

        Args:
            None

        Returns:
            None: Este método no devuelve ningún valor; su única función es modificar el estado de `animacion_activa`.
        """
        # Detener la animación
        self.animacion_activa = False

    def main_menu(self):
        """
        Muestra el menú principal y gestiona la animación y la entrada del usuario en hilos separados.

        Este método inicia un hilo para reproducir una animación en segundo plano mientras espera a que el 
        usuario presione Enter. Cuando el usuario presiona Enter, se detiene la animación y se llama al método `jugar()` 
        para comenzar el juego. 

        Args:
            None

        Returns:
            None: Este método no devuelve ningún valor; su función es coordinar la animación y la entrada del usuario 
        en el menú principal.
        """
        # Inicia la animación en un hilo separado
        animacion_thread = threading.Thread(target=self.reproducir_animacion, daemon=True)
        animacion_thread.start()

        # Iniciar otro hilo para esperar la entrada del usuario
        input_thread = threading.Thread(target=self.esperar_input)
        input_thread.start()

        # Esperar a que el usuario pulse Enter (detendrá la animación)
        input_thread.join()

        # Una vez que se presiona Enter, pasa a jugar
        self.jugar()

        return

    
    def jugar(self):
        """
        Muestra el menú de juegos disponibles y permite al usuario seleccionar uno para jugar.

        Este método limpia la pantalla y presenta una lista de juegos disponibles para que el usuario elija. 
        El usuario puede ingresar un número para seleccionar un juego o escribir "salir" para salir del programa. 
        Basado en la selección, se inicializa el juego correspondiente, y al finalizar, se regresa al menú principal.

        Los juegos disponibles son:
            1. El Ahorcado
            2. Tres en Raya
            3. Piedra, Papel, Tijera, Lagarto, Spock
            4. Preguntados
            5. Visualizar un mensaje especial

        Args:
            None

        Returns:
            None: Este método no devuelve ningún valor; su función principal es gestionar el flujo de selección 
            de juegos y la ejecución de los mismos.
        """
        self.limpiar_pantalla()
        titulo = pyfiglet.figlet_format("GAME ZONE", font="slant")
        print(Fore.MAGENTA + titulo)
        print("")
        print(Fore.RESET + "1º El Ahorcado.")
        print("2º Tres en Raya.")
        print("3º Piedra, Papel, Tijera, Lagarto, Spock")
        print("4º Preguntados")
        print("Escribe salir para Salir.")
        print(Fore.MAGENTA + "Introduce el número del juego que quieres jugar" + Fore.RESET)
        
        # Esperar al usuario para comenzar el juego
        check = 0
        while check == 0:
            entra = input()  # El programa espera la entrada del usuario aquí
            if entra.lower() == "salir":
                check = 1
                break
            try:
                entra = int(entra)
                check = 1
            except:
                print(f"Introduce un número, entre 1 y 4.")
                check = 0
            
            if entra == 1:
                print(Fore.MAGENTA + f"Has elegido: " + Fore.YELLOW + "El Ahorcado" + Fore.RESET)
                input(f"Presiona cualquier tecla para ejecutar el juego: ")
                self.limpiar_pantalla()
                jugar = Ahorcado().menu()
                jugar
                self.main_menu()            
            elif entra == 2:
                print(Fore.MAGENTA + f"Has elegido: " + Fore.YELLOW + "Tres en Raya" + Fore.RESET)
                input(f"Presiona cualquier tecla para ejecutar el juego: ")
                jugar = TresEnRaya().iniciarTTT()
                jugar
                self.main_menu()            
            elif entra == 3:
                print(Fore.MAGENTA + f"Has elegido: " + Fore.YELLOW + "Piedra, Papel, Tijera, Lagarto, Spock." + Fore.RESET)
                input(f"Presiona cualquier tecla para ejecutar el juego: ")
                jugar = PiedraPapelTijeraLagartoSpock().batalla()
                jugar
                self.main_menu()            
            elif entra == 4:
                print(Fore.MAGENTA + f"Has elegido: " + Fore.YELLOW + "Preguntados" + Fore.RESET)
                input(f"Presiona cualquier tecla para ejecutar el juego: ")
                jugar = Preguntados().preguntar()
                jugar
                self.main_menu()       

                #Se me olvido la lógica del menú donde si no pone salir, pero no es un número de 1 al 4, vuelva a preguntar el input         

        return