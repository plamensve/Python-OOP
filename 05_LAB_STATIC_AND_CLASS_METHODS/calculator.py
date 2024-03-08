from functools import reduce


class Calculator:

    @staticmethod
    def add(*nums):
        return sum(nums)

    @staticmethod
    def multiply(*nums):
        return reduce(lambda x, y: x * y, nums)

    @staticmethod
    def divide(*nums):
        return reduce(lambda x, y: x / y, nums)

    @staticmethod
    def subtract(*nums):
        return reduce(lambda x, y: x - y, nums)


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
