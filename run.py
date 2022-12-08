import gspread
from google.oauth2.service_account import Credentials
from datetime import date

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
    print("You can then view your results once completed\n")

    while True:
        introduction_input = input(
            "Please press the letter 'e' and press enter\n"
         )

        if introduction_input_check(introduction_input):
            print("\nLoading...")
            break
        personal_information_name()
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

    except ValueError as emsg:
        print(f"Whoops! Something went wrong. {emsg} \n")
        return False

    return True


def personal_information_name():
    """
    Users are requested to input their name
    """
    print("\nPlease enter your name, including your surname")
    print("Example - Jane Doe\n")

    while True:
        global name_input
        name_input = input("Please enter your name here:\n")

        if name_check(name_input):
            print(f"Thank you {name_input.title()}!")
            print("---------------------------------------------------------")
            break
        personal_information_age()

    return personal_information_name()


def personal_information_age():
    """
    Users are requested to input their age
    """
    while True:
        global age_input
        age_input = input("Please enter your age here:\n")

        if age_check(age_input):
            print("Thank you for telling us your age!\n")
            print("---------------------------------------------------------")
            break

    return personal_information_age()


def name_check(values):
    """
    ValueError if user inputs numbers
    """
    try:
        if values.isdigit():
            raise ValueError(
                "Please enter a name and try again.\nExample: Jane Doe"
            )
    except ValueError as emsg:
        print(f"Whoops! Something went wrong. {emsg} \n")
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

    except ValueError as emsg:
        print(f"Whoops! Something went wrong. {emsg} \n")
        return False

    return True


def car_info_intro():
    """
    Introduction for the user
    to provide basic info
    of their car
    """
    print("Thank you " + str(name_input).title() + " for your details.")
    print(
        "We are now going to ask some basic questions about your car\n"
    )
    car_info_make()


def car_info_make():
    """
    Asks for user to input car manufacturer
    """
    while True:
        global car_make
        car_make = input("Please enter the car manufacter here:\n")

        if car_make_check(car_make):
            car_info_model()
            break
        return car_info_make()


def car_info_model():
    """
    Asks user to input car model
    """
    while True:
        global car_model
        car_model = input("\nPlease enter the car model here:\n")

        car_info_year()
        return car_info_model()


def car_info_year():
    """
    Asks user to input car year
    """
    while True:
        global car_year
        car_year = input("\nPlease enter the year of the car here:\n")

        if car_year_check(car_year):
            car_info_check()
            return car_info_year()


def car_make_check(values):
    """
    ValueError if user inputs numbers
    """
    try:
        if values.isdigit():
            raise ValueError(
                "Please enter a valid manufacturer and try again.\n"
            )
    except ValueError as emsg:
        print(f"Whoops! Something went wrong. {emsg} \n")
        return False

    return True


def car_year_check(values):
    """
    ValueError if user inputs letters
    """
    try:
        if values.isalpha():
            raise ValueError(
                "Please enter a valid year and try again.\nExample: 2003"
            )
    except ValueError as emsg:
        print(f"Whoops! Something went wrong. {emsg} \n")
        return False

    return True


def car_info_check():
    """
    Checks that user is happy with inputs
    """
    print("\nThank you for the details.")
    print("Please confirm the following:\n")
    print("Car Manufacturer: " + car_make.title())
    print("Car Model: " + car_model.title())
    print("Car Year: " + car_year + "\n")

    while True:
        car_info_check_result = input(
            "Please select 'a' to continue. To retry please select 'r':\n"
        )

        if car_info_check_result == "a":
            question_one()
            return False
        
        if car_info_check_result == "r":
            car_info_make()
            return False

        print("Whoops! Something went wrong.")
        print("Please select either 'a' or 'r'.\n")

    
def question_one():
    """
    First question for user to answer
    """
    print("We will now begin asking you questions")
    print("Please answer truthfully, as this helps other people")
    print("\n")
    print("-----------------------------------------------")
    print("\n1) What year did you come into ownership of this car?")

    while True:
        global year_of_ownership
        year_of_ownership = input(
            "Please input the year here:\n"
        )

        if question_one_check(year_of_ownership):
            question_two()
            return question_one()


def question_one_check(values):
    """
    ValueError appears if user inputs letters
    """
    try:
        if values.isalpha():
            raise ValueError(
                "Please enter a valid year and try again.\nExample: 2003"
            )
    except ValueError as emsg:
        print(f"Whoops! Something went wrong. {emsg} \n")
        return False

    return True


def question_two():
    print("Hello")


def main():
    """
    Contains all major functions
    """
    introduction()
    car_info_intro()


main()
