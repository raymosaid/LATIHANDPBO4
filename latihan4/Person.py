class Person():

    #variable/atribut private
    __nik = ""
    __name = ""
    __gender = ""

    #membuat konsruktor untuk mengubah/mengakses variabel/atribut private
    def __init__(self, nik, name, gender):
        self.__nik = nik
        self.__name = name
        self.__gender = gender
    
    #membuat fungsi untuk mengeset variabel/atribut private
    def setnik(self, nik):
        self.__nik = nik
    def setname(self, name):
        self.__name = name
    def setgender(self, gender):
        self.__gender = gender
        
    #membuat fungsi untuk me-return hasil
    def getnik(self):
        return self.__nik
    def getname(self):
        return self.__name
    def getgender(self):
        return self.__gender

    def sleep(self):
        if self.__gender == "male":
            print("This guy is sleeping at day, because he work in night")
        elif self.__gender == "female":
            print("This woman is sleeping at night, because she work at daytime")
