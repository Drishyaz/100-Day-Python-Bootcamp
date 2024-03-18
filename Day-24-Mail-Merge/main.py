
# GET THE NAMES FROM THE invited_names.txt FILE
with open("./Input/Names/invited_names.txt", "r") as f1:
    names = f1.readlines()

# REPLACE THE name VALUE IN THE starting_letter.txt
with open("./Input/Letters/starting_letter.txt", "r+") as f2:
    content = f2.read()
    for name in names:
        name = name.strip()
        new_content = content.replace("[name]", name)
        # SAVE THE NEW content AS NEW FILE UNDER THE ReadyToSend DIRECTORY
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as f3:
            f3.write(new_content)
