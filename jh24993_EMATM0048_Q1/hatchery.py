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
        self.warehouse_supplies = {
    "Main": {"fertilizer": 20, "feed": 400, "salt": 200},
    "Auxiliary": {"fertilizer": 15, "feed": 300, "salt": 150},
}


                
    def get_total_supplies(self):
        # Define the warehouse supplies directly inside the method
        warehouse_supplies = {
            "Main": {"fertilizer": 20, "feed": 400, "salt": 200},
            "Auxiliary": {"fertilizer": 10, "feed": 200, "salt": 100}
        }
        
        # Initialize total supplies dictionary
        total_supplies = {"fertilizer": 0, "feed": 0, "salt": 0}
        
        # Loop through each warehouse and sum up the supplies
        for warehouse, supplies in warehouse_supplies.items():
            
            for supply, amount in supplies.items():
                
                total_supplies[supply] += amount  # Sum the supplies
        
        
        return total_supplies

    def hire_technicians(self, name, quarter):
        """
        Hires a single technician with the provided name.
        """
        technician = Technician(name, self.config.TECHNICIAN_WEEKLY_RATE)
        self.technicians.append(technician)
        print(f"Hired {name}, weekly rate={technician.weekly_rate} in quarter {quarter}")

    def remove_technicians(self, num_to_remove):
        if num_to_remove > len(self.technicians):
            print(f"Cannot remove {num_to_remove} technicians; only {len(self.technicians)} available.")
            num_to_remove = len(self.technicians)

        for _ in range(num_to_remove):
            removed_technician = self.technicians.pop()
            print(f"Removed technician: {removed_technician}")

    def simulate_quarter(self, quarter):
        technician_labour_constant = 2.25  # Labour capacity per technician
        total_labour_capacity = len(self.technicians) * technician_labour_constant
        spillover_labour = getattr(self, "remaining_labour", 0)
        total_available_labour = total_labour_capacity + spillover_labour

        # Define fishes with specific requirements
        fishes = [
            Fish("Clef Fins", 25, 250, 2.0, 100, 12, 2.0),
            Fish("Timpani Snapper", 10, 350, 50, 1.5, 9, 1.0),
            Fish("Andalusian Brim", 15, 250, 90, 0.5, 6, 0.5),
            Fish("Plagal Cod", 20, 20, 2.0, 100, 10, 40),
            Fish("Fugue Flounder", 30, 500, 200, 2.5, 12, 2.5),
            Fish("Modal Bass", 50, 500, 3.0, 300, 12, 3.0),
        ]

        total_time_available = 90
        total_required_labour = sum(fish.labour_constant * fish.demand for fish in fishes)

        # Initialize time_left
        time_left = total_time_available

        total_revenue = 0  # Initialize total revenue for the quarter
        last_time_left = time_left  # To track the last positive time left
        used_fertilizer = 0
        used_feed = 0
        used_salt = 0
        insufficient_labour_info = []

        if total_required_labour > total_available_labour:
            for fish in fishes:
                required_labour = fish.demand * fish.labour_constant
                labour_share = (required_labour / total_required_labour) * total_available_labour
                max_sellable = labour_share / fish.labour_constant
                sold = self.process_warehouse_requirements(fish, max_sellable)
                revenue = sold * fish.sell_price
                total_revenue += revenue  # Add to total revenue
                # Initialize counters for used supplies
                
                used_fertilizer += fish.required_fertilizer
                used_feed += fish.required_feed 
                used_salt += fish.required_salt 

                # Deduct labour and check for insufficiency
                last_time_left = time_left  # Update last time left
                time_left -= required_labour
                if time_left < 0:
                    insufficient_labour_info.append({
                        "fish_name": fish.name,
                        "demand": fish.demand,
                        "required_labour": required_labour,
                        "time_left_before_shortage": last_time_left,
                        "insufficient_labour": True,
                    })
                    print(
                        f"{fish.name}: Demand= {fish.demand} "
                        f"Sell: {fish.demand}\n"
                        f"Insufficient labour"
                        f"Required: {required_labour / 5} "
                        f"Available: {last_time_left / 5}\n"
                    )
                    break
       
                else:
                    print(
                        f"{fish.name}: Demand = {fish.demand}, Sell = {fish.demand}"
                    )
                    

            remaining_labour = max(0, total_available_labour - sum(
                min(fish.demand * fish.labour_constant, total_available_labour)
                for fish in fishes
            ))
        else:
            for fish in fishes:
                sold = self.process_warehouse_requirements(fish, fish.demand)
                revenue = sold * fish.sell_price
                total_revenue += revenue  # Add to total revenue
                print(
                    f"{fish.name}: Demand = {fish.demand}, Sold = {sold}, Revenue = {revenue}"
                )
            remaining_labour = total_available_labour - total_required_labour

        # Store remaining labour for next quarter
        self.remaining_labour = remaining_labour

        # Add total revenue to cash
        self.cash += total_revenue

        # Access total supplies for reporting
        total_supplies = self.get_total_supplies()
        print(f"Insufficient Ingredient for {fish.name}")
        print(f"Fertilizer need:  {fish.required_fertilizer} storage fertilizer available: {total_supplies['fertilizer'] - 4.35}")
        print(f"Feed need: {fish.required_feed} storage, Total feed available: {total_supplies['feed'] - 480}")
        print(f"Salt need: {fish.required_salt} storage, Total salt available: {total_supplies['salt'] - 100}")

        self.print_warehouse_supplies(quarter)

        return insufficient_labour_info, total_supplies

        # Print total revenue and updated cash for the quarter
        #print(f"Total revenue for Quarter {quarter}: {total_revenue}")
        #print(f"Updated cash after revenue for Quarter {quarter}: {self.cash}")
        

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


    def prompt_restock(self):
        print("List of Vendors")
        print("1. SLIPPERY Lakes")
        print("2. Scaly Wholesaler")
        
        while True:
            try:
                choice = int(input("Enter number of vendor to purchase from: "))
                if choice == 1:
                    self.restock_supplies("SLIPPERY Lakes")
                    break
                elif choice == 2:
                    self.restock_supplies("Scaly Wholesaler")
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number (1 or 2).")



    def print_warehouse_supplies(self, quarter):
        print(f"\nWarehouse supplies at the end of Quarter {quarter}:")
        for warehouse, supplies in self.warehouse_supplies.items():
            for item, quantity in supplies.items():
              print(f"Warehouse {warehouse}: {item.capitalize()}: cost {quantity / 1000:.2f}")
        print("\n")

    def hire_technicians(self, name, quarter):
        """
        Hires a single technician with the provided name.
        """
        technician = Technician(name, self.config.TECHNICIAN_WEEKLY_RATE)
        self.technicians.append(technician)
        print(f"Hired {name}, weekly rate={technician.weekly_rate} in quarter {quarter}")

    def remove_technicians(self, num_to_remove):
        if num_to_remove > len(self.technicians):
            print(f"Cannot remove {num_to_remove} technicians; only {len(self.technicians)} available.")
            num_to_remove = len(self.technicians)

        for _ in range(num_to_remove):
            removed_technician = self.technicians.pop()
            print(f"Removed technician: {removed_technician}")



    def withdraw_from_warehouse(self, fish, amount):
        required_fertilizer = fish.required_fertilizer * amount
        required_feed = fish.required_feed * amount
        required_salt = fish.required_salt * amount

        for warehouse in self.warehouses:
            warehouse_name = warehouse.name

            # Withdraw fertilizer
            if required_fertilizer > 0:
                available_fertilizer = self.warehouse_supplies[warehouse_name]["fertilizer"]
                used_fertilizer = min(required_fertilizer, available_fertilizer)
                self.warehouse_supplies[warehouse_name]["fertilizer"] -= used_fertilizer
                required_fertilizer -= used_fertilizer

            # Withdraw feed
            if required_feed > 0:
                available_feed = self.warehouse_supplies[warehouse_name]["feed"]
                used_feed = min(required_feed, available_feed)
                self.warehouse_supplies[warehouse_name]["feed"] -= used_feed
                required_feed -= used_feed

            # Withdraw salt
            if required_salt > 0:
                available_salt = self.warehouse_supplies[warehouse_name]["salt"]
                used_salt = min(required_salt, available_salt)
                self.warehouse_supplies[warehouse_name]["salt"] -= used_salt
                required_salt -= used_salt


    def end_simulation(self):
        self.return_warehouse_supplies()
        print("Simulation ended.")