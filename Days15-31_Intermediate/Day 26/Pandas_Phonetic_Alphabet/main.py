import pandas
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {}

#Creates a dictionary from the csv file that includes all the alphabet and their codes.
for(index,row) in nato_alphabet.iterrows():
    alphabet_dict.update({row.letter:row.code})

# Asks the user to enter a word to convert. It then converts the word to phonetic alphabet.
convert = True
while convert is True:
    user_input = input("Enter a word to convert to the nato alphabet: ").upper()
    user_list = list(user_input)
    phonetic_output = [alphabet_dict[value] for value in user_list if value in alphabet_dict.keys()]
    print(phonetic_output)

    continue_or_stop = ''
    while continue_or_stop != "Y" and continue_or_stop != "N":
        continue_or_stop = input("Continue? (Y/N) ").upper()
        if continue_or_stop == "N":
            print("Thank you for using the phonetic word generator!")
            convert = False
        if continue_or_stop == "Y":
            pass
