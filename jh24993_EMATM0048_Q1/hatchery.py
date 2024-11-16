# models/hatchery.py
from Technician import Technician
from fish import Fish
from warehouse import Warehouse
from config import Config

class Hatchery:
    def __init__(self):
        self.cash = Config.INITIAL_CASH
        self.technicians = []
        self.fish_types = [
            Fish("Clef Fins", 25, 25),
            Fish("Timpani Snapper", 10, 10),
            Fish("Andalusian Brim", 15, 15),
            Fish("Plagal Cod", 20, 20),
            Fish("Fugue Flounder", 30, 30),
            Fish("Modal Bass", 50, 50)
        ]
        self.warehouses = [
            Warehouse("Main", Config.WAREHOUSE_CAPACITY),
            Warehouse("Auxiliary", Config.WAREHOUSE_CAPACITY)
        ]
        
#Add cash function for initial hatchery invest        

    def add_cash(self, amount):
        self.cash += amount
        print(f"Added cash: {amount}. New balance: {self.cash}")
                
#Subtract cash function       
    def deduct_cash(self, amount):
        if amount > self.cash:
            print(f"Cannot deduct {amount}, insufficient cash. Current balance: {self.cash}")
            return False
        self.cash -= amount
        print(f"Deducted cash: {amount}. New balance: {self.cash}")
        return True

#Add the technician name and specialty
    def hire_technician(self, name, specialty=None):
        technician = Technician(name, Config.TECHNICIAN_WEEKLY_RATE, specialty=specialty)
        self.technicians.append(technician)
        print(f"Hired technician: {name} with specialty: {specialty}")
        
    def fire_technician(self, name):
        for i, technician in enumerate(self.technicians):
            if technician.name == name:
                removed_technician = self.technicians.pop(i)
                print(f"Fired technician: {removed_technician.name}")
                return
        print(f"Technician {name} not found.")

    def manage_fish_sales(self, fish_sales):
        total_revenue = 0
        for fish_name, amount in fish_sales.items():
            for fish in self.fish_types:
                if fish.name == fish_name:
                    sold_amount = min(amount, fish.demand)
                    revenue = sold_amount * fish.sell_price
                    total_revenue += revenue
                    print(f"Sold {sold_amount} of {fish.name}, revenue: {revenue}")
                    break
        self.add_cash(total_revenue)
        return total_revenue
 
        
        