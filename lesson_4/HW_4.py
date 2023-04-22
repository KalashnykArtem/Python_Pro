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
        count_ = 0
        for player in team:
            count_ += 1
            print(f"Player № {count_}: {player}")
    else:
        list_ = []
        for player in team:
            list_.append(player.get(field))
        print(f"List of players by {field}: {list_}")


def players_add():
    pl_name = str(input("Enter player name: "))
    pl_age = int(input("Enter player age: "))
    pl_numb = int(input("Enter player number: "))
    list_numb = []
    for player in team:
        list_numb.append(player.get("number"))
    if pl_numb in list_numb:
        print(f"Player with number № {pl_numb} already exists")
    else:
        new_pl = {"name": pl_name, "age": pl_age, "number": pl_numb}
        team.append(new_pl)
        print("Player added")
        print(new_pl)


def players_del():
    num_player = int(input("Enter number of player: "))
    list_ = []
    for player in team:
        list_.append(player.get("number"))
    if num_player not in list_:
        print(f"Player with number № {num_player} does not exists")
    else:
        for player in team:
            if num_player == player.get("number"):
                team.remove(player)
                print(f"Player with number № {num_player} is removed")
                print(f"Line-up: {team}")


def players_find():
    opt = list(team[0].keys())
    search_field = input(f"Enter a search field {opt}: ")
    search_word = input("Enter a search word: ")
    for player in team:
        if search_word == str(player[search_field]):
            print(player)
    list_word = []
    for player in team:
        list_word.append(player.get(search_field))
    if search_word not in list_word:
        print("There is not player in the list")


def players_get_by_name() -> dict:
    """If multiple players with same name - return the first one."""
    search_name = input("Enter a search name: ")
    for player in team:
        if search_name == str(player["name"]):
            print(player)
            break
    list_name = []
    for player in team:
        list_name.append(player.get("name"))
    if search_name not in list_name:
        print("There is not player in the list")


def main():
    options = ["repr", "add", "del", "find", "get", "exit"]
    while True:
        user_input = input(f"Enter your choice {options}: ")
        if not (user_input):
            break
        if user_input == "repr":
            players_repr()
        if user_input == "add":
            players_add()
        if user_input == "del":
            players_del()
        if user_input == "find":
            players_find()
        if user_input == "get":
            players_get_by_name()
        if user_input == "exit":
            break


if __name__ == "__main__":
    main()
