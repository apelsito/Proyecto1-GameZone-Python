import random
import pyfiglet
from colorama import init, Fore
class Ahorcado:
    def __init__(self) -> None:
        
        self.palabras_ahorcado = ["python", "programacion", "ahorcado", "desarrollador", "computadora", "tecnologia", "algoritmo", "inteligencia", "variables", "funcion", "recursividad", "bucle", "depuracion", "ciberseguridad", "internet", "criptografia", "servidor", "cliente", "software", "hardware", "pythonista", "matriz", "inteligencia", "desempeño"]
        self.estados = [
        """
           -----
           |   |
               |
               |
               |
               |
        _______|___
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        _______|___
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        _______|___
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        _______|___
        """,
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        _______|___
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        _______|___
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        _______|___
        """
    ]


    def obtener_lista_entradas(self,entrada, n_veces_encontrada):
        """
        Genera una lista que contiene la entrada repetida un número específico de veces.

        Args:
        entrada (any): El valor que se desea repetir en la lista.
        n_veces_encontrada (int): El número de veces que se desea que la entrada aparezca en la lista.

        Returns:
        list: Una lista que contiene la entrada repetida `n_veces_encontrada` veces.
        """
        obtencion = [entrada] * n_veces_encontrada
        return obtencion

    def reemplazar_texto(self,texto_og, lista_encontradas, posiciones):
        """
        Reemplaza partes de un texto original en posiciones específicas con elementos de una lista dada.

        Args:
            texto_og (str): El texto original que será modificado.
            lista_encontradas (list): Lista de valores que reemplazarán las partes del texto original.
            posiciones (list): Lista de posiciones (índices) en las que se realizarán los reemplazos en el texto.

        Returns:
            str: El texto modificado con las entradas de `lista_encontradas` en las posiciones especificadas.
        """
        texto_lista = list(texto_og)  # Convertimos el string en una lista para manipularlo
        for i, pos in enumerate(posiciones):
            texto_lista[pos * 2] = lista_encontradas[i]  # Al tener los guiones con espacio, hay que tener en cuenta el doble
        return "".join(texto_lista)
        
    def ahorcado(self):
        """
        Inicia un juego interactivo del clásico "Ahorcado", donde el jugador debe adivinar una palabra letra por letra.

        El juego selecciona una palabra al azar de la lista `self.palabras_ahorcado`. El jugador tiene un número limitado 
        de intentos para adivinar la palabra antes de que se pierda. El juego se puede detener en cualquier momento escribiendo "stop". 
        Si el jugador adivina todas las letras correctamente antes de agotar los intentos, gana. 
        En caso de perder, se le muestra la palabra correcta y se le ofrece la opción de jugar otra vez.

        Args:
            None

        Returns:
            None: Este método no devuelve ningún valor, pero imprime el progreso y el estado del juego, y permite al jugador interactuar 
            mediante la consola.
        """

        textogame = pyfiglet.figlet_format(f"GAME ON!")
        print(Fore.CYAN + textogame + Fore.RESET)
        print("")
        n_random = random.randrange(0, len(self.palabras_ahorcado))
        palabra_elegida = self.palabras_ahorcado[n_random]
        longitud_palabra_elegida = len(palabra_elegida)

        texto = "_ " * longitud_palabra_elegida #con esto lo imprimimos tantas veces como haga falta
        errores = 0
        aciertos = 0
        letras_acertadas = []
        letras_erroneas = []
        print(Fore.YELLOW + f"La palabra tiene {longitud_palabra_elegida} letras."+Fore.RESET)

        while errores < len(self.estados) - 1:
            print(self.estados[errores])
            print(texto + "\n")
            print(Fore.RED + f"Letras erróneas: {letras_erroneas}")
            print(f"Errores restantes: {5-errores}")
            entrada = input(Fore.YELLOW + "Escribe una letra: "+Fore.RESET)
            entrada = entrada.lower()
            if entrada.lower() == "stop":
                textostop = pyfiglet.figlet_format(f"STOP")
                print(Fore.RED + textostop)
                print(Fore.YELLOW + f"Has escrito stop, el juego se ha detenido, hasta pronto!")
                print("")
                input(Fore.RESET + f"Pulsa cualquier tecla para salir")
                break
            if entrada in palabra_elegida and entrada not in letras_acertadas:
                pos_encontradas = [i for i, letra in enumerate(palabra_elegida) if letra == entrada]
                letras_acertadas.append(entrada)
                veces_encontrada = len(pos_encontradas)
                lista_entrada = self.obtener_lista_entradas(entrada, veces_encontrada)
                texto = self.reemplazar_texto(texto, lista_entrada, pos_encontradas)
                aciertos += veces_encontrada
                print(Fore.GREEN + f"Correcto! '{entrada}' está en las posiciones: {pos_encontradas}"+Fore.RESET)
            elif entrada in palabra_elegida and entrada in letras_acertadas:
                print(Fore.YELLOW + f"Correcto!, pero ya la habías puesto."+Fore.RESET)

            else:
                print(Fore.RED + f"Incorrecto! '{entrada}' no está en la palabra."+Fore.RESET)
                letras_erroneas.append(entrada)
                errores += 1

            if aciertos == longitud_palabra_elegida:
                textowin = pyfiglet.figlet_format(f"GANAS")
                print(Fore.GREEN + textowin)
                print(Fore.MAGENTA + f"¡Felicidades! Has adivinado la palabra: {palabra_elegida}"+Fore.RESET)
                print("")
                repetir = input(Fore.YELLOW + f"Quieres jugar otra vez? Si / No: "+Fore.RESET)
                print(Fore.RESET)
                if repetir.lower() == "si":
                    self.ahorcado()
                    errores = 0
                    aciertos = 0
                else:
                    print(Fore.MAGENTA + f"Hasta Pronto!")
                    print(Fore.YELLOW + f"Pulsa cualquier tecla para salir."+Fore.RESET)
                    break
        else:
            textowin = pyfiglet.figlet_format(f"PIERDES")
            print(Fore.RED + textowin)
            print(Fore.YELLOW + f"¡Perdiste! La palabra era: {palabra_elegida}"+Fore.RESET)
            print("")
            repetir = input(Fore.YELLOW + f"Quieres jugar otra vez? Si / No: "+Fore.RESET)
            if repetir.lower() == "si":
                self.ahorcado()
                errores = 0
                aciertos = 0
            else:
                print(Fore.MAGENTA + f"Hasta Pronto!")
                print(Fore.YELLOW + f"Pulsa cualquier tecla para salir."+Fore.RESET)

    def menu(self):
        """
        Muestra el menú principal e introduce al jugador a las reglas del juego del Ahorcado. 

        Explica brevemente las reglas del juego, incluyendo cómo adivinar letras, el número de intentos permitidos, y 
        cómo salir del juego escribiendo "stop". Al final, permite al jugador comenzar el juego presionando una tecla.

        Args:
            None

        Returns:
            None: Este método no devuelve ningún valor, solo imprime el menú y llama al método `ahorcado` para iniciar el juego.
        """
        textostop = pyfiglet.figlet_format(f"AHORCADO")
        print(Fore.MAGENTA + textostop)
        print(Fore.YELLOW + f"Bienvenido al Ahorcado!")
        print(Fore.RESET + f"Las reglas son sencillas:")
        print(f"1º Se te dirá la longitud de la palabra a adivinar")
        print(f"Deberás escribir una letra, si está bien se añadirá")
        print(f"Si no está bien, empezaremos a ahorcar a Timmy :/")
        print(f"Tienes 5 intentos antes de que Timmy se duerma.")
        print(f"Si pones varias letras o la palabra completa, te diremos si está bien o mal")
        print(f"Si te aburres escribe 'stop' y listo")
        input(Fore.YELLOW + f"Estás listo? pulsa cualquier tecla para empezar"+Fore.RESET)
        self.ahorcado()
        return