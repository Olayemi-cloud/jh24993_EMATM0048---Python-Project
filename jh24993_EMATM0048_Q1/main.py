"""
Name: Olayemi Amusile
Description:  Main Entry file for managing and running simulation

Date: November 2024
"""

from config import Config
from hatchery import Hatchery

def get_positive_or_negative_int(prompt):
    """
    Prompts the user for a positive or negative integer and validates input.
    """
    while True:
        try:
            value = int(input(prompt))
            if value != 0:  
                return value
            else:
               return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
# Define the fish specialties list
fish_specialties = [
    "Clef Fins",
    "Timpani Snapper",
    "Andalusian Brim",
    "Plagal Cod",
    "Fugue Flounder",
    "Modal Bass"
]


def hire_technicians_individually(simulation, num_technicians, quarter):
    """
    Prompts the user to input names and specialties for a given number of technicians,
    and hires each technician immediately.
    """
    for _ in range(num_technicians):
        # Prompt for technician name
        name = ""
        while not name:
            name = input("Enter Technician Name: ").strip()
            if not name:
                print("Name cannot be empty. Please try again.")

        # Check if the technician has a specialty
        has_specialty = input("Does this technician have a specialty? (yes/no): ").strip().lower()
        
        if has_specialty == "yes":
            # Display fish specialties for selection
            print("\nSelect Fish Specialty (1-6):")
            for index, specialty in enumerate(fish_specialties, start=1):
                print(f"{index}. {specialty}")

            # Validate specialty selection
            specialty = 0
            while not (1 <= specialty <= 6):
                try:
                    specialty = int(input("Enter the number corresponding to the specialty: "))
                    if not (1 <= specialty <= 6):
                        print("Invalid selection. Please choose a number between 1 and 6.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            selected_specialty = fish_specialties[specialty - 1]
        else:
            # Assign a default or general specialty
            selected_specialty = "Generalist"

        # Hire the technician with the selected specialty
        simulation.hire_technicians(name, quarter, selected_specialty)

        print(f"{name} (Specialty: {selected_specialty}) hired for Quarter {quarter}.\n")

def main():
    """
    Main function to run the simulation.
    """
    num_quarters = get_positive_or_negative_int("Please enter number of quarters: ")
    simulation = Hatchery(Config, num_quarters)

    total_technicians = 0  # Tracks the total technicians over all quarters

    for quarter in range(1, num_quarters + 1):
        print(f"\n{'=' * 40}\n====== SIMULATING QUARTER {quarter} ======\n{'=' * 40}")

        num_technicians = get_positive_or_negative_int(
            "Enter number of technicians to add (positive) or remove (negative): "
        )
        total_technicians += num_technicians

        if num_technicians > 0:
            hire_technicians_individually(simulation, num_technicians, quarter)
        elif num_technicians < 0:
            simulation.remove_technicians(abs(num_technicians))

        simulation.simulate_quarter(quarter, total_technicians)
        simulation.prompt_restock()
        simulation.display_technicians()
        print(f"End of Quarter {quarter}")

    print("\nSimulation complete.")
    simulation.display_finances()

if __name__ == "__main__":
    main()


  