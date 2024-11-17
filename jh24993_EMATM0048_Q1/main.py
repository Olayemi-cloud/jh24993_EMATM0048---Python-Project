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
        specialty = input("Does this technician have a specialty fish type? (yes/no): ").strip().lower()
        if specialty == 'yes':
            fish_type = input("Enter the specialty fish type: ").strip()
            hatchery.hire_technician(name, specialty=fish_type)
        else:
            hatchery.hire_technician(name)


    elif choice == 'remove':
        name = input("Enter the name of the technician to remove: ").strip()
        hatchery.fire_technician(name)


def manage_fish_sales(hatchery):
    """Prompt manager to specify the number of fish to sell for each fish type."""
    print("\nManage Fish Sales:")
    fish_sales = {}
    
    for fish in hatchery.fish_types:
        amount = int(input(f"Enter the amount of {fish.name} to sell: ") or 0)
        fish_sales[fish.name] = amount
    
    return fish_sales

if __name__ == "__main__":
    run_simulation()