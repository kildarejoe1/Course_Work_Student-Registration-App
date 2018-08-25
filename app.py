#Udemy Coursework -> Create student registration system
student_list = []

def create_student():
    #Ask the user for students name
    #Create the dictionary
    #Return that dictionary
    name = str(raw_input("Please enter the students name: "))
    student_data={ "name" : name,
                    "marks": []
                    }
    return student_data

def add_mark(student,mark):
    #append mark to student dictionary
    student["marks"].append(mark)
    return None

def calculate_average_mark(student):
    #Add together all of the students[marks]
    #Divide them by the total number of marks
    #What happens if the student has no marks
    try:
        total = sum(student["marks"])
        no_of_marks = len(student["marks"])
        average = total / no_of_marks
        return average
    except:
        print("Error encounter - stopping program")


def print_student_details(student):
    #Prints out use information in a string
    print("{} average mark is {}".format(student["name"],calculate_average_mark(student)))


def print_student_list(students):
    for student in students:
        print(print_student_details(students))


def menu():
    #add a student to student student_list
    #add a mark to student
    #Print a list of students
    #Exit the application
    while True:
        app_decision = str(raw_input("Do you want to exit the application? Y or N "))
        if app_decision == "Y":
            name_of_student=create_student()
            while True:
                app_decision = str(raw_input("Do you want to exit the application? Y or N "))
                if app_decision == "Y":
                    mark_of_student=int(raw_input("Enter the mark of the student : "))
                    add_mark(name_of_student,mark_of_student)
                    decision = str(raw_input("Do you want to add additional marks to to this student? Y or N "))
                    if decision == "Y":
                        continue
                    else:
                        print("Adding {} to the student list..".format(name_of_student["name"]))
                        student_list.append(name_of_student)
                        student_decision = str(raw_input("Do you want to add another student? Y or N "))
                        if student_decision == "Y":
                            break
                        else:
                            for student in student_list:
                                print("Printing the list of students: /n", student)
                                break
        else:
            break

if __name__ == "__main__":
    menu()
