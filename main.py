with open("/home/abubu/workspace/github.com/FelipeLundgren/bookbot/books/frankenstein.txt") as f:
    file_contents = f.read()


words = len(file_contents.split())




count_lower = file_contents.lower()
dicionario = {}

for i in count_lower:
    if i in dicionario:
        dicionario[i] += 1
    else:
        dicionario[i] = 1
dicionario_alpha ={}
for char, count in dicionario.items():
    if char.isalpha():
        dicionario_alpha[char] = count
dicionario_ordem = sorted(dicionario_alpha.items(), key=lambda x: x[1], reverse=True)

print(f"--- Begin report of frankenstein.txt ---")
print(f"{words} words found in the document")

for char, count in dicionario_ordem:
    print(f"the '{char}' character was found {count} times")

print("--- End report ---")





