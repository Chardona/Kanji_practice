import random

file = "kanji"
r_continue = ""
forgotten = []

with open(file, "r", encoding="utf-8") as f:
    content = f.read().split()
    while r_continue != "n":
        kanji = random.choice(content)
        print(kanji)
        r_correctness = input("correct? y/n\n")
        if r_correctness == 'n':
            forgotten.append(kanji)
        r_continue = input("continue? y/n\n")

    print(f"you have forgotten these kanji {forgotten}" if forgotten else "well done! You remember them all")
