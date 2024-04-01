from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT = {'KneePad': KneePad, 'ElbowPad': ElbowPad}
    VALID_TEAMS = {'OutdoorTeam': OutdoorTeam, 'IndoorTeam': IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT:
            raise Exception("Invalid equipment type!")
        new_equipment = self.VALID_EQUIPMENT[equipment_type]()
        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAMS:
            raise Exception("Invalid team type!")

        if len(self.teams) == self.capacity:
            return "Not enough tournament capacity."

        new_team = self.VALID_TEAMS[team_type](team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = next(filter(lambda t: t.name == team_name, self.teams))
        eq = next(filter(lambda e: e.TYPE_ == equipment_type, reversed(self.equipment)))

        if team.budget < eq.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(eq)
        team.equipment.append(eq)
        team.budget -= eq.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        try:
            team_for_remove = next(filter(lambda t: t.name == team_name, self.teams))
        except StopIteration:
            raise Exception("No such team!")

        if team_for_remove.wins > 0:
            raise Exception(f"The team has {team_for_remove.wins} wins! Removal is impossible!")

        self.teams.remove(team_for_remove)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        counter = 0
        for e in self.equipment:
            if e.TYPE_ == equipment_type:
                e.increase_price()
                counter += 1
        return f"Successfully changed {counter}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = next(filter(lambda t1: t1.name == team_name1, self.teams))
        team2 = next(filter(lambda t2: t2.name == team_name2, self.teams))
        if team1.TYPE_ != team2.TYPE_:
            raise Exception("Game cannot start! Team types mismatch!")
        team1_result = team1.sum_points()
        team2_result = team2.sum_points()

        if team1_result == team2_result:
            return "No winner in this game."

        if team1_result > team2_result:
            team1.win()
            return f"The winner is {team1.name}."

        if team2_result > team1_result:
            team2.win()
            return f"The winner is {team2.name}."

    def get_statistics(self):
        result = f"Tournament: {self.name}\n"
        result += f"Number of Teams: {len(self.teams)}\n"
        result += f"Teams:"
        team_info = []
        sorted_teams = sorted(self.teams, key=lambda team: -team.wins)
        for t in sorted_teams:
            team_info.append(t.get_statistics())
        for info in team_info:
            result += '\n' + info

        return result
