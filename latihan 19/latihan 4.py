import re

kalimat = "Kucing, anjing, dan burung adalah hewan peliharaan."
kata_g = re.findall(r"\b\w+g\b", kalimat)
print(kata_g)
