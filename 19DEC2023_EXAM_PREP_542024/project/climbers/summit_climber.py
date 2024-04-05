from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    INITIAL_STRENGTH = 150

    def __init__(self, name: str):
        super().__init__(name, strength=self.INITIAL_STRENGTH)

    def can_climb(self):
        if self.strength >= 75:
            return True
        else:
            return False

    def climb(self, peak: BasePeak):
        peak_level = peak.calculate_difficulty_level()
        if self.can_climb() and self.is_prepared:
            if peak_level == 'Extreme':
                self.strength -= 30 * 2.5
            elif peak_level == 'Advanced':
                self.strength -= 30 * 1.3