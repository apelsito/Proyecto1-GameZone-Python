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
        obtencion = [entrada] * n_veces_encontrada
        return obtencion

    def reemplazar_texto(self,texto_og, lista_encontradas, posiciones):
        texto_lista = list(texto_og)  # Convertimos el string en una lista para manipularlo
        for i, pos in enumerate(posiciones):
            texto_lista[pos * 2] = lista_encontradas[i]  # Al tener los guiones con espacio, hay que tener en cuenta el doble
        return "".join(texto_lista)


    def menu_bienvenida(self):
        textostop = pyfiglet.figlet_format(f"AHORCADO")
        print(Fore.MAGENTA + textostop)
        return
        
    def ahorcado(self):
        n_random = random.randrange(0, len(self.palabras_ahorcado))
        palabra_elegida = self.palabras_ahorcado[n_random]
        longitud_palabra_elegida = len(palabra_elegida)

        texto = "_ " * longitud_palabra_elegida #con esto lo imprimimos tantas veces como haga falta
        errores = 0
        aciertos = 0
        letras_acertadas = []
        letras_erroneas = []
        print(Fore.YELLOW + f"La palabra tiene {longitud_palabra_elegida} letras.")

        while errores < len(self.estados) - 1:
            print(self.estados[errores])
            print(texto + "\n")
            print(Fore.RED + f"Letras erróneas: {letras_erroneas}")
            print(f"Errores restantes: {5-errores}")
            entrada = input(Fore.YELLOW + "Escribe una letra: ").lower()
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
                print(Fore.GREEN + f"Correcto! '{entrada}' está en las posiciones: {pos_encontradas}")
            elif entrada in palabra_elegida and entrada in letras_acertadas:
                print(Fore.YELLOW + f"Correcto!, pero ya la habías puesto.")

            else:
                print(Fore.RED + f"Incorrecto! '{entrada}' no está en la palabra.")
                letras_erroneas.append(entrada)
                errores += 1

            if aciertos == longitud_palabra_elegida:
                textowin = pyfiglet.figlet_format(f"GANAS")
                print(Fore.GREEN + textowin)
                print(Fore.MAGENTA + f"¡Felicidades! Has adivinado la palabra: {palabra_elegida}")
                print("")
                repetir = input(Fore.YELLOW + f"Quieres jugar otra vez?")
                if repetir.lower() == "si":
                    self.ahorcado()
                    errores = 0
                    aciertos = 0
                else:
                    break
        else:
            textowin = pyfiglet.figlet_format(f"PIERDES")
            print(Fore.RED + textowin)
            print(Fore.YELLOW + f"¡Perdiste! La palabra era: {palabra_elegida}")
            print("")
            repetir = input(Fore.YELLOW + f"Quieres jugar otra vez? Si / No")
            if repetir.lower() == "si":
                self.ahorcado()
                errores = 0
                aciertos = 0
            else:
                pass