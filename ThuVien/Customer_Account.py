from ThuVien.Connect_SQL import Database

class Customer_Account(Database):
    def __init__(self, server_list):
        super().__init__(server_list)

    def get_customer_account(self, shop='serverGlobal'):
        query = "SELECT * FROM CUSTOMER"
        return self.get_all(query, shop=shop)
    
    def check_login(self, username, password, shop='serverGlobal'):
        query = "SELECT * FROM CUSTOMER WHERE USERNAME = ? AND PASS_WORD = ?"
        params = (username, password)
        return self.get_one(query, params, shop=shop)
    
    def get_account_id(self, username, shop='serverGlobal'):
        query = "SELECT ACCOUNT_ID FROM CUSTOMER WHERE USERNAME = ?"
        params = (username,)
        return self.get_one(query, params, shop=shop)