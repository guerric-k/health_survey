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
    
get_patients_data()
