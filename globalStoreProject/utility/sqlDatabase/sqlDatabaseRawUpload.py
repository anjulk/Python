from config import config
import mysql.connector 
import sqlalchemy as sa
import pandas as pd 

class mySQLWrapper:
    def __init__(self):
        self.hostName = config.hostname
        self.userName = config.user
        self.password = config.password
        self.databaseName = config.database_name
        self.dataBaseUrl = config.databaseUrl
    
    def get_mySQL_Connection(self):
        connectionObj =None
        engineObj =None
        
        try:
            connectionObj = mysql.connector.connect(
                host=self.hostName,
                user=self.userName,
                password=self.password,
                database=self.databaseName
            )
        except Exception  as e:
            print("Could not connect to" , e)
            
        print(self.dataBaseUrl)
        try:
            engineObj = sa.create_engine(self.dataBaseUrl, echo=False)
        except Exception as e:
            print(e)   
        return (connectionObj, engineObj)
    
    def upload_to_myqlServer(self, conn, engine, file_data_pd, tableName='Global_Superstore' ):
        try:
            file_data_pd.to_sql(tableName=config.tableName, con=engine, if_exists = 'replace', index=False)
        except Exception as e:
            print(e)
    
    def readDataIntoDataFrame(self, conn, engine,):
        
        dbConnection = engine.connect()
        dataFrameTransaction = pd.read_sql(f"SELECT * FROM {config.tableName}", dbConnection)
        print(dataFrameTransaction.head())
        return dataFrameTransaction
    
    
    def createFactTable(self, conn, engine, dataFrame):
        
        orders = pd.DataFrame(dataFrame[[ 
                                        'Customer ID',
                                        'Discount',
                                        'Market',
                                        'Order Date',
                                        'Order ID',
                                        'Order Priority',
                                        'Product ID',
                                        'Profit',
                                        'Quantity',
                                        'Region',
                                        'Row ID',
                                        'Sales',
                                        'Ship Date',
                                        'Ship Mode',
                                        'Shipping Cost',
                                        'State',
                                        'Sub-Category',
                                        'Year',
                                        'Market2',
                                        'weeknum' ]])
        orders.drop_duplicates(keep='first')
        try:
            orders.to_sql('orders', con=engine, if_exists = 'replace', index=False)
        except Exception as e:
            print(e)
    
    def createDimensionTable(self, conn, engine, dataFrame):
        customer = pd.DataFrame(dataFrame[['City','Country', 'Customer ID', 'Customer Name' ]])
        product = pd.DataFrame(dataFrame[['Product ID', 'Product Name', 'Segment']])  
        customer.drop_duplicates(keep='first')
        product.drop_duplicates(keep='first')
        print(type(customer))
        try:
            customer.to_sql('customer', con=engine, if_exists = 'replace', index=False)
        except Exception as e:
            print(e)
            
        try:
            product.to_sql('product', con=engine, if_exists = 'replace', index=False)
        except Exception as e:
            print(e)  
        
        
        
        

        
        