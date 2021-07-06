from Classes.DataClass import *
import numpy as np

class valueBorder:

    vuint8 = (0, 255)
    vuint16 = (0, 65535)
    vuint32 = (0, 4294967295)
    vint16 = (-32768, 32767)
    vint32 = (-2147483648, 2147483647)
    vfloat = (-180, 180)

    def __init__(self, value, error):

        self.top = value + error
        self.bottom = value - error
        self.rangeTop = 1
        self.rangeBottom = 0

        if type(value) == np.uint8:
            self.rangeTop = self.vuint8[1]
            self.rangeBottom = self.vuint8[0]
        elif type(value) == np.uint16:
            self.rangeTop = self.vuint16[1]
            self.rangeBottom = self.vuint16[0]
        elif type(value) == np.uint32:
            self.rangeTop = self.vuint32[1]
            self.rangeBottom = self.vuint32[0]
        elif type(value) == np.int16:
            self.rangeTop = self.vint16[1]
            self.rangeBottom = self.vint16[0]
        elif type(value) == np.int32:
            self.rangeTop = self.vint32[1]
            self.rangeBottom = self.vint32[0]
        elif type(value) == np.float:
            self.rangeTop = self.vfloat[1]
            self.rangeBottom = self.vfloat[0]

class anomalyGenerator:

    @staticmethod

    def generateAnomaly(dataClass: DataClass):
        anomalyClass = DataClass()

        anomalyClass.type.value = anomalyGenerator.newValue(dataClass.type.value, dataClass.type.error)
        anomalyClass.sectionLenght.value = anomalyGenerator.newValue(dataClass.sectionLenght.value, dataClass.sectionLenght.error)
        anomalyClass.checkSum.value = anomalyGenerator.newValue(dataClass.checkSum.value, dataClass.checkSum.error)
        anomalyClass.telemetrySign.value = anomalyGenerator.newValue(dataClass.telemetrySign.value, dataClass.telemetrySign.error)
        anomalyClass.UAVStatus.value = anomalyGenerator.newValue(dataClass.UAVStatus.value, dataClass.UAVStatus.error)
        anomalyClass.voltage.value = anomalyGenerator.newValue(dataClass.voltage.value, dataClass.voltage.error)
        anomalyClass.amperage.value = anomalyGenerator.newValue(dataClass.amperage.value, dataClass.amperage.error)
        anomalyClass.flightTime.value = anomalyGenerator.newValue(dataClass.flightTime.value, dataClass.flightTime.error)
        anomalyClass.height.value = anomalyGenerator.newValue(dataClass.height.value, dataClass.height.error)
        anomalyClass.pitch.value = anomalyGenerator.newValue(dataClass.pitch.value, dataClass.pitch.error)
        anomalyClass.roll.value = anomalyGenerator.newValue(dataClass.roll.value, dataClass.roll.error)
        anomalyClass.prowl.value = anomalyGenerator.newValue(dataClass.prowl.value, dataClass.prowl.error)
        anomalyClass.horSpeed.value = anomalyGenerator.newValue(dataClass.horSpeed.value, dataClass.horSpeed.error)
        anomalyClass.verSpeed.value = anomalyGenerator.newValue(dataClass.verSpeed.value, dataClass.verSpeed.error)
        anomalyClass.numOfSat.value = anomalyGenerator.newValue(dataClass.numOfSat.value, dataClass.numOfSat.error)
        anomalyClass.GPSQuality.value = anomalyGenerator.newValue(dataClass.GPSQuality.value, dataClass.GPSQuality.error)
        anomalyClass.signalStrength.value = anomalyGenerator.newValue(dataClass.signalStrength.value, dataClass.signalStrength.error)
        anomalyClass.gasLevel.value = anomalyGenerator.newValue(dataClass.gasLevel.value, dataClass.gasLevel.error)
        anomalyClass.chargeLevel.value = anomalyGenerator.newValue(dataClass.chargeLevel.value, dataClass.chargeLevel.error)
        anomalyClass.amperageConsumption.value = anomalyGenerator.newValue(dataClass.amperageConsumption.value, dataClass.amperageConsumption.error)
        anomalyClass.powerConsumption.value = anomalyGenerator.newValue(dataClass.powerConsumption.value, dataClass.powerConsumption.error)
        anomalyClass.vibrationLevel.value = anomalyGenerator.newValue(dataClass.vibrationLevel.value, dataClass.vibrationLevel.error)
        anomalyClass.GPSAccuracy.value = anomalyGenerator.newValue(dataClass.GPSAccuracy.value, dataClass.GPSAccuracy.error)
        anomalyClass.UAVLat.value = anomalyGenerator.newValue(dataClass.UAVLat.value, dataClass.UAVLat.error)
        anomalyClass.UAVLon.value = anomalyGenerator.newValue(dataClass.UAVLon.value, dataClass.UAVLon.error)
        anomalyClass.pointLat.value = anomalyGenerator.newValue(dataClass.pointLat.value, dataClass.pointLat.error)
        anomalyClass.pointLon.value = anomalyGenerator.newValue(dataClass.pointLon.value, dataClass.pointLon.error)

        return anomalyClass

    def newValue(value, error):
        if error != None:
            if type(value) == np.uint8:
                returnValue = valueBorder(value, error)
                bottom = None if returnValue.rangeBottom == returnValue.bottom else np.random.randint(returnValue.rangeBottom,
                                                                                                      returnValue.bottom,
                                                                                                      dtype=np.uint8)

                top = None if returnValue.top == returnValue.rangeTop else np.random.randint(returnValue.top,
                                                                                             returnValue.rangeTop,
                                                                                             dtype=np.uint8)
                array = list(filter(None, [bottom, top]))

                if len(array) > 0:
                    index = np.random.randint(0, len(array))
                    return array[index]

                return None

            elif type(value) == np.uint16:
                returnValue = valueBorder(value, error)
                bottom = None if returnValue.rangeBottom == returnValue.bottom else np.random.randint(returnValue.rangeBottom,
                                                                                                      returnValue.bottom,
                                                                                                      dtype=np.uint16)

                top = None if returnValue.top == returnValue.rangeTop else np.random.randint(returnValue.top,
                                                                                             returnValue.rangeTop,
                                                                                             dtype=np.uint16)
                array = list(filter(None, [bottom, top]))

                if len(array) > 0:
                    index = np.random.randint(0, len(array))
                    return array[index]

                return None

            elif type(value) == np.uint32:
                returnValue = valueBorder(value, error)
                bottom = None if returnValue.rangeBottom == returnValue.bottom else np.random.randint(returnValue.rangeBottom,
                                                                                                      returnValue.bottom,
                                                                                                      dtype=np.uint32)

                top = None if returnValue.top == returnValue.rangeTop else np.random.randint(returnValue.top,
                                                                                             returnValue.rangeTop,
                                                                                             dtype=np.uint32)
                array = list(filter(None, [bottom, top]))

                if len(array) > 0:
                    index = np.random.randint(0, len(array))
                    return array[index]

                return None

            elif type(value) == np.int16:
                returnValue = valueBorder(value, error)
                bottom = None if returnValue.rangeBottom == returnValue.bottom else np.random.randint(returnValue.rangeBottom,
                                                                                                      returnValue.bottom,
                                                                                                      dtype=np.int16)

                top = None if returnValue.top == returnValue.rangeTop else np.random.randint(returnValue.top,
                                                                                                   returnValue.rangeTop,
                                                                                                   dtype=np.int16)
                array = list(filter(None, [bottom, top]))

                if len(array) > 0:
                    index = np.random.randint(0, len(array))
                    return array[index]

                return None

            elif type(value) == np.int32:
                returnValue = valueBorder(value, error)
                bottom = None if returnValue.rangeBottom == returnValue.bottom else np.random.randint(returnValue.rangeBottom,
                                                                                                      returnValue.bottom,
                                                                                                      dtype=np.int32)

                top = None if returnValue.top == returnValue.rangeTop else np.random.randint(returnValue.top,
                                                                                             returnValue.rangeTop,
                                                                                             dtype=np.int32)
                array = list(filter(None, [bottom, top]))

                if len(array) > 0:
                    index = np.random.randint(0, len(array))
                    return array[index]

                return None

            elif type(value) == np.float:
                returnValue = valueBorder(value, error)

                bottom = None if returnValue.rangeBottom == returnValue.bottom else round(np.random.uniform(returnValue.rangeBottom,
                                                                                                      returnValue.bottom), 12)

                top = None if returnValue.top == returnValue.rangeTop else round(np.random.uniform(returnValue.top,
                                                                                             returnValue.rangeTop), 12)
                array = list(filter(None, [bottom, top]))

                if len(array) > 0:
                    index = np.random.randint(0, len(array))
                    return array[index]

                return None
        else:
            return value
