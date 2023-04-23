from abc import abstractmethod
from functools import singledispatch

class Operation():
    @abstractmethod
    def apply(self, segment):
        pass

class Segment():
    def __str__(self) -> str:
        return "Father Segment!"
    
class FormatSegment(Segment):
    def execute(self, operation: Operation):
        operation.apply(self)
    
    def __str__(self) -> str:
        return "FormatSegment object!"

class FactSegment(Segment):
    def execute(self, operation: Operation):
        operation.apply(self)
    
    def __str__(self) -> str:
        return "FactSegment object!"

class ReduceNoise(Operation):
    # this is because we do not have methodoverloading in python
    def __init__(self):
        self.apply = singledispatch(self.apply)
        self.apply.register(FormatSegment, self.apply_formatSegment)
        self.apply.register(FactSegment, self.apply_factSegment)

    def apply(self, segment):
        raise TypeError("This type isn't supported: {}".format(type(segment)))

    def apply_formatSegment(self, segment: FormatSegment):
        print('reducing noise on format segment')
    
    def apply_factSegment(self, segment: FactSegment):
        print('reducing noise on fact segment')

class Normalize(Operation):
    # this is because we do not have methodoverloading in python
    def __init__(self):
        self.apply = singledispatch(self.apply)
        self.apply.register(FormatSegment, self.apply_formatSegment)
        self.apply.register(FactSegment, self.apply_factSegment)

    def apply(self, segment):
        raise TypeError("This type isn't supported: {}".format(type(segment)))

    def apply_formatSegment(self, segment: FormatSegment):
        print('normalize on format segment')
    
    def apply_factSegment(self, segment: FactSegment):
        print('normalize on fact segment')
        

class WavFile:
    def __init__(self) -> None:
        self.segments = []
    
    def read(self,filename:str):
        self.segments.append(FormatSegment())
        self.segments.append(FactSegment())
        self.segments.append(FactSegment())
        self.segments.append(FactSegment())

    def execute(self, operation:Operation):
        for segment in self.segments:
            operation.apply(segment)
        
file = WavFile()
file.read('myfile.wav')
file.execute(ReduceNoise())
file.execute(Normalize())
