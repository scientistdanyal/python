class car():
    #result = 5
    def __init__(self,type,model,year):
        self.type = type
        self.model = model
        self.year = year
        self.engine = False

    def start_engine(self):
        if not self.engine:
            self.engine = True
            print("Engine started")
        else:
            print("Engine already started")


    def stop_engine(self):
        if self.engine:
            self.engine = False
            print("Engine stopped")
        else:
            print("Engine already stopped")               






#instance
toyota = car('toyota','vigo','2023')
toyota.month ='april'  

mercedes = car('Mercedes','two seater','2020')
# print(toyota.__dict__)
# #car.result = 45
# print(car.__dict__)





# print(toyota.__dict__)

toyota.start_engine()
toyota.start_engine()


toyota.stop_engine()
toyota.stop_engine()