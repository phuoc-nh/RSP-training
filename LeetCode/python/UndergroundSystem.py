class UndergroundSystem:

    def __init__(self):
        # 10 ^ 5 call getAverageTime so, getAverageTime should be constant run time
        # a map to store start station and end station
        self.stations = {} # (start, end): total time, trip count
        self.userCheckin = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.userCheckin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.userCheckin[id]
        if (startStation, stationName) not in self.stations:
            self.stations[(startStation, stationName)] = (t - startTime, 1)
        else:
            total, count = self.stations[(startStation, stationName)]
            self.stations[(startStation, stationName)] = (total + t - startTime, count + 1)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.stations[(startStation, endStation)]
        return total / count



undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(45, "Leyton", 3) #
undergroundSystem.checkIn(32, "Paradise", 8) #
undergroundSystem.checkIn(27, "Leyton", 10) #
undergroundSystem.checkOut(45, "Waterloo", 15) #  // Customer 45 "Leyton" -> "Waterloo" in 15-3 = 12
undergroundSystem.checkOut(27, "Waterloo", 20) #  // Customer 27 "Leyton" -> "Waterloo" in 20-10 = 10
undergroundSystem.checkOut(32, "Cambridge", 22) # // Customer 32 "Paradise" -> "Cambridge" in 22-8 = 14
undergroundSystem.getAverageTime("Paradise", "Cambridge") # // return 14.00000. One trip "Paradise" -> "Cambridge", (14) / 1 = 14
undergroundSystem.getAverageTime("Leyton", "Waterloo") #    // return 11.00000. Two trips "Leyton" -> "Waterloo", (10 + 12) / 2 = 11
undergroundSystem.checkIn(10, "Leyton", 24) #
undergroundSystem.getAverageTime("Leyton", "Waterloo") #    // return 11.00000
undergroundSystem.checkOut(10, "Waterloo", 38) #  // Customer 10 "Leyton" -> "Waterloo" in 38-24 = 14
undergroundSystem.getAverageTime("Leyton", "Waterloo") #    // return 12.00000. Three trips "Leyton" -> "Waterloo", (10 + 12 + 14) / 3 = 12