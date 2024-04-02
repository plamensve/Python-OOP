from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    PORTION = 200  # 200 GRAMS

    def __init__(self, name, price):
        super().__init__(name, self.PORTION, price)

    def details(self):
        return f"Gingerbread {self.name}: 200g - {self.price:.2f}lv."