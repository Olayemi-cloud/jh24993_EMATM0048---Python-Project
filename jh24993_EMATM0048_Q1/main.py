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

def get_technician_names(num_technicians):
    """
    Prompts the user to input names for a given number of technicians.
    """
    names = []
    for i in range(num_technicians):
        name = input(f"Enter name for Technician {i + 1}: ").strip()
        if name:  # Ensure name is not empty
            names.append(name)
        else:
            print("Name cannot be empty. Please try again.")
            return get_technician_names(num_technicians)  # Restart if validation fails
    return names

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
            technician_names = get_technician_names(num_technicians)
            simulation.hire_technicians(technician_names, quarter)
        elif num_technicians < 0:
            num_to_remove = abs(num_technicians)
            simulation.remove_technicians(num_to_remove)

if __name__ == "__main__":
    main()

   