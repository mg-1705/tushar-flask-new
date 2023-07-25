from flask import Flask
from applicationinsights.flask.ext import AppInsights
from azure.storage.blob import BlobServiceClient
import os
import mysql.connector

app = Flask(__name__)

@app.route("/", methods=['get'])
def index():
#     blob_service_client = BlobServiceClient.from_connection_string(conn_str)
#     container_client = blob_service_client.get_container_client(container)
#     blob_list = container_client.list_blobs(name_starts_with=f"{encrypted_directory}/{file_name}")
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
     