# App to manage an electrivity generation company OOP
# power generators - 5
# Customers - 100
# Power Meter- 100
# ----
# Customer HAS A Power Meter

class Company:
    def __init__(self,CustomersList):
        self.CustomersList = CustomersList # list that stores customers of the company


class powerGenerator:
    # data denots whatever data we need to keep track of that relates to a power generator
    def __init__(self,data,id):
        self.__data = data
        self.id = id

class customer:
     # data denots whatever data we need to keep track of that relates to a customer
    def __init__(self,id,dataC,powerMeter,powerGeneratorUsed):
        self.__dataC = dataC
        self.powerMeter = powerMeter # we pass a Power Meter object 
        self.powerGenerator = powerGeneratorUsed # the power generator object used by the customer
        self.id = id

    def getConsumption():
        consumption = powerMeter.measureConsumption()
        return consumption

class powerMeter:
     # data denots whatever data we need to keep track of that relates to a power meter
    def __init__(self,id,data):
        self.__data = data
        self.id = id

    def measureConsumption():
        pass
        return consumption # calculated consumption




