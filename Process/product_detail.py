from ThuVien.db_Connection import serverList, collection_PRODUCT
from ThuVien.Product import Product

def get_product_detail(product_id):
    mongodb_data = collection_PRODUCT.find_one(
        {"DATA.PRODUCT_ID": product_id},
        {"DATA.$": 1, "_id": 0}
    )
    if not mongodb_data or "DATA" not in mongodb_data:
        return None
    
    product_data = mongodb_data["DATA"][0]
    return {
        "PRODUCT_ID": product_data["PRODUCT_ID"],
        "PRODUCT_NAME": product_data.get("PRODUCT_NAME"),
        "OTHER_INFORMATION": product_data.get("OTHER_INFORMATION", "Không có"),
        "COLOR": product_data.get("COLOR", "Không có"),
        "ORIGIN": product_data.get("ORIGIN", "Không có"),
        "IMAGE_URL": product_data.get("IMAGE_URL", ""),
    }

def get_price(product_id):
    product_db = Product(serverList)
    return product_db.get_price(product_id)

def get_product_information(product_id):
    product_details = get_product_detail(product_id)
    
    product_price = get_price(product_id)
    
    if product_price and isinstance(product_price, dict):
        product_details["PRICE"] = product_price["PRODUCT_MONEY"]
    else:
        product_details["PRICE"] = "Không có giá"
    
    return product_details