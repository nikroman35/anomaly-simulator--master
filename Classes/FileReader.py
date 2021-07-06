from Classes.DataClass import *
from Classes.Time import *
import numpy as np
class fileWorker:

    #READ

    @staticmethod
    def stringToValue(str):
        index = str.index("|")
        substring = str[:index]
        if '/' in substring:
            slashIndex = str.index("/")
            after = substring[slashIndex + 1:]
            before = substring[:slashIndex]
            return before, after
        else:
            return substring

    def formatToBaseValue(index, data, classData):

        if type(data) is tuple:
            firstValue = data[0]
            secondValue = data[1]
        else:
            firstValue = data
            secondValue = None

        if index == 0:
            classData.signature = firstValue
        elif index == 1:
            secondValue = np.uint8(secondValue) if secondValue != None else None
            classData.type = BaseValue(np.uint8(firstValue), secondValue)
        elif index == 2:
            secondValue = np.uint8(secondValue) if secondValue != None else None
            classData.sectionLenght = BaseValue(np.uint8(firstValue), secondValue)
        elif index == 3:
            secondValue = np.uint16(secondValue) if secondValue != None else None
            classData.checkSum = BaseValue(np.uint16(firstValue), secondValue)
        elif index == 4:
            secondValue = np.uint8(secondValue) if secondValue != None else None
            classData.telemetrySign = BaseValue(np.uint8(firstValue), secondValue)
        elif index == 5:
            secondValue = np.uint32(secondValue) if secondValue != None else None
            classData.UAVStatus = BaseValue(np.uint32(firstValue), secondValue)
        elif index == 6:
            secondValue = np.uint16(secondValue) if secondValue != None else None
            classData.voltage = BaseValue(np.uint16(firstValue), secondValue)
        elif index == 7:
            secondValue = np.uint16(secondValue) if secondValue != None else None
            classData.amperage = BaseValue(np.uint16(firstValue), secondValue)
        elif index == 8:
            secondValue = np.uint32(secondValue) if secondValue != None else None
            classData.flightTime = BaseValue(np.uint32(firstValue), secondValue)
        elif index == 9:
            secondValue = np.int32(secondValue) if secondValue != None else None
            classData.height = BaseValue(np.int32(firstValue), secondValue)
        elif index == 10:
            secondValue = np.int16(secondValue) if secondValue != None else None
            classData.pitch = BaseValue(np.int16(firstValue), secondValue)
        elif index == 11:
            secondValue = np.int16(secondValue) if secondValue != None else None
            classData.roll = BaseValue(np.int16(firstValue), secondValue)
        elif index == 12:
            secondValue = np.int16(secondValue) if secondValue != None else None
            classData.prowl = BaseValue(np.int16(firstValue), secondValue)
        elif index == 13:
            secondValue = np.int16(secondValue) if secondValue != None else None
            classData.horSpeed = BaseValue(np.int16(firstValue), secondValue)
        elif index == 14:
            secondValue = np.int16(secondValue) if secondValue != None else None
            classData.verSpeed = BaseValue(np.int16(firstValue), secondValue)
        elif index == 15:
            secondValue = np.uint8(secondValue) if secondValue != None else None
            classData.numOfSat = BaseValue(np.uint8(firstValue), secondValue)
        elif index == 16:
            secondValue = np.uint8(secondValue) if secondValue != None else None
            classData.GPSQuality = BaseValue(np.uint8(firstValue), secondValue)
        elif index == 17:
            secondValue = np.uint8(secondValue) if secondValue != None else None
            classData.signalStrength = BaseValue(np.uint8(firstValue), secondValue)
        elif index == 18:
            secondValue = np.uint8(secondValue) if secondValue != None else None
            classData.gasLevel = BaseValue(np.uint8(firstValue), secondValue)
        elif index == 19:
            secondValue = np.uint8(secondValue) if secondValue != None else None
            classData.chargeLevel = BaseValue(np.uint8(firstValue), secondValue)
        elif index == 20:
            secondValue = np.uint16(secondValue) if secondValue != None else None
            classData.amperageConsumption = BaseValue(np.uint16(firstValue), secondValue)
        elif index == 21:
            secondValue = np.uint16(secondValue) if secondValue != None else None
            classData.powerConsumption = BaseValue(np.uint16(firstValue), secondValue)
        elif index == 22:
            secondValue = np.uint16(secondValue) if secondValue != None else None
            classData.vibrationLevel = BaseValue(np.uint16(firstValue), secondValue)
        elif index == 23:
            secondValue = np.uint16(secondValue) if secondValue != None else None
            classData.GPSAccuracy = BaseValue(np.uint16(firstValue), secondValue)
        elif index == 24:
            secondValue = np.float(secondValue) if secondValue != None else None
            classData.UAVLat = BaseValue(np.float(firstValue), secondValue)
        elif index == 25:
            secondValue = np.float(secondValue) if secondValue != None else None
            classData.UAVLon = BaseValue(np.float(firstValue), secondValue)
        elif index == 26:
            secondValue = np.float(secondValue) if secondValue != None else None
            classData.pointLat = BaseValue(np.float(firstValue), secondValue)
        elif index == 27:
            secondValue = np.float(secondValue) if secondValue != None else None
            classData.pointLon = BaseValue(np.float(firstValue), secondValue)

    def readDataFromFile():
        file = open("attackValue.txt")
        data = file.readlines()
        while '\n' in data:
            data.remove('\n')

        returnData = DataClass()

        for i in range(len(data)):
            item = data[i]
            value = fileWorker.stringToValue(item)
            fileWorker.formatToBaseValue(i,value,returnData)

        file.close()
        return returnData

    #WRITE

    @staticmethod
    #filedata - List<DataClass>

    def classToString(dataClass): #разбиене первых 4 байт добавить
        currenttime = timeFunc.getTimeWithFormat()
        returnString = '\n({signature}, ' \
                       '{type},' \
                       ' {sectionLenght}, ' \
                       '{checkSum},' \
                       ' {telemetrySign}, ' \
                       '{UAVStatus}, ' \
                       '{voltage}, ' \
                       '{amperage}, ' \
                       '{flightTime},' \
                       ' {height}, ' \
                       '{pitch}, ' \
                       '{roll}, ' \
                       '{prowl}, ' \
                       '{horSpeed}, ' \
                       '{verSpeed},' \
                       ' {numOfSat},' \
                       ' {GPSQuality},' \
                       ' {signalStrength},' \
                       ' {gasLevel}, ' \
                       '{chargeLevel},' \
                       ' {amperageConsumption},' \
                       ' {powerConsumption},' \
                       ' {vibrationLevel},' \
                       ' {GPSAccuracy},' \
                       ' {UAVLat},' \
                       ' {UAVLon},' \
                       ' {pointLat},' \
                       ' {pointLon}); {time}'.format(signature=dataClass.signature,
                                                       type=dataClass.type.value,
                                                       sectionLenght=dataClass.sectionLenght.value,
                                                       checkSum=dataClass.checkSum.value,
                                                       telemetrySign=dataClass.telemetrySign.value,
                                                       UAVStatus=dataClass.UAVStatus.value,
                                                       voltage=dataClass.voltage.value,
                                                       amperage=dataClass.amperage.value,
                                                       flightTime=dataClass.flightTime.value,
                                                       height=dataClass.height.value,
                                                       pitch=dataClass.pitch.value,
                                                       roll=dataClass.roll.value,
                                                       prowl=dataClass.prowl.value,
                                                       horSpeed=dataClass.horSpeed.value,
                                                       verSpeed=dataClass.verSpeed.value,
                                                       numOfSat=dataClass.numOfSat.value,
                                                       GPSQuality=dataClass.GPSQuality.value,
                                                       signalStrength=dataClass.signalStrength.value,
                                                       gasLevel=dataClass.gasLevel.value,
                                                       chargeLevel=dataClass.chargeLevel.value,
                                                       amperageConsumption=dataClass.amperageConsumption.value,
                                                       powerConsumption=dataClass.powerConsumption.value,
                                                       vibrationLevel=dataClass.vibrationLevel.value,
                                                       GPSAccuracy=dataClass.GPSAccuracy.value,
                                                       UAVLat=dataClass.UAVLat.value,
                                                       UAVLon=dataClass.UAVLon.value,
                                                       pointLat=dataClass.pointLat.value,
                                                       pointLon=dataClass.pointLon.value,
                                                       time=currenttime)
        return returnString


    def createFileWithData(filename, fileData):
        name = "%s.txt" % filename
        data = fileWorker.classToString(fileData)
        myfile = open(name, 'a')
        lines = data.split("\n")

        non_empty_lines = [line for line in lines if line.strip() != ""]

        string_without_empty_lines = ""

        for line in non_empty_lines:
            string_without_empty_lines += line + "\n"

        print(string_without_empty_lines)
        myfile.write(string_without_empty_lines)

        myfile.close()

