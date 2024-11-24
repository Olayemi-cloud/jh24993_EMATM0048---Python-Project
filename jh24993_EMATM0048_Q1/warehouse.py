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

    def add_stock(self, quantity):
        """
        Adds stock to the warehouse, ensuring capacity is not exceeded.
        """
        if self.current_stock + quantity <= self.capacity:
            self.current_stock += quantity
            return True
        return False

    def remove_stock(self, quantity):
        """
        Removes stock from the warehouse, ensuring it does not go negative.
        """
        if self.current_stock >= quantity:
            self.current_stock -= quantity
            return True
        return False