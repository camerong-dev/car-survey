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
    print("After finishing this introduction section")
    print("You'll us provide some personal details")
    print("Once filled out, you can then answer the questions which appear")
    print("Your results will then be stored on a spreadsheet")
    print("You can then view your results once completed")

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
    try:
        if ((values != "e") or (len(values) != 1)):
            raise ValueError(
                "Please enter 'e' and try again."
            )

    except ValueError as x:
        print(f"Whoops! Something went wrong. {x} \n")
        return False

    return True


def personal_information_name():
    """
    Users are requested to input their name
    """
    print("Please enter your name, including your surname")
    print("Example - Jane Doe\n")

    while True:
        name_input = input("Please enter your name here:\n")

        if name_check(name_input):
            print(f"Thank you {name_input}!")
            break
        print("-----------------------------------------------------------")

    return name_input


def personal_information_age():
    """
    Users are requested to input their age
    """
    while True:
        age_input = input("Please enter your age here:\n")

        if age_check(age_input):
            age_input = print("Thank you for telling us your age!")
            break
        print("-----------------------------------------------------------")

    return age_input


def name_check(values):
    """
    ValueError if user inputs numbers
    """
    try:
        if values.isdigit():
            raise ValueError(
                "Please enter a name and try again.\nExample: Jane Doe"
            )
    except ValueError as x:
        print(f"Whoops! Something went wrong. {x} \n")
        return False

    return True


def age_check(values):
    """
    ValueError if user inputs letters
    """
    try:
        if values.isalpha():
            raise ValueError(
                "Please enter an age and try again."
            )
    except ValueError as x:
        print(f"Whoops! Something went wrong. {x} \n")
        return False

    return True


introduction()
personal_information_name()
personal_information_age()
