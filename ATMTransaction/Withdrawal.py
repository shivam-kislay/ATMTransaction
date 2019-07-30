import pymysql
from DataSourceQueries import DataSourceQueries


class Withdrawal:

    def __init__(self):
        self.amount = 0

    def Transaction(self, deductingAmount, CustomerData):
        BalanceAmount = CustomerData.AccountBalance - deductingAmount
        self.amount = BalanceAmount
        CustomerData.AccountBalance = BalanceAmount
        d1 = DataSourceQueries()
        d1.Update_Cutomer_Account_Balance(CustomerData.CustomerId, CustomerData.AccountBalance)
        return BalanceAmount
