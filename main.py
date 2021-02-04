#TODO: Create a letter using starting_letter.txt

names = open("./Input/Names/invited_names.txt", mode="r").readlines()
print(names)

# for each name in invited_names.txt
new_names = []
for name in names:
    new_name = name.strip("\n")
    new_names.append(new_name)

# Replace the [name] placeholder with the actual name.
for name in new_names:
    with open("./Input/Letters/starting_letter.txt", mode="r") as infile:
        infile_data = infile.read()
    infile_data = infile_data.replace("[name]", name)

    # Save the letters in the folder "ReadyToSend".
    with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode="w") as outfile:
        outfile.write(infile_data)

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
