with open("./Input/Letters/starting_letter.txt") as f:
    sample_content = f.read()

with open("./Input/Names/invited_names.txt") as n:
    names = n.readlines()
for name in names:
    stripped_name = name.strip()
    invitees = sample_content.replace("[name]", f"{stripped_name}")
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as n:
        n.write(invitees)
