"""
Name: Olayemi Amusile
Exam Number: 
Description:   A class that accounts for technicians(name, and weekly rate).

Date: November 2024
"""


class Technician:
    """
    A class that accounts for technicians(name, and weekly rate)

       
    """
    def __init__(self, name, weekly_rate, specialty):
        self.name = name
        self.weekly_rate = weekly_rate
        self.specialty = specialty
    def __str__(self):
        return f"Technician {self.name}"

    def __repr__(self):
        return f"Technician(name={self.name})"
    
    