from ThuVien.db_Connection import serverList, collection_PRODUCT
from ThuVien.Product import Product
def get_products_by_TypeAndID():
    product_db = Product(serverList)
    sql_products = product_db.get_all_products() 

    products = []
    for product in sql_products:
        products.append({"TYPE": product['_TYPE'], 
                         "PRODUCT_NAME": product['PRODUCT_NAME'],
                         "PRODUCT_ID": product['PRODUCT_ID'],
                        })
    return products

def get_imageUrl(product_list):
    products = []
    for product_info in product_list:
        product_type = product_info["TYPE"]
        product_id = product_info["PRODUCT_ID"]
        product_name = product_info["PRODUCT_NAME"] 
        
        mongodb_data = collection_PRODUCT.find_one(
            {"TYPE": product_type, "DATA.PRODUCT_ID": product_id},
            {"DATA.$": 1, "_id": 0} 
        )

        if mongodb_data and "DATA" in mongodb_data:
            image_url = mongodb_data['DATA'][0].get('IMAGE_URL', '')
        else:
            image_url = ''
        
        products.append({
            "PRODUCT_ID": product_id,
            "image_url": image_url,
            "PRODUCT_NAME": product_name
        })
    
    return products
