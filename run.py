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

min_temp = 26.0 # minimum normal temperature in °C
max_temp = 38.0 # maximum normal temperature in °C
min_height = 61.0 # minimum height in cm
max_height = 260.0 # maximum height in cm
min_weight = 5.5 # minimum weight in kg
max_weight = 700 # maximum weight in kg
min_age = 15 # minimum age of participants in the health survey is 15 years
max_age = 120 # maximum age of participants in the health survey is 120 years
max_medical_condition_length = 200  # maximum character length for medical condition

print("WELCOME TO HEALTH SURVEY AUTOMATED SYSTEM. \n")
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
        print("\nNo records found with this name! Check and ensure that the name is correct.\n")
        reply = input(f"Would you like to Enter the name again or Add {name_str} as a new patient? (enter/add): ").strip().lower()
        
        if reply == 'enter':
            get_patients_data()
            
        elif reply == 'add':
            add_new_patient(name_str)
        else:
            print("Invalid input. Please enter 'enter' to search again or 'add' to add a new patient.\n")

def add_new_patient(name_str):
    """
    Prompts the user to confirm if patient is new and, if yes, to enter patient details.
    Validates each input before adding to the sheet.
    """  
    response = input(f"Are you confirming {name_str} is a new patient? (yes/no): ").strip().lower()
    if response == 'yes':
        print(f"Please enter the following details for: {name_str}:\n")


        #Validates each entry befor storing it 
        while True:
            try:

                #Age validation: Age must be an Integer and within range
                # Age validation with retry loop
                while True:
                    age = int(input("Enter age: ").strip())
                    if age < min_age:
                        raise ValueError(f"Age must be at least {min_age} years.")
                    break  # Break loop if age is valid

                # Temperature validation (it must be a float in the range of min_temp and max_temp defined above)
                # Temperature validation
                while True:
                    temperature = float(input("Enter temperature (°C): ").strip())
                    if not (min_temp <= temperature <= max_temp):
                        print(f"Caution!!! Temperature is out of range ({min_temp} - {max_temp}°C).")
                    break  # Proceed regardless, as temperature can be recorded even if out of range

                # Weight validation: must be a float within min and max weight range
                # Weight validation with retry loop
                while True:
                    weight = float(input("Enter weight (Kg): ").strip())
                    if not (min_weight <= weight <= max_weight):
                        raise ValueError(f"Weight must be between {min_weight} and {max_weight} Kg.")
                    break  # Break loop if weight is valid

                # Height validation: must be an integer within min and max height range
                # Height validation with retry loop
                while True:
                    height = int(input("Enter height (cm): ").strip())
                    if not (min_height <= height <= max_height):
                        raise ValueError(f"Height must be between {min_height} and {max_height} cm.")
                    break  # Break loop if height is valid

                # Calculate BMI
                bmi = round(weight / (height / 100) ** 2, 2)
                print(f"{name_str}'s BMI is: {bmi}\n")

                # Medical condition (must be a string, no special validation applied here)
                # Medical condition validation
                while True:
                    medical_condition = input(f"Enter {name_str}'s existing medical condition (max {max_medical_condition_length} characters): ").strip()
                    if len(medical_condition) > max_medical_condition_length:
                        raise ValueError(f"Medical condition should be less than {max_medical_condition_length} characters.")
                    break  # Break loop if medical condition is valid
                
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
