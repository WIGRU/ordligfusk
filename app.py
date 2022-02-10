from random import randint

with open("ord.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

wordlist = []
for word in lines:
    if not "-" in word and len(word.strip()) == 5 and not word[0].isupper():
        wordlist.append(word.strip())


# Count how many times each letter appears
letter_count = {}
for word in wordlist:
    for letter in word:
        if letter in letter_count.keys():
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

print(letter_count)

# Calculate score for each letter
letter_score = {}
for letter in letter_count:
    score = round(letter_count[letter] / list(letter_count.items())[0][1], 2)
    letter_score[letter] = score

# Calculate score for each word
wordlist_score = {}
for word in wordlist:
    score = 0
    letters = set(word) # remove "double" point for two of the same letter
    for letter in letters:
        score += letter_score[letter]
    wordlist_score[word] = round(score, 2)

wordlist_score = dict(sorted(wordlist_score.items(), reverse=True, key=lambda item: item[1]))

print(list(wordlist_score)[randint(0, len(wordlist_score) - 1)])

def remove_word_with_letter(wordlist, letters_to_remove):
    if letters_to_remove[0] != "":
        to_remove = []
        to_remove = set()
        for word in wordlist:
            for letter in letters_to_remove:
                if letter in word:
                    to_remove.add(word)
        for word in to_remove:
            wordlist.pop(word)
    return wordlist


def checkpos(wordlist, letters):
    if len(letters) != 0:
        to_remove = []
        for word in wordlist:
            rem = False
            for letter in letters:
                if letter[1] not in word or letter[1] == word[int(letter[0]) + 1]:
                    rem = True
            if rem:
                to_remove.append(word)
        for word in to_remove:
            wordlist.pop(word)
    
    return wordlist


def correctLetter(wordlist, letters):
    if len(letters) != 0:
        to_remove = []
        for word in wordlist:
            rem = False
            for letter in letters:
                if letter[1] != word[int(letter[0]) + 1]:
                    rem = True
            if rem:
                to_remove.append(word)
        for word in to_remove:
            wordlist.pop(word)
    
    return wordlist

letters_to_remove = []
correct_letter_wrong_pos = []
correct_letter = []

while True:
    print(f"try: {list(wordlist_score)[0]}")

    ltr = input("Wrong letters (abc...): ")
    for i in ltr:
        letters_to_remove.append(i.strip())
    wordlist_score = remove_word_with_letter(wordlist_score, letters_to_remove)

    clwp = input("Correct letters wrong position (ex 1a2b...): ")
    for i in range(0, len(clwp), 2):
        correct_letter_wrong_pos.append((clwp[i], clwp[i + 1]))
    wordlist_score = checkpos(wordlist_score, correct_letter_wrong_pos)

    clrp = input("Correct letters (ex 1a2b...): ")
    for i in range(0, len(clrp), 2):
        correct_letter.append((clrp[i], clrp[i + 1]))
    wordlist_score = correctLetter(wordlist_score, correct_letter)