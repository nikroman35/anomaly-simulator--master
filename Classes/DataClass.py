
class BaseValue:

    def __init__(self, value, error=None):
        self.value = value
        self.error = error

class DataClass:

    def __init__(self,
                 signature="b'A', b'E', b'N', b'T'",
                 type=BaseValue(4),
                 sectionLenght=BaseValue(81),
                 checkSum=BaseValue(0),
                 telemetrySign=BaseValue(0),
                 UAVStatus=BaseValue(0),
                 voltage=BaseValue(0),
                 amperage=BaseValue(0),
                 flightTime=BaseValue(0),
                 height=BaseValue(0),
                 pitch=BaseValue(0),
                 roll=BaseValue(0),
                 prowl=BaseValue(0),
                 horSpeed=BaseValue(0),
                 verSpeed=BaseValue(0),
                 numOfSat=BaseValue(0),
                 GPSQuality=BaseValue(0),
                 signalStrength=BaseValue(0),
                 gasLevel=BaseValue(0),
                 chargeLevel=BaseValue(0),
                 amperageConsumption=BaseValue(0),
                 powerConsumption=BaseValue(0),
                 vibrationLevel=BaseValue(0),
                 GPSAccuracy=BaseValue(0),
                 UAVLat=BaseValue(0),
                 UAVLon=BaseValue(0),
                 pointLat=BaseValue(0),
                 pointLon=BaseValue(0)):

        self.signature = signature
        self.type = type
        self.sectionLenght = sectionLenght
        self.checkSum = checkSum
        self.telemetrySign = telemetrySign
        self.UAVStatus = UAVStatus
        self.voltage = voltage
        self.amperage = amperage
        self.flightTime = flightTime
        self.height = height
        self.pitch = pitch
        self.roll = roll
        self.prowl = prowl
        self.horSpeed = horSpeed
        self.verSpeed = verSpeed
        self.numOfSat = numOfSat
        self.GPSQuality = GPSQuality
        self.signalStrength = signalStrength
        self.gasLevel = gasLevel
        self.chargeLevel = chargeLevel
        self.amperageConsumption = amperageConsumption
        self.powerConsumption = powerConsumption
        self.vibrationLevel = vibrationLevel
        self.GPSAccuracy = GPSAccuracy
        self.UAVLat = UAVLat
        self.UAVLon = UAVLon
        self.pointLat = pointLat
        self.pointLon = pointLon