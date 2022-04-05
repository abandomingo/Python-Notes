class Car:
    
     
    
    def __init__(self, make ,model, year):
        #Constructor
        self.make = make
        self.model = model
        self.year = year
        
    def GetDescription(self):
        #Gets the description of the car
        print(f"{self.year} {self.make} {self.model}")
    
    def SetOdometer(self, odo):
        if odo < 0:
            print("shame on you")
            return
        
        self.odometer = odo
    def GetOdometer(self):
        print(f"This car has {self.odometer} miles")
        
    def FillTank(self,gallons):
        self.tank += gallons
    

#calling the init function
myCar = Car("Toyota", "Tacoma", 2016)
myCar.GetDescription()

yourCar = Car("Audi", "A5", "2016")
yourCar.GetDescription()

myCar.SetOdometer(3600)
yourCar.odometer = 2300

myCar.GetOdometer()
yourCar.GetOdometer()



class Battery():
    batterySize = 75
    batteryBrand = "Duracell"
    batteryDimensionH = 8
    batteryDimensionW = 10
    batteryDimensionD = 4
    
    def __init__(self):
        self.batterySize = 75


class ElectricCar(Car):
    #respresents electric cars
    def __init__(self, make, model, year):
        #Constructor
        super().__init__(make, model, year)    
        
    
    def DescribeBattery(self):
        print(f"This car has a {Battery.batterySize} kwhs")
        
    def FillTank(self, gallons):
        print("You can't fill tank")
        super().FillTank(gallons)
        
myEv = ElectricCar("Tesla", 'Model S', 2019)
myEv.GetDescription()
myEv.DescribeBattery()
