import gspread
import pandas as pd
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
    print("\n\nWelcome to the Car Survey!\n")
    print("What happens:")
    print("After finishing this introduction section")
    print("You'll have the choice to complete a survey or find a survey")
    print("\nIf completing a survey:")
    print("You'll us provide some personal details")
    print("Once filled out, you can then answer the questions which appear")
    print(
        "Your results will then be stored on a spreadsheet for others to see"
        )
    print("\nIf finding a survey:")
    print("You'll provide us the make, model and year of car")
    print("Then we will search for all available surveys of that car\n")

    while True:
        introduction_input = input(
            "Please press the letter 'e' and press enter\n"
         )

        if introduction_input_check(introduction_input):
            print("\nLoading...")
            break
    user_choice()

    return introduction_input


def introduction_input_check(values):
    """
    Error displayed if user inputs letter other than e
    """
    try:
        if ((values != "e") or (len(values) == 0)):
            raise ValueError(
                "Please enter 'e' and try again"
            )
    except ValueError as emsg:
        print(f"\nWhoops! Something went wrong. {emsg} \n")
        return False

    return True


def user_choice():
    """
    Giving user the choice of finding a car or doing the survey
    """
    print("\nWould you like to:")
    print("A) Complete the survey")
    print("B) Find existing surveys")

    user_choice_input = input("\nPlease select either 'a' or 'b':\n")

    if user_choice_input == "a":
        personal_information_name()
        return False

    if user_choice_input == "b":
        import_all_values()
        return False

    print("Whoops! Something went wrong.")
    print("Please select either 'y' or 'n'.\n")


def personal_information_name():
    """
    Users are requested to input their name
    """
    print("\nPlease enter your name, including your surname")
    print("Example - Jane Doe\n")

    while True:
        name_input = input("Please enter your name here:\n")

        if name_check(name_input):
            print(f"\nThank you {name_input.title()}!")
            print("---------------------------------------------------------")
            break

    personal_information_age()

    global username
    username = name_input

    return name_input


def personal_information_age():
    """
    Users are requested to input their age
    """
    while True:
        age_input = input("Please enter your age here:\n")

        if age_check(age_input):
            print("\nThank you for this!\n")
            print("---------------------------------------------------------")
            break

    global user_age
    user_age = age_input


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
        print(f"\nWhoops! Something went wrong. {emsg} \n")
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
        print(f"\nWhoops! Something went wrong. {emsg} \n")
        return False

    return True


def car_info_intro():
    """
    Introduction for the user
    to provide basic info
    of their car
    """
    name_input = username
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
        return car_info_year()


def car_info_model():
    """
    Asks user to input car model
    """
    while True:
        global car_model
        car_model = input("\nPlease enter the car model here:\n")

        car_info_year()
        break
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
    print("Car Year: " + car_year)

    while True:
        car_info_check_result = input(
            "\nSelect 'y' to continue. To retry please select 'n':\n"
        )

        if car_info_check_result == "y":
            question_one()
            return False

        if car_info_check_result == "n":
            car_info_make()
            return False

        print("\nWhoops! Something went wrong.")
        print("Please select either 'y' or 'n'.")


def question_one():
    """
    First question for user to answer
    """
    print("\n\nWe will now ask you some questions")
    print("Please answer to the best of your ability")
    print("As this can provide helpful insights for others.")
    print("-----------------------------------------------")
    print("\n1) What year did you come into ownership of this car?")

    while True:
        global one_input
        one_input = input(
            "\nPlease input the year here:\n"
        )

        if question_one_check(one_input):
            question_two()


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
        print(f"\nWhoops! Something went wrong. {emsg} \n")
        return False

    return True


def question_two():
    """
    Second question for user to answer
    """
    print("\n2) List two things you like about your car")
    print("   eg - Sound of car, comfortable seats \n")
    global two_input
    two_input = input("Please answer here:\n")

    question_three()


def question_three():
    """
    Third question for user to answer
    """
    print("\n3) List two thing you dislike about your car")
    print("   eg - Stiff ride, cheap feeling interior \n")
    global three_input
    three_input = input("Please answer here:\n")

    final_check()


def final_check():
    """
    Prompt for user to confirm updating worksheet
    """
    user_inputs = [
        username, user_age, car_make, car_model, car_year,
        one_input, two_input, three_input]
    print("\nAre you happy with your inputs?\n")
    print("1) " + one_input)
    print("2) " + two_input)
    print("3) " + three_input)
    final_check_answer = input("\nPlease answer Yes 'y' or No 'n':\n")

    if final_check_answer == "y":
        update_worksheet(user_inputs)
        return False

    if final_check_answer == "n":
        introduction()
        return False

    print("Whoops! Something went wrong.")
    print("Please select either 'y' or 'n'.\n")

    return user_inputs


def update_worksheet(results):
    """
    Updating spreadsheet, adds new row
    """
    print("\nUpdating worksheet...")
    survey_sheet = SHEET.worksheet("survey_answers")
    survey_sheet.append_row(results)
    print("Worksheet updated\n\n")
    end_of_survey()


def end_of_survey():
    """
    Giver user choice to view surveys or complete another
    """
    print("Thank you for completing this survey!")
    print("Would you like to:\n")
    print("A) View other surveys")
    print("B) Exit the program")

    while True:
        end_of_survey_result = input(
            "\nPlease select 'a' or 'b':\n"
        )

        if end_of_survey_result == "a":
            import_all_values()
            return False

        if end_of_survey_result == "b":
            exit()
            return False

        print("\nWhoops! Something went wrong.")


def import_all_values():
    """
    Imports all values on spreadsheet into dataframe
    """
    survey_sheet = SHEET.worksheet("survey_answers")
    data = survey_sheet.get_all_values()
    global table
    table = pd.DataFrame(data, columns=[
        'Name: ', 'Age: ', 'Make Of Car: ', 'Model Of Car: ',
        'Year Of Car: ', 'Year Of Ownership: ',
        'Pros: ', 'Cons: '
        ])
    input_choice()


def input_choice():
    """
    Give user different choices for filtering surveys
    """
    print("\nHow would you like to filter the surveys?\n")
    print("A) By manufacturer")
    print("B) By manufacturer and model")
    print("C) By manufacturer, model and year")
    print("D) By manufacturer and year")
    print("E) By year")

    while True:
        input_choice_answer = input(
             "\nPlease select 'a' , 'b' , 'c' , 'd' or 'e':\n"
        )

        if input_choice_answer == "a":
            find_survey_input_one()
            return False

        if input_choice_answer == "b":
            find_survey_input_two_p1()
            return False

        if input_choice_answer == "c":
            exit()
            return False

        print("\nWhoops! Something went wrong.")


def find_survey_input_one():
    """
    Asks user for car make to search in spreadsheet
    """
    global find_survey_manufacturer
    find_survey_manufacturer = input(
        "\nPlease enter the manufacturer below:\n"
    )
    if find_survey_manufacturer_check(find_survey_manufacturer):
        start_search_one()
        
    return find_survey_input_one()


def find_survey_input_two_p1():
    """
    Asks user for car manufacturer to search in spreadsheet
    """
    global find_man_model_p1
    find_man_model_p1 = input(
        "\nPlease enter the manufacturer below:\n"
    )
    if find_survey_input_two_p1_check(find_man_model_p1):
        find_survey_input_two_p2()

    return find_survey_input_two_p1()


def find_survey_input_two_p2():
    """
    Asks user for car model to search in spreadsheet
    """
    global find_man_model_p2
    find_man_model_p2 = input(
        "\nPlease enter the model below:\n"
    )
    if find_survey_input_two_p2_check(find_man_model_p2):
        start_search_two()
    
    return find_survey_input_two_p2()


def find_survey_input_three():
    """
    Asks user for car year to search in spreadsheetS
    """
    while True:
        global find_survey_year
        find_survey_year = input(
            "Please enter the year below:\n"
        )
        if find_survey_input_three_check(find_survey_year):
            start_search_one()
        return find_survey_input_three()


def find_survey_manufacturer_check(values):
    """
    ValueError if user inputs numbers or leaves
    """
    try:
        if (values.isdigit() or (len(values) == 0)):
            raise ValueError(
                "Please enter a valid manufacturer and try again.\n"
            )
    except ValueError as emsg:
        print(f"Whoops! Something went wrong. {emsg} \n")
        return False

    return True


def find_survey_input_two_p1_check(values):
    """
    ValueError if user inputs numbers or leaves blank
    """
    try:
        if (values.isdigit() or (len(values) == 0)):
            raise ValueError(
                "Please enter a valid manufacturer and try again.\n"
            )
    except ValueError as emsg:
        print(f"Whoops! Something went wrong. {emsg} \n")
        return False

    return True


def find_survey_input_two_p2_check(values):
    """
    ValueError if user leaves blank
    """
    try:
        if (len(values) == 0):
            raise ValueError(
                "Please enter a valid model and try again.\n"
            )
    except ValueError as emsg:
        print(f"Whoops! Something went wrong. {emsg} \n")
        return False

    return True


def find_survey_input_three_check(values):
    """
    ValueError if user inputs letters
    """
    try:
        if values.isalpha()():
            raise ValueError(
                "Please enter a valid year and try again.\n"
            )
    except ValueError as emsg:
        print(f"Whoops! Something went wrong. {emsg} \n")
        return False

    return True


def start_search_one():
    """
    Searches spreadsheet with manufacturer user inputted
    """
    filter_one = table[table['Make Of Car: '] == find_survey_manufacturer]
    print("\n")
    print(filter_one)

    print("\n\nThank you for checking out this survey.")

    while True:
        input_one_choice = input(
            "\nPlease select 'e' to exit program: \n"
        )

        if input_one_choice == "e":
            exit()
            return False

        print("\nWhoops! Something went wrong.")


def start_search_two():
    """
    Searches spreadsheet with manufacturer and model user inputted
    """
    filter_two = \
        table[(table['Make Of Car: '] == find_man_model_p1) \
            & (table['Model Of Car: '] == find_man_model_p2)]
    print("\n")
    print(filter_two)

    print("\n\nThank you for checking out this survey.")

    while True:
        input_one_choice = input(
            "\nPlease select 'e' to exit program: \n"
        )

        if input_one_choice == "e":
            exit()
            return False

        print("\nWhoops! Something went wrong.")


def main():
    """
    Contains all major functions
    """
    introduction()
    car_info_intro()


main()
