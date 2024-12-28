from ThuVien.Connect_SQL import Database
class Order(Database):
    def __init__(self, server_list):
        super().__init__(server_list)

    def get_order_by_id(self, order_id, shop='serverGlobal'):
        query = "SELECT * FROM ORDERS WHERE ORDER_ID = ?"
        params = (order_id,)
        return self.get_one(query, params, shop=shop)

    def create_order(self, order_id, account_id, order_date, address, city, shop='serverGlobal'):
        query = "INSERT INTO ORDERS (ORDER_ID, ORDRER_DATE, _ADDRESS, CITY, ACCOUNT_ID) VALUES (?, ?, ?, ?, ?)"
        params = (order_id, order_date, address, city, account_id)
        self.execute_q(query, params, shop=shop)

    def add_order_detail(self, order_id, product_id, quantity, unit_price, percent, shop='serverGlobal'):
        query = """INSERT INTO ORDER_DETAIL (ORDER_ID, PRODUCT_ID, QUANTITY, UNIT_PRICE, PERCENTS) 
                  VALUES (?, ?, ?, ?, ?) """
        params = (order_id, product_id, quantity, unit_price, percent)
        self.execute_q(query, params, shop=shop)

    def get_order_details(self, order_id, shop='serverGlobal'):
        query = """
            SELECT OD.PRODUCT_ID, P.PRODUCT_NAME, OD.QUANTITY, OD.UNIT_PRICE, OD.PERCENTS
            FROM ORDER_DETAIL AS OD
            INNER JOIN PRODUCTS AS P ON OD.PRODUCT_ID = P.PRODUCT_ID
            WHERE OD.ORDER_ID = ?
        """
        params = (order_id,)
        return self.get_all(query, params, shop=shop)

    def get_orders_by_account_id(self, account_id, shop='serverGlobal'):
        """
        Lấy danh sách đơn hàng của một tài khoản từ bảng ORDERS
        """
        query = "SELECT * FROM ORDERS WHERE ACCOUNT_ID = ?"
        params = (account_id,)
        return self.get_all(query, params, shop=shop)
