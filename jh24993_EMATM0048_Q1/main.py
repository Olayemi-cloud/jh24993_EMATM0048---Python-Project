from hatchery import Hatchery

def run_simulation():
    print("Welcome to the Hatchery Simulation!")
    
    # Set up initial conditions
    hatchery = Hatchery()
    quarters = int(input("Enter the number of quarters to run the simulation (default is 8 for two years): ") or 8)

 # Run each quarter
    for quarter in range(1, quarters + 1):
        print(f"\n{'='*40}\nQuarter {quarter}")
        
        # Prompt for technician adjustments      
        manage_technicians(hatchery)
        
        
def manage_technicians(hatchery):
    """Prompt manager to add or remove technicians."""
    print("\nManage Technicians:")
    choice = input("Would you like to add or remove technicians? (add/remove/none): ").strip().lower()
    
    if choice == 'add':
        name = input("Enter technician's name: ").strip()
        
