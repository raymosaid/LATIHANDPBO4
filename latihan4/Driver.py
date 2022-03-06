from Person import Person

class Driver(Person):

    #variable/atribut private
    __licenseID = ""
    __activeUntil = 0
    __vehicleType = ""

    #membuat konsruktor untuk mengubah/mengakses variabel/atribut private
    def __init__(self, licenseID, activeUntil, vehicleType):
        self.__licenseID = licenseID
        self.__activeUntil = activeUntil
        self.__vehicleType = vehicleType
    
    #membuat fungsi untuk mengeset variabel/atribut private
    def setlicenseID(self, licenseID):
        self.__licenseID = licenseID
    def setactiveUntil(self, activeUntil):
        self.__activeUntil = activeUntil
    def setvehicleType(self, vehicleType):
        self.__vehicleType = vehicleType
        
    #membuat fungsi untuk me-return hasil
    def getlicenseID(self):
        return self.__licenseID
    def getactiveUntil(self):
        return self.__activeUntil
    def getvehicleType(self):
        return self.__vehicleType

    pass
