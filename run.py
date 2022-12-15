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
        if ((values != "e") or (len(values) == 0) or (len(values) >= 2)):
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
        main()
        return False

    if user_choice_input == "b":
        import_all_values()
        return False

    if user_choice_input != "a" or "b":
        print("\nWhoops! Something went wrong.")
        print("Please select either 'a' or 'b'.\n")
        user_choice()
        return False


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
    username = name_input.lower()

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
    ValueError if user inputs numbers or leaves blank
    """
    try:
        if ((values.isdigit()) or (len(values) == 0)):
            raise ValueError(
                "Please enter a name and try again.\nExample: Jane Doe"
            )
    except ValueError as emsg:
        print(f"\nWhoops! Something went wrong. {emsg} \n")
        return False

    return True


def age_check(values):
    """
    ValueError if user inputs letters, leaves blank or more than 3 digits
    """
    try:
        if (
            (values.isalpha()) or (len(str(values)) <= 1) or
                (len(str(values)) >= 3)):
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
    print("Thank you " + str(username).title() + " for your details.")
    print(
        "We are now going to ask some basic questions about your car:"
    )
    car_info_make()


def car_info_make():
    """
    Asks for user to input car manufacturer
    """
    while True:
        global car_make
        car_make = input("\nPlease enter the car manufacter here:\n").lower()

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
        car_model = input("\nPlease enter the car model here:\n").lower()

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
    ValueError if user inputs numbers or leaves blank
    """
    try:
        if ((values.isdigit()) or (len(values) == 0)):
            raise ValueError(
                "Please enter a valid manufacturer and try again.\n"
            )
    except ValueError as emsg:
        print(f"Whoops! Something went wrong. {emsg} \n")
        return False

    return True


def car_year_check(values):
    """
    ValueError if user inputs letters, inputs year less or more than 4 digits
    """
    try:
        if ((values.isalpha()) or (len(values) >= 5) or (len(values) <= 3)):
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

        if car_info_check_result != "y" or "n":
            print("\nWhoops! Something went wrong.")
            print("Please select either 'y' or 'n'.")
        

def question_one():
    """
    First question for user to answer
    """
    print("\n\nWe will now ask you some questions")
    print("Please answer to the best of your ability")
    print("Note a maximum character count of 15 per answer.")
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
    ValueError appears if user inputs letters, less or more than 4 digits
    """
    try:
        if ((values.isalpha()) or (len(values) >= 5) or (len(values) <= 3)):
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
    print("   e.g. - Sound of car, comfortable seats \n")
    print("\n   Please answer using 15 characters or less\n")

    while True:
        global two_input
        two_input = input(
            "Please answer here:\n"
        )

        if question_two_check(two_input):
            question_three()


def question_two_check(values):
    """
    ValueError appears if user leaves blank or enters more than 15 characters
    """
    try:
        if ((len(values) == 0) or (len(values) >= 15)):
            raise ValueError(
                "Please answer using 15 characters or less.\n"
            )
    except ValueError as emsg:
        print(f"\nWhoops! Something went wrong. {emsg} \n")
        return False

    return True


def question_three():
    """
    Third question for user to answer
    """
    print("\n3) List two thing you dislike about your car")
    print("   e.g. - Stiff ride, cheap feeling interior \n")
    print("\n   Please answer using 15 characters or less\n")

    while True:
        global three_input
        three_input = input(
            "Please answer here:\n"
        )

        if question_three_check(three_input):
            final_check()


def question_three_check(values):
    """
     ValueError appears if user leaves blank or enters more than 15 characters
    """
    try:
        if ((len(values) == 0) or (len(values) >= 15)):
            raise ValueError(
                "Please answer using 15 characters or less.\n"
            )
    except ValueError as emsg:
        print(f"\nWhoops! Something went wrong. {emsg} \n")
        return False

    return True


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
        question_one()
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
    print("B) Complete another survey")
    print("C) Exit the program")

    while True:
        end_of_survey_result = input(
            "\nPlease select 'a', 'b' or 'c':\n"
        )

        if end_of_survey_result == "a":
            import_all_values()
            return False

        if end_of_survey_result == "b":
            reset_survey_inputs()
            return False

        if end_of_survey_result == "c":
            exit()
            return False

        print("\nWhoops! Something went wrong.")


def reset_survey_inputs():
    username = None
    user_age = None
    car_make = None
    car_model = None
    car_year = None

    main()


def import_all_values():
    """
    Imports all values on spreadsheet into dataframe
    """
    survey_sheet = SHEET.worksheet("survey_answers")
    data = survey_sheet.get_all_values()
    global table
    table = pd.DataFrame(data, columns=[
        'Name: ', 'Age: ', 'Make Of Car: ', 'Model Of Car: ',
        'Year Of Car: ', 'Owned Since: ',
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
            find_survey_input_three_p1()
            return False

        if input_choice_answer == "d":
            find_survey_input_four_p1()
            return False

        if input_choice_answer == "e":
            find_survey_input_five()
            return False

        print("\nWhoops! Something went wrong.")


def find_survey_input_one():
    """
    Asks user for car make to search in spreadsheet
    """
    global display_manufacturer
    display_manufacturer = input(
        "\nPlease enter the manufacturer below:\n"
    )
    if find_survey_manufacturer_check(display_manufacturer):
        start_search_one()

    return find_survey_input_one()


def find_survey_input_two_p1():
    """
    Asks user for car manufacturer to search in spreadsheet
    """
    global display_mm1
    display_mm1 = input(
        "\nPlease enter the manufacturer below:\n"
    )
    if find_survey_input_two_p1_check(display_mm1):
        find_survey_input_two_p2()

    return find_survey_input_two_p1()


def find_survey_input_two_p2():
    """
    Asks user for car model to search in spreadsheet
    """
    global display_mm2
    display_mm2 = input(
        "\nPlease enter the model below:\n"
    )
    if find_survey_input_two_p2_check(display_mm2):
        start_search_two()

    return find_survey_input_two_p2()


def find_survey_input_three_p1():
    """
    Asks user for car manufacturer to search in spreadsheet
    """
    while True:
        global display_mmy1
        display_mmy1 = input(
            "\nPlease enter the Manufacturer below:\n"
        )
        if find_survey_input_three_p1_check(display_mmy1):
            find_survey_input_three_p2()
        return find_survey_input_three_p1()


def find_survey_input_three_p2():
    """
    Asks user for car model to search in spreadsheet
    """
    while True:
        global display_mmy2
        display_mmy2 = input(
            "\nPlease enter the model below:\n"
        )
        if find_survey_input_three_p2_check(display_mmy2):
            find_survey_input_three_p3()
        return find_survey_input_three_p2()


def find_survey_input_three_p3():
    """
    Asks user for car year to search in spreadsheet
    """
    while True:
        global display_mmy3
        display_mmy3 = input(
            "\nPlease enter the year below:\n"
        )
        if find_survey_input_three_p3_check(display_mmy3):
            start_search_three()
        return find_survey_input_three_p3()


def find_survey_input_four_p1():
    """
    Asks user for car manufacturer to search in spreadsheet
    """
    while True:
        global display_my1
        display_my1 = input(
            "\nPlease enter the Manufacturer below:\n"
        )
        if find_survey_input_four_p1_check(display_my1):
            find_survey_input_four_p2()
        return find_survey_input_four_p1()


def find_survey_input_four_p2():
    """
    Asks user for car year to search in spreadsheet
    """
    while True:
        global display_my2
        display_my2 = input(
            "\nPlease enter the year:\n"
        )
        if find_survey_input_four_p2_check(display_my2):
            start_search_four()
        return find_survey_input_four_p2()


def find_survey_input_five():
    """
    Asks user for car year to search in spreadsheet
    """
    while True:
        global display_y1
        display_y1 = input(
            "\nPlease enter the year:\n"
        )
        if find_survey_input_five_check(display_y1):
            start_search_five()
        return find_survey_input_five()


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


def find_survey_input_three_p1_check(values):
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


def find_survey_input_three_p2_check(values):
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


def find_survey_input_three_p3_check(values):
    """
    ValueError if user inputs letters or leaves blank
    """
    try:
        if (values.isalpha() or (len(values) == 0)):
            raise ValueError(
                "Please enter a valid year and try again.\n"
            )
    except ValueError as emsg:
        print(f"Whoops! Something went wrong. {emsg} \n")
        return False

    return True


def find_survey_input_four_p1_check(values):
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


def find_survey_input_four_p2_check(values):
    """
    ValueError if user inputs letters or leaves blank
    """
    try:
        if (values.isalpha() or (len(values) == 0)):
            raise ValueError(
                "Please enter a valid year and try again.\n"
            )
    except ValueError as emsg:
        print(f"Whoops! Something went wrong. {emsg} \n")
        return False

    return True


def find_survey_input_five_check(values):
    """
    ValueError if user inputs letters or leaves blank
    """
    try:
        if (values.isalpha() or (len(values) == 0)):
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
    filter_one = table[table['Make Of Car: '] == display_manufacturer]
    print("\n")

    any_value = len(filter_one.index)

    if any_value == 0:
        print("Sorry, no surveys match your search.")

    else:
        print(filter_one)
        print("\n\nThank you for checking this out!")

    while True:
        print("\nWould you like to:")
        print("A) Search for more surveys")
        print("B) Fill out a survey")
        print("C) Exit the program")

        input_choice = input(
            "\nPlease select 'a', 'b' or 'c': \n"
        )

        if input_choice == "a":
            reset_filters()
            return False

        if input_choice == 'b':
            main()
            return False

        if input_choice == "c":
            exit()
            return False

        print("\nWhoops! Something went wrong.")


def start_search_two():
    """
    Searches spreadsheet with manufacturer and model user inputted
    """
    con_one = table['Make Of Car: '] == display_mm1
    con_two = table['Model Of Car: '] == display_mm2
    filter_two = table[con_one & con_two]
    print("\n")

    any_value = len(filter_two.index)

    if any_value == 0:
        print("Sorry, no surveys match your search.")

    else:
        print(filter_two)
        print("\n\nThank you for checking this out!")

    while True:
        print("\nWould you like to:")
        print("A) Search for more surveys")
        print("B) Fill out a survey")
        print("C) Exit the program")

        input_choice = input(
            "\nPlease select 'a', 'b' or 'c': \n"
        )

        if input_choice == "a":
            reset_filters()
            return False

        if input_choice == 'b':
            main()
            return False

        if input_choice == "c":
            exit()
            return False

        print("\nWhoops! Something went wrong.")


def start_search_three():
    """
    Search spreadsheet with manufacturer, model and year user inputted
    """
    con_one = table['Make Of Car: '] == display_mmy1
    con_two = table['Model Of Car: '] == display_mmy2
    con_three = table['Year Of Car: '] == display_mmy3
    filter_three = table[con_one & con_two & con_three]
    print("\n")

    any_value = len(filter_three.index)

    if any_value == 0:
        print("Sorry, no surveys match your search.")

    else:
        print(filter_three)
        print("\n\nThank you for checking this out!")

    while True:
        print("\nWould you like to:")
        print("A) Search for more surveys")
        print("B) Fill out a survey")
        print("C) Exit the program")

        input_choice = input(
            "\nPlease select 'a', 'b' or 'c': \n"
        )

        if input_choice == "a":
            reset_filters()
            return False

        if input_choice == 'b':
            main()
            return False

        if input_choice == "c":
            exit()
            return False

        print("\nWhoops! Something went wrong.")


def start_search_four():
    """
    Search spreadsheet for manufacturer and year user inputted
    """
    con_one = table['Make Of Car: '] == display_my1
    con_two = table['Year Of Car: '] == display_my2
    filter_four = table[con_one & con_two]
    print("\n")

    any_value = len(filter_four.index)

    if any_value == 0:
        print("Sorry, no surveys match your search.")

    else:
        print(filter_four)
        print("\n\nThank you for checking this out!")

    while True:
        print("\nWould you like to:")
        print("A) Search for more surveys")
        print("B) Fill out a survey")
        print("C) Exit the program")

        input_choice = input(
            "\nPlease select 'a', 'b' or 'c': \n"
        )

        if input_choice == "a":
            reset_filters()
            return False

        if input_choice == 'b':
            main()
            return False

        if input_choice == "c":
            exit()
            return False

        print("\nWhoops! Something went wrong.")


def start_search_five():
    """
    Search spreadsheet for year user inputted
    """
    filter_five = table[table['Year Of Car: '] == display_y1]
    print("\n")

    any_value = len(filter_five.index)

    if any_value == 0:
        print("Sorry, no surveys match your search.")

    else:
        print(filter_five)
        print("\n\nThank you for checking this out!")

    while True:
        print("\nWould you like to:")
        print("A) Search for more surveys")
        print("B) Fill out a survey")
        print("C) Exit the program")

        input_choice = input(
            "\nPlease select 'a', 'b' or 'c': \n"
        )

        if input_choice == "a":
            reset_filters()
            return False

        if input_choice == 'b':
            main()
            return False

        if input_choice == "c":
            exit()
            return False

        print("\nWhoops! Something went wrong.")


def reset_filters():
    """
    Resets user inputs for the filters they used to search
    """
    display_manufacturer = None
    display_mm1 = None
    display_mm2 = None
    display_mmy1 = None
    display_mmy2 = None
    display_mmy3 = None
    display_my1 = None
    display_my2 = None
    display_y1 = None

    import_all_values()


def main():
    """
    Contains key function starting points
    """
    personal_information_name()
    car_info_intro()


introduction()
user_choice()
main()
