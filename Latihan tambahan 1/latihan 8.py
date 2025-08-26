kalimat = input("Masukkan sebuah kalimat: ")
vokal = "aiueoAIUEO"

for huruf in kalimat:
    if huruf in vokal:
        continue
    print(huruf, end="")

print()
