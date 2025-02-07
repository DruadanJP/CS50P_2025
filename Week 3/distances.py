favoriteGames = [
    {"name": "Zero Escape: Zero Time Dilemma", "date" : "Jun 28, 2026", "Producer": "Spike Chunsoft"},
    {"name": "Elden Ring", "date" : "Feb 25, 2022", "Producer": "From Software"},
    {"name": "Yakuza 0", "date" : "March 12, 2015", "Producer": "Sega Games"},
]

def main():
    for games in favoriteGames:
        print("The name of the Game is", games["name"])


main()