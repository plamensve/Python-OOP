from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []  # contains all players

    def add_player(self, player: Player):
        try:
            player = next(filter(lambda p: p == player, self.__players))
            return f"Player {player.name} has already joined"
        except StopIteration:
            self.__players.append(player)
            return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        try:
            player = next(filter(lambda p: p.name == player_name, self.__players))
            self.__players.remove(player)
            return player
        except StopIteration:
            return f"Player {player_name} not found"