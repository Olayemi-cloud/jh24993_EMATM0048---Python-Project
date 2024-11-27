"""
Name: Olayemi Amusile
Description:  A class to represent types of fish and manage its sales and supply requirements.

Date: November 2024
"""


class Fish:
    """
    A class to represent a type of fish and manage its sales and supply requirements.

       
    """

    def __init__(self, name, demand, sell_price, labour_constant, required_fertilizer, required_feed, required_salt, max_demand):
       
        self.name = name
        self.demand = demand
        self.sell_price = sell_price
        self.labour_constant = labour_constant
        self.required_fertilizer = required_fertilizer
        self.required_feed = required_feed
        self.required_salt = required_salt
        self.max_demand = max_demand

    def simulate_sales(self):
        """
        simulate_sales():
            Simulates sales of the fish based on its demand and returns the amount sold.
        Returns:
            int: The amount of fish sold .
        """
        return min(self.demand, self.demand)  


        

