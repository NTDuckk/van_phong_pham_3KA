from ThuVien.db_Connection import collection_PRODUCT
class Database:
    def __init__(self, collection):
        self.collection = collection

    def get_all(self, filter_query=None):
        if filter_query is None:
            filter_query = {}
        try:
            data = self.collection.find(filter_query)
            result = [doc for doc in data] 
            return result
        except Exception as e:
            print(f"Lỗi: {e}")
            return []

    def get_one(self, filter_query):
        try:
            result = self.collection.find_one(filter_query)
            return result
        except Exception as e:
            print(f"Lỗi: {e}")
            return None