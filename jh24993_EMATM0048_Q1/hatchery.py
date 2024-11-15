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
        
#Add the technician name and specialty
def hire_technician(self, name, specialty=None):
        technician = Technician(name, Config.TECHNICIAN_WEEKLY_RATE, specialty=specialty)
        self.technicians.append(technician)
        print(f"Hired technician: {name} with specialty: {specialty}")
 
        
        