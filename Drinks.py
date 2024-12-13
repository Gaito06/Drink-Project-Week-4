from typing import List

class Drink:
    """
    A class to represent a drink with a base and a list of flavors.
    
    Attributes:
        base (str): The base of the drink (e.g., 'water', 'sbrite').
        flavors (List[str]): A list of added flavors to the drink.
    
    Methods:
        get_base: Returns the base of the drink.
        get_flavors: Returns the list of flavors in the drink.
        add_flavor: Adds a flavor to the drink if it is valid.
        set_flavors: Sets a list of flavors for the drink.
        get_total: Returns the total cost of the drink based on size and flavors.
        set_size: Allows changing the size of the drink.
    """
    
    # List of possible valid bases and flavors (these don't change)
    _valid_bases = ["water", "sbrite", "pokeacola", "Mr. Salt", "hill fog", "leaf wine"]
    _valid_flavors = ["lemon", "cherry", "strawberry", "mint", "blueberry", "lime"]
    
    # List of possible sizes and their associated prices
    _size_prices = {
        "small": 1.50,
        "medium": 1.75,
        "large": 2.05,
        "mega": 2.15
    }
    
    def __init__(self, base: str, size: str):
        if base.lower() in Drink._valid_bases:
            self._base = base.lower()  # Store base in lowercase
        else:
            raise ValueError("Invalid base")
        
        if size.lower() in Drink._size_prices:
            self._size = size.lower()  # Store size in lowercase
        else:
            raise ValueError("Invalid size")
        
        self._flavors = []

    def get_base(self) -> str:
        return self._base

    def get_flavors(self) -> List[str]:
        return self._flavors

    def add_flavor(self, flavor: str):
        if flavor.lower() not in Drink._valid_flavors:
            raise ValueError(f"Invalid flavor: {flavor}")
        
        if flavor.lower() not in self._flavors:
            self._flavors.append(flavor.lower())

    def set_flavors(self, flavors: List[str]):
        for flavor in flavors:
            if flavor.lower() not in Drink._valid_flavors:
                raise ValueError(f"Invalid flavor: {flavor}")
        self._flavors = list(set(flavors))

    def get_total(self) -> float:
        total_cost = Drink._size_prices[self._size]
        total_cost += 0.15 * len(self._flavors)
        return total_cost

    def set_size(self, size: str):
        if size.lower() in Drink._size_prices:
            self._size = size.lower()
        else:
            raise ValueError("Invalid size")
    
    def get_num_flavors(self) -> int:
        return len(self._flavors)

    def __str__(self) -> str:
        return f"Base: {self._base}, Size: {self._size}, Flavors: {', '.join(self._flavors)}, Total: ${self.get_total():.2f}"

class Food:
    """
    A class to represent a food item with toppings and its associated cost.
    
    Attributes:
        food_type (str): The type of food (e.g., 'hotdog', 'french fries').
        toppings (List[str]): A list of toppings added to the food.
    
    Methods:
        get_food_type: Returns the type of the food.
        add_topping: Adds a topping to the food.
        get_toppings: Returns the list of toppings added to the food.
        get_price: Returns the price of the base food item.
        get_total: Returns the total cost of the food, including toppings.
        get_topping_count: Returns the number of toppings added to the food.
    """
    
    _food_prices = {
        "hotdog": 2.30,
        "corndog": 2.00,
        "ice cream": 3.00,
        "onion rings": 1.75,
        "french fries": 1.50,
        "tater tots": 1.70,
        "nacho chips": 1.90
    }
    
    _valid_toppings = {
        "cherry": 0.00,
        "whipped cream": 0.00,
        "caramel sauce": 0.50,
        "chocolate sauce": 0.50,
        "nacho cheese": 0.30,
        "chili": 0.60,
        "bacon bits": 0.30,
        "ketchup": 0.00,
        "mustard": 0.00
    }
    
    def __init__(self, food_type: str):
        if food_type.lower() in Food._food_prices:
            self.food_type = food_type.lower()
        else:
            raise ValueError(f"Invalid food type: {food_type}")
        
        self.toppings = []

    def get_food_type(self) -> str:
        return self.food_type

    def add_topping(self, topping: str):
        if topping.lower() not in Food._valid_toppings:
            raise ValueError(f"Invalid topping: {topping}")
        
        if topping.lower() not in self.toppings:
            self.toppings.append(topping.lower())

    def get_toppings(self) -> List[str]:
        return self.toppings

    def get_price(self) -> float:
        return Food._food_prices[self.food_type]

    def get_total(self) -> float:
        total_cost = Food._food_prices[self.food_type]
        for topping in self.toppings:
            total_cost += Food._valid_toppings[topping]
        return total_cost

    def get_topping_count(self) -> int:
        return len(self.toppings)

    def __str__(self) -> str:
        return f"Type: {self.food_type}, Toppings: {', '.join(self.toppings)}, Total: ${self.get_total():.2f}"

class IceStorm:
    """
    A class to represent an Ice Storm, a popular mixed ice cream with toppings.
    
    Attributes:
        flavor (str): The flavor of the ice storm.
        toppings (List[str]): A list of added toppings to the ice storm.
    
    Methods:
        get_flavors: Returns the list of available flavors for the Ice Storm.
        add_flavor: Adds a flavor to the Ice Storm.
        get_base: Returns the flavor of the Ice Storm.
        get_size: Ice Storms do not have sizes, so this method is optional.
        get_total: Returns the total cost of the Ice Storm based on flavor and toppings.
        get_num_flavors: Returns the number of flavors added to the Ice Storm.
        __str__: Returns a string representation of the Ice Storm.
    """

    _valid_flavors = {
        "mint chocolate chip": 4.00,
        "chocolate": 3.00,
        "vanilla bean": 3.00,
        "banana": 3.50,
        "butter pecan": 3.50,
        "s'more": 4.00
    }

    _valid_toppings = {
        "cherry": 0.00,
        "whipped cream": 0.00,
        "caramel sauce": 0.50,
        "chocolate sauce": 0.50,
        "storios": 1.00,
        "dig dogs": 1.00,
        "t&t's": 1.00,
        "cookie dough": 1.00,
        "pecans": 0.50
    }
    
    def __init__(self, flavor: str):
        if flavor.lower() in IceStorm._valid_flavors:
            self._flavor = flavor.lower()
        else:
            raise ValueError("Invalid flavor")
        
        self._toppings = []

    def get_flavors(self) -> List[str]:
        return list(IceStorm._valid_flavors.keys())

    def add_flavor(self, flavor: str):
        if flavor.lower() not in IceStorm._valid_flavors:
            raise ValueError(f"Invalid flavor: {flavor}")
        
        self._flavor = flavor.lower()

    def get_base(self) -> str:
        return self._flavor

    def get_size(self) -> str:
        return "N/A"  # Ice Storms do not have sizes

    def get_total(self) -> float:
        total_cost = IceStorm._valid_flavors[self._flavor]
        total_cost += sum(IceStorm._valid_toppings[topping] for topping in self._toppings)
        return total_cost

    def get_num_flavors(self) -> int:
        return 1  # Ice Storms only have one flavor

    def __str__(self) -> str:
        return f"Flavor: {self._flavor}, Toppings: {', '.join(self._toppings)}, Total: ${self.get_total():.2f}"

    def add_topping(self, topping: str):
        if topping.lower() not in IceStorm._valid_toppings:
            raise ValueError(f"Invalid topping: {topping}")
        
        if topping.lower() not in self._toppings:
            self._toppings.append(topping.lower())

