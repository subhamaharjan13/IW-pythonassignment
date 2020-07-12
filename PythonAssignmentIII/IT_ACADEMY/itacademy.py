import csv
import sys
import os.path
import courses as cs
import deposit as dep

class Student:

    def __init__(self,name):
        self.name = name

    # register new students information
    def addInfo(self):
        newName = (self.name).title()
        age = int(input("Age: "))
        course = (input("Your preferred course ['C','C++','C#','JAVA','JAVASCRIPT','PYTHON','R','.NET']: ")).upper()
        newRegistration = (newName, age, course)
        return newRegistration

    # show the information of existing student
    def existingStudentInfo(self):
        existingname = (self.name).title()
        details = list()
        with open('PythonAssignmentIII/IT_ACADEMY/csvfiles/list.csv','r') as read_file:
            csv_reader = csv.reader(read_file)
            for _, row in enumerate(csv_reader):
                if row[0] == existingname:
                    details = row
            
        return details

    # leave the program and delete the info from csv file
    def leaveProgram(self):
        verify = input("Enter yes to leave the program else no: ")
        if verify.lower() == 'yes':
            name = (self.name).title()

            lines = list()
            with open('PythonAssignmentIII/IT_ACADEMY/csvfiles/list.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    lines.append(row)

            result_list = [(stdname, stdage, stdcourse) for stdname, stdage, stdcourse in lines if stdname != name]

            with open('PythonAssignmentIII/IT_ACADEMY/csvfiles/list.csv', 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(result_list)
            
            print("You have left the program")

        elif verify == 'no':
            print("You are still in our Academy. Thank You")


class Academy(Student):

    # choose the option from menu
    def menu(self):
        print("Welcome to our IT Academy \n1. Existing Student Information \n2. New Registration \n3. Courses Inquiry\
                \n4. Deposit the amount \n5. Leave the program \n6. Exit")
        choice = int(input("Enter the number You would like to know about: "))

        if choice == 1:
            info = self.existingStudentInfo()
            if info == []:
                print(f"Sorry, We don't have a student named {(self.name).title()} in our academy")
            else:
                print(info) 

        if choice == 2:
            newRegisteredInfo = self.addInfo()
            with open('PythonAssignmentIII/IT_ACADEMY/csvfiles/list.csv','a') as write_file:
                csv_writer = csv.writer(write_file)
                headers = ['Name','Age','Course']
                fileEmpty = os.stat('PythonAssignmentIII/IT_ACADEMY/csvfiles/list.csv').st_size == 0
                if fileEmpty:
                    csv_writer.writerow(headers)
                csv_writer.writerow(newRegisteredInfo)

                print("Congratulations.You have been registered")

        if choice == 3:
            return cs.Courses().courseInfo()
            
        if choice == 4:
            due = dep.Deposit().payment()
            if due == 0:
                print("You have no remaining dues")
            else:
                print("Your Remaining Balance is: Rs", due)

        if choice == 5:
            return self.leaveProgram()

        if choice == 6:
            print("Program Terminated")
            sys.exit()



studentName = input("Enter your Name:")
main = Academy(studentName)
main.menu()