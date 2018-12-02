import re

import pandas as pd
import requests


def saveImage(cityID):
    image_backgroud_url = 'https://maps.googleapis.com/maps/api/staticmap?&center=' + cityID[0] + ',' + cityID[
        1] + '&zoom=10&format=png&maptype=roadmap&style=feature:road|visibility:off&style=element:labels%7Cvisibility:off&size=640x640&scale=2&key=AIzaSyCBj1rX0X4g7KaGueU1du_l4jzGfIQO1NY'
    image_road_url = 'https://maps.googleapis.com/maps/api/staticmap?&center=' + cityID[0] + ',' + cityID[
        1] + '&zoom=10&format=png&maptype=roadmap&style=visibility:off&style=feature:road|visibility:on&style=element:labels%7Cvisibility:off&size=640x640&scale=2&key=AIzaSyCBj1rX0X4g7KaGueU1du_l4jzGfIQO1NY'
    image_roadmap_url = 'https://maps.googleapis.com/maps/api/staticmap?&center=' + cityID[0] + ',' + cityID[
        1] + '&zoom=10&format=png&maptype=roadmap&style=element:labels%7Cvisibility:off&size=640x640&scale=2&key=AIzaSyCBj1rX0X4g7KaGueU1du_l4jzGfIQO1NY'
    backgroud = requests.get(image_backgroud_url)
    road = requests.get(image_road_url)
    roadmap = requests.get(image_roadmap_url)
    cityID[0] = re.sub('/', '', cityID[0])
    cityID[1] = re.sub('/', '', cityID[1])
    with open("./ImageSet/Background/" + cityID[0] + ".background_" + cityID[1] + "|" + cityID[2] + ".png", "wb") as f:
        f.write(backgroud.content)
    with open("./ImageSet/Road/" + cityID[0] + ".road_" + cityID[1] + "|" + cityID[2] + ".png", "wb") as f:
        f.write(road.content)
    with open("./ImageSet/RoadMap/" + cityID[0] + ".roadmap_" + cityID[1] + "|" + cityID[2] + ".png", "wb") as f:
        f.write(roadmap.content)


def saveImageTwo(cityID, id):
    image_backgroud_url = 'https://maps.googleapis.com/maps/api/staticmap?&center=' + cityID[
        0] + '&zoom=10&format=png&maptype=roadmap&style=feature:road|visibility:off&style=element:labels%7Cvisibility:off&size=640x640&scale=2&key=AIzaSyCBj1rX0X4g7KaGueU1du_l4jzGfIQO1NY'
    image_road_url = 'https://maps.googleapis.com/maps/api/staticmap?&center=' + cityID[
        0] + '&zoom=10&format=png&maptype=roadmap&style=visibility:off&style=feature:road|visibility:on&style=element:labels%7Cvisibility:off&size=640x640&scale=2&key=AIzaSyCBj1rX0X4g7KaGueU1du_l4jzGfIQO1NY'
    image_roadmap_url = 'https://maps.googleapis.com/maps/api/staticmap?&center=' + cityID[
        0] + '&zoom=10&format=png&maptype=roadmap&style=element:labels%7Cvisibility:off&size=640x640&scale=2&key=AIzaSyCBj1rX0X4g7KaGueU1du_l4jzGfIQO1NY'
    backgroud = requests.get(image_backgroud_url)
    road = requests.get(image_road_url)
    roadmap = requests.get(image_roadmap_url)
    cityID[0] = re.sub('/', '', cityID[0])
    # use \\ to avoid dangling metacharacter
    cityID[0] = re.sub('\\?','',cityID[0])
    with open("./ImageSet/LabelBackground/" + id + '_' + cityID[0] + "_background.png", "wb") as f:
        f.write(backgroud.content)
    with open("./ImageSet/LabelRoad/" + id + '_' + cityID[0] + "_road.png", "wb") as f:
        f.write(road.content)
    with open("./ImageSet/LabelRoadMap/" + id + '_' + cityID[0] + "_roadmap.png", "wb") as f:
        f.write(roadmap.content)


def saveIt(dataFile):
    for i in range(0, len(dataFile)):
        print(i)
        # saveImage([str(data[i][0]), data[i][2], data[i][3]]) # Searching the 437 city maps
        saveImageTwo(dataFile[i], str(i))


data = pd.read_csv('./Data/NoCountryCityGDP300.csv').values
saveIt(data)
