import os
import sys
import pandas as pd
from datetime import datetime
from utility.logging_util.loggingConfig import *


class transformData:
    def __init__(self, dataFrame):
        self.dataFrame = dataFrame
    
    def schemaValidation(self):
         logger.info("{0}".format("Schema Validation Start") )
         print(self.dataFrame.columns)
         logger.info("{0}".format("Schema Validation Ends") )
        
    
    def nullValidation(self):
         logger.info("{0}".format("nullValidation Start") )
         nullDict = {}
         for col in self.dataFrame.columns:
             non_rows = self.dataFrame[col].isnull().sum()
             nullDict[col] = non_rows
         print(nullDict)
         
         for key, value in nullDict.items():
             if value > 0:
                 if self.dataFrame[key].dtypes != 'object':
                     self.dataFrame[key].fillna(value = self.dataFrame[key].median , axis=1, inplace=True)
                     logger.info("{0} null values fixed".format(self.dataFrame[key]) )
         
         logger.info("{0}".format("nullValidation Ends") )
         return nullDict
    
    def removeDuplicates(self):
         logger.info("{0}".format("removeDuplicates Start") )
         self.dataFrame.drop_duplicates(keep='first')
         logger.info("{0}".format("removeDuplicates Ends") )
    
    def dropBadData(self, nullDict):
         logger.info("{0}".format("dropBadData Start") )
         for col in self.dataFrame.columns:
             newDataFrame = self.dataFrame.drop(self.dataFrame[self.dataFrame[col].isnull()].index)
         logger.info("{0}".format("dropBadData Ends") )
         return newDataFrame
     
     
    def transfrom(self):
       self.schemaValidation()
       nullDict=self.nullValidation()
       self.removeDuplicates()
       newDataFrame= self.dropBadData(nullDict)
       return newDataFrame 