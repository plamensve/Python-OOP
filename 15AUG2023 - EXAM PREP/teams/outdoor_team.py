from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    INITIAL_BUDGET = 1000.0
    TYPE_ = 'OutdoorTeam'

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=self.INITIAL_BUDGET)

    def win(self):
        self.wins += 1
        self.advantage += 115

    def sum_points(self):
        advantage = self.advantage
        protection = sum(p.protection for p in self.equipment)
        return advantage + protection
