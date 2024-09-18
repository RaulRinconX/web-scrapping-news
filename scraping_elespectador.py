import requests
import csv

# Función para extraer noticias de una sección específica
def extraer_noticias(seccion, size=10):
    url = f"https://www.elespectador.com/pf/api/v3/content/fetch/general?query=%7B%22externalSite%22%3A%22%22%2C%22section%22%3A%22{seccion}%22%2C%22site%22%3A%22el-espectador%22%2C%22size%22%3A{size}%2C%22sourceInclude%22%3A%22_id%2Ccanonical_url%2Cheadlines.basic%2Cdescription.basic%2Ctaxonomy.primary_section.name%2Cfirst_publish_date%2Ccredits.by.name%2Cpromo_items.basic.url%22%7D&_website=el-espectador"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica si la solicitud fue exitosa
        data = response.json()  # Decodifica la respuesta JSON
        
        # Extrae y devuelve los elementos de contenido
        noticias = []
        for item in data.get('content_elements', []):
            noticia = {
                'titulo': item.get('headlines', {}).get('basic', 'Sin título'),
                'descripcion': item.get('description', {}).get('basic', 'Sin descripción'),
                'seccion': item.get('taxonomy', {}).get('primary_section', {}).get('name', 'Sin sección'),
                'fecha_publicacion': item.get('first_publish_date', 'Sin fecha'),
                'autores': ', '.join([autor.get('name', 'Desconocido') for autor in item.get('credits', {}).get('by', [])]),
            }
            noticias.append(noticia)
        
        return noticias
    
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
        return []

# Función para guardar noticias en un archivo CSV
def guardar_noticias_csv(noticias, nombre_archivo='noticias.csv'):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['titulo', 'descripcion', 'seccion', 'fecha_publicacion', 'autores'])
        writer.writeheader()
        for noticia in noticias:
            writer.writerow(noticia)
    print(f"Noticias guardadas en {nombre_archivo}")

# Secciones que se quieren scrapear
secciones = [
    '/politica', '/judicial', '/economia', '/mundo', '/bogota', '/entretenimiento',
    '/deportes', '/colombia', '/el-magazin-cultural', '/salud', '/ambiente',
    '/investigacion', '/educacion', '/ciencia', '/genero-y-diversidad', '/tecnologia',
    '/actualidad', '/reportajes', '/historias-visuales', '/colecciones', '/podcast'
]
# Número de noticias por categoría
tamaño_por_categoria = 20

# Lista para almacenar todas las noticias
todas_las_noticias = []

# Extraer noticias de cada sección
for seccion in secciones:
    print(f"Extrayendo noticias de la sección {seccion}...")
    noticias = extraer_noticias(seccion, tamaño_por_categoria)
    todas_las_noticias.extend(noticias)

# Guardar todas las noticias en un archivo CSV
guardar_noticias_csv(todas_las_noticias, 'noticias_elespectador.csv')
