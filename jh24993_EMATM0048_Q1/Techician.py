class Technician:
    def __init__(self, name, weekly_rate, specialty):
        self.name = name
        self.weekly_rate = weekly_rate
        self.specialty = specialty
        
    def get_name(self):
        return self.name

    def get_weekly_rate(self):
        return self.weekly_rate
    
    def get_specialty(self):
        return self.specialty

    def __str__(self):
        return self.name