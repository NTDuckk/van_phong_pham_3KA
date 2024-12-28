from ThuVien.Customer_Account import Customer_Account
from ThuVien.db_Connection import serverList

def check_login(username, password):
    customer_account = Customer_Account(serverList)
    user = customer_account.check_login(username, password)
    return user
