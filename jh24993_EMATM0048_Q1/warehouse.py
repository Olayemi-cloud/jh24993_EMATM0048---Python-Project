# In warehouse.py
class Warehouse:
    def __init__(self, name, capacity):
        """
        param name: Name of the warehouse
        param capacity: Maximum capacity of the warehouse
        """
        self.name = name
        self.capacity = capacity
        self.current_stock = 0


