def syllabify(word):
    vowels = 'aeiouаеёиоуыэюя'
    syllables = []
    current_syllable = ""

    for char in word:
        if char.lower() in vowels:
            current_syllable += char
            syllables.append(current_syllable)
            current_syllable = ""
        else:
            if current_syllable and current_syllable[-1] == char and len(current_syllable) == 1:
                syllables[-1] += char
            else:
                current_syllable += char

    if current_syllable:
        syllables.append(current_syllable)

    return syllables

with open("input.txt", "r", encoding="utf-8") as f:
    words = [word.strip() for word in f.readlines()]  
with open("output.txt", "w", encoding="utf-8") as f:
    for word in words:
        syllables = syllabify(word)
        syllable_str = "-".join(syllables)
        f.write(syllable_str + "\n")

print("Слова разбиты на слоги и сохранены в output.txt")
