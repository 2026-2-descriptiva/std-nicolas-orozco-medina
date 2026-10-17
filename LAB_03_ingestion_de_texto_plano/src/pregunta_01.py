import pandas as pd
import re
def pregunta_01():
    """
    El archivo `data/clusters_report.txt` es un reporte de clústeres de
    palabras clave pensado para ser leído por una persona, no por un programa:
    los encabezados ocupan varias líneas, las columnas están alineadas con
    espacios y la lista de palabras clave de un clúster continúa en las líneas
    siguientes.

    Su tarea es convertir ese reporte en un DataFrame de Pandas con una fila
    por clúster y las columnas:

    - `cluster`: número del clúster, como entero.
    - `cantidad_de_palabras_clave`: como entero.
    - `porcentaje_de_palabras_clave`: como número decimal; por ejemplo, el
      texto `15,9 %` debe quedar como `15.9`.
    - `principales_palabras_clave`: todas las palabras clave del clúster en un
      solo texto, separadas por una coma y un único espacio.

    Retorne el DataFrame.

    Ejemplo del formato de la respuesta (se omite la última columna):

           cluster  cantidad_de_palabras_clave  porcentaje_de_palabras_clave
        0        1                         105                          15.9
        1        2                         102                          15.4
        ...
    """
    clusters = []
    current_cluster = None

    with open("data/clusters_report.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Saltamos las primeras líneas que contienen los encabezados y la línea divisoria
    lines = lines[4:]

    for line in lines:
        # Expresión regular para detectar las líneas que inician un nuevo clúster
        # Busca: número_cluster  cantidad_palabras  porcentaje %  palabras_clave
        match = re.match(r"^\s*(\d+)\s+(\d+)\s+([\d,]+)\s*%\s+(.*)", line)

        if match:
            # Si ya veníamos procesando un clúster anterior, lo guardamos
            if current_cluster is not None:
                # Limpiar y formatear las palabras clave acumuladas
                text = " ".join(current_cluster["keywords"]).strip()
                # Quitar punto final si existe
                if text.endswith("."):
                    text = text[:-1]
                # Reemplazar múltiples espacios internos por un solo espacio
                text = re.sub(r"\s+", " ", text)
                
                current_cluster["principales_palabras_clave"] = text
                del current_cluster["keywords"]
                clusters.append(current_cluster)

            cluster_num = int(match.group(1))
            cantidad = int(match.group(2))
            porcentaje = float(match.group(3).replace(",", "."))
            keywords_first_line = match.group(4).strip()

            current_cluster = {
                "cluster": cluster_num,
                "cantidad_de_palabras_clave": cantidad,
                "porcentaje_de_palabras_clave": porcentaje,
                "keywords": [keywords_first_line]
            }
        else:
            # Si es una línea de continuación de palabras clave
            line_str = line.strip()
            if line_str and current_cluster is not None:
                current_cluster["keywords"].append(line_str)

    # Agregar el último clúster procesado
    if current_cluster is not None:
        text = " ".join(current_cluster["keywords"]).strip()
        if text.endswith("."):
            text = text[:-1]
        text = re.sub(r"\s+", " ", text)
        
        current_cluster["principales_palabras_clave"] = text
        del current_cluster["keywords"]
        clusters.append(current_cluster)

    df = pd.DataFrame(clusters)
    return df
    raise NotImplementedError
