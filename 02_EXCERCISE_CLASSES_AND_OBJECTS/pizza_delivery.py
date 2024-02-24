class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict, ordered=False):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = ordered

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if not self.ordered:

            if ingredient in self.ingredients.keys():
                self.ingredients[ingredient] += quantity
                self.price += quantity * price_per_quantity

            else:
                self.ingredients[ingredient] = quantity
                self.price += quantity * price_per_quantity
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if not self.ordered:

            if ingredient not in self.ingredients.keys():
                return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

            elif ingredient in self.ingredients.keys() and self.ingredients[ingredient] < quantity:
                return f"Please check again the desired quantity of {ingredient}!"

            else:
                self.ingredients[ingredient] -= quantity
                self.price -= quantity * price_per_quantity
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def make_order(self):
        self.ordered = True
        ingredients_ordered = []

        for k, v in self.ingredients.items():
            ingredients_ordered.append(f'{k}: {v}')

        return f"You've ordered pizza {self.name} prepared with {', '.join(ingredients_ordered)} and the price will be {self.price}lv."


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})    # -> instance of PizzaDelivery
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
