import unittest
from Drinks import Drink, Food, IceStorm, Order

class TestDrink(unittest.TestCase):
    def test_get_base(self):
        """Test the getter for base."""
        drink = Drink("hill fog", size="medium")
        self.assertEqual(drink.get_base(), "hill fog")
    
    def test_get_flavors_empty(self):
        """Test the getter for flavors when no flavors are added."""
        drink = Drink("hill fog", size="medium")
        self.assertEqual(drink.get_flavors(), [])
    
    def test_get_size(self):
        """Test the getter for size."""
        drink = Drink("hill fog", size="medium")
        self.assertEqual(drink.get_size(), "medium")
    
    def test_get_total(self):
        """Test the total cost calculation, including flavors."""
        drink = Drink("hill fog", size="medium")
        drink.add_flavor("lemon")
        self.assertEqual(drink.get_total(), 1.75 + 0.15)
    
    def test_set_size(self):
        """Test setting the size."""
        drink = Drink("hill fog", size="medium")
        drink.set_size("large")
        self.assertEqual(drink.get_size(), "large")
    
    def test_invalid_base(self):
        """Test invalid base."""
        with self.assertRaises(ValueError):
            drink = Drink("invalid base", size="medium")
    
    def test_invalid_size(self):
        """Test invalid size."""
        with self.assertRaises(ValueError):
            drink = Drink("hill fog", size="extra large")


class TestFood(unittest.TestCase):
    def test_get_food_type(self):
        """Test the getter for food type."""
        food = Food("hotdog")
        self.assertEqual(food.get_food_type(), "hotdog")
    
    def test_add_topping(self):
        """Test adding valid toppings to food."""
        food = Food("french fries")
        food.add_topping("nacho cheese")
        self.assertIn("nacho cheese", food.get_toppings())
    
    def test_add_invalid_topping(self):
        """Test adding an invalid topping to food."""
        food = Food("french fries")
        with self.assertRaises(ValueError):
            food.add_topping("invalid topping")
    
    def test_get_total(self):
        """Test the total cost of food including toppings."""
        food = Food("french fries")
        food.add_topping("nacho cheese")
        food.add_topping("chili")
        self.assertEqual(food.get_total(), 1.50 + 0.30 + 0.60)
    
    def test_get_price(self):
        """Test the price of the base food item."""
        food = Food("corndog")
        self.assertEqual(food.get_price(), 2.00)
    
    def test_topping_count(self):
        """Test the number of toppings added to food."""
        food = Food("ice cream")
        food.add_topping("whipped cream")
        food.add_topping("chocolate sauce")
        self.assertEqual(food.get_topping_count(), 2)


class TestIceStorm(unittest.TestCase):
    def test_get_base(self):
        """Test the getter for the base of Ice Storm."""
        ice_storm = IceStorm("mint chocolate chip")
        self.assertEqual(ice_storm.get_base(), "mint chocolate chip")
    
    def test_get_flavors(self):
        """Test the getter for Ice Storm flavors."""
        ice_storm = IceStorm("mint chocolate chip")
        self.assertEqual(ice_storm.get_flavors(), [
            "mint chocolate chip", "chocolate", "vanilla bean", 
            "banana", "butter pecan", "s'more"
        ])
    
    def test_add_flavor(self):
        """Test adding a valid flavor to Ice Storm."""
        ice_storm = IceStorm("chocolate")
        ice_storm.add_flavor("banana")
        self.assertEqual(ice_storm.get_base(), "banana")

    def test_add_invalid_flavor(self):
        """Test adding an invalid flavor to Ice Storm."""
        ice_storm = IceStorm("chocolate")
        with self.assertRaises(ValueError):
            ice_storm.add_flavor("invalid flavor")
    
    def test_get_total(self):
        """Test the total cost of Ice Storm including toppings."""
        ice_storm = IceStorm("vanilla bean")
        ice_storm.add_topping("caramel sauce")
        ice_storm.add_topping("cookie dough")
        self.assertEqual(ice_storm.get_total(), 3.00 + 0.50 + 1.00)
    
    def test_get_num_flavors(self):
        """Test the number of flavors in Ice Storm (should be 1)."""
        ice_storm = IceStorm("banana")
        self.assertEqual(ice_storm.get_num_flavors(), 1)

    def test_add_topping(self):
        """Test adding a valid topping to Ice Storm."""
        ice_storm = IceStorm("s'more")
        ice_storm.add_topping("chocolate sauce")
        self.assertIn("chocolate sauce", ice_storm._toppings)

    def test_add_invalid_topping(self):
        """Test adding an invalid topping to Ice Storm."""
        ice_storm = IceStorm("s'more")
        with self.assertRaises(ValueError):
            ice_storm.add_topping("invalid topping")
    
    def test_str(self):
        """Test the string representation of Ice Storm."""
        ice_storm = IceStorm("mint chocolate chip")
        ice_storm.add_topping("cherry")
        ice_storm.add_topping("whipped cream")
        self.assertEqual(str(ice_storm), "Flavor: mint chocolate chip, Toppings: cherry, whipped cream, Total: $4.00")


class TestOrder(unittest.TestCase):
    def test_get_items(self):
        """Test the getter for items in the order."""
        order = Order()
        drink1 = Drink("hill fog", size="medium")
        food1 = Food("hotdog")
        ice_storm1 = IceStorm("chocolate")
        order.add_item(drink1)
        order.add_item(food1)
        order.add_item(ice_storm1)
        self.assertEqual(order.get_items(), [drink1, food1, ice_storm1])
    
    def test_get_total(self):
        """Test the total calculation for the order."""
        order = Order()
        drink1 = Drink("hill fog", size="medium")
        ice_storm1 = IceStorm("mint chocolate chip")
        ice_storm1.add_topping("cherry")
        ice_storm1.add_topping("caramel sauce")
        food1 = Food("french fries")
        food1.add_topping("chili")
        
        order.add_item(drink1)
        order.add_item(food1)
        order.add_item(ice_storm1)
        
        expected_total = (1.75 + 0.15) + (1.50 + 0.60) + (4.00 + 0.50 + 1.00)
        expected_total_with_tax = expected_total * (1 + 0.0725)
        self.assertAlmostEqual(order.get_total(), expected_total_with_tax, places=2)
    
    def test_get_receipt(self):
        """Test the receipt generation."""
        order = Order()
        drink1 = Drink("hill fog", size="medium")
        drink1.add_flavor("lemon")
        ice_storm1 = IceStorm("vanilla bean")
        ice_storm1.add_topping("whipped cream")
        ice_storm1.add_topping("pecans")
        food1 = Food("french fries")
        food1.add_topping("nacho cheese")
        
        order.add_item(drink1)
        order.add_item(food1)
        order.add_item(ice_storm1)
        
        expected_receipt = (
            "Receipt:\n"
            "Drink 1: Base = hill fog, Flavors = lemon, Size = medium, Cost: $1.90\n"
            "Food 1: Type = french fries, Toppings = nacho cheese, Cost: $2.40\n"
            "Ice Storm 1: Flavor = vanilla bean, Toppings = whipped cream, pecans, Cost: $4.50\n"
            "Order Total: $8.66\n"
        )
        self.assertEqual(order.get_receipt(), expected_receipt)


if __name__ == "__main__":
    unittest.main()
