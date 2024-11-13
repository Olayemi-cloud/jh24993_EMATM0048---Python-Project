# In warehouse.py
class Warehouse:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.depreciation = 0  # Initial depreciation if needed

    def apply_depreciation(self, depreciation_amount):
        self.depreciation += depreciation_amount
        # Adjust other attributes if needed

