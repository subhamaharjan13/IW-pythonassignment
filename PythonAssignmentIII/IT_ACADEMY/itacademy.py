import csv
import sys
import os.path

class Academy:

    coursesList = [{"Course": "C", "Duration": "3 weeks", "Time": "2hr"},
                {"Course": "C++", "Duration": "3.5 weeks", "Time": "2.5hr"},
                {"Course": "C#", "Duration": "2 weeks", "Time": "1.5hr"},
                {"Course": ".NET", "Duration": "2.5 weeks", "Time": "1.5hr"},
                {"Course": "JAVA", "Duration": "3.5 weeks", "Time": "2.5hr"},
                {"Course": "JAVASCRIPT", "Duration": "2.5 weeks", "Time": "2hr"},
                {"Course": "PYTHON", "Duration": "2 weeks", "Time": "1hr"},
                {"Course": "R", "Duration": "4 weeks", "Time": "2hr"}
                ]

    totalCourseBalance = 20000

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
        with open('list.csv','r') as read_file:
            csv_reader = csv.reader(read_file)
            for _, row in enumerate(csv_reader):
                if row[0] == existingname:
                    details = row
            
        return details

    # display the course info
    def courseInfo(self):
        courseName = (input("Enter the course name:")).upper()
        course = next((item for item in self.coursesList if item["Course"] == courseName), None)
        if (course is not None):
            print(f"Course Details: \nCourse: {course.get('Course')}\
                    \nDuration:{course.get('Duration')} \nTime: {course.get('Time')}")
        else:
            print(f"Sorry,We have no such course in our academy")

    # calculate the remaining balance  
    def deposit(self):
        print(f"Total cost of the course is Rs. {self.totalCourseBalance}.\
            \nYou can pay the full amount at once or You can pay 50% in the first month and rest in the later month.")
        amount = int(input("Enter the amount you want to deposit: "))
        if amount == 10000:
            due = self.totalCourseBalance - amount
        elif amount == self.totalCourseBalance:
            due = 0

        return due

    # leave the program and delete the info from csv file
    def leaveProgram(self):
        verify = input("Enter yes to leave the program else no: ")
        if verify.lower() == 'yes':
            name = (self.name).title()

            lines = list()
            with open('list.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    lines.append(row)

            result_list = [(x, y, z) for x, y, z in lines if x != name]

            with open('list.csv', 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(result_list)
            
            print("You have left the program")

        elif verify == 'no':
            print("You are still in our Academy. Thank You")

    # choose the option from menu
    def menu(self):
        print("Welcome to our IT Academy \n1. Existing Student Information \n2. New Registration \n3. Courses Inquiry\
                \n4. Deposit the amount \n5. Leave the program \n6. Exit")
        choice = int(input("Enter the number You would like to know about: "))

        if choice == 1:
            info = self.existingStudentInfo()
            if info == []:
                print(f"We don't have a student named {(self.name).title()} in our academy")
            else:
                print(info) 

        if choice == 2:
            newRegisteredInfo = self.addInfo()
            with open('list.csv','a') as write_file:
                csv_writer = csv.writer(write_file)
                headers = ['Name','Age','Course']
                fileEmpty = os.stat('list.csv').st_size == 0
                if fileEmpty:
                    csv_writer.writerow(headers)
                csv_writer.writerow(newRegisteredInfo)

                print("Welcome to our Academy.You have been registered")

        if choice == 3:
            return self.courseInfo()

        if choice == 4:
            due = self.deposit()
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
student = Academy(studentName)
student.menu()