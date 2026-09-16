
from character import Character


nova = Character("Nova", 100, 50)
bolt = Character("Bolt", 80, 75)

characters = [nova, bolt]

current_character = None


print("================================")
print("      RPG CHARACTER MANAGER")
print("================================")

while current_character is None:
    print("\nChoose a character:")

    for i, character in enumerate(characters, start=1):
        print(f"{i}. {character.name}")

    choice = input("> ")

    if choice == "1":
        current_character = nova
    elif choice == "2":
        current_character = bolt
    else:
        print("Invalid character selection. Please choose 1 or 2.")


while True:
    print("\n================================")
    print(f"Current Character: {current_character.name}")
    print("================================")
    print("1. Take Damage")
    print("2. Heal")
    print("3. Use Energy")
    print("4. Level Up")
    print("5. Rest")
    print("6. Show Status")
    print("7. Switch Character")
    print("8. Quit")

    command = input("\nChoose an action: ")

    if command == "1":
        try:
            amount = int(input("How much damage? "))
            current_character.take_damage(amount)
        except ValueError:
            print("Please enter a valid number.")

    elif command == "2":
        try:
            amount = int(input("How much should they heal? "))
            current_character.heal(amount)
        except ValueError:
            print("Please enter a valid number.")

    elif command == "3":
        try:
            amount = int(input("How much energy should they use? "))
            current_character.use_energy(amount)
        except ValueError:
            print("Please enter a valid number.")

    elif command == "4":
        current_character.level_up()

    elif command == "5":
        current_character.rest()

    elif command == "6":
        current_character.show_status()

    elif command == "7":
        print("\nChoose a character:")

        for i, character in enumerate(characters, start=1):
            print(f"{i}. {character.name}")

        choice = input("> ")

        if choice == "1":
            current_character = nova
            print("Switched to Nova.")
        elif choice == "2":
            current_character = bolt
            print("Switched to Bolt.")
        else:
            print("Invalid character selection.")

    elif command == "8":
        print("Thanks for playing!")
        break

    else:
        print("Invalid command. Please choose an option from 1 to 8.")

