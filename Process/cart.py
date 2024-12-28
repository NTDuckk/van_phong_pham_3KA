from ThuVien.db_Connection import serverList
from ThuVien.Cart import Cart

# def add_product_to_cart(account_id, product_id, product_price, quantity):
#     cart = Cart(serverList)
#     cart.add_or_update_cart(account_id, product_id, product_price, quantity)

# def update_cart_quantity(account_id, product_id, change):
#     cart = Cart(serverList)
#     cart.update_product_quantity(account_id, product_id, change)

def get_cart_items(account_id):
    cart = Cart(serverList)
    return cart.get_cart_detail(account_id)