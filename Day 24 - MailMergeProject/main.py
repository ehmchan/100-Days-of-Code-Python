#TODO: Create a letter using starting_letter.txt

PLACEHOLDER = "[name]"

names = open("./Input/Names/invited_names.txt", mode="r").readlines()

# for each name in invited_names.txt
stripped_names = []
for name in names:
    stripped_name = name.strip("\n")
    stripped_names.append(stripped_name)

# Replace the [name] placeholder with the actual name.
with open("./Input/Letters/starting_letter.txt", mode="r") as infile:
    infile_data = infile.read()
# Save the letters in the folder "ReadyToSend".
for stripped_name in stripped_names:
    outfile_data = infile_data.replace(PLACEHOLDER, stripped_name)
    with open(f"./Output/ReadyToSend/letter_to_{stripped_name}.txt", mode="w") as outfile:
        outfile.write(outfile_data)

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
