import pandas

#TODO 1. Create a dictionary in this format {"A": "Alfa", "B": "Bravo"}:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter:row.code for (index, row) in data.iterrows()}
# print(alphabet)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
phonetic_code = [alphabet[letter] for letter in word]
print(phonetic_code)

