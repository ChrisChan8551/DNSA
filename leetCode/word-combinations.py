import itertools
from nltk.corpus import words

# Download the words corpus if not already downloaded
import nltk
nltk.download('words')

# Define the letters to use
letters = 'knits'

# Load the list of English words
word_list = set(words.words())

# Generate all 6-letter permutations of the given letters
three = itertools.permutations(letters, 3)
four = itertools.permutations(letters, 4)
five = itertools.permutations(letters, 5)
six = itertools.permutations(letters, 6)

# Filter permutations to find valid English words
valid_words = set()

for perm in three:
    word = ''.join(perm)
    if word in word_list:
        valid_words.add(word)

for perm in four:
    word = ''.join(perm)
    if word in word_list:
        valid_words.add(word)

for perm in five:
    word = ''.join(perm)
    if word in word_list:
        valid_words.add(word)

for perm in six:
    word = ''.join(perm)
    if word in word_list:
        valid_words.add(word)

# Print valid words
for word in sorted(valid_words):
    print(word)
