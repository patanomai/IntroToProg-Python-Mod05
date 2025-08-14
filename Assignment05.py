# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   PSrianomai,08/10/2025,Created Script
# ------------------------------------------------------------------------------------------
import json #import code from Python's JSON module into my script
# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

# Define the Data Constants:
# set to the value of Enrollments.json file
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # Holds one row of student data (TODO: Change this to a Dictionary)
students: list = [] # hold a list of dictionaries
file = None  # Holds a reference to an opened file.
menu_choice: str = '' # Hold the choice made by the user.


# When the program starts, the contents of the "Enrollments.json" are
# automatically read into the students two-dimensional list of
# dictionary rows using the json.load() function
# read from the json file
try: # use error handling
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print("text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()


# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")
    print() # Adding extra space to make it look nicer.

    # Input user data:
    # On menu choice 1, the program prompts the user to enter the student's
    # first name and last name, followed by the course name, using the input()
    # function and stores the inputs in the respective variables.
    # using try-except to check when users input first names and last name
    if menu_choice == "1":  # This will not work if it is an integer!
        try: # use error handling
            print("-"*50)
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers. ")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            # Data collected for menu choice 1 is added to a dictionary
            # named student_data. Next, student_data is added to the students
            # two-dimensional list of dictionaries rows.
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data) # add row to list of dictionaries 2D
            # print statement inside the try block to only confirm the
            # registration if all inputs are valid and the data was
            # successfully added. If any error occurs during input,
            # the program should skip the confirmation message.
            print(f"You have registered {student_data["FirstName"]}",
                  f"{student_data["LastName"]} for",
                  f"{student_data["CourseName"]}.")
            print("-" * 50)
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        continue

    # Present the current data:
    # On menu choice 2, the presents a string by formatting the collected
    # data using the print() function.
    elif menu_choice == "2":
        print("-"*50)
        for student in students:
            print(f'{student["FirstName"]},{student["LastName"]},'
                  f'{student["CourseName"]}')
        print("-"*50)
        continue

    # Save the data to a file:
    # On menu choice 3, the program opens a file named "Enrollments.json"
    # in write mode using the open() function. It writes the contents of
    # the students variable to the file using the json.dump() function.
    # Next, the file is closed using the close() method. Finally, the
    # program displays what was written to the file using the students variable
    elif menu_choice == "3":
        try: # Error Handling
            file = open(FILE_NAME,"w") #open the file in write mode
            json.dump(students, file, indent = 2) #write file using json dump
            # print statement inside the try block to only print the
            # statement if writing succeeds
            print("The following data was saved to file!")
            for student in students:
                print(f'Student {student["FirstName"]} {student["LastName"]}',
                      f'is enrolled in {student["CourseName"]}')
        except FileNotFoundError as e:
            print("Text file must exist before running this script!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        finally: # ensures the file is closed properly before continue
            if file.closed == False:
                file.close()
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
