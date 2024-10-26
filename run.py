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
        
        if re.fullmatch(r"^[A-Z][a-z]+(?: [A-Z][a-z]+)+$", name_str):
        
        # r"^[A-Z][a-z]+(?: [A-Z][a-z]+)+$: expression to validate name format
        # - ^ and $: Anchors to ensure the pattern matches the entire string.
        # - [A-Z][a-z]+: Matches names that start with a capital letter followed by lowercase letters.
        # - (?: [A-Z][a-z]+)+$: Ensures the second name follows the same pattern.
            
            print(f"Patient's name: {name_str}")
            break
        else:
            print("Invalid input! Ensure each name starts with a capital letter, contains only letters, and has no special characters.")
            print("Please try again.\n")

get_patients_data()


