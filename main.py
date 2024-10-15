with open("/home/abubu/workspace/github.com/FelipeLundgren/bookbot/books/frankenstein.txt") as f:
    file_contents = f.read()

print(file_contents)
words = len(file_contents.split())

print(f"total de palavras no texto é de: {words}")