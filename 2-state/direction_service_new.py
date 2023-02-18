from abc import ABC, abstractmethod

class TravelService(ABC):
    @abstractmethod
    def get_eta(self):
        pass
    
    @abstractmethod
    def get_direction(self):
        pass

class Driving(TravelService):
    def get_eta(self):
        print("Calculating ETA (driving)")
        return 1

    def get_direction(self):
        print("Calculating Direction (driving)")
        return 1

class Bicycling(TravelService):
    def get_eta(self):
        print("Calculating ETA (bicycling)")
        return 2

    def get_direction(self):
        print("Calculating Direction (bicycling)")
        return 2

class Transit(TravelService):
    def get_eta(self):
        print("Calculating ETA (transit)")
        return 3

    def get_direction(self):
        print("Calculating Direction (transit)")
        return 3

class Walking(TravelService):
    def get_eta(self):
        print("Calculating ETA (walking)")
        return 4
    
    def get_direction(self):
        print("Calculating Direction (walking)")
        return 4

class DirectionService():
    def __init__(self,travelService:TravelService) -> None:
        self.travelService = travelService

    def get_eta(self):
        return self.travelService.get_eta()

    def get_direction(self):
        return self.travelService.get_direction()

def main():
    service = DirectionService(Walking())
    service.get_direction()
    service.get_eta()

    service.travelService = Bicycling()
    service.get_direction()
    service.get_eta()

    service.travelService = Driving()
    service.get_direction()

if __name__ == "__main__":
    main()