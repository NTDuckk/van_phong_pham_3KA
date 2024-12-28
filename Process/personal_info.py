from ThuVien.db_Connection import serverList
from ThuVien.Personal_Information import Personal_Information

def get_all_personal_info():
    personal_info = Personal_Information(serverList)
    return personal_info.get_all_personal_information()

def get_personal_info_by_id(account_id):
    personal_info = Personal_Information(serverList)
    return personal_info.get_pinfo_by_id(account_id)
