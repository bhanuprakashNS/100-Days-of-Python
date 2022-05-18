# ................ NATO Alphabet code word ................................ #
# ............. Created and modified by N.S.Bhanuprakash on 04-04-2022 .....#
import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_alphabet_data = {data.letter: data.code for (index, data) in nato_data.iterrows()}
# print(NATO_alphabet_data)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def create_code_word():
    user_input = input("What's your word?\n").upper()
    try:
        user_code = [NATO_alphabet_data[letter] for letter in user_input]
        print(user_code)
    except KeyError:
        print("Please enter only NATO alphabets")
        create_code_word()


create_code_word()





