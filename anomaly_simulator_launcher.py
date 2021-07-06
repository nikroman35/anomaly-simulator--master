
from Classes.DataClass import *
from Classes.Time import timeFunc
from Classes.FileReader import *
from Classes.Generator import *


readData = fileWorker.readDataFromFile()
fileName = input("Введите имя файла\n")
numberOfIterations = int(input("Введите кол-во итераций\n"))
arrayWithAnomaly = []

for i in range(numberOfIterations):
    anomalyData = anomalyGenerator.generateAnomaly(readData)
    arrayWithAnomaly.append(anomalyData)
    fileWorker.createFileWithData(fileName, anomalyData)




