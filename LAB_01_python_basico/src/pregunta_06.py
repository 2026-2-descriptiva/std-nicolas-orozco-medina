import gzip
from collections import defaultdict
def pregunta_06():
    """
    La quinta columna (`metrics`) contiene pares `clave:valor` separados por
    comas. Para cada clave, encuentre el valor mínimo y el valor máximo que
    aparecen en todo el archivo. Retorne una lista de tuplas
    `(clave, mínimo, máximo)` ordenada alfabéticamente por la clave.
    """
    stats = defaultdict(lambda: {"min": float("inf"), "max": float("-inf")})
    with gzip.open("data/data.csv.gz", "rt", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("\t")
            metrics_str = parts[4]
            for pair in metrics_str.split(","):
                k, v = pair.split(":")
                v = int(v)
                if v < stats[k]["min"]:
                    stats[k]["min"] = v
                if v > stats[k]["max"]:
                    stats[k]["max"] = v
    return sorted([(k, v["min"], v["max"]) for k, v in stats.items()])
