import os
import cx_Oracle
from flask import Flask
from flask import render_template

db_user = os.environ.get('DBAAS_USER_NAME', 'REFADM')
db_password = os.environ.get('DBAAS_USER_PASSWORD', 'Hx3J7u8L')
db_connect = os.environ.get('DBAAS_DEFAULT_CONNECT_DESCRIPTOR', "jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=dbs-pdv-vm-3052.cisco.com)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=DV1ESM.CISCO.COM)(Server=Dedicated)))")
service_port = port=os.environ.get('PORT', '8080')

app = Flask(__name__)

@app.route('/')
def index():
    connection = cx_Oracle.connect(db_user, db_password, db_connect)
    print connection.version
    connection.close()
    return "Hello World!"

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()
