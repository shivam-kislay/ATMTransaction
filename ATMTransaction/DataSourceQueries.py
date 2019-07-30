import pymysql
from CustomerData import CustomerData


class DataSourceQueries:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='shivam_kislay',
            password='Shubham46@',
            db='atmtransaction'
        )

    def Get_Customers_List(self):
        try:
            with self.connection.cursor() as cursor:
                sql = "Select * from customerdata"
                try:
                    cursor.execute(sql)
                    result = cursor.fetchall()
                except:
                    print("Unable to fetch customer list")

        finally:
            return result
            self.connection.close()

    def Update_Customer_Data(self, userId, userName, userBalance, userPassword):
        try:
            with self.connection.cursor() as cursor:
                sql = "Insert into customerdata ('CustomerId','CustomerName','AccountBalance','UserPassword') " \
                      "VALUES (%d,%s,%d,%s)"
                values = (userId, userName, userBalance, userPassword)
                try:
                    cursor.execute(sql, values)
                    self.connection.commit()
                except:
                    print("Cannot Update Table")
        finally:
            self.connection.close()

    def Update_Cutomer_Account_Balance(self, userId, userBalance):

        with self.connection.cursor() as cursor:
            sql = "Update customerdata Set AccountBalance = " + str(userBalance) + " where CustomerId = " + str(userId)

            cursor.execute(sql)
            self.connection.commit()

            print("Cannot Update User Balance")

        self.connection.close()
