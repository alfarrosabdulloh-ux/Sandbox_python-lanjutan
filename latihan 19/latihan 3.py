import re

teks = "python adalah bahasa yang menyenangkan, python mudah dipelajari."

# re.search
hasil_search = re.search("python", teks)
print("re.search:", hasil_search.group())

# re.findall
hasil_findall = re.findall("python", teks)
print("re.findall:", hasil_findall)
