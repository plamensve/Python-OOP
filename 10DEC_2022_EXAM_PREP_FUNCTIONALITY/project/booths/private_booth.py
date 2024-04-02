from project.booths.booth import Booth


class PrivateBooth(Booth):
    PRICE_PER_PERSON_TO_RESERVE_BOOTH = 3.50

    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        price_for_reservation = self.PRICE_PER_PERSON_TO_RESERVE_BOOTH * number_of_people
        self.price_for_reservation = price_for_reservation
        self.is_reserved = True
