from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    PROTECTION = 90
    PRICE = 25.0
    INCREASING_PRICE = 0.1
    TYPE_ = 'ElbowPad'

    def __init__(self):
        super().__init__(protection=self.PROTECTION, price=self.PRICE)

    def increase_price(self):
        self.price = self.price + (self.price * self.INCREASING_PRICE)
