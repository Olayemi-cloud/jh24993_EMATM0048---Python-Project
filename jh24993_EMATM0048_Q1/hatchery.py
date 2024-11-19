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

        
    

   
 
        
        