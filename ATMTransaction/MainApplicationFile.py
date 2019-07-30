from Withdrawal import Withdrawal as Withdrawal
from DataSourceQueries import DataSourceQueries
from CustomerData import CustomerData


class Main:

    def __init__(self):
        self.customer_data = None
        self.p1 = Withdrawal()
        self.password = "ABC"
        self.x = True

    def Withdrawal_Test(self):
        return self.p1.amount

    def afterTransaction(self, Transaction_Amount, BalanceAmount):
        NewBalanceMount = self.p1.Transaction(Transaction_Amount, BalanceAmount)
        return NewBalanceMount

    def getUserList(self):
        DSQ = DataSourceQueries()
        ListOfCustomers = DSQ.Get_Customers_List()
        return ListOfCustomers


p2 = Main()
IdCheck = False
PasswordCheck = False
print("---Welcome to SKY ATM Application---")
customer = p2.getUserList()

UserId = int(input("Enter your Customer ID: "))

for b in customer:
    ID = b[0]
    if ID == UserId:
        IdCheck = True
        print("Welcome ", b[1])
        password = input("Enter your password: ")
        if password == b[3]:
            PasswordCheck = True
            p2.customer_data = CustomerData(b[0], b[1], b[2], b[3])
        break

if not IdCheck:
    print("Incorrect User ID")
# elif not PasswordCheck:
#    print("Incorrect Password")

if PasswordCheck:
    while p2.x:
        print("--Choose Service--")
        print("1. View Balance")
        print("2. Withdraw Amount")
        print("3. Exit")

        choice = int(input("Your Choice: "))
        if choice == 1:
            print("Available Balance is: ", p2.customer_data.AccountBalance)
        elif choice == 2:
            amount = int(input("Enter the amount to be withdrawn: "))
            # availableAmount = p2.afterTransaction(amount)
            p2.customer_data.AccountBalance = p2.afterTransaction(amount, p2.customer_data)
            print("The available amount in your account is: ", p2.customer_data.AccountBalance)

        elif choice == 3:
            p2.x = False
        else:
            print("Incorrect input try again")

elif not PasswordCheck and IdCheck:
    print("--Incorrect password try again later--")
