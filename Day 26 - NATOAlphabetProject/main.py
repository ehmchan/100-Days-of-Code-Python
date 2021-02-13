import pandas

#TODO 1. Create a dictionary in this format {"A": "Alfa", "B": "Bravo"}:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter:row.code for (index, row) in data.iterrows()}
# print(alphabet)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# converting = True
# while converting:
#     word = input("Enter a word: ").upper()
#     try:
#         phonetic_code = [alphabet[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         converting = True
#     else:
#         print(phonetic_code)
#         converting = False

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        phonetic_code = [alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_code)

generate_phonetic()
