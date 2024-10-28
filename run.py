import re
import gspread
from google.oauth2.service_account import Credentials

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

min_temp = 35.0
max_temp = 40.0

def get_patients_data():
    """
    Get patient name input from the user with validation.
    Ensures the name only contains alphabetic characters and each part begins with a capital letter.
    """

    while True:
        print("Please enter patient's Firstname and Surname.")
        print("Example: John Crawford \n")
        name_str = input("Enter patient's name here: ").strip()
        
        # r"^[A-Z][a-z]+(?: [A-Z][a-z]+)+$ Regular expression to validate the name format

        if re.fullmatch(r"^[A-Z][a-z]+(?: [A-Z][a-z]+)+$", name_str):
            print(f"Patient's name: {name_str}")
            print(f"Searching system for: {name_str}...")
            search_patient_in_sheet(name_str) # Call function to search patient after validation
            break  
        else:
            print("Invalid input! Ensure each name starts with a capital letter, contains only letters, and has no special characters.")
            print("Please try again.\n")

def search_patient_in_sheet(name_str):
    """
    Searches for a patient by name in the 'patients' worksheet.
    Prints the row with patient details if found; otherwise, notifies the user if no match is found.
    """
    all_patients = PATIENTS_WORKSHEET.get_all_records()

    # Flag to track if a match is found
    found = False

    # Iterate over each record to find a match by name
    for patient in all_patients:
        if patient['name'] == name_str:  
            # Print the patient details
            print("\nPatient details found:")
            print(f"Name: {patient['name']}")
            print(f"Age: {patient['age']}")
            print(f"Temperature: {patient['temperature(°C)']}°C")
            print(f"Weight: {patient['weight (Kg)']} Kg")
            print(f"Height: {patient['height(cm)']} cm")
            print(f"Existing Medical Condition: {patient['existing medical condition']}")
            print(f"BMI: {patient['bmi']}\n")
            
            found = True
            break

    if not found:
        # If no match is found, notify the user
        print("No records found with this name! Check the name and try again.\n")
        add_new_patient(name_str)

def add_new_patient(name_str):
    """
    Prompts the user to confirm if patient is new and, if yes, to enter patient details.
    Validates each input before adding to the sheet.
    """  
    response = input("Is this a new patient? (yes/no): ").strip().lower()
    if response == 'yes':
        print(f"Please enter the following details for: {name_str}:\n")


        #Validates each entry befor storing it 
        while True:
            try:

                #Age validation: Age must be an Integer
                age = int(input("Enter age: ").strip())

                # Temperature validation (it must be a float in the range of min_temp and max_temp defined above)
                temperature = float(input("Enter temperature (°C): ").strip())
                if temperature < min_temp or temperature > max_temp:
                    print("Caution!!! Temperature is out of range.")

                # Validate weight (must be a float)
                weight = float(input("Enter weight (Kg): ").strip())

                # Validate height (must be an integer)
                height = int(input("Enter height (cm): ").strip())

                # Calculate BMI
                bmi = round(weight / (height / 100) ** 2, 2)
                print(f"{name_str}'s BMI is: {bmi})

                # Medical condition (must be a string, no special validation applied here)
                medical_condition = input(f"Enter {name_str}'s existing medical condition: ").strip()
                
                confirm = input(f"Do you want to add {name_str} to the system? (yes/no): \n").strip().lower()
                if confirm == 'yes':
                    # Append new patient details to the worksheet
                    PATIENTS_WORKSHEET.append_row([name_str, age, temperature, weight, height, medical_condition, bmi])
                    print(f"\nPatient {name_str} added successfully!\n")
                else:
                    print("Patient details not saved.\n")
                break

            except ValueError as e:
                print(f"Invalid input: {e}. Please enter the details again.\n")

    elif response == 'no':
        print("Check the spelling and order of names, then try again.\n")


get_patients_data()
