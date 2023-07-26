from flask import Flask
from azure.storage.blob import BlobServiceClient
import mysql.connector

app = Flask(__name__)

@app.route("/", methods=['get'])
def index():
    account_name = "discoverdollarstorage"
    private_endpoint = "discoverdollarstorage.privatelink.blob.core.windows.net"
    blob_service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=discoverdollarstorage;AccountKey=AHN5nmtkkskh7qAK6FH+CbTQJZGram73/9lttw+g1HoX66dMq9lKLo6r+tHRGFKYGcaz4XcFFVDz+AStsAFQIw==;EndpointSuffix=core.windows.net")
    containers = blob_service_client.list_containers()
    name="ferer"
    for container in containers:
        name="madhur"
        name = container.name


    Hostname = "mysql-discover-dollar-pvt.mysql.database.azure.com"
    DB_Name = "test"
    Username = "adminvm"
    Password ="Mandelbulb@1234"
    conn = mysql.connector.connect(user = Username,
                               host = Hostname,
                              database = DB_Name,
                              password = Password)

    if conn.is_connected():
        return(f'Connection established successfully. {name} ')
    else :
        return(f'Connection not established successfully {name} ')
     
