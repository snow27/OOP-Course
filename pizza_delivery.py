class PizzaDelivery:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if not self.ordered:
            extra_price = quantity * ingredient_price
            if ingredient not in self.ingredients:
                self.ingredients[ingredient] = quantity
            else:
                self.ingredients[ingredient] += quantity
            self.price += extra_price
        return f"Pizza {self.name} already prepared and we can't make any changes!"

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if not self.ordered:
            extra_price = quantity * ingredient_price
            if ingredient not in self.ingredients:
                return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
            elif ingredient in self.ingredients:
                if self.ingredients[ingredient] < quantity:
                    return f"Please check again the desired quantity of {ingredient}!"
                else:
                    self.ingredients[ingredient] -= quantity
                    self.price -= extra_price
        return f"Pizza {self.name} already prepared and we can't make any changes!"

    def make_order(self):
        self.ordered = True
        products = []
        for key in self.ingredients:
            products.append(f"{key}: {self.ingredients[key]}")
        return f"You've ordered pizza {self.name} prepared with {', '.join(products)} and the price will be {self.price}lv."



