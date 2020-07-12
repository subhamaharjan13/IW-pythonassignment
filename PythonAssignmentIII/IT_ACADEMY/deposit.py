import csv
import sys
import os.path

class Deposit:

    totalCourseBalance = 20000


    # calculate the remaining balance  
    def payment(self):
        print(f"Total cost of the course is Rs. {self.totalCourseBalance}.\
            \nYou can pay the full amount at once or You can pay 50% in the first month and rest in the later month.")
        amount = input("Enter the amount you want to deposit: ")
        amount = amount.replace(',','')
        amount = int(amount)
        if amount >= 10000:
            paid = amount
        elif amount == self.totalCourseBalance:
            paid = self.totalCourseBalance
        else:
            print("Amount not taken")
            self.payment()

        return paid