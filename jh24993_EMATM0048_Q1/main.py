from config import Config
from hatchery import Hatchery

def get_positive_or_negative_int(prompt):
    """
    Prompts the user for a positive or negative integer and validates input.
    """
    while True:
        try:
            value = int(input(prompt))
            if value != 0:  # Ensure the input is not zero
                return value
            else:
                print("Please enter a non-zero integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def hire_technicians_individually(simulation, num_technicians, quarter):
    """
    Prompts the user to input names for a given number of technicians
    and hires each technician immediately.
    """
    for _ in range(num_technicians):
        name = input("Enter Technician Name: ").strip()
        if name:  # Ensure name is not empty
            # Ensure name is treated as a single string
            simulation.hire_technicians(name, quarter)
        else:
            print("Name cannot be empty. Please try again.")

def main():
    """
    Main function to run the simulation.
    """
    num_quarters = get_positive_or_negative_int("Please enter number of quarters: ")
    simulation = Hatchery(Config, num_quarters)

    for quarter in range(1, num_quarters + 1):
        print(f"\n{'=' * 40}\n====== SIMULATING quarter {quarter} ======\n{'=' * 40}")

        num_technicians = get_positive_or_negative_int(
            "Enter number of technicians to add (positive) or remove (negative): "
        )
        
        if num_technicians > 0:
            hire_technicians_individually(simulation, num_technicians, quarter)
        elif num_technicians < 0:
            num_to_remove = abs(num_technicians)
            simulation.remove_technicians(num_to_remove)
            
        simulation.simulate_quarter(quarter, num_technicians)
        simulation.prompt_restock()
        simulation.display_technicians()
        print (f"End of Quarter {quarter}")

    print("\nSimulation complete.")
    simulation.display_finances()

if __name__ == "__main__":
    main()
    
