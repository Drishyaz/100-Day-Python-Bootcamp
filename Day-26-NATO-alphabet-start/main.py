# WHEN SPELLING OUT A WORD ON THE PHONE SOME LETTERS CAN BE CONFUSED WITH THE OTHER.
# FOR EXAMPLE, 'T' WITH A 'D' OR 'J' WITH A 'G'
# SO THE NATO PHONETIC CODES ARE USED TO NAME A WORD WITH THAT LETTER TO GET THE CALLER ON THE OTHER SIDE
# UNDERSTAND IT. SO IF THE WORD IS JOY,THE CODES ARE ['Juliet', 'Oscar', 'Yankee']

# LONGER AND SIMPLER VERSION
# import pandas
# data = pandas.read_csv("nato_phonetic_alphabet.csv")        # this is a dataframe
# # TODO 1. Create a dictionary in this format:
# # {"A": "Alfa", "B": "Bravo"}
# data_dict = {}
# for (index, row) in data.iterrows():
#     data_dict[row.letter] = row.code
# print(data_dict)
#
# # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# word = input("Type your word: ").upper()
# phonetic_codes = []
# for letter in word:
#     code_word = data_dict[letter]
#     phonetic_codes.append(code_word)
# print(phonetic_codes)

# SHORTER AND COMPLEX VERSION
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")        # this is a dataframe

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(data_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Type your word: ").upper()
phonetic_codes = [data_dict[letter] for letter in word]
print(phonetic_codes)