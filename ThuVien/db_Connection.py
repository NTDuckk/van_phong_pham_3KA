from pymongo import MongoClient
serverList = {
    "serverGlobal": "DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-LOVB477;DATABASE=TMDT;UID=sa;PWD=123",
    "serverSouth": "DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-LOVB477\\MSSQLSERVER02;DATABASE=TMDT;UID=sa;PWD=123",
    "serverNorth": "DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-LOVB477\\MSSQLSERVER03;DATABASE=TMDT;UID=sa;PWD=123",
}

client = MongoClient('mongodb://localhost:27017/')
db = client['TMDT']  
collection_PRODUCT = db['PRODUCT_TYPE'] 