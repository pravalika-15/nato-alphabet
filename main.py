import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dic = {row.letter: row.code for (index, row) in data.iterrows()}
game_on = True
while game_on:
    word = input("enter the word: ").upper()
    try:
        phonetic_list = [phonetic_dic[letter] for letter in word]
    except KeyError:
        print('sorry, only alphabets please!')
    else:
        print(phonetic_list)
        game_on = False

