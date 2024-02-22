class SteamUser:
    def __init__(self, username, games, played_hours=0):
        self.username = username
        self.games = games
        self.played_hours = played_hours

    def play(self, game, hours):
        if game in self.games:
            self.played_hours += hours
            self.games[game] += 1
            return f"{self.username} is playing {game}"
        return f"{game} is not in library"

    def buy_game(self, game):
        if game not in self.games:
            self.games.append(game)
            return f"{self.username} bought {game}"
        return f"{game} is already in your library"

    def status(self):
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"

    def games_info(self):
        games = ''
        games += ', '.join(map(str, self.games))
        return games


user = SteamUser("Peter", {"Rainbow Six Siege": 0, "CS:GO": 0, "Fortnite": 0})
user2 = SteamUser("John", ["Valorant", "Diablo", "Age of Empires"])
print(user.buy_game("Valorant"))
print(user.buy_game("Diablo"))
print(user.buy_game("Age of Empires"))
print(user2.buy_game("Rainbow Six Siege"))
print(user2.buy_game("CS:GO"))
print(user2.buy_game("Fortnite"))
print(user.games_info())
print(user2.games_info())
