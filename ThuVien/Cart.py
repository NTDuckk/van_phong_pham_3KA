from ThuVien.Connect_SQL import Database
from datetime import datetime

class Cart(Database):
    def __init__(self, server_list):
        super().__init__(server_list)

    def get_cart(self, account_id, shop='serverGlobal'):
        query = "SELECT * FROM CART WHERE ACCOUNT_ID = ? "
        params = (account_id,)
        return self.get_one(query, params, shop=shop)

    def get_cart_detail(self, account_id, shop='serverGlobal'):
        cart = self.get_cart(account_id, shop=shop)
        if not cart:
            return []
        cart_id = cart['CART_ID']
        query = """ SELECT CD.PRODUCT_ID, P.PRODUCT_NAME, CD.NUMBER_OF_PRODUCT, CD.TOTAL_AMOUNT 
                    FROM CART_DETAIL as CD
                    INNER JOIN PRODUCTS as P
                    ON CD.PRODUCT_ID = P.PRODUCT_ID
                    WHERE CD.CART_ID = ? """
        params = (cart_id,)
        return self.get_all(query, params, shop=shop)

    def update_cart_date(self, account_id, shop='serverGlobal'):
        current_date = datetime.now()

        query_update = "UPDATE CART SET UPDATE_DATE = ? WHERE ACCOUNT_ID = ?"
        params_update = (current_date, account_id)
        self.execute_q(query_update, params_update, shop=shop)

    def update_cart(self, account_id, product_id, product_price, quantity, shop='serverGlobal'):
        cart = self.get_cart(account_id, shop=shop)
        cart_id = cart['CART_ID']

        query = "SELECT * FROM CART_DETAIL WHERE CART_ID = ? AND PRODUCT_ID = ?"
        params = (cart_id, product_id)
        item = self.get_one(query, params, shop=shop)

        if item:
            new_quantity = item['NUMBER_OF_PRODUCT'] + quantity
            new_total = new_quantity * product_price
            query_update = """UPDATE CART_DETAIL
                            SET NUMBER_OF_PRODUCT = ?, TOTAL_AMOUNT = ?
                            WHERE CART_ID = ? AND PRODUCT_ID = ? """
            params = (new_quantity, new_total, cart_id, product_id)
            self.execute_q(query_update, params, shop=shop)
        else:
            query_insert = """ INSERT INTO CART_DETAIL (CART_ID, PRODUCT_ID, NUMBER_OF_PRODUCT, TOTAL_AMOUNT)
                            VALUES (?, ?, ?, ?) """
            params = (cart_id, product_id, quantity, product_price * quantity)
            self.execute_q(query_insert, params, shop=shop)

        self.update_cart_date(cart_id, shop=shop)