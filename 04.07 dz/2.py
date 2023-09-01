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
            #VN: здесь ещё можно сделать проверку такую:
            # если char == последней букве в current_syllable и в current_syllable всего одна буква
            # то значит, мы наткнулись на сдвоенную согласную, и char нужно не к current_syllable приписать,
            # а к последнему слогу в syllables
            current_syllable += char

    if current_syllable:
        syllables.append(current_syllable)

    return syllables

with open("input.txt", "r", encoding="utf-8") as f:
    words = f.read().splitlines()
with open("output.txt", "w", encoding="utf-8") as f:
    for word in words:
        syllables = syllabify(word)
        #VN: Слова нужно очищать от пробелов в начале и конце, иначе получается лишний дефис: "а-рбу-зы-"
        syllable_str = "-".join(syllables)
        f.write(syllable_str + "\n")

print("Слова разбиты на слоги и сохранены в output.txt")
