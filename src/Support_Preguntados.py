import random
#Voy a hacer 10 categorías

historia = [{"¿En qué año comenzó la Primera Guerra Mundial?" : {"Respuestas":{"1914":True,"1918":False,"1939":False,"1945":False}}},
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

series = [
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

cine = [
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

musica = [
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

ciencia = [
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

deportes = [
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

geografia = [
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

literatura = [
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

tecnologia = [
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

arte = [
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

def random_question(categoria_lista):
    n = random.randrange(0,10,1)
    preguntita = categoria_lista[n]
    return preguntita

def obtener_preguntas(lista_preguntas):
    pregunta = list(lista_preguntas)[0]
    return pregunta

def obtener_respuestas_y_(lista_respuestas):
    op = list(lista_respuestas.values())[0] #Saco el conjunto Respuestas
    r1 = list(op.values())[0]
    return r1

def bool_respuesta(respuesta):
    resp1 = list(respuesta.values())[0]
    #resp2 = list(respuesta.values())[1]
    #resp3 = list(respuesta.values())[2]
    #resp4 = list(respuesta.values())[3]
    #res = [resp1,resp2,resp3,resp4]
    return resp1

def hacer_preguntas(pregunta,respuestas):
    
    respuesta = input(f"{pregunta}")
    return
categorias = [historia,series,cine,musica,ciencia,deportes,geografia,literatura,tecnologia,arte]
preguntas_seleccionadas = list(map(random_question,categorias)) #Escoger 10 preguntas aleatorias y guardarlas en una lista
preguntas = list(map(obtener_preguntas,preguntas_seleccionadas)) #Saca la Pregunta en formato String
respuestas = list(map(bool_respuesta,preguntas_seleccionadas))#Saca cada diccionario de respuestas

print(list(map(bool_respuesta,respuestas)))#Esto me da una lista de listas de las respuestas 