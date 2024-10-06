import random
import pyfiglet
from colorama import init, Fore


class Preguntados:
    def __init__(self) -> None:
        
        self.historia = [
        {"¿En qué año comenzó la Primera Guerra Mundial?" : {"Respuestas":{"1914":True,"1918":False,"1939":False,"1945":False}}},
        {"¿Quién fue el primer presidente de los Estados Unidos?": {"Respuestas": {"George Washington": True,"Abraham Lincoln": False,"Thomas Jefferson": False,"John Adams": False}}},
        {"¿En qué año cayó el Imperio Romano de Occidente?" : {"Respuestas": {"476": True, "1453": False, "1492": False, "800": False}}},
        {"¿Quién pintó 'La última cena'?" : {"Respuestas": {"Leonardo da Vinci": True, "Miguel Ángel": False, "Vincent van Gogh": False, "Pablo Picasso": False}}},
        {"¿En qué país se originó el ajedrez?" : {"Respuestas": {"China": False, "India": True, "Grecia": False, "Egipto": False}}},
        {"¿Qué metal se encuentra principalmente en el bronce?" : {"Respuestas": {"Hierro": False, "Cobre": True, "Plata": False, "Oro": False}}},
        {"¿Cuál es el país más grande del mundo por superficie?" : {"Respuestas": {"China": False, "Estados Unidos": False, "Canadá": False, "Rusia": True}}},
        {"¿Qué científico propuso la teoría de la relatividad?" : {"Respuestas": {"Isaac Newton": False, "Albert Einstein": True, "Nikola Tesla": False, "Marie Curie": False}}},
        {"¿En qué continente se encuentra el desierto del Sahara?" : {"Respuestas": {"Asia": False, "África": True, "Oceanía": False, "América del Sur": False}}},
        {"¿Quién escribió 'Don Quijote de la Mancha'?" : {"Respuestas": {"Miguel de Cervantes": True, "Gabriel García Márquez": False, "William Shakespeare": False, "Jorge Luis Borges": False}}}
        ]

        self.series = [
            {"¿Cómo se llama el protagonista de la serie 'Breaking Bad'?" : {"Respuestas": {"Walter White": True, "Jesse Pinkman": False, "Saul Goodman": False, "Hank Schrader": False}}},
            {"¿En qué ciudad se desarrolla la serie 'Friends'?" : {"Respuestas": {"Los Ángeles": False, "Nueva York": True, "Chicago": False, "San Francisco": False}}},
            {"¿Qué personaje es el principal en la serie 'Stranger Things'?" : {"Respuestas": {"Eleven": True, "Dustin": False, "Mike": False, "Lucas": False}}},
            {"¿Cómo se llama el reino donde ocurre la mayor parte de los eventos de 'Game of Thrones'?" : {"Respuestas": {"Westeros": True, "Narnia": False, "Middle-Earth": False, "Hogwarts": False}}},
            {"¿En qué año se estrenó la serie 'The Office' (versión estadounidense)?" : {"Respuestas": {"2005": True, "2010": False, "2001": False, "2008": False}}},
            {"¿Qué serie de Netflix está basada en una saga de libros de Andrzej Sapkowski?" : {"Respuestas": {"The Witcher": True, "Shadow and Bone": False, "Locke & Key": False, "The Umbrella Academy": False}}},
            {"¿Quién interpretó a Sheldon Cooper en la serie 'The Big Bang Theory'?" : {"Respuestas": {"Jim Parsons": True, "Johnny Galecki": False, "Simon Helberg": False, "Kunal Nayyar": False}}},
            {"¿En qué serie aparece el personaje de Tony Soprano?" : {"Respuestas": {"Los Soprano": True, "Breaking Bad": False, "Boardwalk Empire": False, "Mad Men": False}}},
            {"¿Cómo se llama el personaje principal de la serie 'House'?" : {"Respuestas": {"Gregory House": True, "John Carter": False, "Mark Sloan": False, "Meredith Grey": False}}},
            {"¿Qué serie cuenta la historia de un grupo de supervivientes en una isla desierta tras un accidente aéreo?" : {"Respuestas": {"Lost": True, "Prison Break": False, "Survivor": False, "The Walking Dead": False}}}
        ]

        self.cine = [
            {"¿Quién dirigió la película 'Titanic'?" : {"Respuestas": {"James Cameron": True, "Steven Spielberg": False, "Christopher Nolan": False, "Quentin Tarantino": False}}},
            {"¿En qué año se estrenó 'El Padrino'?" : {"Respuestas": {"1972": True, "1980": False, "1969": False, "1975": False}}},
            {"¿Qué actor interpretó a Jack Sparrow en 'Piratas del Caribe'?" : {"Respuestas": {"Johnny Depp": True, "Orlando Bloom": False, "Keanu Reeves": False, "Tom Cruise": False}}},
            {"¿Cómo se llama el personaje principal en 'El Rey León'?" : {"Respuestas": {"Simba": True, "Mufasa": False, "Timon": False, "Pumbaa": False}}},
            {"¿Qué película ganó el Oscar a Mejor Película en 2020?" : {"Respuestas": {"Parasite": True, "1917": False, "Joker": False, "Once Upon a Time in Hollywood": False}}},
            {"¿Quién es el director de la trilogía de 'El Señor de los Anillos'?" : {"Respuestas": {"Peter Jackson": True, "George Lucas": False, "Martin Scorsese": False, "Francis Ford Coppola": False}}},
            {"¿Qué película de Pixar cuenta la historia de un niño llamado Miguel que viaja al Mundo de los Muertos?" : {"Respuestas": {"Coco": True, "Ratatouille": False, "Toy Story": False, "Up": False}}},
            {"¿Quién interpretó a Batman en la trilogía de Christopher Nolan?" : {"Respuestas": {"Christian Bale": True, "Ben Affleck": False, "Michael Keaton": False, "Robert Pattinson": False}}},
            {"¿En qué película se escucha la frase 'Hasta la vista, baby'?" : {"Respuestas": {"Terminator 2: Judgment Day": True, "RoboCop": False, "Matrix": False, "Die Hard": False}}},
            {"¿Qué actriz protagonizó 'La La Land' junto a Ryan Gosling?" : {"Respuestas": {"Emma Stone": True, "Emma Watson": False, "Jennifer Lawrence": False, "Scarlett Johansson": False}}}
        ]

        self.musica = [
            {"¿Quién es conocido como el 'Rey del Pop'?" : {"Respuestas": {"Michael Jackson": True, "Elvis Presley": False, "Freddie Mercury": False, "Prince": False}}},
            {"¿En qué año se lanzó el álbum 'Thriller'?" : {"Respuestas": {"1982": True, "1990": False, "1979": False, "1985": False}}},
            {"¿Qué banda británica lanzó el álbum 'Abbey Road'?" : {"Respuestas": {"The Beatles": True, "The Rolling Stones": False, "Led Zeppelin": False, "Pink Floyd": False}}},
            {"¿Quién es el cantante principal de la banda U2?" : {"Respuestas": {"Bono": True, "Mick Jagger": False, "Freddie Mercury": False, "Sting": False}}},
            {"¿Qué artista lanzó la canción 'Like a Prayer'?" : {"Respuestas": {"Madonna": True, "Whitney Houston": False, "Cyndi Lauper": False, "Tina Turner": False}}},
            {"¿Cuál es el nombre de la gira mundial de Taylor Swift en 2023?" : {"Respuestas": {"The Eras Tour": True, "Lover Tour": False, "1989 Tour": False, "Fearless Tour": False}}},
            {"¿Qué grupo escribió la canción 'Bohemian Rhapsody'?" : {"Respuestas": {"Queen": True, "The Who": False, "Led Zeppelin": False, "Pink Floyd": False}}},
            {"¿En qué festival legendario se presentó Jimi Hendrix en 1969?" : {"Respuestas": {"Woodstock": True, "Glastonbury": False, "Coachella": False, "Isle of Wight": False}}},
            {"¿Quién es el cantante principal de Coldplay?" : {"Respuestas": {"Chris Martin": True, "Jon Bon Jovi": False, "Dave Grohl": False, "Brandon Flowers": False}}},
            {"¿Qué grupo de K-Pop es conocido mundialmente por su éxito 'Dynamite'?" : {"Respuestas": {"BTS": True, "Blackpink": False, "EXO": False, "TWICE": False}}}
        ]

        self.ciencia = [
            {"¿Quién formuló la teoría de la evolución?" : {"Respuestas": {"Charles Darwin": True, "Isaac Newton": False, "Albert Einstein": False, "Gregor Mendel": False}}},
            {"¿Qué elemento tiene el símbolo químico 'O'?" : {"Respuestas": {"Oxígeno": True, "Oro": False, "Plata": False, "Ozono": False}}},
            {"¿En qué año se llevó a cabo el primer alunizaje?" : {"Respuestas": {"1969": True, "1972": False, "1957": False, "1980": False}}},
            {"¿Cuál es el planeta más grande del sistema solar?" : {"Respuestas": {"Júpiter": True, "Saturno": False, "Urano": False, "Neptuno": False}}},
            {"¿Qué científico descubrió la penicilina?" : {"Respuestas": {"Alexander Fleming": True, "Marie Curie": False, "Louis Pasteur": False, "Isaac Newton": False}}},
            {"¿Cuál es la unidad básica de la vida?" : {"Respuestas": {"Célula": True, "Molécula": False, "Átomo": False, "Tejido": False}}},
            {"¿Qué fuerza mantiene a los planetas en órbita alrededor del Sol?" : {"Respuestas": {"Gravedad": True, "Fuerza centrífuga": False, "Magnetismo": False, "Inercia": False}}},
            {"¿Qué órgano del cuerpo humano es responsable de bombear la sangre?" : {"Respuestas": {"Corazón": True, "Pulmones": False, "Riñones": False, "Hígado": False}}},
            {"¿Cómo se llama la fase de la materia que tiene volumen fijo pero forma variable?" : {"Respuestas": {"Líquido": True, "Sólido": False, "Gas": False, "Plasma": False}}},
            {"¿Quién es conocido como el 'padre de la física moderna'?" : {"Respuestas": {"Albert Einstein": True, "Isaac Newton": False, "Galileo Galilei": False, "Niels Bohr": False}}}
        ]

        self.deportes = [
            {"¿Qué país ganó la Copa Mundial de Fútbol en 2018?" : {"Respuestas": {"Francia": True, "Croacia": False, "Brasil": False, "Argentina": False}}},
            {"¿Qué jugador de baloncesto es conocido como 'Air Jordan'?" : {"Respuestas": {"Michael Jordan": True, "LeBron James": False, "Kobe Bryant": False, "Shaquille O'Neal": False}}},
            {"¿En qué deporte se utiliza una raqueta y una pelota pequeña llamada 'shuttlecock'?" : {"Respuestas": {"Bádminton": True, "Tenis": False, "Squash": False, "Ping-pong": False}}},
            {"¿En qué año se celebraron los primeros Juegos Olímpicos modernos?" : {"Respuestas": {"1896": True, "1900": False, "1912": False, "1920": False}}},
            {"¿Cuál es el único país que ha ganado la Copa Mundial de Fútbol en todos los continentes?" : {"Respuestas": {"Brasil": True, "Alemania": False, "Italia": False, "Argentina": False}}},
            {"¿Quién tiene el récord de más títulos de Grand Slam en tenis masculino?" : {"Respuestas": {"Rafael Nadal": False, "Roger Federer": False, "Novak Djokovic": True, "Pete Sampras": False}}},
            {"¿En qué equipo jugó Diego Maradona en la década de los 80?" : {"Respuestas": {"Napoli": True, "Barcelona": False, "Boca Juniors": False, "Sevilla": False}}},
            {"¿Qué boxeador es conocido como 'El más grande'?" : {"Respuestas": {"Muhammad Ali": True, "Mike Tyson": False, "Floyd Mayweather": False, "Rocky Marciano": False}}},
            {"¿Qué equipo de la NFL ha ganado más Super Bowls?" : {"Respuestas": {"Pittsburgh Steelers": False, "New England Patriots": True, "Dallas Cowboys": False, "San Francisco 49ers": False}}},
            {"¿Qué país ha ganado más medallas olímpicas en la historia?" : {"Respuestas": {"Estados Unidos": True, "China": False, "Rusia": False, "Reino Unido": False}}}
        ]

        self.geografia = [
            {"¿Cuál es el país más grande del mundo?" : {"Respuestas": {"Rusia": True, "Canadá": False, "China": False, "Estados Unidos": False}}},
            {"¿Qué país tiene la mayor cantidad de islas en el mundo?" : {"Respuestas": {"Suecia": True, "Indonesia": False, "Filipinas": False, "Japón": False}}},
            {"¿En qué continente se encuentra el río Nilo?" : {"Respuestas": {"África": True, "Asia": False, "América del Sur": False, "Europa": False}}},
            {"¿Cuál es la capital de Japón?" : {"Respuestas": {"Tokio": True, "Osaka": False, "Kioto": False, "Nagoya": False}}},
            {"¿Qué océano es el más grande del mundo?" : {"Respuestas": {"Pacífico": True, "Atlántico": False, "Índico": False, "Ártico": False}}},
            {"¿En qué país se encuentra la Torre Eiffel?" : {"Respuestas": {"Francia": True, "Italia": False, "España": False, "Reino Unido": False}}},
            {"¿Cuál es el país más pequeño del mundo?" : {"Respuestas": {"Ciudad del Vaticano": True, "Mónaco": False, "Malta": False, "Liechtenstein": False}}},
            {"¿Qué cordillera se extiende a lo largo de la costa occidental de América del Sur?" : {"Respuestas": {"Los Andes": True, "Los Alpes": False, "El Himalaya": False, "Las Montañas Rocosas": False}}},
            {"¿Qué país tiene la mayor población del mundo?" : {"Respuestas": {"China": True, "India": False, "Estados Unidos": False, "Indonesia": False}}},
            {"¿Cuál es la capital de Australia?" : {"Respuestas": {"Canberra": True, "Sídney": False, "Melbourne": False, "Perth": False}}}
        ]

        self.literatura = [
            {"¿Quién escribió 'Cien años de soledad'?" : {"Respuestas": {"Gabriel García Márquez": True, "Mario Vargas Llosa": False, "Julio Cortázar": False, "Pablo Neruda": False}}},
            {"¿Qué novela fue escrita por George Orwell?" : {"Respuestas": {"1984": True, "Matar a un ruiseñor": False, "El Gran Gatsby": False, "Rebelión en la Granja": False}}},
            {"¿En qué país nació el escritor William Shakespeare?" : {"Respuestas": {"Inglaterra": True, "Francia": False, "España": False, "Italia": False}}},
            {"¿Cuál es el título de la primera novela de J.K. Rowling?" : {"Respuestas": {"Harry Potter y la piedra filosofal": True, "Harry Potter y la cámara secreta": False, "Harry Potter y el prisionero de Azkaban": False, "Harry Potter y el cáliz de fuego": False}}},
            {"¿Quién escribió 'Don Quijote de la Mancha'?" : {"Respuestas": {"Miguel de Cervantes": True, "Lope de Vega": False, "Luis de Góngora": False, "Francisco de Quevedo": False}}},
            {"¿Qué autor escribió 'Orgullo y Prejuicio'?" : {"Respuestas": {"Jane Austen": True, "Emily Brontë": False, "Charlotte Brontë": False, "Mary Shelley": False}}},
            {"¿En qué novela aparece el personaje de Jean Valjean?" : {"Respuestas": {"Los Miserables": True, "Crimen y Castigo": False, "Guerra y Paz": False, "El Conde de Montecristo": False}}},
            {"¿Qué obra de Dante Alighieri narra un viaje por el infierno?" : {"Respuestas": {"La Divina Comedia": True, "El Paraíso Perdido": False, "La Odisea": False, "La Eneida": False}}},
            {"¿Qué autor escribió 'El viejo y el mar'?" : {"Respuestas": {"Ernest Hemingway": True, "F. Scott Fitzgerald": False, "John Steinbeck": False, "Mark Twain": False}}},
            {"¿En qué país está ambientada la novela 'Matar a un ruiseñor'?" : {"Respuestas": {"Estados Unidos": True, "Canadá": False, "Reino Unido": False, "Australia": False}}}
        ]

        self.tecnologia = [
            {"¿Quién fundó la empresa Microsoft?" : {"Respuestas": {"Bill Gates": True, "Steve Jobs": False, "Mark Zuckerberg": False, "Elon Musk": False}}},
            {"¿En qué año se lanzó el primer iPhone?" : {"Respuestas": {"2007": True, "2005": False, "2010": False, "2003": False}}},
            {"¿Qué empresa es conocida por crear el sistema operativo Android?" : {"Respuestas": {"Google": True, "Apple": False, "Microsoft": False, "IBM": False}}},
            {"¿Qué red social fue comprada por Facebook en 2012?" : {"Respuestas": {"Instagram": True, "Twitter": False, "Snapchat": False, "TikTok": False}}},
            {"¿Qué lenguaje de programación es conocido por ser usado en inteligencia artificial?" : {"Respuestas": {"Python": True, "Java": False, "C++": False, "PHP": False}}},
            {"¿Qué inventor es conocido por desarrollar el primer motor de búsqueda en la web?" : {"Respuestas": {"Larry Page": True, "Elon Musk": False, "Steve Jobs": False, "Jeff Bezos": False}}},
            {"¿En qué año se fundó Amazon?" : {"Respuestas": {"1994": True, "1999": False, "1985": False, "2000": False}}},
            {"¿Qué consola de videojuegos lanzó Nintendo en 2006?" : {"Respuestas": {"Nintendo Wii": True, "Nintendo Switch": False, "Nintendo DS": False, "GameCube": False}}},
            {"¿Qué empresa lanzó el primer navegador web comercial?" : {"Respuestas": {"Netscape": True, "Microsoft": False, "Google": False, "Mozilla": False}}},
            {"¿Quién inventó el lenguaje de programación Java?" : {"Respuestas": {"James Gosling": True, "Tim Berners-Lee": False, "Guido van Rossum": False, "Dennis Ritchie": False}}}
        ]

        self.arte = [
            {"¿Quién pintó la 'Mona Lisa'?" : {"Respuestas": {"Leonardo da Vinci": True, "Pablo Picasso": False, "Vincent van Gogh": False, "Claude Monet": False}}},
            {"¿En qué museo se encuentra la pintura 'La Noche Estrellada'?" : {"Respuestas": {"Museo de Arte Moderno (MoMA)": True, "Museo del Louvre": False, "Galería Uffizi": False, "Museo del Prado": False}}},
            {"¿Qué pintor es conocido por su obra 'Guernica'?" : {"Respuestas": {"Pablo Picasso": True, "Salvador Dalí": False, "Joan Miró": False, "Francisco Goya": False}}},
            {"¿Qué estilo artístico se caracteriza por representar imágenes distorsionadas y abstractas?" : {"Respuestas": {"Cubismo": True, "Impresionismo": False, "Surrealismo": False, "Renacimiento": False}}},
            {"¿Quién esculpió el 'David'?" : {"Respuestas": {"Miguel Ángel": True, "Donatello": False, "Bernini": False, "Leonardo da Vinci": False}}},
            {"¿En qué ciudad se encuentra la Capilla Sixtina?" : {"Respuestas": {"Ciudad del Vaticano": True, "Florencia": False, "Roma": False, "Milán": False}}},
            {"¿Qué artista pintó 'Las Meninas'?" : {"Respuestas": {"Diego Velázquez": True, "Francisco Goya": False, "El Greco": False, "Salvador Dalí": False}}},
            {"¿En qué país nació el pintor Vincent van Gogh?" : {"Respuestas": {"Países Bajos": True, "Francia": False, "Bélgica": False, "Alemania": False}}},
            {"¿Quién fue el creador del estilo arquitectónico conocido como 'La Sagrada Familia'?" : {"Respuestas": {"Antoni Gaudí": True, "Frank Gehry": False, "Le Corbusier": False, "Frank Lloyd Wright": False}}},
            {"¿Qué movimiento artístico surgió como una reacción a la Primera Guerra Mundial?" : {"Respuestas": {"Dadaísmo": True, "Impresionismo": False, "Romanticismo": False, "Futurismo": False}}}
        ]

        self.categorias = [self.historia,self.series,self.cine,self.musica,self.ciencia,self.deportes,self.geografia,self.literatura,self.tecnologia,self.arte]
        self.nombre_categorias = ["Historia","Series","Cine","Música","Ciencia","Deportes","Geografía","Literatura","Tecnología","Arte"]
        self.selecciones = list(map(self.random_number, self.categorias))
        self.preguntas_seleccionadas = list(map(self.random_question, self.categorias, self.selecciones))
        self.preguntas = list(map(self.obtener_preguntas, self.preguntas_seleccionadas))
        self.respuestas = list(map(self.bool_respuesta, self.preguntas_seleccionadas, self.preguntas))

    def random_number(self, categoria):
        """
        Genera un número aleatorio en forma de cadena.

        Este método genera un número entero aleatorio entre 0 y 9 (incluidos) y lo 
        devuelve como una cadena de texto. Aunque se pasa un parámetro 'categoria', 
        actualmente no se utiliza dentro de la función.

        Args:
            categoria (str): Un argumento que puede utilizarse para categorizar el número
                            generado, aunque no se utiliza en la lógica actual.

        Returns:
            str: El número aleatorio generado, convertido a cadena.
        """
        numero_random = random.randrange(0, 10, 1)
        return str(numero_random)

    def random_question(self, categoria_lista, n):
        """
        Selecciona una pregunta aleatoria de una lista de categorías.

        Este método toma una lista de preguntas (categoria_lista) y un índice (n) 
        y devuelve la pregunta correspondiente a ese índice. Se asume que el índice 
        proporcionado está dentro del rango de la lista.

        Args:
            categoria_lista (list): Una lista que contiene las preguntas disponibles.
            n (int): El índice de la pregunta a seleccionar de la lista.

        Returns:
            str: La pregunta seleccionada de la lista.
        """
        preguntita = categoria_lista[int(n)]
        return preguntita

    def obtener_preguntas(self, lista_preguntas):
        """
        Obtiene la primera pregunta de una lista de preguntas.

        Este método toma una lista de preguntas y devuelve la primera pregunta de 
        la lista. Se asume que la lista no está vacía.

        Args:
            lista_preguntas (list): Una lista que contiene las preguntas disponibles.

        Returns:
            str: La primera pregunta de la lista.
        """
        pregunta = list(lista_preguntas)[0]
        return pregunta

    def bool_respuesta(self, respuesta, pregunta):
        """
        Obtiene las respuestas posibles para una pregunta específica.

        Este método accede a un diccionario de respuestas y devuelve las opciones 
        de respuesta asociadas a una pregunta dada. Se asume que la pregunta está 
        presente en el diccionario.

        Args:
            respuesta (dict): Un diccionario que contiene las respuestas, donde 
                            cada clave es una pregunta y el valor es otro diccionario 
                            que incluye una clave "Respuestas".
            pregunta (str): La pregunta para la cual se desean obtener las respuestas.

        Returns:
            list: Una lista de respuestas posibles para la pregunta dada.
        """
        answers = respuesta[pregunta]["Respuestas"]
        return answers
    
    def preguntar(self):
        """
        Realiza un juego de preguntas y respuestas.

        Este método presenta al usuario una serie de 10 preguntas de opción múltiple 
        y evalúa sus respuestas. El usuario puede salir del juego en cualquier momento 
        escribiendo "stop". Por cada respuesta correcta, el usuario gana un punto.

        Args:
            preguntita (list): Una lista de preguntas que se mostrarán al usuario. 
                                Cada pregunta debe ser un string.

        Returns:
            None: Este método no devuelve ningún valor, pero imprime los resultados 
                de las respuestas al final del juego.
        """
        aciertos = 0
        fallos = 0
        n_pregunta = 0
        init(autoreset=True)
        titulo = pyfiglet.figlet_format("PREGUNTADOS", font="slant")
        print(Fore.GREEN + titulo)
        print("Bienvenido a preguntados!:")
        print("Las reglas son simples, responde a las preguntas correctamente y obtendrás un punto!")
        print("Hay 10 preguntas, para salir si te aburres o rindes, pulsa stop.")
        print("Tu respuesta debe ser igual que las opciones dadas por ej: Gabriel García Márquez")
        input(Fore.YELLOW + "Estas listo?, Presiona Cualquier Tecla para Jugar!")
        print("")

        while n_pregunta < 10:
            i = 0
            try:
                while i < 10:
                    answers = list(self.respuestas[n_pregunta].keys())
                    r1 = answers[0]
                    r2 = answers[1]
                    r3 = answers[2]
                    r4 = answers[3]
                    question = input(Fore.LIGHTCYAN_EX + f"Categoría {self.nombre_categorias[n_pregunta]}\n"
                            f"Pregunta {n_pregunta + 1}: {self.preguntas[n_pregunta]}:" + Fore.RESET +
                            f"\na) {r1}"+
                            f"\nb) {r2}"+
                            f"\nc) {r3}"+
                            f"\nd) {r4}\n"+
                            f"Introduce tu Respuesta: ")
                    if question.lower() == "stop":
                        i = 12
                        n_pregunta = 14
                    else:
                        valor = self.respuestas[n_pregunta][question]
                        if valor == True:
                            print(Fore.GREEN + f"Acertaste!")
                            print("")
                            aciertos += 1
                            n_pregunta += 1
                            i += 1
                        else:
                            print(Fore.RED + f"Fallaste!")
                            print("")
                            fallos += 1
                            n_pregunta += 1
                            i += 1

            except:
                print(f"No es una respuesta válida, vuelve a introducirla")

        if question.lower() == "stop":
            fin = pyfiglet.figlet_format("STOP", font="slant")
            print(Fore.RED + fin)
            print(f"")
            print("Has salido del Juego, chao!")
            print("Presiona cualquier tecla para salir:")
        else:
            fin = pyfiglet.figlet_format(f"RESULTADOS\n{aciertos} / 10", font="slant")
            print(Fore.GREEN + fin)
            print(f"")
            print(f"Terminamos!, Has acertado {aciertos} preguntas, y has fallado {fallos} preguntas, tu puntuación es de: {aciertos}/10")
            print("Presiona cualquier tecla para salir:")
