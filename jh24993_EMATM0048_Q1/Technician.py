 # Technician class 
class Technician:
    def __init__(self, name, weekly_rate):
        self.name = name
        self.weekly_rate = weekly_rate

    def __str__(self):
        return f"Technician {self.name}"
    
    def __repr__(self):
        return f"Technician(name={self.name})"