import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
import re
import string

# Cargar el archivo CSV
file_path = 'Datos/noticias_elespectador.csv'  # Cambia por la ruta de tu archivo CSV
data = pd.read_csv(file_path)

# Verificar si la columna 'contenido_articulo' existe
if 'contenido_articulo' not in data.columns:
    raise KeyError("La columna 'contenido_articulo' no existe en el archivo CSV")

# Función para limpiar el texto manteniendo las tildes
def limpiar_contenido(texto):
    # Convertir a minúsculas
    texto = texto.lower()
    
    # Eliminar puntuación
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    
    # Eliminar números
    texto = re.sub(r'\d+', '', texto)
    
    # Eliminar exceso de espacios
    texto = re.sub(r'\s+', ' ', texto).strip()
    
    return texto

# Aplicar la función de limpieza a los contenidos del artículo
data['contenido_limpio'] = data['contenido_articulo'].apply(limpiar_contenido)

# Lista estándar de palabras vacías (stop words) en español
stop_words_spanish = [
    'a', 'al', 'algo', 'algunas', 'algunos', 'ante', 'bajo', 'cabe', 'cada', 'como', 'con', 
    'contra', 'cual', 'cuando', 'de', 'del', 'desde', 'donde', 'durante', 'e', 'el', 'ella', 
    'ellas', 'ellos', 'en', 'entre', 'era', 'erais', 'eran', 'eras', 'eres', 'es', 'esa', 'esas', 
    'ese', 'eso', 'esos', 'esta', 'estaba', 'estabais', 'estaban', 'estabas', 'estad', 'estada', 
    'estadas', 'estado', 'estados', 'estamos', 'estando', 'estar', 'estaremos', 'estará', 'estarán', 
    'estarás', 'estaré', 'estaréis', 'estaría', 'estaríais', 'estaríamos', 'estarían', 'estarías', 
    'estas', 'este', 'estemos', 'esto', 'estos', 'estoy', 'estuve', 'estuviera', 'estuvierais', 
    'estuvieran', 'estuvieras', 'estuvieron', 'estuviese', 'estuvieseis', 'estuviesen', 'estuvieses', 
    'estuvimos', 'estuviste', 'estuvisteis', 'estuviéramos', 'estuviésemos', 'fue', 'fueron', 'fui', 
    'fuimos', 'ha', 'habida', 'habidas', 'habido', 'habidos', 'habiendo', 'habremos', 'habrá', 'habrán', 
    'habrás', 'habré', 'habréis', 'habría', 'habríais', 'habríamos', 'habrían', 'habrías', 'han', 'has', 
    'hasta', 'hay', 'haya', 'hayamos', 'hayan', 'hayas', 'hayáis', 'he', 'hemos', 'hube', 'hubiera', 
    'hubierais', 'hubieran', 'hubieras', 'hubieron', 'hubiese', 'hubieseis', 'hubiesen', 'hubieses', 
    'hubimos', 'hubiste', 'hubisteis', 'hubiéramos', 'hubiésemos', 'la', 'las', 'le', 'les', 'lo', 
    'los', 'me', 'mi', 'mis', 'mucho', 'muchos', 'muy', 'nos', 'nosotras', 'nosotros', 'nuestra', 
    'nuestras', 'nuestro', 'nuestros', 'o', 'os', 'otra', 'otras', 'otro', 'otros', 'para', 'pero', 
    'poco', 'por', 'porque', 'que', 'quien', 'quienes', 'qué', 'se', 'sea', 'seamos', 'sean', 'seas', 
    'seremos', 'será', 'serán', 'serás', 'seré', 'seréis', 'sería', 'seríais', 'seríamos', 'serían', 
    'serías', 'si', 'sin', 'sobre', 'sois', 'somos', 'son', 'soy', 'su', 'sus', 'también', 'tanto', 
    'te', 'tenida', 'tenidas', 'tenido', 'tenidos', 'teniendo', 'tenéis', 'tendremos', 'tendrá', 
    'tendrán', 'tendrás', 'tendré', 'tendréis', 'tendría', 'tendríais', 'tendríamos', 'tendrían', 
    'tendrías', 'tened', 'tenemos', 'tenga', 'tengamos', 'tengan', 'tengas', 'tengo', 'tengáis', 
    'tenida', 'tuviera', 'tuvierais', 'tuvieran', 'tuvieras', 'tuvieron', 'tuviese', 'tuvieseis', 
    'tuviesen', 'tuvieses', 'tuvimos', 'tuviste', 'tuvisteis', 'tuyos', 'tuyas', 'un', 'una', 'unas', 
    'uno', 'unos', 'usted', 'vos', 'vosotras', 'vosotros', 'y', 'ya', 'yo'
]

# Usar TF-IDF para identificar las palabras más importantes con la lista personalizada de stop words en español
tfidf = TfidfVectorizer(stop_words=stop_words_spanish)
tfidf_matrix = tfidf.fit_transform(data['contenido_limpio'])

# Obtenemos los nombres de las características (palabras) y las puntuaciones
feature_names = tfidf.get_feature_names_out()

# Sumamos las puntuaciones TF-IDF de cada palabra en todos los artículos
word_scores = tfidf_matrix.sum(axis=0).A1

# Empaquetamos las palabras con sus puntuaciones
palabra_puntajes = list(zip(feature_names, word_scores))

# Ordenamos las palabras por su relevancia (puntuaciones TF-IDF) de mayor a menor
palabra_puntajes_ordenados = sorted(palabra_puntajes, key=lambda x: x[1], reverse=True)

# Función para formatear la lista de palabras
def formatear_lista_palabras(palabras_tfidf):
    return '\n'.join([f"{palabra[0]}: {palabra[1]}" for palabra in palabras_tfidf])

# Mostramos las 20 palabras más importantes basadas en frecuencia y relevancia

num = int(input("Ingrese el numero de palabras que quiere obtener apartir del modelo: "))
palabras_importantes = formatear_lista_palabras(palabra_puntajes_ordenados[:num])
print(palabras_importantes)
