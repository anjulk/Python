import pandas as pd
import requests 
import json
from config.config import *
import sqlalchemy as sa
import mysql.connector as connector



class API:
    def __init__(self , url):
        self.url = url     
        
    def get_api_data(self):
        data = None
        dataType = None
        try:
            self.response = requests.get(self.url)
            print(self.response.headers["Content-Type"])
            print(self.response.status_code)
            if 'json' in self.response.headers["Content-Type"]:
                data = self.response.json()
                dataType = 'json'
            else: 
                data  = self.response.text
                dataType = 'text'

        except requests.exceptions.RequestException as e:
            print(" Error getting API data: {}".format(e))
            return None
        return data , dataType    
    
    def send_data_to_api():
      pass

class sqlData:
    def __init__(self, data, type, dataBaseConfig):
        self.data = data
        self.type = type
        self.sqlConnectorObj = None
        self.sqlEngineObj = None
        self.config = dataBaseConfig
        self.databaseUrl = f"mysql+mysqlconnector://{dataBaseConfig['user']}:{dataBaseConfig['password']}@{dataBaseConfig['host']}/{dataBaseConfig['database']}"

        
    def dataBaseConnect(self):
        print(self.config)
        print(self.databaseUrl)
        try:
            self.sqlConnectorObj = connector.connect(**self.config)
            print(self.sqlConnectorObj)
        except Exception as e:
            print("Error connecting to SQL Server: {}".format(e))
        
        try:
            self.sqlEngineObj = sa.create_engine(self.databaseUrl)
            print(self.sqlEngineObj)
        except Exception as e:
            print("Error connecting to SQL Engine: {}".format(e))

    def dataParse(self):
        data_df = pd.DataFrame()
        data_list = []
        if self.type == 'json':
            dataTemp = {}
            for i in self.data:
#                print("{0} {1} {2}  ".format( i['id'], i['name'], i['tagline']))
                data_dict = {
                    'id': i['id'],
                    'name' : i['name'],
                    'tagline' : i['tagline'],
                    'method' : str(i['method'])
                }
                list_data = [i['id'], i['name'], i['tagline'] ]
                data_list.append(tuple(list_data))      
        else:
            pass
        return data_list
        
    def store_api_data(self):
        self.dataBaseConnect()
        dataStore = self.dataParse()
        print(dataStore)
       
        cursor = self.sqlConnectorObj.cursor()
        
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS DUMMY_DATA (
                           ID INT,
                           NAME VARCHAR(50),
                           TAGLINE VARCHAR(100)
                       )
                      """)   
        query = "INSERT INTO DUMMY_DATA (ID, NAME, TAGLINE) VALUES (%s, %s, %s);"
        cursor.executemany(query, dataStore)

        self.sqlConnectorObj.commit()
        self.sqlConnectorObj.close()
        
        dataframe_data = pd.DataFrame(dataStore, columns=['id', 'name', 'tagline'])

        
        dataframe_data.to_sql('DUMMY_DATA', self.sqlEngineObj, if_exists='append', index=False)
        

    def get_stored_data(self):
        pass

def main():
   url = 'https://api.punkapi.com/v2/beers?food=burger'
   apiObj = API(url)
   data, dataType = apiObj.get_api_data()
   print(dataType)
# Store the data in the database
   dataBaseConfig = {
       'host' : HOST,
       'user' : USER,
       'password' : PASSWORD,
       'database' : DATABASENAME
   }
   sqlObj = sqlData(data, dataType, dataBaseConfig)
   sqlObj.store_api_data()
   
   
   


if __name__ == "__main__":
    main()

#url = 'https://randomuser.me/api'
#url = 'https://api.punkapi.com/v2/beers?food=burger'
#url = 'https://xkcd.com/353/'

