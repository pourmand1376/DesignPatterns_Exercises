from enum import Enum
class TravelMode(Enum):
    DRIVING=0,
    BICYCLING=1,
    TRANSIT=2,
    WALKING=3

class DirectionService():
    def __init__(self,travelMode:TravelMode):
        self.travelMode = travelMode

    def getEta(self):
        if self.travelMode == TravelMode.DRIVING:
            print("Calculating ETA (driving)")
            return 1
        elif self.travelMode == TravelMode.BICYCLING:
            print("Calculating ETA (bicycling)")
            return 2
        elif self.travelMode == TravelMode.TRANSIT:
            print("Calculating ETA (transit)")
            return 3
        else:
            print("Calculating ETA (walking)")
            return 4

    def get_direction(self):
        if self.travelMode == TravelMode.DRIVING:
            print("Calculating Direction (driving)")
            return 1;
        elif self.travelMode == TravelMode.BICYCLING:
            print("Calculating Direction (bicycling)")
            return 2
        elif self.travelMode == TravelMode.TRANSIT:
            print("Calculating Direction (transit)")
            return 3
        else:
            print("Calculating Direction (walking)")
            return 4

def main():
    service = DirectionService(TravelMode.DRIVING)
    service.getEta()
    service.get_direction()

    service.travelMode = TravelMode.TRANSIT
    service.getEta()

if __name__ == "__main__":
    main()
