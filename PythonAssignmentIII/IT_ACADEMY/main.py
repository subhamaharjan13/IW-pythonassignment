import csv
import sys
import os.path
import courses as cs
import deposit as dep

class Student:

    totalCourseBalance = 20000

    def __init__(self,name):
        self.name = name

    # register new students information
    def addInfo(self):
        newName = (self.name).title()
        age = int(input("Age: "))
        course = (input("Your preferred course ['C','C++','C#','JAVA','JAVASCRIPT','PYTHON','R','.NET']: ")).upper()
        paid = dep.Deposit().payment()
        newRegistration = (newName, age, course, paid)
        return newRegistration

    # show the information of existing student
    def existingStudentInfo(self):
        existingname = (self.name).title()
        details = list()
        with open('csvfiles/list.csv','r') as read_file:
            csv_reader = csv.reader(read_file)
            for _, row in enumerate(csv_reader):
                if row[0] == existingname:
                    details = row
            
        return details


class Academy(Student):

    # choose the option from menu
    def menu(self):
        print("Welcome to our IT Academy \n1. Existing Student Information \n2. New Registration \n3. Courses Inquiry\
                \n4. Payment Information \n5. Leave the Course \n6. Exit")
        choice = int(input("Enter the number You would like to know about: "))

        if choice == 1:
            info = self.existingStudentInfo()
            if info == []:
                print(f"Sorry, We don't have a student named {(self.name).title()} in our academy")
            else:
                print(info) 

        if choice == 2:
            newRegisteredInfo = self.addInfo()
            with open('csvfiles/list.csv','a') as write_file:
                csv_writer = csv.writer(write_file)
                headers = ['Name','Age','Course','Balance']
                fileEmpty = os.stat('csvfiles/list.csv').st_size == 0
                if fileEmpty:
                    csv_writer.writerow(headers)
                csv_writer.writerow(newRegisteredInfo)

                print("Congratulations.You have been registered")

        if choice == 3:
            return cs.Courses().courseInfo()
            
        if choice == 4:
            balance = self.totalDue()
            if balance == self.totalCourseBalance:
                print("You have no remaining dues")
            elif balance == 10000:
                print("Your Remaining Balance is: Rs", balance)
            else:
                print("Invalid command")

        if choice == 5:
            return self.leaveProgram()

        if choice == 6:
            print("Program Terminated")
            sys.exit()

    def totalDue(self):
        data = list()
        with open('csvfiles/list.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                data.append(row)
        
        result_list = [(stdname, stdage, stdcourse, stddue) for stdname, stdage, stdcourse, stddue in data if stdname == (self.name).title()]
        result = [(stdname, stdage, stdcourse, stddue) for stdname, stdage, stdcourse, stddue in data if stdname != (self.name).title()]

        for _, _,_, stddue in result_list:
            result = int(stddue)
        return result

    # leave the program and delete the info from csv file
    def leaveProgram(self):
        name = (self.name).title()
        lines = list()
        with open('csvfiles/list.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
        res = name in (item for sublist in lines for item in sublist)
        if str(res) == True:

            verify = input("Enter yes to leave the program else no: ")
            if verify.lower() == 'yes':

                result_list = [(stdname, stdage, stdcourse, stddue) for stdname, stdage, stdcourse, stddue in lines if stdname != name]

                balance = self.totalDue()
                if balance == self.totalCourseBalance:
                    print("Your balance has been fully refunded")
                else:
                    print(f"Your payment {balance} has been refunded")

                with open('csvfiles/list.csv', 'w') as writeFile:
                    writer = csv.writer(writeFile)
                    writer.writerows(result_list)
                
                print("You have left the program")

            elif verify == 'no':
                print("You are still in our Academy. Thank You")
        else:
            print("You cannot leave the course as you are not a student of our academy.")

studentName = input("Enter your Name:")
main = Academy(studentName)
main.menu()