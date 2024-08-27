from csv import writer
import csv
import requests
import json

def extraer_noticias(url):
    noticias = []
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica si la solicitud fue exitosa
        data = response.json()  # Decodifica la respuesta JSON

        # Iterar a través de los elementos de contenido
        for item in data.get('content_elements', []):
            titulo = item.get('headlines', {}).get('basic', 'Sin título')
            autores = ", ".join([autor.get('name', 'Desconocido') for autor in item.get('credits', {}).get('by', [])])
            fecha = item.get('display_date', 'Sin fecha')
            contenido = item.get('description', {}).get('basic', 'Sin contenido')

            noticia = {
                'titulo': titulo,
                'autores': autores,
                'fecha_publicacion': fecha,
                'contenido': contenido
            }
            noticias.append(noticia)

    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")

    return noticias

# Lista de secciones del Espectador:
secciones = [
    "genero-y-diversidad",
    "entretenimiento",
    "autos",
    "turismo",
    "deportes",
    "mundo",
    "colombia",
    "colombia-20",
    "ambiente",
    "politica",
    "judicial",
    "economia",
    "bogota"
]

csv_file = 'noticias.csv'

# Generar la URL de la API para la sección "TEXTO"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Titulo', 'Seccion', 'Autores', 'Fecha de publicacion', 'Contenido'])  # Encabezados del CSV

    for i in secciones:
        url = "https://www.elespectador.com/pf/api/v3/content/fetch/general?query=%7B%22externalSite%22%3A%22%22%2C%22section%22%3A%22%2F"+i+"%22%2C%22site%22%3A%22el-espectador%22%2C%22size%22%3A20%2C%22sourceInclude%22%3A%22_id%2Cadditional_properties%2Ccanonical_url%2Ctype%2Csubtype%2Cdescription.basic%2Cheadlines.basic%2Csubheadlines.basic%2Ctaxonomy.primary_section._id%2Ctaxonomy.primary_section.name%2Ctaxonomy.primary_section.path%2Ctaxonomy.sections.name%2Ctaxonomy.tags.text%2Ctaxonomy.tags.slug%2Cfirst_publish_date%2Cdisplay_date%2Clast_updated_date%2Cpromo_items.basic%2Cpromo_items.comercial%2Cpromo_items.comercial_movil%2Cpromo_items.jw_player%2Clabel%2Ccredits.by._id%2Ccredits.by.name%2Ccredits.by.additional_properties.original%2Ccredits.by.image.url%2CcommentCount%22%7D&d=950&_website=el-espectador"
        noticias = extraer_noticias(url)
        for noticia in noticias:
            writer.writerow([noticia['titulo'], i, noticia['autores'], noticia['fecha_publicacion'], noticia['contenido']])

print(f"Datos guardados en {csv_file}")
