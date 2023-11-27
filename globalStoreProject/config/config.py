import os

key = "youtube_project"
iv = "youtube_encyptyo"
salt = "youtube_AesEncryption"

#AWS Access And Secret key
aws_access_key = "H4Hcb4zv5R9sfTgS77hwz9EAuBlKq7e+qpPXwj87sjw="
aws_secret_key = "x3LAsYc8JWQvidTx71mNjjCqJjsiaYkjxM0UEe9MU+mU5SZ9UFdWL7iZd6BQZ0ZC"
bucket_name = "youtube-project-testing"

s3_customer_datamart_directory = "customer_data_mart"
s3_sales_datamart_directory = "sales_data_mart"
s3_source_directory = "sales_data/"
s3_error_directory = "sales_data_error/"
s3_processed_directory = "sales_data_processed/"


#Database credential
# MySQL database connection properties
database_name = "MYPROJECTDEMO"
tableName='Global_Superstore'
user = "root"
password = "A#kash1987"
driver = "com.mysql.cj.jdbc.Driver"
hostname = "localhost"
port = "3306"
url = f"jdbc:mysql://{hostname}:{port}/{database_name}"
databaseUrl = f"mysql+mysqlconnector://{user}:{password}@{hostname}/{database_name}"

# Table name
customer_table_name = "customer"
product_staging_table = "product_staging_table"
product_table = "product"
sales_team_table = "sales_team"
store_table = "store"

#Data Mart details
customer_data_mart_table = "customers_data_mart"
sales_team_data_mart_table = "sales_team_data_mart"

# Required columns
mandatory_columns = ["customer_id","store_id","product_name","sales_date","sales_person_id","price","quantity","total_cost"]


# File Download location
local_directory = "C:\\Users\\nikita\\Documents\\data_engineering\\spark_data\\file_from_s3\\"
customer_data_mart_local_file = "C:\\Users\\nikita\\Documents\\data_engineering\\spark_data\\customer_data_mart\\"
sales_team_data_mart_local_file = "C:\\Users\\nikita\\Documents\\data_engineering\\spark_data\\sales_team_data_mart\\"
sales_team_data_mart_partitioned_local_file = "C:\\Users\\nikita\\Documents\\data_engineering\\spark_data\\sales_partition_data\\"
error_folder_path_local = "C:\\Users\\nikita\\Documents\\data_engineering\\spark_data\\error_files\\"