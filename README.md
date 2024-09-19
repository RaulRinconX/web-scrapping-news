# Web scrapper Espectador newspaper.

## 1. Explicacion del proyecto
## 2. Paquetes necesarios para ejecutarlo
## 3. Pasos para ver el resultado


## 1. Explicacion del proyecto

### ¿Qué es TF-IDF y cómo funciona?

TF-IDF es una técnica comúnmente utilizada en procesamiento de lenguaje natural (NLP) para medir la importancia de una palabra en un documento dentro de un conjunto de documentos. Se utiliza para convertir texto en una representación numérica que se puede procesar mediante algoritmos de aprendizaje automático o análisis de texto.

TF-IDF es una combinación de dos medidas:

- TF (Term Frequency) – Frecuencia de término:
  Mide cuántas veces aparece una palabra (término) en un documento en relación con el número total de palabras en el documento.
- IDF (Inverse Document Frequency) – Frecuencia inversa de documento:
  Mide la importancia de una palabra en todo el conjunto de documentos (corpus). Si una     palabra aparece en muchos documentos, se considera menos importante.

La puntuación TF-IDF de una palabra en un documento es el producto de las dos medidas anteriores:

TF-IDF  = TF × IDF

Esto permite que una palabra sea puntuada más alto si:

Aparece frecuentemente en un documento (alto TF).
No aparece en muchos otros documentos (alto IDF).

### ¿Por qué es útil usar TF-IDF?

TF-IDF es útil porque resalta las palabras más importantes y relevantes en un documento sin ser demasiado influyente por las palabras comunes que se encuentran en todos los textos. Esto es muy útil para tareas como el análisis de contenido, clasificación de texto, búsqueda de información, y más.

- Filtra palabras comunes: Las palabras que son comunes en muchos documentos (por ejemplo, "el", "de", "la") obtienen una puntuación IDF baja y no dominan los resultados.

- Resalta la relevancia de palabras específicas: Las palabras que son específicas de un documento pero no comunes en otros obtienen una puntuación más alta, lo que indica que son importantes para entender ese documento en particular.

- No requiere etiquetas: A diferencia de otros métodos, TF-IDF es una técnica no supervisada, lo que significa que no requiere un conjunto de datos etiquetado para funcionar.
  
### ¿Por qué es bueno usar TF-IDF en este caso?

En el caso de extraer las palabras más importantes de los artículos, TF-IDF es una técnica excelente porque:

1. Relevancia en el contenido: Permite identificar palabras que son específicas y relevantes para los temas que se discuten en cada artículo, sin estar dominadas por términos comunes.

2. Elimina ruido: Palabras comunes en el idioma (stop words) como "el", "la", "de" son filtradas de manera efectiva, lo que ayuda a resaltar los términos verdaderamente importantes.

3. Análisis de textos largos: En el caso de artículos, es útil destacar términos clave sin que los resultados se vean afectados por la longitud del artículo.

4. No se centra solo en la frecuencia: Solo contar las palabras más repetidas podría traer ruido, pero al incluir la frecuencia inversa de documento (IDF), TF-IDF pondera qué términos son importantes tanto en el documento como en todo el corpus, dándonos un análisis equilibrado.

### ¿Qué representa la puntuación TF-IDF?

TF (Term Frequency): Mide cuántas veces aparece una palabra en un documento (artículo).
IDF (Inverse Document Frequency): Mide cuán común o rara es esa palabra en todos los documentos (artículos). Las palabras que aparecen en muchos documentos obtendrán una puntuación IDF más baja.

### Interpretación:

Una puntuación TF-IDF alta indica que la palabra es frecuente en un artículo, pero rara en otros artículos. Esto sugiere que la palabra es más importante y específica para ese artículo en particular.
Una puntuación TF-IDF baja indica que la palabra aparece frecuentemente en muchos artículos, lo que la hace menos relevante o más común (como las stop words que eliminamos: "el", "la", etc.).

Por ejemplo, si una palabra como "salud" tiene una puntuación de 6.66, significa que es relevante para el contenido del artículo donde aparece, pero no tan común en todos los documentos, por lo que se considera importante en su contexto.

## 2. Paquetes necesarios para ejecutarlo

------ instalar en la terminal los paquetes necesarios ------

buscar en windows terminal o directamente en la terminal de VSCode

- pip install requests
- pip install spacy
- python -m spacy download es_core_news_sm

## 3. Pasos para ver el resultado

1. Clonar el archivo usando en una terminal -> git clone https://github.com/RaulRinconX/web-scrapping-news.git
2. Abrir el proyecto y ejecutar "scraping_elespectador.py"
3. En dadoo caso que falle el scrapper por error de SSL o TLS, ejecutarlo de nuevo sin problema y asi hasta que funcione :P
4. Al terminar de ejecutarse el scrapper nos genera un archivo csv con los datos de las noticias en la carpeta Datos
5. Ejecutar data_analisis.py 
6. Ingresar el numero de palabras deseadas a retornar por el modelo
7. Ver el resultado.
