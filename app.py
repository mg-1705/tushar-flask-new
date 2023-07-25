from flask import Flask
from azure.storage.blob import BlobServiceClient
import mysql.connector

app = Flask(__name__)

@app.route("/", methods=['get'])
def index():
    account_name = "discoverdollarstorage"
    private_endpoint = "discoverdollarstorage.privatelink.blob.core.windows.net"
    blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.privateendpoint.net", credential=None, endpoint_suffix=private_endpoint)
    containers = blob_service_client.list_containers()
    for container in containers:
        print(container.name)


    Hostname = "mysql-discover-dollar-pvt.mysql-discover-dollar-pvt.mysql.database.azure.com"
    DB_Name = "mysql-discover-dollar-pvt"
    Username = "adminvm"
    Password ="Mandelbulb@1234"
    conn = mysql.connector.connect(user = Username,
                               host = Hostname,
                              database = DB_Name,
                              password = Password)

    if conn.is_connected():
        return('Connection established successfully.', container.name)
    else :
        return("Connection not established successfully.", container.name)
     
