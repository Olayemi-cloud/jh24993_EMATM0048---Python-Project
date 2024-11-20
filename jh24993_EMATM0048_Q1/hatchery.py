from Technician import Technician
from warehouse import Warehouse
from config import Config
from fish import Fish

class Hatchery:
    def __init__(self, config, num_quarters):
        self.config = config
        self.num_quarters = num_quarters
        self.cash = config.INITIAL_CASH
        self.technicians = []
        self.warehouses = [
            Warehouse("Main", config.WAREHOUSE_CAPACITY),
            Warehouse("Auxiliary", config.WAREHOUSE_CAPACITY),
        ]
        self.warehouse_supplies = {warehouse.name: {"fertilizer": 20, "feed": 400, "salt": 100} for warehouse in self.warehouses}
                

    def hire_technicians(self, names, quarter):
        for name in names:
            technician = Technician(name, self.config.TECHNICIAN_WEEKLY_RATE)
            self.technicians.append(technician)
            print(f"Hired {name}, weekly rate={technician.weekly_rate} in quarter {quarter}")

        
    def simulate_quarter(self, quarter):
        technician_labour_constant = 2.25  # Labour capacity per technician
        total_labour_capacity = len(self.technicians) * technician_labour_constant
        spillover_labour = getattr(self, "remaining_labour", 0)
        total_available_labour = total_labour_capacity + spillover_labour

        # Define fishes with specific requirements
        fishes = [
            Fish("Clef Fins", 25, 250, 2.0, 2, 2, 2.0),
            Fish("Timpani Snapper", 10, 350, 1.5, 1.5, 1, 1.0),
            Fish("Andalusian Brim", 15, 250, 1.8, 0.5, 1.2, 0.5),
            Fish("Plagal Cod", 20, 20, 400, 2.0, 1.5, 2.0),
            Fish("Fugue Flounder", 30, 500, 2.5, 2.5, 2.5, 2.5),
            Fish("Modal Bass", 50, 500, 3.0, 3, 3, 3.0),
        ]

       # total_required_labour = sum(1 + c.labour_constant for c in fishes)
        total_required_labour = sum(c.labour_constant for c in fishes)
        print(f"Quarter {quarter}: Labour required = {total_required_labour}, Labour available = {total_available_labour}")

    total_revenue = 0  # Initialize total revenue for the quarter

     if total_required_labour > total_available_labour:
            print("Insufficient labour for this quarter!")
            for fish in fishes:
                required_labour = fish.demand * fish.labour_constant
                labour_share = (required_labour / total_required_labour) * total_available_labour
                max_sellable = labour_share / fish.labour_constant
                sold = self.process_warehouse_requirements(fish, max_sellable)
                revenue = fish.sell_price
                total_revenue += revenue  # Add to total revenue
                print(
                    f"{fish.name}: Demand = {fish.demand}, Sold = {sold}, Revenue = {revenue}"
                )
            remaining_labour = total_available_labour - sum(
                min(fish.demand * fish.labour_constant, total_available_labour)
                for fish in fishes
            )
        else:
            print("Labour is sufficient for all demands.")
            for fish in fishes:
                sold = self.process_warehouse_requirements(fish, fish.demand)
                revenue = sold * fish.sell_price
                total_revenue += revenue  # Add to total revenue
                print(
                    f"{fish.name}: Demand = {fish.demand}, Sold = {sold}, Revenue = {revenue}"
                )
            remaining_labour = total_available_labour - total_required_labour

        

    def process_warehouse_requirements(self, fish, amount):
        required_fertilizer = fish.required_fertilizer * amount
        required_feed = fish.required_feed * amount
        required_salt = fish.required_salt * amount

        total_fertilizer = sum(self.warehouse_supplies[warehouse]["fertilizer"] for warehouse in self.warehouse_supplies)
        total_feed = sum(self.warehouse_supplies[warehouse]["feed"] for warehouse in self.warehouse_supplies)
        total_salt = sum(self.warehouse_supplies[warehouse]["salt"] for warehouse in self.warehouse_supplies)

        if total_fertilizer < required_fertilizer or total_feed < required_feed or total_salt < required_salt:
            max_fertilizer_limit = total_fertilizer / fish.required_fertilizer
            max_feed_limit = total_feed / fish.required_feed
            max_salt_limit = total_salt / fish.required_salt
            max_possible_amount = min(max_fertilizer_limit, max_feed_limit, max_salt_limit)
            self.withdraw_from_warehouse(fish, max_possible_amount)
            return max_possible_amount
        else:
            self.withdraw_from_warehouse(fish, amount)
            return amount
 
        
        