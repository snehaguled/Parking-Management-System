
import mysql.connector
#import json
class DBOperation():

    def __init__(self):
        # file = open("./config.json", "r")
        # datadic = json.loads(file.read())
        # file.close()
        self.mydb = mysql.connector.connect(host="localhost", username="root", password="vaishnavi@123", database="vehicle_parking")
        if self.mydb.is_connected():
            print("success")

    def CreateTables(self):
        cursor= self.mydb.cursor()
        cursor.execute("CREATE TABLE admin (id int (255) AUTO_INCREMENT PRIMARY KEY, username varchar(30), password varchar(10), created_at varchar(30))")
        cursor.execute("CREATE TABLE slots (id int (255) AUTO_INCREMENT PRIMARY KEY, vehicle_id varchar(30), space_for int(10), is_empty int(30))")
        cursor.execute("CREATE TABLE vehicles (id int (255) AUTO_INCREMENT PRIMARY KEY, name varchar(30), mobile varchar(10), empty_time varchar(30), exit_time varchar(30), vehicle_no varchar(30), created_at varchar(30), updated_at varchar(30))")
        cursor.close()

    def InsertOneTimeData(self, space_for_two, space_for_four):
        cursor= self.mydb.cursor()
        for x in range(space_for_two):
            cursor.execute("INSERT into slots (space_for, is_empty) values ('2','1')")
            self.mydb.commit()
        for x in range(space_for_four):
            cursor.execute("INSERT into slots (space_for, is_empty) values ('4','1')")
            self.mydb.commit()
        cursor.close()

    def InsertAdmin(self, username, password):
        cursor= self.mydb.cursor()
        val= (username, password)
        cursor.execute("INSERT into admin (username, password) values (%s,%s)", val)
        self.mydb.commit()
        cursor.close()

        


