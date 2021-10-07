import sqlite3

def victim_details():
    connection = sqlite3.connect("Details.db")
    cursor = connection.cursor()
    details = cursor.execute("SELECT * FROM VICTIMS")       
    data_list = details.fetchall()
    return data_list

def location():
    details = victim_details()
    lat_list = []
    long_list = []
    place_list = []
    for detail in details:
        lat_list.append(detail[4])
        long_list.append(detail[5])
        place_list.append(detail[6])
    return (lat_list, long_list, place_list)