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
SHEET = GSPREAD_CLIENT.open('car_survey')


def introduction():
    """
    Introduces the user to the program.
    A short welcome message appears, followed by how it works
    """
    print("Welcome to the Car Survey!")
    print("This survey is collect as many different opinons on peoples cars")
    print("So everyone can have honest insight to these cars. \n")

    print("What happens:")
    print("After finishing this introduction section you will read the rules")
    print("Once you've read the rules, you'll then provide some personal info")
    print("Once filled out, you can then answer the questions which appear")
    print("Your results will then be stored on a spreadsheet")

    while True:
        introduction_input = input("Please enter letter 'e' and press enter\n")

        if introduction_input_check(introduction_input):
            print("Loading...")
            break
    print("------------------------------------------------------------------")

    return introduction_input


def introduction_input_check(values):
    """
    ValueError if input does not match letter 'e'
    ValueError if input is more than one letter
    """
    if values != "e":
        raise ValueError(
            "Invalid letter, please enter 'e' and try again."
        )
        return False

    if len(values) != 1:
        raise ValueError(
            "Too many characters, please enter 'e' and try again."
        )
        return False

    else:
        return True


introduction()