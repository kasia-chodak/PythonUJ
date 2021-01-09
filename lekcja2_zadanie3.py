from collections import defaultdict
przestankowe = ['.', ',', ':', ';', '!', '?', '...', '–', '—', '-']

ciag = input("Wpisz ciąg znaków: ")

for znak in przestankowe :
    ciag = ciag.replace(znak, ' ')

words = ciag.split(' ')
words = list(filter(lambda x : len(x) > 0, words)) #jeżeli istnieją 'puste' elementy, to je usuwam

print(f"Ilość słów wynosi: {len(words)}")

length = 0
for word in words :
    length += len(word)

print(f"Ilość znaków wynosi: {length}")

letter_count = defaultdict(int)

for letter in ciag :
    letter_count[letter.lower()] += 1 #funkcja .lower() zmienia uppercase na lowercase

del letter_count[' '] #usuwam obliczone spacje (niepotrzebne)

print(f"Statystyka występowania znaków: {dict(letter_count)}")