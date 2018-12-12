import re

import pandas as pd
import requests


def saveImage(cityID):



    print(cityID[2])
    for i in [2,3]:
        cityID[i] = re.sub('/', '', cityID[i])
        # use \\ to avoid dangling metacharacter
        cityID[i] = re.sub('\\?','',cityID[i])
        cityID[i] = re.sub(' ','',cityID[i])
        cityID[i] = re.sub('\r','',cityID[i])
        cityID[i] = re.sub('\n','',cityID[i])
    image_backgroud_url = 'https://maps.googleapis.com/maps/api/staticmap?&center='  + cityID[2] + ',' + cityID[3] + '&zoom=10&format=png&maptype=roadmap&style=feature:road|visibility:off&style=element:labels%7Cvisibility:off&size=640x640&scale=2&key=AIzaSyCBj1rX0X4g7KaGueU1du_l4jzGfIQO1NY'
    image_road_url = 'https://maps.googleapis.com/maps/api/staticmap?&center='  + cityID[2] + ',' + cityID[3] +  '&zoom=10&format=png&maptype=roadmap&style=visibility:off&style=feature:road|visibility:on&style=element:labels%7Cvisibility:off&size=640x640&scale=2&key=AIzaSyCBj1rX0X4g7KaGueU1du_l4jzGfIQO1NY'
    image_roadmap_url = 'https://maps.googleapis.com/maps/api/staticmap?&center=' + cityID[2] + ',' + cityID[3] + '&zoom=10&format=png&maptype=roadmap&style=element:labels%7Cvisibility:off&size=640x640&scale=2&key=AIzaSyCBj1rX0X4g7KaGueU1du_l4jzGfIQO1NY'
    image_satellite_url = 'https://maps.googleapis.com/maps/api/staticmap?&center=' + cityID[2] + ',' + cityID[3] + '&zoom=10&format=png&maptype=satellite&style=element:labels%7Cvisibility:off&size=640x640&scale=2&key=AIzaSyCBj1rX0X4g7KaGueU1du_l4jzGfIQO1NY'
    satellite = requests.get(image_satellite_url)
    backgroud = requests.get(image_backgroud_url)
    road = requests.get(image_road_url)
    roadmap = requests.get(image_roadmap_url)
    with open("./ImageSet/Background/" + str(cityID[0]) + ".background_"  + str(cityID[2]) + ".png", "wb") as f:
        f.write(backgroud.content)
    with open("./ImageSet/Road/" + str(cityID[0]) + ".road_"  + str(cityID[2]) + ".png", "wb") as f:
        f.write(road.content)
    with open("./ImageSet/RoadMap/" + str(cityID[0]) + ".roadmap_"  + str(cityID[2]) + ".png", "wb") as f:
        f.write(roadmap.content)
    with open("./ImageSet/Satellite/" + str(cityID[0]) + ".satellite_" + str(cityID[2]) + ".png", "wb") as f:
        f.write(satellite.content)


def saveImageTwo(cityID, id):
    image_backgroud_url = 'https://maps.googleapis.com/maps/api/staticmap?&center=' + cityID[
        0] + '&zoom=10&format=png&maptype=roadmap&style=feature:road|visibility:off&style=element:labels%7Cvisibility:off&size=640x640&scale=2&key=AIzaSyCBj1rX0X4g7KaGueU1du_l4jzGfIQO1NY'
    image_road_url = 'https://maps.googleapis.com/maps/api/staticmap?&center=' + cityID[
        0] + '&zoom=10&format=png&maptype=roadmap&style=visibility:off&style=feature:road|visibility:on&style=element:labels%7Cvisibility:off&size=640x640&scale=2&key=AIzaSyCBj1rX0X4g7KaGueU1du_l4jzGfIQO1NY'
    image_roadmap_url = 'https://maps.googleapis.com/maps/api/staticmap?&center=' + cityID[
        0] + '&zoom=10&format=png&maptype=roadmap&style=element:labels%7Cvisibility:off&size=640x640&scale=2&key=AIzaSyCBj1rX0X4g7KaGueU1du_l4jzGfIQO1NY'
    image_satellite_url = 'https://maps.googleapis.com/maps/api/staticmap?&center=' + cityID[
        0] + '&zoom=10&format=png&maptype=satellite&style=element:labels%7Cvisibility:off&size=640x640&scale=2&key=AIzaSyCBj1rX0X4g7KaGueU1du_l4jzGfIQO1NY'
    backgroud = requests.get(image_backgroud_url)
    road = requests.get(image_road_url)
    roadmap = requests.get(image_roadmap_url)
    satellite = requests.get(image_satellite_url)
    cityID[0] = re.sub('/', '', cityID[0])
    # use \\ to avoid dangling metacharacter
    cityID[0] = re.sub('\\?','',cityID[0])
    with open("./ImageSet/LabelBackground/" + id + '_' + cityID[0] + "_background.png", "wb") as f:
        f.write(backgroud.content)
    with open("./ImageSet/LabelRoad/" + id + '_' + cityID[0] + "_road.png", "wb") as f:
        f.write(road.content)
    with open("./ImageSet/LabelRoadMap/" + id + '_' + cityID[0] + "_roadmap.png", "wb") as f:
        f.write(roadmap.content)
    with open("./ImageSet/LabelSatellite/" + id + '_' + cityID[0] + "_satellite.png", "wb") as f:
        f.write(satellite.content)


def saveIt(dataFile,idxS,idxE):
    for i in range(idxS,idxE):
        print(i)
        # saveImage([str(data[i][0]), data[i][2], data[i][3]]) # Searching the 437 city maps
        print(dataFile[i])
        saveImage(dataFile[i])

# My Multi-threading
import threading

data = pd.read_csv('./Data/OldData/PopulationLatitudeLongitudeNoKorea.csv').values
#saveIt(data,3950,3953)
ThreadStart = True
if ThreadStart:
    thread_size = 60
    thread_length = len(data)//thread_size
    count = 0
    threadList = []
    print(thread_length)
    for i in range(thread_size+1):
        newThread = threading.Thread(target=saveIt,args=(data,count, min(count + thread_length,len(data)),))
        count += thread_length
        newThread.start()
        threadList.append(newThread)
    for i in range(thread_size):
        threadList[i].join()
    print("Done")

'''
t1 = threading.Thread(target=saveIt,args=(data,0,500,))
t2 = threading.Thread(target=saveIt,args=(data,500,1000,))
t3 = threading.Thread(target=saveIt,args=(data,1000,1500,))
t4 = threading.Thread(target=saveIt,args=(data,1500,2000,))
t5 = threading.Thread(target=saveIt,args=(data,2000,2500,))
t6 = threading.Thread(target=saveIt,args=(data,2500,3000,))
t7 = threading.Thread(target=saveIt,args=(data,3000,len(data)-1,))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()



t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
print("Done")
'''
