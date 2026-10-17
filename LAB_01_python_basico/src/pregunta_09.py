import gzip
from collections import Counter
def pregunta_09():
    """
    Cuente cuántas veces aparece cada clave en la quinta columna (`metrics`)
    de todo el archivo. Retorne un diccionario `{clave: cantidad}` con las
    claves en orden alfabético.
    """
    counter = Counter()
    with gzip.open("data/data.csv.gz", "rt", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("\t")
            metrics_str = parts[4]
            for pair in metrics_str.split(","):
                k, _ = pair.split(":")
                counter[k] += 1
    return dict(sorted(counter.items()))