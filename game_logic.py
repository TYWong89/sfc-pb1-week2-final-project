import random


def explore(player):
    if player["health"] == 0:
        while True:
            answer = input(
            "You have 0 health. Exploring will kill you. Continue? (y/n): "
        ).strip().lower()

            if answer == "y":
                print("You should have rested. You kept exploring with 0 health.")
                print("Now you're dead. Game over!")
                return False

            if answer == "n":
                print("You wisely return to camp. Choose Rest to recover.")
                return True

            print("Please enter y or n.")

    gold_before = player["gold"]

    event = random.choice([
        "treasure",
        "goblin",
        "wolf",
        "thorn_bush",
        "spider",
        "quiet",
        "health_potion"
    ])

    if event == "treasure":
        player["gold"] += 2
        print("You find a treasure chest! You gain 2 gold.")

    elif event == "goblin":
        player["health"] = max(0, player["health"] - 2)
        player["gold"] += 3
        print("You defeat a goblin! You lose 2 health and gain 3 gold.")

    elif event == "health_potion":
        player["health"] = max(0, player["health"] + 1)
        player["health"] += 1
        print("You found a potion! You recover 1 health.")

    elif event == "wolf":
        player["health"] = max(0, player["health"] - 4)
        player["gold"] += 1
        print("A wolf attacks! You fight back and lose 4 health and gain 1 gold.")

    elif event == "thorn_bush":
        player["health"] = max(0, player["health"] - 1)
        print("You walk through thorny bushes and lose 1 health.")

    elif event == "spider":
        player["health"] = max(0, player["health"] - 1)
        print("A spider bit you! You lose 1 health.")

    else:
        print("You follow a quiet forest path. Nothing happens.")

    if gold_before < 10 and player["gold"] >= 10:
        print("Quest complete! You collected 10 gold!")


def rest(player):
    player["health"] = 10
    print("You rest at camp. Your health is back to 10.")