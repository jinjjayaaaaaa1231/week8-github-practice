def delete_participant():
    '''
    Deletes an existing participant
    '''

    with open("participants.txt", "r") as file:
        lines = file.readlines()

    if len(lines) == 0:
        print("No participants to delete.")
        return

    view_participants()

    choice = input("Enter the participant number to delete: ")
    if not choice.isdigit():
        print("Invalid selection.")
        return

    choice = int(choice)
    if choice < 1 or choice > len(lines):
        print("Invalid selection.")
        return

    removed = lines.pop(choice - 1)

    with open("participants.txt", "w") as file:
        file.writelines(lines)

    print("Participant deleted successfully!")
