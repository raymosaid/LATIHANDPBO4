from Vehicle import Vehicle

class Airplane(Vehicle):

    #variable/atribut private
    __airplanetype = ""
    __airplaneage = 0
    __wingsLength = 0

    #membuat konsruktor untuk mengubah/mengakses variabel/atribut private
    def __init__(self, airplanetype, airplaneage, wingsLength):
        self.__airplanetype = airplanetype
        self.__airplaneage = airplaneage
        self.__wingsLength = wingsLength
    
    #membuat fungsi untuk mengeset variabel/atribut private
    def setairplanetype(self, airplanetype):
        self.__airplanetype = airplanetype
    def setage(self, airplaneage):
        self.__airplaneage = airplaneage
    def setwingsLength(self, wingsLength):
        self.__wingsLength = wingsLength
        
    #membuat fungsi untuk me-return hasil
    def getairplanetype(self):
        return self.__airplanetype
    def getage(self):
        return self.__airplaneage
    def getwingsLength(self):
        return self.__wingsLength

    pass
        