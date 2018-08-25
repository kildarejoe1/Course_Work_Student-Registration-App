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
        


s=create_student()
add_mark(s,90)
add_mark(s,50)
print(s)
print("{} average mark is {}".format(s["name"],calculate_average_mark(s)))
