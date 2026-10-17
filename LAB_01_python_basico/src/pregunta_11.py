import gzip
from collections import defaultdict
def pregunta_11():
    """
    La cuarta columna (`codes`) contiene letras minúsculas separadas por
    comas. Para cada una de esas letras, sume los valores de la segunda
    columna (`value`) de los registros en los que aparece. Retorne un
    diccionario `{letra: suma}` con las letras en orden alfabético.
    """
    sums = defaultdict(int)
    with gzip.open("data/data.csv.gz", "rt", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("\t")
            val = int(parts[1])
            codes = parts[3].split(",")
            for code in codes:
                sums[code] += val
    return dict(sorted(sums.items()))