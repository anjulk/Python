import os

key = "add key"
iv = "16 digit iv"
salt = "add salt"

#AWS Access And Secret key
aws_access_key = "Add AWS access key"
aws_secret_key = "Add AWS Secret key"




#Database credential
# MySQL database connection properties
database_name = "MYPROJECTDEMO"
tableName='Global_Superstore'
user = "root"
password = "Add password"
driver = "com.mysql.cj.jdbc.Driver"
hostname = "localhost"
port = "3306"
url = f"jdbc:mysql://{hostname}:{port}/{database_name}"
databaseUrl = f"mysql+mysqlconnector://{user}:{password}@{hostname}/{database_name}"
