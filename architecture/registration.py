import registrar as reg
import datetime
import pickle
from pathlib import Path

def load_institution_data():
    load_existing = input('Would you like to load existing data? Enter Yes or No: ').lower()

    if load_existing == 'yes':
        file_path = input('Please enter the filepath (must be a .pickle file): ')
        try:
            with open(file_path, 'rb') as pickle_file:
                institution = pickle.load(pickle_file)
            print('Existing data loaded successfully.\n')
        except FileNotFoundError:
            print("Error: The file does not exist.")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
    else:
        return create_new_institution()

def create_new_institution():
    name = input('Please enter an institution name: ')
    domain = input('Please enter a domain name (format: <institution>.edu): ')
    institution = reg.Institution(name, domain)
    print(f"New institution '{name}' created.\n")
    return institution

def get_valid_input(prompt, valid_values, input_type=str):
    while True:
        user_input = input(prompt)
        if input_type == str and user_input in valid_values:
            return user_input
        elif input_type == int:
            try:
                int_input = int(user_input)
                if int_input in valid_values:
                    return int_input
            except ValueError:
                pass
        print(f"Invalid input. Please enter a valid {prompt.lower()}.")

def create_course(institution):
    dept = get_valid_input('Please enter department code (max 4 chars): ', range(1, 10000), str)
    num = get_valid_input('Please enter a course number: ', range(1, 10000), int)
    name = input('Please enter course name: ')
    credits = get_valid_input('Please enter number of credits (1-4): ', range(1, 5), int)
    
    course = reg.Course(dept, num, name, credits)
    institution.add_course(course)
    print(f"\n{course.name} added to course list!\n")

def schedule_course_offering(institution):
    course = get_valid_input('Course name: ', institution.course_catalog.keys(), str)
    section = int(input('Please enter a section number: '))
    quarter = get_valid_input('Please enter quarter (Fall, Winter, Spring, Summer): ', ['Fall', 'Winter', 'Spring', 'Summer'], str)
    year = get_valid_input('Please enter year (YYYY): ', range(1900, 2100), int)
    
    course_offering = reg.CourseOffering(course, section, year, quarter)
    institution.add_course_offering(course_offering)
    print(f'\n{course_offering} has been scheduled!\n')

def hire_instructor(institution):
    last_name = input('Please enter instructor last name: ')
    first_name = input('Please enter instructor first name: ')
    dob = datetime.date(
        get_valid_input('Please enter year of birth (YYYY): ', range(1900, 2100), int),
        get_valid_input('Please enter birth month (MM): ', range(1, 13), int),
        get_valid_input('Please enter birth day (DD): ', range(1, 32), int)
    )
    username = input('Please give instructor a unique username: ')
    
    instructor = reg.Instructor(last_name, first_name, institution, dob, username)
    institution.hire_instructor(instructor)
    print(f'\nYou have hired {instructor.first_name} {instructor.last_name}\n')

# Main program
print('\nWelcome to the Registration System\n')

institution = load_institution_data()
if not institution:
    exit()

menu_string = '''
Please select an option from the following:

MENU
----------------------------------------
1 Create a course
2 Schedule a course offering
3 List course catalog
4 List course schedule
5 Hire an instructor
6 Assign an instructor to a course
7 Enroll a student
8 Register a student for a course
9 List enrolled students
10 List students registered for a course
11 List faculty
12 Submit student grade
13 Get student records
14 EXIT
'''

while True:
    print(menu_string)
    menu_input = input('Enter Menu Choice: ')

    if menu_input == '14':
        print('\nEXITING... Thank you!\n')
        break
    elif menu_input == '1':
        create_course(institution)
    elif menu_input == '2':
        schedule_course_offering(institution)
    elif menu_input == '5':
        hire_instructor(institution)
    # Add further options as necessary...
    else:
        print('\nINVALID MENU OPTION: Please try again\n')

# Save session
save_session = input('Would you like to save the contents of this session? Enter Yes or No: ').lower()
if save_session == 'yes':
    file_name = input('Please enter a filename for saving your data (this is a .pickle file): ')
    with open(file_name, 'wb') as pickle_file:
        pickle.dump(institution, pickle_file)
    print('Session contents saved, goodbye!')
else:
    print('Goodbye!')
