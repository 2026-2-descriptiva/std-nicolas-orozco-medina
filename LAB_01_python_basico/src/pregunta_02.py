import gzip
from collections import Counter
def pregunta_02():
    """
    Cuente cuántos registros hay para cada letra de la primera columna
    (`letter`). Retorne una lista de tuplas `(letra, cantidad)` ordenada
    alfabéticamente por la letra.
    """
    counter = Counter()
    with gzip.open("data/data.csv.gz", "rt", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("\t")
            counter[parts[0]] += 1
    return sorted(counter.items())
