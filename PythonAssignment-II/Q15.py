# Imagine you are designing a banking application. What would a customer look like?
# What attributes would she have? What methods would she have?

class CustomerInformation:

    minimumBalance = 500

    def __init__(self,accName,accNumber):
        self.accName = accName
        self.accNumber = accNumber
        
    def info(self):
        print("Customer Details: \nAccount Name: {} \nAccount Number: {}"
                    .format(self.accName,self.accNumber))

    @classmethod
    def balance(cls):
        return cls.minimumBalance

    def totalbalance(self,totalBalance):
        print("Total Balance in your account", totalBalance)

customer = CustomerInformation("Subha", 100)
customer.info()
print("Minimum balance:",CustomerInformation.balance())
customer.totalbalance(1500)