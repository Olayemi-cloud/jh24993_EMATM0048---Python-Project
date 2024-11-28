"""
Name: Olayemi Amusile
Description: This script simulates a hatchery system, processing supplies and inventory.

Date: November 2024
"""



from Technician import Technician
from warehouse import Warehouse
from config import Config
from fish import Fish
import sys

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
    "Auxiliary": {"fertilizer": 10, "feed": 200, "salt": 100},
}


                
    def get_total_supplies(self):
        """
        Define the warehouse supplies  and calculate the total supplies.

        This method defines the supplies in two warehouses, "Main" and "Auxiliary", and calculates the 
        total amount of each supply (fertilizer, feed, salt) across both warehouses.

        Returns:
            dict: A dictionary with the total amounts of fertilizer, feed, and salt across all warehouses.
        """
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
        Hires a single technician with the provided name for each quarters.

        Returns:
            string: Technician names and weekly rates
    
        """
        technician = Technician(name, self.config.TECHNICIAN_WEEKLY_RATE)
        self.technicians.append(technician)
        print(f"Hired {name}, weekly rate={technician.weekly_rate} in quarter {quarter}")

    def remove_technicians(self, num_to_remove):
        """
        Removes technicians based on the number of technicians passed to num_to_remove in each quarter simulation.

        Returns:
            string: name of techncian that was removed
    
        """
        if num_to_remove > len(self.technicians):
            print(f"Cannot remove {num_to_remove} technicians; only {len(self.technicians)} available.")
            num_to_remove = len(self.technicians)

        for _ in range(num_to_remove):
            removed_technician = self.technicians.pop()
            print(f"Removed technician: {removed_technician}")


    def display_num_technicians(self):
        """
        Returns the number of technicians as an integer.
        """
        return len(self.technicians)

    def simulate_quarter(self, quarter, num_technicians):

        """
        This is the core function of the simulation
        simulate_quarter computes and simulate operations for
        - each quarters simualation
        - demand and labour allocations for different fish species
        - tracking revenue and checking for bankrupcy in business model
       
        
        The function calculates the total labour capacity, compares available labour with
        required labour for processing the fish demands and updates the revenue and remaining labour.
        and supplies used-fertilizer, feed, salt-for the quarter. It also checks for labour shortage.
        It also monitors unprocessed fish in cases where there is inadequate labor to satisfy demand. The results
        for the quarter are printed including the revenue, remaining cash, and usage of supplies.
                    
        

        Returns:
        None: Updates the state of the simulation by printing out results, including total revenue
        remaining cash, and supplies used for the quarter. The method also stores the remaining
        labour for the next quarter.

        """

        technician_labour_constant = 2.25  # Labour capacity per technician
        total_labour_capacity = len(self.technicians) * technician_labour_constant
        spillover_labour = getattr(self, "remaining_labour", 0)
        total_available_labour = total_labour_capacity + spillover_labour
        remaining_labour = 0  # Default value
        """
         Define fishes with specific requirements
        """
        fishes = [
            Fish("Clef Fins", 25, 250, 2.0, 2.5, 300, 50, 25),
            Fish("Timpani Snapper", 10, 350, 1.0, 0.5, 90, 20, 10),
            Fish("Andalusian Brim", 15, 250, 0.5, 1.35, 90, 30, 15),
            Fish("Plagal Cod", 20, 400, 2.0, 2.0, 120, 40, 20),
            Fish("Fugue Flounder", 30, 500, 2.5, 2.5, 2.5, 2.5, 30),
            Fish("Modal Bass", 50, 500, 3.0, 3, 3, 3.0, 50),
        ]
        """
         Prompt user to set demand for each fish
        """
        total_processed_fish = 0
        print("\nSet demand for each fish:")
        for fish in fishes:
            total_required_labour = sum(fish.labour_constant * fish.demand for fish in fishes)
            total_cost = sum(fish.sell_price * fish.demand for fish in fishes)

            while True:
                try:
                    demand = int(input(f"Fish {fish.name}, demand {fish.demand}, Sell {fish.max_demand}: "))
                   
                    if 0 <= demand <= fish.max_demand:
                        fish.demand = demand
                        break
                    else:
                        print(f"Invalid input. Enter a number between 0 and {fish.max_demand}.")

                    
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        total_time_available = 45 * num_technicians
        total_required_labour = sum(fish.labour_constant * fish.demand for fish in fishes)

        """ 
            Initialize time_left
        """
        total_processed_fish = 2
        time_left = total_time_available

        total_revenue = 0  # Initialize total revenue for the quarter
        last_time_left = time_left  # To track the last positive time left
        used_fertilizer = 0
        used_feed = 0
        used_salt = 0
        insufficient_labour_info = []
        unprocessed_fishes = []

        if total_required_labour > total_available_labour:
            for i, fish in enumerate(fishes):
                required_labour = fish.demand * fish.labour_constant
                labour_share = (required_labour / total_required_labour) * total_available_labour
                max_sellable = labour_share / fish.labour_constant
                sold = self.process_warehouse_requirements(fish, max_sellable)
                revenue = sold * fish.sell_price
                total_revenue += revenue  
                

                """
                Deduct labour and check for insufficiency

                """
                last_time_left = time_left  
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
                        f"Fish {fish.name}: Demand= {fish.demand},  "
                        f"Sell: {fish.demand}\n"
                        f"Insufficient labour"
                        f"Required: {required_labour / 5} "
                        f"Available: {last_time_left / (5 if num_technicians == 1 else 2.5 * num_technicians)}\n"
                    )
                    unprocessed_fishes.append(f"Fish {fish.name}: Demand = {fish.demand}, Sell = 0")
                   
                    for remaining_fish in fishes[i + 1:]:
                        unprocessed_fishes.append(
                            f"{remaining_fish.name}: Demand = {remaining_fish.demand}, Sell = 0"
                        )
                    break
            ...
        else:
            for fish in fishes:
                sold = self.process_warehouse_requirements(fish, fish.demand)
                revenue = sold * fish.sell_price
                total_revenue += revenue  # Add to total revenue
                print(
                    f"{fish.name}: Demand = {fish.demand}, Sold = {sold}, Revenue = {revenue}"
                )
            remaining_labour = total_available_labour - total_required_labour

       
        self.remaining_labour = remaining_labour
        num_unprocessed_fishes = len(unprocessed_fishes)

        if unprocessed_fishes:
            for info in unprocessed_fishes:
                print(info)

        """
          Add total revenue to cash
        """
        pro_fish = 6 - num_unprocessed_fishes
        subset = fishes[:-pro_fish]
        used_fertilizer = round(sum(fish.required_fertilizer for fish in subset) * 0.1, 2)
        used_feed = sum(fish.required_feed for fish in subset)
        used_salt = sum(fish.required_salt for fish in subset)
        revenue_total = sum(fish.sell_price * fish.demand  for fish in subset)
               
        self.cash += revenue_total

        
        total_supplies = self.get_total_supplies()
        print(f"Insufficient Ingredient for {6 - num_unprocessed_fishes} {fish.name}{revenue_total}")
        print(f"Fertilizer need:  {fish.required_fertilizer} storage fertilizer available: {total_supplies['fertilizer'] - used_fertilizer}")
        print(f"Feed need: {fish.required_feed} storage, Total feed available: {total_supplies['feed'] - used_feed}")
        print(f"Salt need: {fish.required_salt} storage, Total salt available: {total_supplies['salt'] - used_salt}")


        """"
         Access total supplies for reporting
        """
        total_supplies = self.get_total_supplies()
        # print(f"Total revenue for Quarter {quarter}: {revenue_total}, {used_salt / 10}, {used_feed} {used_fertilizer}")
        # print(f"Remaining cash after Quarter {quarter}: {self.cash}")

        


        self.print_warehouse_supplies(quarter, used_fertilizer, used_salt, used_feed)
        self.pay_rent_and_utilities()
        self.pay_technicians()
        #self.display_finances()

        if self.cash < 0:
            print("\nThe business has gone bankrupt. Simulation terminated.")
        #return False        

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

    def restock_supplies(self, vendor):

        # Define prices for each commodity per vendor
        vendor_prices = {
            "SLIPPERY Lakes": {"fertilizer": 0.3, "feed": 0.1, "salt": 1},
            "Scaly Wholesaler": {"fertilizer": 0.2, "feed": 0.4, "salt": 0.25}
        }

        # Check if vendor is valid
        if vendor not in vendor_prices:
            print("Invalid vendor specified. No restocking done.")
            return

        # Quantities to restock based on vendor
        if vendor == "SLIPPERY Lakes":
            restock_quantities = {"fertilizer": 42, "feed": 660, "salt": 300}
        elif vendor == "Scaly Wholesaler":
            restock_quantities = {"fertilizer": 10, "feed": 200, "salt": 10}

        # Use vendor-specific prices
        commodity_prices = vendor_prices[vendor]

        # Calculate total cost and update supplies
        total_cost = 0
        for commodity, quantity in restock_quantities.items():
            cost = quantity * commodity_prices[commodity]
            total_cost += cost

            # Separate warehouses by type
            main_warehouses = [wh for wh in self.warehouses if wh.name == "Main"]
            aux_warehouses = [wh for wh in self.warehouses if wh.name == "Auxiliary"]
            total_warehouses = len(main_warehouses) + len(aux_warehouses)

            if total_warehouses > 0:
                per_warehouse_quantity = quantity // total_warehouses

                # Stock main warehouses
                for warehouse in main_warehouses:
                    self.warehouse_supplies[warehouse.name][commodity] += per_warehouse_quantity

                # Stock auxiliary warehouses
                for warehouse in aux_warehouses:
                    self.warehouse_supplies[warehouse.name][commodity] += per_warehouse_quantity

        self.cash -= total_cost

        # Display restocking details
        print(f"Hatchery Name: Estaboga, Cash {self.cash}:")

    
        for warehouse in main_warehouses:
            print(f"  {warehouse.name}:")
            for commodity, quantity in restock_quantities.items():
                per_warehouse_quantity = quantity / total_warehouses
                print(f"  Warehouses Main:  {commodity.capitalize()}: {per_warehouse_quantity:.2f} (capacity={per_warehouse_quantity:.2f})")

        # Display details for auxiliary warehouses
        print("\nAuxiliary Warehouses:")
        for warehouse in aux_warehouses:
            print(f"  {warehouse.name}:")
            for commodity, quantity in restock_quantities.items():
                per_warehouse_quantity = quantity / total_warehouses
                print(f"    {commodity.capitalize()}: {per_warehouse_quantity:.2f} (capacity={per_warehouse_quantity})")


        if self.cash < 0:
            print("\nThe business has gone bankrupt. Simulation terminated.")
            sys.exit()

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


    def display_technicians(self):
        """
        Displays details of all technicians.
        """
        if not self.technicians:
            print("No technicians are currently hired.")
        else:
            print("\nTechnicians:")
            for index, technician in enumerate(self.technicians, start=1):
                print(f"Technician: {technician.name}, Weekly Rate: {technician.weekly_rate}")


    # def print_warehouse_supplies(self, quarter):
    #     print(f"\nWarehouse supplies at the end of Quarter {quarter}:")
    #     for warehouse, supplies in self.warehouse_supplies.items():
    #         for item, quantity in supplies.items():
    #           print(f"Warehouse {warehouse}: {item.capitalize()}: cost {quantity * 10: 2f}")
    #     print("\n")
    def print_warehouse_supplies(self, quarter, used_fertilizer, used_salt, used_feed):
        main_aux_warehouse_supplies = {
            "Main": {"fertilizer": 2, "feed": 400, "salt": 200},
            "Auxiliary": {"fertilizer": 1, "feed": 200, "salt": 100},
        }

        # Helper function to handle subtraction
        def subtract_from_warehouse(main_quantity, aux_quantity, used_quantity):
            remaining_main = max(main_quantity - used_quantity, 0)
            overflow = max(used_quantity - main_quantity, 0)
            remaining_aux = max(aux_quantity - overflow, 0)
            return remaining_main, remaining_aux

        # Subtract used quantities and calculate remaining supplies
        remaining_supplies = {
            "Main": {},
            "Auxiliary": {}
        }

        for item in ["fertilizer", "salt", "feed"]:
            main_quantity = main_aux_warehouse_supplies["Main"][item]
            aux_quantity = main_aux_warehouse_supplies["Auxiliary"][item]
            used_quantity = {"fertilizer": used_fertilizer, "salt": used_salt, "feed": used_feed}[item]

            remaining_main, remaining_aux = subtract_from_warehouse(main_quantity, aux_quantity, used_quantity)
            remaining_supplies["Main"][item] = remaining_main
            remaining_supplies["Auxiliary"][item] = remaining_aux

        # Display the results
        # print(f"\nWarehouse supplies at the end of Quarter {quarter}:")
        # print(f"Used Fertilizer: {used_fertilizer}")
        # print(f"Used Salt: {used_salt}")
        # print(f"Used Feed: {used_feed}")

        for warehouse, supplies in remaining_supplies.items():
            print(f"\nWarehouse {warehouse}:")
            for item, quantity in supplies.items():
                print(f"  - {item.capitalize()}: {quantity} units")

    def hire_technicians(self, name, quarter):
        """
        Hires a single technician with the provided name.l
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

    def pay_technicians(self):
            for tech in self.technicians:
                amount = tech.weekly_rate * 12  
                self.cash -= amount
                print(f"Paid {tech.name}, weekly rate={tech.weekly_rate}, amount={amount}")

    def pay_rent_and_utilities(self):
        self.cash -= self.config.RENT_UTILITIES_COST
        print(f"Paid rent/utilities: {self.config.RENT_UTILITIES_COST}")

    def display_finances(self):
        print(f"Current cash: {self.cash}")

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
