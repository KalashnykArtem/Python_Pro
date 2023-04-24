team = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Marry", "age": 33, "number": 3},
    {"name": "Cavin", "age": 33, "number": 12},
    {"name": "John", "age": 30, "number": 10},
]


def players_repr():
    opt = list(team[0].keys())
    field = str(input(f"Enter your choice {opt} or all information: "))
    if field == "all information":
        players_amount = 0
        for player in team:
            players_amount += 1
            print(f"Player № {players_amount}: {player}")
    else:
        fields = []
        for player in team:
            fields.append(player.get(field))
        print(f"List of players by {field}: {fields}")


def players_add():
    pl_name = input("Enter player name: ")
    pl_age = int(input("Enter player age: "))
    pl_numb = int(input("Enter player number: "))
    for player in team:
        if player["number"] == pl_numb:
            print(f"Player with number № {pl_numb} already exists")
            break
        else:
            new_pl = {"name": pl_name, "age": pl_age, "number": pl_numb}
            team.append(new_pl)
            print("Player added")
            print(new_pl)
            break


def players_del():
    num_player = int(input("Enter number of player: "))
    for player in team:
        if num_player != player["number"]:
            print(f"Player with number № {num_player} does not exists")
            break
        else:
            team.remove(player)
            print(f"Player with number № {num_player} is removed")
            print(f"Line-up: {team}")
            break


def players_find():
    opt = list(team[0].keys())
    search_field = input(f"Enter a search field {opt}: ")
    search_word = input("Enter a search word: ")
    for player in team:
        if search_word == str(player[search_field]):
            print(player)
        else:
            print("There is not player in the list")


def players_get_by_name() -> dict:
    """If multiple players with same name - return the first one."""
    search_name = input("Enter a search name: ")
    for player in team:
        if search_name == str(player["name"]):
            print(player)
            break
        else:
            print("There is not player in the list")
            break


def main():
    options = ["repr", "add", "del", "find", "get", "exit"]
    while True:
        user_input = input(f"Enter your choice {options}: ")
        if not (user_input):
            break
        elif user_input == "repr":
            players_repr()
        elif user_input == "add":
            players_add()
        elif user_input == "del":
            players_del()
        elif user_input == "find":
            players_find()
        elif user_input == "get":
            players_get_by_name()
        elif user_input == "exit":
            break


if __name__ == "__main__":
    main()
