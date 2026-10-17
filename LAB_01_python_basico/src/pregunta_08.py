import gzip
from collections import defaultdict
def pregunta_08():
    """
    Repita la pregunta 7, pero ahora cada lista de letras debe contener cada
    letra una sola vez y estar ordenada alfabéticamente. Retorne una lista de
    tuplas `(valor, letras)` ordenada por el valor.
    """
    mapping = defaultdict(set)
    with gzip.open("data/data.csv.gz", "rt", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("\t")
            val = int(parts[1])
            letter = parts[0]
            mapping[val].add(letter)
    return sorted([(k, sorted(list(v))) for k, v in mapping.items()])
