class Fish:
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
        # Placeholder for sales simulation logic
        return min(self.demand, self.demand)  # Simulate selling all available demand



        

