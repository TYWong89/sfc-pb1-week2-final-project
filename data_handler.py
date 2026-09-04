import json
from pathlib import Path

SAVE_FILE = Path(__file__).with_name("save_game.json")


def load_game():
    if SAVE_FILE.exists():
        with SAVE_FILE.open("r", encoding="utf-8") as file:
            player = json.load(file)

        print("Saved adventure loaded!")
        return player

    print("Starting a new adventure!")
    return {"health": 10, "gold": 0}


def save_game(player):
    with SAVE_FILE.open("w", encoding="utf-8") as file:
        json.dump(player, file, indent=4)

    print("Progress saved!")