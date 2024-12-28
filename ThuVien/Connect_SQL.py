import pyodbc
from ThuVien.db_Connection import *
class Database:
    def __init__(self, server_list):
        self.server_list = server_list

    def connect(self, shop='serverGlobal'):
        connection_string = self.server_list.get(shop, self.server_list["serverGlobal"])
        return pyodbc.connect(connection_string)

    def get_all(self, query, params=(), shop='serverGlobal'):
        conn = self.connect(shop)
        cursor = conn.cursor()
        try:
            cursor.execute(query, params)
            data = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            result = [dict(zip(columns, row)) for row in data]
            return result
        finally:
            conn.close()

    def get_one(self, query, params=(), shop='serverGlobal'):
        conn = self.connect(shop)
        cursor = conn.cursor()
        try:
            cursor.execute(query, params)
            row = cursor.fetchone()
            if row:
                columns = [column[0] for column in cursor.description]
                result = dict(zip(columns, row))
                return result
            return None
        finally:
            conn.close()

    def execute_q(self, query, params=(), shop='serverGlobal'):
        conn = self.connect(shop)
        cursor = conn.cursor()
        try:
            cursor.execute(query, params)
            conn.commit()
            return cursor.rowcount 
        finally:
            conn.close()
