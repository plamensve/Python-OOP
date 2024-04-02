from abc import ABC

from formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam, ABC):
    EXPENSES_PER_RACE = 250_000
    earns_by_sponsors = 0
    total = earns_by_sponsors - EXPENSES_PER_RACE

    sponsors = {
        'Oracle': {
            1: 1_500_00,
            2: 800_000
        },
        'Honda': {
            8: 20_000,
            9: 20_000,
            10: 10_000
        }
    }

    def calculate_revenue_after_race(self, race_pos: int):
        if race_pos in RedBullTeam.sponsors['Oracle']:
            RedBullTeam.earns_by_sponsors += RedBullTeam.sponsors['Oracle'][race_pos]

        if race_pos in RedBullTeam.sponsors['Honda']:
            RedBullTeam.earns_by_sponsors += RedBullTeam.sponsors['Honda'][race_pos]

        if race_pos < 8:
            RedBullTeam.earns_by_sponsors += RedBullTeam.sponsors['Honda'][8]

        return f"The revenue after the race is {self.earns_by_sponsors}$. Current budget {self.total}$"