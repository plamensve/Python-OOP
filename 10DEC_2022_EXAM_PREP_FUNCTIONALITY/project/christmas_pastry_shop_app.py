from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACY = {'Gingerbread': Gingerbread, 'Stolen': Stolen}
    VALID_BOOTH = {'Open Booth': OpenBooth, 'Private Booth': PrivateBooth}

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        try:
            current_delicacy = next(filter(lambda d: d.name == name, self.delicacies))
            raise Exception(f"{name} already exists!")
        except StopIteration:
            pass

        if type_delicacy not in self.VALID_DELICACY:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        new_delicacy = self.VALID_DELICACY[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {new_delicacy.name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        try:
            current_booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
            raise Exception(f"Booth number {booth_number} already exists!")
        except StopIteration:
            pass

        if type_booth not in self.VALID_BOOTH:
            raise Exception(f"{type_booth} is not a valid booth!")

        new_booth = self.VALID_BOOTH[type_booth](booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        try:
            current_booth = next(filter(lambda b: b.capacity >= number_of_people and b.is_reserved == False, self.booths))
        except StopIteration:
            raise Exception(f"No available booth for {number_of_people} people!")

        current_booth.reserve(number_of_people)
        return f"Booth {current_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        try:
            current_booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            current_delicacy = next(filter(lambda d: d.name == delicacy_name, self.delicacies))
        except StopIteration:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        current_booth.delicacy_orders.append(current_delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        current_booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        total_sum = 0
        total_sum += current_booth.price_for_reservation

        for order in current_booth.delicacy_orders:
            total_sum += order.price

        self.income += total_sum

        current_booth.delicacy_orders = []
        current_booth.is_reserved = False
        current_booth.price_for_reservation = 0
        message = f"Booth {booth_number}:\n"
        message += f"Bill: {total_sum:.2f}lv."
        return message

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
