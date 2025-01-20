#Reads the letter template into a variable
with open("Input/Letters/starting_letter.txt", 'r') as file:
    letter_template = file.read()
#Reads the names into a file
with open("Input/Names/invited_names.txt", 'r') as file:
    names = file.readlines()

#Removes the extra line breaks in the names file by going through each item in the list one by one.
names = [name.replace('\n','') for name in names]

# Create a list of letters from the letter_template by removing the [name] placeholder and replacing it with the
# actual name.
letters = [letter_template.replace("[name]", names[i])for i in range(len(names)-1)]

#Creates new files for each letter.
for i in range (len(letters)-1):
    with open(f"Output/ReadyToSend/{names[i]}_invite.txt", 'w') as file:
        file.write(letters[i])
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp