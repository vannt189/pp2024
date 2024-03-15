class info: 
    def __init__(self,id,name):
        self.__id = id
        self.__name = name

    def getID(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def setName(self,name):
        self.__name = name
    def getInfo(self):
        print(f"ID: {self.__id}, Name: {self.__name}")

class Student(info):
    def __init__(self,id,name,dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
    
    def getID(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getDOB(self):
        return self.__dob
    
  

class Course(info):
    def __init__(self,id,name,credit):
        self.__id = id
        self.__name = name
        self.__credit = credit

    def getID(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getCredit(self):
        return self.__credit