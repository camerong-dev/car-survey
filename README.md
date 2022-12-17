# Car Survey

Car Survey allows users to fill out a basic survey and search for existing surveys based on either manufacturer, model and/or year.

## Live site
[Car Survey](https://car-survey.herokuapp.com/)

## Project Goals

The idea of Car Survey was for people in the market of purchasing a car, be able to easily view surveys of real world owners of the vehicle.  From this idea I wanted to:

  - To enter basic vehicle details
  - To enter basic user details
  - Save this data to an external spreadsheet
  - Import back into the program and print when required
  
## Database Structure

Google Sheets is used to store all user inputs. 

Table consists of 8 columns: Name, Age, Make Of Car, Model Of Car, Year Of Car, Owned Since, Pros and Cons.

![Image of Database](docs/img/database-titles.jpg)

Each column has individually assigned values that the end user has entered.  Each of the inputs have maximum character limits, exceeding them will display an error and prompt the user to try again. 

## Features

### Introduction

Start screen of the program consists of a welcome message, an explanantion of the program and one option.  The input is validated and an error is thrown if it does not match the requirements.

![Image of introduction](docs/img/introduction.jpg)

### Complete Survey or Find Survey

Here the user as the option of either completing a survey or finding a survey.  The input is validated and an error is thrown if it does not match the requirements.

![Image of a user choice](docs/img/user-choice.jpg)

### Name Input

The user can enter their name, including their surname if desired.  The input is validated and an error is thrown if the input includes numbers, is left blank or if the input exceeds 20 characters.

![Image of name input](docs/img/name-input.jpg)

### Age Input

The user can enter their age here.  Input is validated and an error is thrown if the input includes letters, left blank or exceeds 3 digits.

![Image of age input](docs/img/age-input.jpg)

### Manufacturer Input (Completing Survey)

The user can enter the manufacturer of their car. Input is validated and an error is thrown if the input contains numbers, is left blank or exceeds 20 characters.

![Image of manufacturer input when completing survey](docs/img/make-input.jpg)

### Model Input (Completing Survey)

The user can enter the model of their car. Input is validated and an error is thrown if the input is left blank or exceeds 20 characters.

![Image of model input when completing survey](docs/img/model-input.jpg)

### Year Input (Completing Survey)

The user can enter the year of their car. Input is validated and an error is thrown if the input contains letters, left blank or exceeds 4 digits.

![Image of year input when completing survey](docs/img/year-input.jpg)

### Car Details Check

The user is shown the values they just inputted. From here they have the choice of continuing with the survey, or if a mistake was made they can go back through the last three questions. Input is validated and an error is thrown if the input doesn't match the requirements. 

![Image of car details check](docs/img/car-input-check.jpg)

### Question One

The user is shown the first question out of three.  The input is validated and an error is thrown if it contains letters, is left blank or exceeds 4 digits.

![Image of question one](docs/img/question-one-input.jpg)

### Question Two

The user is then shown the second question. Input is validated and an error is thrown if it is left blank or exceeds 20 characters.

![Image of question two](docs/img/question-two-input.jpg)

### Question Three

The user is finally shown the last question. Input is validated and an error is throw if it is left blank or exceeds 20 characters.

![Image of question three](docs/img/question-three-input.jpg)

### Question Input Check

The user is show the answers they just entered for the questions. They have the choice of confirming their answers, or they can go through the questions again and change answers if needed. Input is validated and an error is thrown if the input doesn't match the requirements.

![Image of question input check](docs/img/question-check.jpg)

### Updated Worksheet & Final Options

Here the user has a message to let them know that the worksheet has been updated with their data.  They then have the option to find existing surveys, complete the survey again or exit out of the program. The input is validated and an error is thrown if the input doesn't match the requirements.

![Image of update worksheet message and final options](docs/img/update-sheet-final-options.jpg)

### Finding Surveys

The user has 5 different options to choose from.  The input is validated and an error is thrown if the input doesn't match the requirements.

![Image of survey finding options](docs/img/survey-filter.jpg)

### Finding Survey via a Manufacturer

If the user selected 'a' they will be asked to input a manufacturer. Input is validated and an error is thrown if it contains numbers or if left blank. User can input as many letters as they want but will no results will appear.  If the database does not contain a manufacturer matching the input, a message will appear letting the user know. 

![Image of survey search via manufacturer](docs/img/manufacturer-output.jpg)

### Finding Survey via Manufacturer and Model

If the user selected 'b' they will be asked to input a manufacturer and model. As inputs are seperate, they are validated on their own. Manufacturer input will throw an error if left blank or containing numbers. The model input will throw an error if left blank, there is also no limit to number of characters being inputted. If database does not contain a manufacturer and model matching the inputs, a message will appear letting the user know.

![Image of survey search via manufacturer and model](docs/img/manufacturer-model-output.jpg)

### Finding Survey via Manufacturer, Model and Year

If the user selected 'c' they will be asked to input a manufacturer, model and year. As inputs are seperate, they are each validated on their own. Manufacturer input will throw an error if left blank or containing numbers. Model input will throw an error if left blank. The year input will throw an error if left blank or containing letters, again no limit to number of characters being inputted.  If database does not contain the manufacturer, model and year matching the inputs a message will appear letting the user know. 

![Image of survey search via manufacturer, model and year](docs/img/manufacturer-model-year-output.jpg)

### Finding Survey via Manufacturer and Year

If the user selected 'd' they will be asked to input a manufacturer and year. As inputs are seperate, they validated on their own. Manufacturer input will throw an error if left blank or containing numbers. The year input will throw an error if left blank or containing letters, no limit to number of characters being inputted. If database does not contain the manufacturer and year matching the inputs a message will appear letting the user know. 

![Image of survey search via manufacturer and year](docs/img/manufacturer-year-output.jpg)

### Finding Survey via the Year & After Survey Options

If the user selected 'e' they will be asked to input a manufacturer and year. Input is validated and an error is thrown if it contains letters or if left blank. User can input as many characters as they want. If the database does not contain any year matching the input,  a message will appear letting the user know. 

At the same time of any surveys being printed, an option list will be printed underneath. This gives the user the option to search for a survey again, complete a survey or exit the program.

![Image of survey search via year](docs/img/year-output.jpg)
