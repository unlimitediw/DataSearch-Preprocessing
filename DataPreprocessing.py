'''
Population, City Name, Country name, latitude and longitude
'''
import sys
import pandas as pd
import re
import numpy as np

class CSVPurer(object):

    def __init__(self, readPath):
        self.data = pd.read_csv(readPath)
        # csv.label is list(pd.axes[1])
        self.labelList = list(self.data.axes[1])
        # Now self.data is np.ndarray
        self.data = self.data.values
        # the final csv file label

    def saveCSV(self, savePath,resLabel = False):
        pdData = pd.DataFrame(self.data)
        pdData.to_csv(savePath,header = resLabel, index=False)

    # remove the data row of self.data with row and column specific
    def removeRow(self, rowList=[], columnList=[]):
        # Delete index with list operation
        self.data = np.delete(self.data, rowList, axis=0)
        self.data = np.delete(self.data, columnList, axis=1)

    # remove the data row pf self.data by specific regex rule
    def removeSpecificRow(self,rule):
        if rule == '2014CitiesFeature':

            def checkCountry(name):
                # this means that it is the country name
                if name[3] == ':':
                    return True
                else:
                    return False

            removeList = []
            for i in range(len(self.data)):
                if checkCountry(self.data[i][0]):
                    removeList.append(i)
                # Get the pure city name
                self.data[i][0] = self.data[i][0][9:]
            self.data = np.delete(self.data,removeList,axis=0)

    # switch column order of the self.data
    def switchColumn(self,order):
        self.data = self.data[:,order]

    def addFeatureByCityName(self,newPath):
        # Get New data file in ndarray format
        newData = pd.read_csv(newPath).values
        # City Name Searching Dic
        cityDic = {}
        for city in self.data:
            cityName = city[0]
            cityDic[cityName] = city
        # Check if newData exist in cityDic and save in a new list then change to ndarray
        combineData = []
        for checkCity in newData:
            cityName = checkCity[0]
            if cityName in cityDic:
                combineData.append(list(cityDic[cityName]) + list(checkCity[1:]))
        self.data = np.asarray(combineData)

    def NanProcessing(self,rule,idx):
        if rule == 'replenishByMedian':
            processList = self.data[:,idx] == None
            tempList = self.data[:,idx] != None
            medianValue = np.median(self.data[tempList].T[idx])
            self.data = self.data.T
            self.data[idx][processList] = medianValue

    def DataRandomize(self):
        indices = np.random.choice(self.data.shape[0],self.data.shape[0],replace = False)
        self.data = self.data[indices]



'''
# Some Old Processing Example
#a = CSVPurer('./Data/2014CitiesFeature.csv')
a = CSVPurer('./Data/2014CitiesFeature.csv')
a.removeRow(rowList=[0,1, 2, 3], columnList=[1, 3, 9, 10])
a.removeSpecificRow('2014CitiesFeature')
a.saveCSV('./Data/2014CitiesFeatureCheck.csv',resLabel= ['CityName','Population','Latitude','Longitude','Area','GreenAreaPerPers', 'Polycentricity','PopulationInCore','#Gov','#GovInCore','GDP'])

b = CSVPurer('./Data/PopulationLatitudeLongitude.csv')
b.removeRow([],[0,3])
b.switchColumn([1,0,2,3])
b.saveCSV('./Data/CitiesPLL.csv')
'''
a = CSVPurer('./Data/CityFeatures2014.csv')
a.addFeatureByCityName('./Data/CityPopLaLg.csv')
a.addFeatureByCityName('./Data/CityGDP.csv')
a.DataRandomize()
a.saveCSV('./Data/Final229CitiesData.csv',resLabel = ['CityName','Area','GreenAreaPerPers', 'Polycentricity','PopulationInCore','#Gov','#GovInCore','Population','Latitude','Longitude','GDP'])