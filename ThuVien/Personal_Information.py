from ThuVien.Connect_SQL import Database

class Personal_Information(Database):
    def __init__(self, server_list):
        super().__init__(server_list)

    def get_all_personal_information(self, shop='serverGlobal'):
        query = "SELECT * FROM PERSONAL_INFORMATION"
        return self.get_all(query, shop=shop)
    
    def get_pinfo_by_id(self, account_id, shop='serverGlobal'):
        query = "SELECT * FROM PERSONAL_INFORMATION WHERE ACCOUNT_ID = ?"
        params = (account_id,)
        return self.get_one(query, params, shop=shop)