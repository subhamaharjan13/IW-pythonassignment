import csv
import os.path

class Courses:

    coursesList = [{"C_id": "C01","Course_Name": "C", "Duration": "3 weeks", "Time": "2hr"},
            {"C_id": "C02","Course_Name": "C++", "Duration": "3.5 weeks", "Time": "2.5hr"},
            {"C_id": "C03","Course_Name": "C#", "Duration": "2 weeks", "Time": "1.5hr"},
            {"C_id": "C04","Course_Name": ".NET", "Duration": "2.5 weeks", "Time": "1.5hr"},
            {"C_id": "C05","Course_Name": "JAVA", "Duration": "3.5 weeks", "Time": "2.5hr"},
            {"C_id": "C06","Course_Name": "JAVASCRIPT", "Duration": "2.5 weeks", "Time": "2hr"},
            {"C_id": "C07","Course_Name": "PYTHON", "Duration": "2 weeks", "Time": "1hr"},
            {"C_id": "C08","Course_Name": "R", "Duration": "4 weeks", "Time": "2hr"}
            ]

    def listToCsv(self):
        keys = self.coursesList[0].keys()
        with open('csvfiles/course.csv', 'w') as write_file:
            dict_writer = csv.DictWriter(write_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.coursesList)
 
    # display the course info
    def courseInfo(self):
        print("Our available courses are: ")
        availableCourses = [ i['Course_Name'] for i in self.coursesList] 
        print(str(availableCourses))

        courseName = (input("Enter the course name:")).upper()
        course = next((item for item in self.coursesList if item["Course_Name"] == courseName), None)
        if (course is not None):
            print(f"Course Details: \nCourse ID: {course.get('C_id')} \nCourse Name: {course.get('Course_Name')}\
                    \nDuration:{course.get('Duration')} \nTime: {course.get('Time')}")
        else:
            print(f"Sorry,We have no such course in our academy")


# course = Courses()
# course.listToCsv()
# course.courseInfo()