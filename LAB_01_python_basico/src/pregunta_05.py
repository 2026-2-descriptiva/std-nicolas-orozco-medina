import gzip
from collections import defaultdict
def pregunta_05():
    """
    Para cada letra de la primera columna (`letter`), encuentre el valor
    máximo y el valor mínimo de la segunda columna (`value`). Retorne una lista
    de tuplas `(letra, máximo, mínimo)` ordenada alfabéticamente por la letra.
    """
    stats = defaultdict(lambda: {"max": float("-inf"), "min": float("inf")})
    with gzip.open("data/data.csv.gz", "rt", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("\t")
            letter = parts[0]
            val = int(parts[1])
            if val > stats[letter]["max"]:
                stats[letter]["max"] = val
            if val < stats[letter]["min"]:
                stats[letter]["min"] = val
    return sorted([(k, v["max"], v["min"]) for k, v in stats.items()])
