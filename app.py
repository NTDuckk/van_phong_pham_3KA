from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from Process.product import get_products_by_TypeAndID, get_imageUrl
from Process.product_detail import get_product_information
from Process.cart import get_cart_items
from Process.order import process_order
from Process.account import check_login
from ThuVien.db_Connection import serverList

app = Flask(__name__)
app.secret_key = "supersecretkey"  

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('page')) 
    return redirect(url_for('login')) 

@app.route('/index')
def page():
    if 'user' not in session: 
        flash("Vui lòng đăng nhập", "danger")
        return redirect(url_for('login'))
    return render_template('index.html') 

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        check = check_login(username, password) 
        if check:
            session['user'] = check['ACCOUNT_ID']
            return redirect(url_for('index')) 
        else:
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/product/<product_id>')
def single_product(product_id):
    product_details = get_product_information(product_id)
    if not product_details:
        flash("Không có thông tin", "danger")
        return redirect(url_for('product'))
    return render_template('single_product.html', product=product_details)

@app.route('/products')
def product():
    product_list = get_products_by_TypeAndID()
    product_information = get_imageUrl(product_list)
    return render_template('product.html', products=product_information)

@app.route('/cart')
def cart():
    account_id = session.get('user')
    cart_items = get_cart_items(account_id) 
    return render_template('cart.html', cart_items=cart_items)

# @app.route('/add_to_cart', methods=['POST'])
# def add_to_cart():
#     if 'user' not in session:
#         flash("Bạn cần đăng nhập để thêm sản phẩm vào giỏ hàng", "danger")
#         return redirect(url_for('login'))
    
#     account_id = session.get('user')
#     product_id = request.form.get('product_id')

#     # Default quantity = 1
#     quantity = 1

#     # Fetch product price
#     product_price = get_price(product_id)  # Function to get the price from the database

#     # Add to cart logic
#     add_product_to_cart(account_id, product_id, product_price, quantity)
#     flash("Sản phẩm đã được thêm vào giỏ hàng", "success")
#     return redirect(url_for('product'))

# @app.route('/update_cart', methods=['POST'])
# def update_cart():
#     if 'user' not in session:
#         flash("Bạn cần đăng nhập để cập nhật giỏ hàng", "danger")
#         return redirect(url_for('login'))
    
#     account_id = session.get('user')
#     product_id = request.form.get('product_id')
#     action = request.form.get('action')

#     # Update cart logic
#     if action == "increase":
#         update_cart_quantity(account_id, product_id, 1)
#     elif action == "decrease":
#         update_cart_quantity(account_id, product_id, -1)

#     return redirect(url_for('cart'))

# @app.route('/cart')
# def cart():
#     if 'user' not in session:
#         flash("Bạn cần đăng nhập để xem giỏ hàng", "danger")
#         return redirect(url_for('login'))
    
#     account_id = session.get('user')
#     cart_items = get_cart_items(account_id)
#     return render_template('cart.html', cart_items=cart_items)

@app.route('/process_order', methods=['POST'])
def make_order():
    try:
        account_id = session['user']  
        data = request.json
        cart_items = data.get('cart_items')

        result = process_order(account_id, cart_items, server_list=serverList)
        return jsonify({"status": "success", "order_id": result['order_id']})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
