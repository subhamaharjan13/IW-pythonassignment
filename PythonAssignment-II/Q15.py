# Imagine you are designing a banking application. What would a customer look like?
# What attributes would she have? What methods would she have?

class BankApplication:

    minimumBalance = 500

    def __init__(self,accName,accNumber,totalBalance):
        self.accName = accName
        self.accNumber = accNumber
        self.totalBalance = totalBalance

    def info(self):
        print("Customer Details:")
        print("Account Name:",self.accName)
        print("Account Number:",self.accNumber)

    @classmethod
    def balance(cls):
        return cls.minimumBalance

    def totalbalance(self):
        print("Total Balance in your account", self.totalBalance)

customer = BankApplication("Subha", 100,1500)
customer.info()
print("Minimum balance:",BankApplication.balance())
customer.totalbalance()