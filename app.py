#Udemy Coursework -> Create student registration system


def create_student():
    #Ask the user for students name
    #Create the dictionary
    #Return that dictionary
    name = str(raw_input("Please enter the students name: "))
    student_data={ "name" : name,
                    "marks": []
                    }
    return student_data



student1_json=create_student()
student1_json["marks"].append(20)
print(student1_json)
