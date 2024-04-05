from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    VALID_CLIMBERS = {'ArcticClimber': ArcticClimber, 'SummitClimber': SummitClimber}
    VALID_PEAKS = {'ArcticPeak': ArcticPeak, 'SummitPeak': SummitPeak}

    def __init__(self):
        self.climbers = []
        self.peaks = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.VALID_CLIMBERS:
            return f"{climber_type} doesn't exist in our register."
        try:
            current_climber = next(filter(lambda c: c.name == climber_name, self.climbers))
            return f"{current_climber.name} has been already registered."
        except StopIteration:
            new_climber = self.VALID_CLIMBERS[climber_type](climber_name)
            self.climbers.append(new_climber)
            return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.VALID_PEAKS:
            return f"{peak_type} is an unknown type of peak."
        new_peak = self.VALID_PEAKS[peak_type](peak_name, peak_elevation)
        self.peaks.append(new_peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear):
        missing_items = []
        try:
            current_climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        except StopIteration:
            pass

        try:
            current_peak = next(filter(lambda p: p.name == peak_name, self.peaks))
            recommended_gear = current_peak.get_recommended_gear()
        except StopIteration:
            pass

        for item in recommended_gear:
            if item not in gear:
                current_climber.is_prepared = False
                missing_items.append(item)

        if not missing_items:
            return f"{climber_name} is prepared to climb {peak_name}."
        return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted(missing_items))}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        try:
            current_climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        except StopIteration:
            return f"Climber {climber_name} is not registered yet."

        try:
            current_peak = next(filter(lambda p: p.name == peak_name, self.peaks))
        except StopIteration:
            return f"Peak {peak_name} is not part of the wish list."

        if current_climber.can_climb() and current_climber.is_prepared:
            current_climber.climb(current_peak)
            current_climber.conquered_peaks.append(current_peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {current_peak.difficulty_level}."

        if not current_climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        else:
            current_climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        total_conquered_peaks = []
        for climber in self.climbers:
            for peak in climber.conquered_peaks:
                if peak not in total_conquered_peaks:
                    total_conquered_peaks.append(peak)

        climbers_stat = []
        sorted_climbers = sorted(self.climbers, key=lambda p: (-len(p.conquered_peaks), p.name))
        for climber in sorted_climbers:
            if climber.conquered_peaks:
                climbers_stat.append(climber.__str__())

        message = f"Total climbed peaks: {len(total_conquered_peaks)}\n"
        message += f"**Climber's statistics:**\n"
        message += '\n'.join(climbers_stat)
        return message
