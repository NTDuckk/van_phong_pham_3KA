from ThuVien.Order import Order
from ThuVien.Product import Product
from Process.personal_info import get_personal_info_by_id
from datetime import datetime
import random

def create_rand_id():
    Chu_Cai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    So = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    _Chu = random.choices(Chu_Cai, k=4)
    _So = random.choices(So, k=2)
    ID = _Chu + _So
    random.shuffle(ID)
    return ''.join(ID)

# kiểm tra số lượng còn
def check_inventory(cart_items, server_list, main_shop, sub_shop):
    product = Product(server_list)
    for item in cart_items:
        product_id = item['product_id']
        required_quantity = item['quantity']

        product_quantity1 = product.get_quantity(product_id, shop=main_shop)
        main_quantity = product_quantity1['QUANTITY'] if product_quantity1 else 0

        product_quantity2 = product.get_quantity(product_id, shop=sub_shop)
        sub_quantity = product_quantity2['QUANTITY'] if product_quantity2 else 0

        total_quantity = main_quantity + sub_quantity

        if total_quantity < required_quantity:
            return False, product_id  

    return True, None  

def add_order_detail(server_list, order_id, product_id, quantity, percent, shop):
    order = Order(server_list)
    product = Product(server_list)

    stock_price= product.get_price_from_shop(product_id, shop=shop)
    unit_price = stock_price['PRODUCT_MONEY']

    order.add_order_detail(order_id, product_id, quantity, unit_price, percent, shop='serverGlobal')

def process_order(account_id, cart_items, server_list):
    order = Order(server_list)
    product = Product(server_list)

    user_info = get_personal_info_by_id(account_id)
    address = user_info['_ADDRESS']
    city = user_info['CITY']

    if city == 'TP.HCM':
        main_shop = 'serverSouth'
        sub_shop = 'serverNorth'
    else:
        main_shop = 'serverNorth'
        sub_shop = 'serverSouth'

    # Kiểm tra tồn 
    kt, ma_shop_con_hang = check_inventory(cart_items, server_list, main_shop, sub_shop)
    if not kt or not ma_shop_con_hang:
        raise Exception(f"Có sản phẩm hết hàng")
    
    new_order_id = ""
    while True:
        new_order_id = create_rand_id()
        kq = order.get_order_by_id(new_order_id, shop='serverGlobal')
        if not kq:
            break

    order_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    order.create_order(new_order_id, account_id, order_date, address, city, shop='serverGlobal')

    # Thêm chi tiết đơn hàng
    for item in cart_items:
        product_id = item['product_id']
        quantity = item['quantity']
        percent = 0
        add_order_detail(server_list, new_order_id, product_id, quantity, percent, ma_shop_con_hang)

    return {"order_id": new_order_id, "status": "success"}