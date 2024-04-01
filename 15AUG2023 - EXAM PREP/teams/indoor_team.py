from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    INITIAL_BUDGET = 500.0
    TYPE_ = 'IndoorTeam'

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=self.INITIAL_BUDGET)

    def win(self):
        self.wins += 1
        self.advantage += 145

    def sum_points(self):
        advantage = self.advantage
        protection = sum(p.protection for p in self.equipment)
        return advantage + protection
