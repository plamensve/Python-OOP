from abc import ABC

from formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam, ABC):
    EXPENSES_PER_RACE = 250_000
    earns_by_sponsors = 0
    total = earns_by_sponsors - EXPENSES_PER_RACE

    sponsors = {
        'Petronas': {
            1: 1_000_00,
            2: 1_000_000,
            3: 500_000
        },
        'TeamViewer': {
            5: 100_000,
            6: 100_000,
            7: 50_000
        }
    }

    def calculate_revenue_after_race(self, race_pos: int):
        if race_pos in MercedesTeam.sponsors['Petronas']:
            MercedesTeam.earns_by_sponsors += MercedesTeam.sponsors['Petronas'][race_pos]

        if race_pos in MercedesTeam.sponsors['TeamViewer']:
            MercedesTeam.earns_by_sponsors += MercedesTeam.sponsors['Honda'][race_pos]

        if race_pos < 5:
            MercedesTeam.earns_by_sponsors += MercedesTeam.sponsors['TeamViewer'][5]

        return f"The revenue after the race is {self.earns_by_sponsors}$. Current budget {self.total}$"