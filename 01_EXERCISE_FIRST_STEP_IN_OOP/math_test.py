class MathTest:
    def __init__(self, *args):
        self.args = args

    def multiply(self):
        return self.args[0] * self.args[1]

    def divide(self):
        return self.args[0] // self.args[1]

    def subtraction(self):
        return self.args[0] - self.args[1]

    def add(self):
        return self.args[0] + self.args[1]

