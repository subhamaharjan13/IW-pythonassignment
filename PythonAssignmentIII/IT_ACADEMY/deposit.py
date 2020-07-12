import csv
import sys
import os.path

class Deposit:

    totalCourseBalance = 20000

    # calculate the remaining balance  
    def payment(self):
        print(f"Total cost of the course is Rs. {self.totalCourseBalance}.\
            \nYou can pay the full amount at once or You can pay 50% in the first month and rest in the later month.")
        amount = int(input("Enter the amount you want to deposit: "))
        if amount == 10000:
            paid = self.totalCourseBalance - amount
        elif amount == self.totalCourseBalance:
            paid = self.totalCourseBalance

        return paid