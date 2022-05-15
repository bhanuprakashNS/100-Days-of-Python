# ................... Mail Merge Project .................................. #
# ............. Created and modified by N.S.Bhanuprakash on 01-04-2022 .....#

REPLACEMENT_TEXT = "[name]"

with open("./Input/Names/invited_names.txt") as invitee:
    names = invitee.readlines()
for name in names:
    name = name.strip()
    with open(f"./Output/ReadyToSend/{name}.txt", "a") as new_file:
        letter = open("./Input/Letters/starting_letter.txt", "r")
        lines = letter.read()
        new_file.write(lines.replace(REPLACEMENT_TEXT, name))
        letter.close()

        # Another method using "readlines" command ..............
        # lines = letter.readlines()
        # first_line = lines[0]
        # new_first_line = first_line.replace(REPLACEMENT_TEXT, name)
        # lines[0] = new_first_line
        # num = 0
        # for num in range(len(lines)):
        #     new_file.write(lines[num])
        # letter.close()
