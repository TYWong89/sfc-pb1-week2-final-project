"""
Week 2 Final Project - Starter Code
Console Application Template

This is a basic structure to get you started. Modify it for your project!
"""

from data_handler import load_game, save_game
from game_logic import explore, rest


def main():
    print("Your quest: collect 10 gold. You can keep playing afterward.")
    player = load_game()

    while True:
        print(f"\nHealth: {player['health']}/10 | Gold: {player['gold']}")
        print("1. Explore the forest")
        print("2. Rest at camp")
        print("3. Save progress")
        print("4. Quit without saving")


        choice = input("Choose 1-4: ").strip().lower()

        if choice == "1":
            explore(player)

        elif choice == "2":
            rest(player)

        elif choice == "3":
            save_game(player)
            
        elif choice == "4":
            print("Thanks for playing. Goodbye!")
            break
        else:
            print("Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()