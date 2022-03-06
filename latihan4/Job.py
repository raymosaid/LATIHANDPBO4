from Person import Person

class Job(Person):

   #variable/atribut private
    __nip = ""
    __companyName = ""
    __position = ""

    #membuat konsruktor untuk mengubah/mengakses variabel/atribut private
    def __init__(self, nip, companyName, position):
        self.__nip = nip
        self.__companyName = companyName
        self.__gender = position
    
    #membuat fungsi untuk mengeset variabel/atribut private
    def setnip(self, nip):
        self.__nip = nip
    def setcompanyName(self, companyName):
        self.__companyName = companyName
    def setposition(self, position):
        self.__position = position
        
    #membuat fungsi untuk me-return hasil
    def getnip(self):
        return self.__nip
    def getcompanyName(self):
        return self.__companyName
    def getposition(self):
        return self.__position

    pass
