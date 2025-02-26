# Title         : Student Academic Performance Analysis
# Purpose       : To analyze the student performance based on assignments and
#                 quiz marks to generate the student report for one subject.
# Programmer    : Bipul Bohara, Anu Darlami, Ruchika Upreti
# Date          : April 7, 2024
# Reference     : (Reference.1)https://www.geeksforgeeks.org/python-unpack-whole-list-into-variables/
#                  https://www.geeksforgeeks.org/python-string-join-method/(Reference.4)

# Algorithm:
# 1. Display a menu for following :
#      1.Read and display content from the first file.
#      2.Read and display content from the second file
#      3.Search Student record
#      4.Add marks
#      5.Create third file
#      6.Display third file
#      7.Exit
# 2. For option 1)Read and display content from the first file.
# 2. For option 2)Read and display content from the second file line by line.
# 3. For option 3)Search the student record to know if it exits it or not.
# 4. For option 4)Add student record that is student id, assignment marks, quiz
#    marks in first and second file.
# 4. For option 5)Create a third file by combining data from the first and
#    second file and calculate the garde of the students.
# 5. For option 6)Display the third file.
# 6. For option 7)Exit the program.

# Constants for menu choices.
READ_1ST_FILE = 1
READ_2ND_FILE = 2
SEARCH = 3
ADD = 4
CREATE_3RD_FILE = 5
DISPLAY_3RD_FILE = 6
END = 7
FIRST_FILE = 'FIRST_FILE.txt'
SECOND_FILE = 'SECOND_FILE.txt'
THIRD_FILE = 'THIRD_FILE.txt'


def main():
    print('\n' + '👾' * 35)
    print('👾\t\tStudent Academic Performance Analysis\t    👾')
    print('👾  \t\tProgrammed by:\t\t\t            👾')
    print('👾\t\t Bipul, Anu, Ruchika\t\t\t    👾')
    print('👾' * 35)

    choice = 0

    while choice != END:

        print('\nMENU:')
        print('1. Read and display content from the first file.')
        print('2. Read and display content from the second file')
        print('3. Search student record')
        print('4. Add marks')
        print('5. Create third file')
        print('6. Display third file')
        print('7. Exit')
        print()

        try:
            choice = int(input('Enter your choice: '))
            print('*' * 78)

            if choice == READ_1ST_FILE:
                read_first_file()
            elif choice == READ_2ND_FILE:
                read_second_file_line_by_line()
            elif choice == SEARCH:
                search()
            elif choice == ADD:
                add_marks()
            elif choice == CREATE_3RD_FILE:
                create_third_file()
            elif choice == DISPLAY_3RD_FILE:
                display_third_file()
            elif choice == END:
                print('THANK YOU!!!')
            else:
                print('ERROR: ***Invalid choice***')
        except ValueError:
            print('ERROR: Please enter a valid integer choice.')

    print('Exiting the program...')
    print('*' * 78)


def read_first_file():
    try:
        file = open(FIRST_FILE,'r')
        file_contents = file.read()

        # Check if the file is empty or not
        if file_contents:
            print()
            print('-' * 45)
            print(f'{"student_id":<15}{"student_name":<20}{"course":<15}')
            print('-' * 45)

            for line in file_contents.split('\n'):
                values = line.strip().split(', ')
                if len(values) == 3:
                    # Unpacking 'values' list into individual variables for
                    # better readability.(Reference.1)
                    student_id, student_name, course = values 

                    print(f'{student_id:<15}{student_name:<20}{course:<15}')

            print('-' * 45)
        else:
            print(f'File "{FIRST_FILE}" is empty.')
    except FileNotFoundError:
        print(f'Error: File "{FIRST_FILE}" not found.')
    
    
    file.close()
        


def read_second_file_line_by_line():
    try:
        file = open(SECOND_FILE, 'r')
        print()
        print('-' * 78)
        print(f'{"student_id":<15}{"assignment_name":<20}{"marks1":<15}'
              f'{"quiz_name":<20}{"marks2":<20}')
        print('-' * 78)

        # Read each line of the file
        for line in file:
            values = line.strip().split(',')
            if len(values) == 5:
                # Unpacking 'values' list into individual variables for
                # better readability.(Reference.1)
                student_id, assignment_name, marks1, quiz_name, marks2 = values

                print(f'{student_id:<15}{assignment_name:<20}{marks1:<15}'
                      f'{quiz_name:<20}{marks2:<20}')

        print('-' * 78)
    except FileNotFoundError:
        print(f'Error: File "{SECOND_FILE}" not found.')

    file.close()


def search():
    find = input('Enter the student ID to search: ')
    
    try:
        file = open(FIRST_FILE, 'r')
        for line in file:
            student_id, student_name, course = line.strip().split(', ')
            if student_id.strip() == find.strip():
                print('\nRecord found:')
                print('-' * 30)
                print(f'Student ID      : {student_id}')
                print(f'Student Name    : {student_name}')
                print(f'Course          : {course}')
                print('-' * 30)
                return  
        else:  
            print('-' * 30)
            print('*** No record found ***')
            print('-' * 30)
    except FileNotFoundError:
        print(f'Error: File "{FIRST_FILE}" not found.')

    file.close()


def add_marks():
    student_id = input('Enter the student ID for adding marks: ')
    student_name = input('Enter the student name: ')
    course = input('Enter the course: ')
    assignment_marks = input('Enter the assignment marks: ')
    quiz_marks = input('Enter the quiz marks: ')

    try:
        # Convert input to float and perform validation.
        assignment_marks = float(assignment_marks)
        quiz_marks = float(quiz_marks)

        # Check if marks are within a valid range.
        while not ((0 <= assignment_marks <= 100) and 
           (0 <= quiz_marks <= 100)):
            print('Error: Marks should be between 0 and 100.')
            return

        # Open the first file in append mode ('a') to add data directly at
        # the end of file.
        file1 = open(FIRST_FILE, 'a') 
        file1.write(f'{student_id}, {student_name}, {course}\n')

        file2 = open(SECOND_FILE, 'a')
        file2.write(f'{student_id}, Assignment 1, {assignment_marks}, Quiz 1,'
                   f'{quiz_marks}\n')

        print('-' * 75)
        print('Marks added successfully for the new student.')
        print('-' * 75)
        
    except ValueError:
        print('Error: Invalid input for marks. Please enter numeric values.')


def create_third_file():
    try:
        # Read data from the second file into memory
        with open(SECOND_FILE, 'r') as file2:
            file2_lines = file2.readlines()[1:]  # Skip header line

        with open(FIRST_FILE, 'r') as file1, open(THIRD_FILE, 'w') as file3:
            # Read data from the first file
            for line1 in file1:
                if line1.strip():  # Check if the line is not empty
                    values = line1.strip().split(', ')
                    if len(values) == 3:
                        student_id, student_name, course = values
                        print(f"Processing data for student ID: {student_id}")

                        total_marks = 0  # Initialize total marks for each student

                        # Read data from the second file in memory
                        for line2 in file2_lines:
                            data = line2.strip().split(', ')
                            if len(data) == 5 and data[0] == student_id:
                                try:
                                    total_marks += (float(data[2]) + float(data[4])) / 2
                                except ValueError:
                                    print(f'Error: Non-numeric value found in marks'
                                          f' for student {student_id}. Skipping...')

                        # Assign grades based on total marks
                        if total_marks >= 90:
                            grade = 'A'
                        elif 80 <= total_marks < 90:
                            grade = 'B'
                        elif 70 <= total_marks < 80:
                            grade = 'C'
                        elif 60 <= total_marks < 70:
                            grade = 'D'
                        else:
                            grade = 'F'

                        # Write student data to third file
                        file3.write(f'{student_id}, {student_name}, {course}, '
                                    f'{total_marks:.2f}, {grade}\n')
                        print(f'Total marks calculated for student {student_id}: '
                              f'{total_marks:.2f}, Grade: {grade}')
                        print()

                    else:
                        print(f'Invalid data format in line: {line1.strip()}')
                else:
                    print('Skipping empty line...')

        print('-' * 75)
        print('Third file creation completed.')
        print('-' * 75)

    except FileNotFoundError:
        print(f'One of the files ({FIRST_FILE}, {SECOND_FILE}) not found.')



def display_third_file():
    try:
        print('\nData from third file:\n')
        print('-' * 75)
        print(f'{"Student ID":<15}{"Student Name":<20}{"Course":<15}'
              f'{"Total Grade":<15}')
        print('-' * 75)

        file = open(THIRD_FILE, 'r')
        for line in file:
            values = line.strip().split(', ')
            if len(values) >= 4:
                student_id, student_name, course, *extra = values
                total_grade = ', '.join(extra)  # Combine extra values into
                                                # total_grade (Reference.4)
                print(f'{student_id:<15}{student_name:<20}{course:<15}'
                      f'{total_grade:<15}')
            else:
                print(f'Error: Invalid data format in line: {line.strip()}')

        print('-' * 75)
    except FileNotFoundError:
        print(f'Error: File "{THIRD_FILE}" not found.')


    file.close()


main()
