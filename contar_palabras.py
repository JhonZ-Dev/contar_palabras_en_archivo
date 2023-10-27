import re
from collections import defaultdict
def contar_palabras_en_archivo(archivo):
    """
    Esta función toma un archivo de texto como entrada y cuenta cuántas veces aparece cada palabra en el archivo.
    """
    
    
    contador_palabras = defaultdict(int)
    with open(archivo, 'r') as file:
        contenido = file.read()
        palabras = re.findall(r'\w+', contenido)
        for palabra in palabras:
            """
            Convertir la palabra a minúsculas para evitar distinción entre mayúsculas y minúsculas
            """
            palabra = palabra.lower()
            contador_palabras[palabra] += 1

