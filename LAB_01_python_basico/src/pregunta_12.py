import gzip
from collections import defaultdict
def pregunta_12():
    """
    Para cada letra de la primera columna (`letter`), sume todos los valores
    numéricos de los pares `clave:valor` de la quinta columna (`metrics`).
    Retorne un diccionario `{letra: suma}` con las letras en orden alfabético.
    """
    sums = defaultdict(int)
    with gzip.open("data/data.csv.gz", "rt", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("\t")
            letter = parts[0]
            metrics_str = parts[4]
            for pair in metrics_str.split(","):
                _, v = pair.split(":")
                sums[letter] += int(v)
    return dict(sorted(sums.items()))