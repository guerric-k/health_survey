import re
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('health_survey')
PATIENTS_WORKSHEET = SHEET.worksheet('patients')

min_temp = 33.2  # minimum normal temperature in °C
max_temp = 38.2  # maximum normal temperature in °C
min_height = 54.6  # minimum height in cm
max_height = 272.0  # maximum height in cm
min_weight = 5.5  # minimum weight in kg
max_weight = 635  # maximum weight in kg
min_age = 15  # minimum age of participants in the health survey
max_age = 100  # maximum age of participants
# maximum character length for medical condition
max_medical_condition_length = 200

# ANSI escape codes for red text
RED = "\033[91m"
RESET = "\033[0m"  # Reset to default color


def display_date_time():
    """
    Display the current version, date, and time in a readable format.
    """
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print("WELCOME TO HEALTH SURVEY AUTOMATED SYSTEMS \n")
    print(f"==== Version 1.0: {formatted_time} ==== \n")


display_date_time()


def get_patients_data():
    """
    Get patient name input from the user with validation.
    Ensures the name only contains alphabetic characters and each part begins
    with a capital letter.
    """
    while True:
        print("Please enter patient's Firstname and Surname.")
        print("If the patient is not in the system, you will be ")
        print("prompted to add the patient. \n")
        print("Example: John Crawford \n")

        name_str = input("Enter patient's name here: \n").strip()

        # Regular expression to validate the name format
        if re.fullmatch(r"^[A-Z][a-z]+(?: [A-Z][a-z]+)+$", name_str):
            print(f"Patient's name: {name_str}")
            print(f"Searching system for: {name_str}...")

            # Call function to search patient after validation
            search_patient_in_sheet(name_str)
            break

        else:
            print("Invalid input! Ensure each name starts with a ")
            print("capital letter, contains only letters, and has no special")
            print("characters. \n")
            print("Please try again.\n")
            print("----------------------------------------------\n")


def search_patient_in_sheet(name_str):
    """
    Searches for a patient by name in the 'patients' worksheet.
    Prints the row with patient details if found; otherwise, notifies the user
    if no match is found.
    """
    all_patients = PATIENTS_WORKSHEET.get_all_records()

    # Flag to track if a match is found
    found = False

    # Iterate over each record to find a match by name
    # Start at 2 to account for header row
    for index, patient in enumerate(all_patients, start=2):
        if patient['name'] == name_str:
            # Print the patient details
            print("\nPatient details found:")
            print(f"Name: {patient['name']}")
            print(f"Age: {patient['age']}")
            print(f"Temperature: {patient['temperature(°C)']}°C")
            print(f"Weight: {patient['weight (Kg)']} Kg")
            print(f"Height: {patient['height(cm)']} cm")
            print(
                f"Existing Medical Condition: "
                f"{patient['existing medical condition']}"
            )
            print(f"BMI: {patient['bmi']}\n")
            print("----------------------------------------------\n")
            found = True

            # Ask if user wants to update details
            update = input(
                f"Do you wish to update {name_str}'s details? (yes/no): "
            ).strip().lower()

            if update == 'yes':
                # Pass row index to update the same row
                add_new_patient(name_str, index)
            else:
                print("No updates made to patient details.\n")
                print("----------------------------------------------\n")
            break

    if not found:
        # If no match is found, notify the user
        print("\nNo records found with this name! ")
        print("Check and ensure that the name is correct.\n")
        print("----------------------------------------------\n")

        reply = input(
            f"Would you like to search again or add {name_str} as patient? "
            f"(search/add): "
        ).strip().lower()

        if reply == 'search':
            get_patients_data()

        elif reply == 'add':
            add_new_patient(name_str)
        else:
            print(
                "Invalid input! "
                "Please enter 'search' to try again or 'add' "
            )
            print("to add a new patient.\n")
            print("----------------------------------------------\n")


def add_new_patient(name_str, row=None):
    """
    Prompts the user to confirm if patient is new and, if yes, to enter
    patient details and validates each input before adding to the sheet.
    """
    response = input(
        f"Are you confirming to add {name_str}'s details in the system?"
        f"(yes/no): "
    ).strip().lower()

    if response == 'yes':
        print(f"Please enter the following details for: {name_str}:\n")
        print("----------------------------------------------\n")

        # Validates each entry before storing it
        while True:
            try:
                # Age validation: Age must be an Integer and within range
                while True:
                    age = int(input("Enter age: \n").strip())
                    if not (min_age <= age <= max_age):
                        raise ValueError(
                            f"Age must be "
                            f">= {min_age} and <= {max_age}years."
                        )
                    break  # Break loop if age is valid

                # Temperature validation
                while True:
                    temperature = float(input(
                        "Enter temperature (°C): \n"
                    ).strip())
                    if not (min_temp <= temperature <= max_temp):
                        print(
                            f"{RED}Caution!!! Temperature is out of range "
                            f"({min_temp} - {max_temp}°C).{RESET}"
                        )
                    break  # Temperature can be recorded even if out of range

                # Weight validation with retry loop
                while True:
                    weight = float(input("Enter weight (Kg): \n").strip())
                    if not (min_weight <= weight <= max_weight):
                        raise ValueError(
                            f"Weight must be between "
                            f"{min_weight} and {max_weight} Kg."
                        )
                    break  # Break loop if weight is valid

                # Height validation
                while True:
                    height = int(input("Enter height (cm): \n").strip())
                    if not (min_height <= height <= max_height):
                        raise ValueError(
                            f"Height must be between {min_height} and "
                            f"{max_height} cm."
                        )
                    break  # Break loop if height is valid

                # Calculate BMI
                bmi = round(weight / (height / 100) ** 2, 2)
                print(f"{name_str}'s BMI is: {bmi}\n")

                # Medical condition validation
                while True:
                    medical_condition = input(
                        f"Enter {name_str}'s existing medical condition "
                        f"(max {max_medical_condition_length} characters): "
                    ).strip()

                    if len(medical_condition) > max_medical_condition_length:
                        raise ValueError(
                            f"Medical condition should be less than "
                            f"{max_medical_condition_length} characters."
                        )
                    break  # Break loop if medical condition is valid

                confirm = input(
                    f"Do you confirm to add {name_str} to the system? "
                    "(yes/no): \n"
                ).strip().lower()

                if confirm == 'yes':
                    # Append new patient details to the worksheet
                    PATIENTS_WORKSHEET.append_row(
                        [name_str, age, temperature, weight, height,
                         medical_condition, bmi]
                    )
                    print("System updating...\n")
                    print(f"\nPatient {name_str} added successfully!\n")
                    print("----------------------------------------------\n")
                else:
                    print("Patient details not saved.\n")
                    print("----------------------------------------------\n")
                break

            except ValueError as e:
                print(f"Invalid input: {e}. Please enter the details again.\n")
                print("----------------------------------------------\n")

    elif response == 'no':
        print("Check the spelling and order of names, then try again.\n")
        print("----------------------------------------------\n")


get_patients_data()
