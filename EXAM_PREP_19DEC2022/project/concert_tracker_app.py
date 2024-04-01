from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIANS = {'Guitarist': Guitarist, 'Drummer': Drummer, 'Singer': Singer}

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIANS:
            raise ValueError("Invalid musician type!")
        try:
            musician = next(filter(lambda m: m.name == name, self.musicians))
            raise Exception(f"{name} is already a musician!")
        except StopIteration:
            pass

        new_musician = self.VALID_MUSICIANS[musician_type](name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        try:
            band = next(filter(lambda b: b.name == name, self.bands))
            raise Exception(f"{name} band is already created!")
        except StopIteration:
            pass

        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        try:
            concert = next(filter(lambda c: c.place == place, self.concerts))
            raise Exception(f"{place} is already registered for {genre} concert!")
        except StopIteration:
            pass

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        try:
            musician = next(filter(lambda m: m.name == musician_name, self.musicians))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician = next(filter(lambda m: m.name == musician_name, band.members))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        valid_members_for_the_concert = {'Singer': False, 'Drummer': False, 'Guitarist': False}
        band = next(filter(lambda b: b.name == band_name, self.bands))
        concert = next(filter(lambda c: c.place == concert_place, self.concerts))

        for member in band.members:
            for k, v in valid_members_for_the_concert.items():
                if member.TYPE_ == k:
                    valid_members_for_the_concert[k] = True

        for values in valid_members_for_the_concert.values():
            if not values:
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        validation_band_can_play = {'Rock':
            {
                'Drummer': 'play the drums with drumsticks',
                'Singer': 'sing high pitch notes',
                'Guitarist': 'play rock',
            },

            'Metal':
                {
                    'Drummer': 'play the drums with drumsticks',
                    'Singer': 'sing low pitch notes',
                    'Guitarist': 'play metal',
                },

            'Jazz':
                {
                    'Drummer': 'play the drums with drum brushes',
                    'Singer': 'sing high pitch notes and sing low pitch notes',
                    'Guitarist': 'play jazz',
                }
        }
        concert_genre = concert.genre
        skills = []
        for member in band.members:
            skills.append(', '.join(member.skills))

        for k, v in validation_band_can_play[concert_genre].items():
            if v not in skills:
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert_genre} concert in {concert_place}."
