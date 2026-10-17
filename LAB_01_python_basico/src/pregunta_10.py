import gzip
def pregunta_10():
    """
    Para cada registro del archivo, en el mismo orden en que aparecen,
    retorne una tupla con la letra de la primera columna (`letter`), la
    cantidad de elementos de la cuarta columna (`codes`) y la cantidad de
    pares de la quinta columna (`metrics`). El resultado es una lista con una
    tupla por registro.
    """
    result = []
    with gzip.open("data/data.csv.gz", "rt", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("\t")
            letter = parts[0]
            codes_count = len(parts[3].split(","))
            metrics_count = len(parts[4].split(","))
            result.append((letter, codes_count, metrics_count))
    return result
