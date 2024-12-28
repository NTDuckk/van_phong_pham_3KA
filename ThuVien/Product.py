from ThuVien.Connect_SQL import Database

class Product(Database):
    def __init__(self, server_list):
        super().__init__(server_list) 

    def get_all_products(self, shop='serverGlobal'):
        query = "SELECT * FROM PRODUCTS"
        return self.get_all(query, shop=shop)

    def get_product_by_id(self, product_id, shop='serverGlobal'):
        query = "SELECT * FROM PRODUCTS WHERE PRODUCT_ID = ?"
        params = (product_id,)
        return self.get_one(query, params, shop=shop)
    
    def get_price(self, product_id, shop='serverGlobal'):
        query = """ SELECT TOP 1 PRODUCT_MONEY 
                    FROM STOCK_IN_DETAIL
                    WHERE PRODUCT_ID = ? AND QUANTITY > 0
                    ORDER BY CAST(SUBSTRING(STOCK_IN_ID, PATINDEX('%[0-9]%', STOCK_IN_ID), LEN(STOCK_IN_ID)) AS INT) ASC """
        params = (product_id,)
        result = self.get_one(query, params, shop=shop)
        
        if result:
            return {"PRODUCT_MONEY": result} if not isinstance(result, dict) else result
        return None
    
    def get_quantity(self, product_id, shop):
        query = """ SELECT TOP 1 PRODUCT_ID, STOCK_IN_ID, PRODUCT_MONEY, QUANTITY
                    FROM STOCK_IN_DETAIL
                    WHERE PRODUCT_ID = ?
                    ORDER BY STOCK_IN_ID ASC """
        params = (product_id,)
        return self.get_one(query, params, shop=shop)

    def get_price_from_shop(self, product_id, shop):
        query = """ SELECT TOP 1 PRODUCT_MONEY 
                    FROM STOCK_IN_DETAIL
                    WHERE PRODUCT_ID = ? AND QUANTITY > 0
                    ORDER BY CAST(SUBSTRING(STOCK_IN_ID, PATINDEX('%[0-9]%', STOCK_IN_ID), LEN(STOCK_IN_ID)) AS INT) ASC """
        params = (product_id,)
        result = self.get_one(query, params, shop=shop)
        
        if result:
            return {"PRODUCT_MONEY": result} if not isinstance(result, dict) else result
        return None