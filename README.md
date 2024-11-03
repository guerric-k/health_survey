# HEALTH SURVEY AUTOMATED SYSTEMS
The Health Survey Automation System is an efficient, data-driven tool designed to track and manage health data for adult patients. With a focus on medical conditions in adults, the system collects essential health metrics—including age, weight, height, temperature, BMI, and any pre-existing medical conditions. Abnormal figures are flagged, often indicating potential health concerns, allowing healthcare providers to monitor patients’ health status over time.

A Google Sheets database is used as the system’s backend, providing a secure and accessible repository for patient records. This integration with Google Sheets enables seamless storage, retrieval, and updates of health data. It also allows multiple users to view or modify patient records, making it a collaborative resource for healthcare teams and researchers. By leveraging Google Sheets, the system combines data accessibility with the power of cloud storage, allowing real-time updates and easy data sharing across different locations.

In addition to individual patient monitoring, this system’s aggregated data supports public health campaigns and preventive care planning. Healthcare providers and researchers can use the information to identify trends and organize targeted health initiatives, enhancing community health outcomes based on accurate and up-to-date data.

![Home Screen](/readme_images/home_page.JPG)

[View Health Survey Automated Systems live project here](https://health-survey-0dc097ffd267.herokuapp.com/)
- - -

## Table of Contents
### [How to use the system](#how-to-use-the-system-1)
### [Logic Flowchart](#logic-flowchart-1)
### [User Experience (UX)](#user-experience-ux-1)
* [User Stories](#user-stories)
### [Design](#design-1)
### [Features](#features-1)
* [Existing Features](#existing-features)
### [Features Left to Implement](#features-left-to-implement-1)
### [Technologies Used](#technologies-used-1)
### [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used-1)
### [Testing](#testing-1)
### [Manual Testing](#manual-testing-1)
### [Input validation testing](#input-validation-testing-1)
### [Fixed Bugs](#fixed-bugs-1)
### [Deployment](#deployment-1)
* [Deployment to Heroku](#deployment-to-heroku)
* [Forking the GitHub Repository](#forking-the-github-repository)
* [Local Clone](#local-clone)
### [Credits](#credits-1)
* [Code](#code)
* [Content](#content)
### [Acknowledgements](#acknowledgements-1)
---

## How to use the system
* Launch the Application
To start the application, click on the Run button.
The system will prompt you to enter patient details interactively.

* Adding a New Patient
    * When prompted to confirm adding a new patient, type yes   
      and press Enter.
    * Follow the prompts to enter each piece of information, 
      including:
        * Age: Enter the patient’s age (validated to ensure       it’s  a reasonable value).
        * Temperature: Enter the temperature in °C. If it falls outside the normal range, a warning will appear, but the value will still be accepted.
        * Weight: Enter the patient’s weight in kg. The system checks that the weight falls within a realistic range.
        * Height: Enter the height in cm. This value is validated against typical ranges.
        * Existing Medical Condition: Describe any current medical conditions the patient has (limited to a specific number of characters).
    * After entering all details, the system calculates and displays the patient’s BMI.

* Confirming the Patient Details
  * After all fields are completed, you’ll be prompted to confirm if you wish to add the patient’s details to the system.
  * Type yes to save the information to the Google Sheets database, or no to cancel and exit without saving.

* Updating Patient Records
  * The system supports updating information for existing patients as well. You can search for a patient by name and make changes as required.

* Monitoring Patient Health Indicators
  * Each time you run the application, you can review or update patient records. The Google Sheets integration allows easy tracking of any changes over time, so you can identify trends in the patients’ health.

* Accessing the Data
  * Data is stored in a Google Sheet linked to the app, so you can view, filter, or analyze it as needed.

## Logic flowchart

![Flowchart](/readme_images/flow_chart.JPG)

---
## User Experience (UX)

The Health Survey Automation System prioritizes user experience through an intuitive interface, offering clear prompts and guided input validation to minimize errors. Real-time feedback alerts users to abnormal health indicators, while responsive navigation caters to both first-time and returning visitors. Seamless integration with Google Sheets ensures efficient data storage and access, allowing healthcare providers to monitor patient trends effectively. Visual cues and ultimately creating a reliable tool for informed healthcare decisions.

---
### User Stories

* First-Time Visitor Goals
  * First-time visitors are typically new healthcare staff or   system users who need to understand the system and its benefits.

  * Understanding Health Survey Automation Systems' Purpose, so they can see how it benefits patient care and health tracking.

  * Learning How to Use the System using clear guidance on how to enter and review patient data so that they can easily navigate the system without mistakes.

  * Entering a New Patient Record
    Add a new patient’s information with confidence, following prompts and validations, so they can contribute to the patient database right away.

  * Observing Data Security and Privacy: They want reassurance that patient data is securely stored and private, so they can trust the system with sensitive information.

* Returning Visitor Goals
  * Returning visitors will have basic familiarity with the system and may want to quickly locate or update specific information.

  * Searching for Existing Patients records to review their latest health status.

  * Updating Patient Details such as temperature or medical conditions, so that the record stays current.

  * Navigation, using familiar prompts, to navigate the system quickly without repetitive instructions.

  * Viewing Validation and Alerts for unusual health indicators in updated records so as to quickly follow up on changes.

* Frequent User Goals
  * Access to Historical Data for Analysis
  * Generate Health Insights and Summaries
  * Explore new features and updates if any


## Design

* Colors
    * orange
    * Blue
    * red

* Flowchart
    * [Lucid chart](https://lucid.app/lucidchart/)

---
## Features

* User-Friendly Interface: An intuitive design that simplifies navigation for both first-time and returning users.
* Patient Data Management: Secure input and storage of essential patient information, including age, weight, height, temperature, BMI, and medical conditions.
* Real-Time Input Validation: Immediate feedback on data entry ensures that users provide accurate and acceptable values, minimizing errors.
* Abnormality Alerts: Alerts users to any abnormal health indicators, helping to identify potential medical conditions early.
* Google Sheets Integration: Seamless backend integration for efficient data storage, retrieval, and management, enabling healthcare providers to monitor patient health trends effectively.
* Patient Record Search: Easy search functionality to retrieve existing patient records quickly.
* Data-Driven Insights: Helps healthcare providers and researchers analyze patient data to plan targeted health campaigns and preventive measures based on identified trends.
* Privacy and Security: Measures in place to protect patient data and ensure compliance with privacy regulations.
* Customizable Reporting: Ability to generate reports based on collected data for further analysis and planning.

### Existing Features

* Intro screen
    * Displays program name, welcome message, app version, date and time and first prompts.

![Home Screen](/readme_images/home_page.JPG)

* Enter patient's name

![Patient's name](/readme_images/enter_patient_name.JPG)

* Record not found 'search' or 'add'?
![add](/readme_images/add.JPG)

* Input patient's details with validation alerts and BMI calculation

![Input details into the system](/readme_images/enter_patient_details.JPG)

* Confirm yes or no to add inputed details into the system
    * if yes,

![yes add](/readme_images/add_input_in_system.JPG)

  * If no,
  
![No don't add](/readme_images/patient_details_not_saved.JPG)

* User enters patient details and finds details in system

![Patient found](/readme_images/patient_details_found.JPG)

  * Does user want to update details? yes/no
    * if yes, user inputs details and confirms to add in system

![yes, to update details](/readme_images/patient_details_updated.JPG)

    * if no, patient details not saved

* Use run button to run the program
![Run app](/readme_images/run.JPG)

---
## Features Left to Implement

* Multiple Google sheets per region of survey
* Additional parameter
* More validation

---
## Technologies Used

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

---

## Frameworks, Libraries & Programs Used

* [Gitpod](https://www.gitpod.io/)
    * To write the code.
* [Github](https://github.com/)
    * Deployment of the website and storing the files online.
* [Lucid chart](https://lucid.app/lucidchart/)
    * To create a logic flowchart of Health Survey Automated Systems.
* [Heroku](https://www.heroku.com/)
    * To deploy the project.
* [CI Python Linter](https://pep8ci.herokuapp.com/)
    * Check code for any issues.
---

## Testing 

CI Python Linter was used to test run.py

<details>
<summary> run.py CI Python Linter check
</summary>

![run.py linter check](/readme_images/ci_linter.JPG)
</details>

## Manual Testing

The code was manually tested extensively using Gitpod's local terminal and once the app was deployed on Heroku it was manually tested again, during the inception of the code till its completion. Testing home window, user input validation, prompt navigation, valid and invalid responses.



| Feature | Expected Result | Steps Taken | Actual Result |
| ------- | -------------- | ----------- | ------------- | 
| Home Screen   | To display title and welcome message with app version, date and time | None | As Expected |
| Patient's name | To display prompts and requesto for user input of patient's name | Input name to serarch | As Expected |
| Patient details found? | To display patient details if found in Google Sheet | Input name begining with Uppercase letter for each name | As Expected |
| Prompt to update patient details | Enter yes or no to update details or abort respectively| entered yes and no | As Expected |
| Patient details not found   | To display message and prompts if patient not found in system | Enter serarch to try again or add to add new patient in system | As Expected |
| Update system with patient details| Prompts update data base | Input yes to confirm an no| As Expected | 
| Google Sheet responsiveness| To store information from app and push data to app when requested by user | Updated fields in Google sheet for new patients | As Expected |
| Input Validation  | To display messages if input is not valid and request user to input again | Input invalid data | As Expected | 

## Input validation testing

* Patient name validation
    * First and Last name must start with capital letter
    * No special charaters

![Name validation](/readme_images/name_validation.JPG)

* Age Validation
    * Must be an interger 
    * Must fall within range

![Age validation](/readme_images/age_validation.JPG)

* Height Validation
    * Must  be an integer 
    * Must fall within range

![Height validation](/readme_images/height_validation.JPG)

* Temperature Validation
    * must be a float
    * Must fall within range
    * Temperatures out of range still permitted as patients often have abnormal temperatures but this cannot put the entire system on hold

![Temperature Validation](/readme_images/temperature_validation.JPG)

* Weight Validation
    * must be a float
    * Must fall within range

![TWeight validation](/readme_images/weight_validation.JPG)

* Choice prompt Validation
  * must enter only the provided options
  

## Fixed Bugs

* Code breaking after wrong input. This was fixed by restructuring the code and using while loops
* Age taking too large numbers. This was fixed by introducing max_age variable and adjusting the validation
* sections of the code not executing. This was fixed by adjusting the indentation of the functions.
* Medical condition taking too many characters. Solved this by putting a 200 character maximum in the input field of the medical condition.
* Missing colors in vital validation of the code and home screen. Introduced ANSI escape codes for coloring text

## Deployment

### Deploying to Heroku

To deploy with Heroku, Code Institute Python Essentials Template was used so the python code can be viewed in a terminal in a browser
1. Log in to Heroku or create a new account
2. On the main page click "New" and select "Create new app"
3. Choose your unique app name and select your region
4. Click "Create app"
5. On the next page find "settings" and locate "Config Vars"
6. Click "Reveal Config Vars" and add "PORT" key and value "8000", click "Add"
7. Scroll down, locate "Buildpack" and click "Add", select "Python"
8. Repeat step 7. only this time add "Node.js", make sure "Python" is first
9. Scroll to the top and select "Deploy" tab
10. Select GitHub as deployment method and search for your repository and link them together
11. Scroll down and select either "Enable Automatic Deploys" or "Manual Deploy"
12. Deployed site [Health Survey Automated Systems](https://health-survey-0dc097ffd267.herokuapp.com/)

### Forking the GitHub Repository

By forking the repository, we make a copy of the original repository on our GitHub account to view and change without affecting the original repository by using these steps:

1. Log in to GitHub and locate [GitHub Repository health_survey](https://github.com/guerric-k/health_survey)
2. At the top of the Repository(under the main navigation) locate "Fork" button.
3. Now you should have a copy of the original repository in your GitHub account.

### Local Clone

1. Log in to GitHub and locate [GitHub Repository health_survey](https://github.com/guerric-k/health_survey)
2. Under the repository name click "Clone or download"
3. Click on the code button, select clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone` and then paste The URL copied in the step 3.
7. Press Enter and your local clone will be created.

## Credits

### Code

* I gained understanding of python through code institute lessons. and 
* I gained more python concepts through [Real Python](https://realpython.com/)
* ANSI color documentation.

### Content
* Health Survey Automated systems.
* All content was written by the developer.

## Acknowledgements
* My mentor Mitko Bachvarov provided feedback and support.

