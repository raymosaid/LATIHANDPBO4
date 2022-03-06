from Driver import Driver

class Vehicle(Driver):

    #variable/atribut private
    __fuelType = ""
    __maxPassengers = 0

    #membuat konsruktor untuk mengubah/mengakses variabel/atribut private
    def __init__(self, fuelType, maxPassengers):
        self.__fuelType = fuelType
        self.__maxPassengers = maxPassengers
    
    #membuat fungsi untuk mengeset variabel/atribut private
    def setfuelType(self, fuelType):
        self.__fuelType = fuelType
    def setmaxPassengers(self, maxPassengers):
        self.__maxPassengers = maxPassengers
        
    #membuat fungsi untuk me-return hasil
    def getfuelType(self):
        return self.__fuelType
    def getmaxPassengers(self):
        return self.__maxPassengers

    def move(self):
        if self.__vehicleType == "ship":
            print("This person is sailing ship")
        elif self.__vehicleType == "airplane":
            print("This person is flying airplane")

    pass
        