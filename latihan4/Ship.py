from Vehicle import Vehicle

class Ship(Vehicle):

    #variable/atribut private
    __shipage = 0
    __shiptype = ""
    __countryOfManufacture = ""

    #membuat konsruktor untuk mengubah/mengakses variabel/atribut private
    def __init__(self, shipage, shiptype, countryOfManufacture):
        self.__shipage = shipage
        self.__shiptype = shiptype
        self.__countryOfManufacture = countryOfManufacture
    
    #membuat fungsi untuk mengeset variabel/atribut private
    def setage(self, shipage):
        self.__age = shipage
    def setshiptype(self, shiptype):
        self.__shiptype = shiptype
    def setcountryOfManufacture(self, countryOfManufacture):
        self.__countryOfManufacture = countryOfManufacture
        
    #membuat fungsi untuk me-return hasil
    def getage(self):
        return self.__shipage
    def getshiptype(self):
        return self.__shiptype
    def getcountryOfManufacture(self):
        return self.__countryOfManufacture

    pass
