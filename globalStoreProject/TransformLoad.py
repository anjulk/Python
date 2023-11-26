import os 
import sys
import argparse
from utility.logging_util.loggingConfig import *
from utility.sqlDatabase.sqlDatabaseRawUpload import *
from config import config
from utility.encryptDecrypt.encrypt_decrypt import encrypt , decrypt
from utility.Transform.transformData import *



def TransformLoad():
    
    
    logger.info("Running {0}. Connecting to SQL database {1}".format("TransformLoad Program",config.database_name) )
    mysqlObj = mySQLWrapper()
    (connection, engine) = mysqlObj.get_mySQL_Connection()
    
    logger.info("Running {0}. Connected to SQL database {1}".format("TransformLoad Program",config.database_name) )
   

    logger.info("Running {0}. Reading from SQL database {1}".format("TransformLoad Program",config.database_name) )
   
    dataFrameFile = mysqlObj.readDataIntoDataFrame(connection, engine)

    logger.info("Running {0}. Finished reading from SQL database {1}".format("TransformLoad Program",config.database_name) )
    
    transformObj = transformData(dataFrameFile)
    newDataFrame = transformObj.transfrom()
    if dataFrameFile.shape == newDataFrame.shape:
        logger.info("No records are dropped Old dataframe Shape {0}  and New  Dataframe shape{1}"\
            .format(dataFrameFile.shape, newDataFrame.shape)) 
    else:
        logger.info("records are dropped Old dataframe Shape {0}  and New  Dataframe shape{1}"\
            .format(dataFrameFile.shape, newDataFrame.shape)) 
        
    logger.info("Create Dimension Table {0} and {1}".format("Customer","Product") )
    
    mysqlObj.createDimensionTable(connection, engine, newDataFrame)
    logger.info("Dimension Tables {0} and {1} are created".format("Customer","Product") )  


    logger.info("Create Fact Table {0} ".format("Order") )
    mysqlObj.createFactTable(connection, engine, newDataFrame)
    logger.info("Fact Table {0} is created".format("Order") )  
        
    connection.close()
    
    
    
   


