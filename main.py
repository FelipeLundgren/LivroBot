with open("/home/abubu/workspace/github.com/FelipeLundgren/bookbot/books/frankenstein.txt") as f:
    file_contents = f.read()

print(file_contents)
words = len(file_contents.split())

print(f"total de palavras no texto é de: {words}")

def contador ()
    count_lower = file_contents.lower()
    dicionario = {}
    for i in count_lower:
        if i in dicionario:
            dicionario[i] += 1
        else:
            dicionario[i] = 1
    print(dicionario)

