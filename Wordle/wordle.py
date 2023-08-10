from nltk.corpus import gutenberg
from collections import Counter
import random
from termcolor import colored

text = gutenberg.words()
common_words = Counter(text).most_common(1000)
words = [word[0] for word in common_words if len(word[0]) == 5]
picked_word = random.choice(words)
letters_true = [word for word in picked_word]
guessed_letters = ["_|"] * len(picked_word)

print("Try to see if you can guess the word:")
while True:
    to_print = ["|"] + guessed_letters
    print("|", *guessed_letters, sep="")
    guess = input("")
    if len(guess) != len(picked_word): continue
    letters_guessed = [word for word in guess.lower()]
    for i, (lt, lg) in enumerate(zip(letters_true, letters_guessed)):
        if lt == lg: guessed_letters[i] = colored(lt, "green")
        elif lg in letters_true: guessed_letters[i] = colored(lg, "yellow")
        else: guessed_letters[i] = lg
        guessed_letters[i] += "|"
    if guess.lower() == picked_word.lower(): break

print("Congrats! You guessed the word!")
print("|", *guessed_letters, sep="")