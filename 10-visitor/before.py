class Segment():
    def reduce_noise(self):
        print('Reducing noise')

    def add_reverb(self):
        print('Adding reverb')
    
    def normalize(self):
        print('Normalizing')

class FormatSegment(Segment):
    def __init__(self) -> None:
        super().__init__()

class FactSegment(Segment):
    def __init__(self) -> None:
        super().__init__()

class WavFile:
    def __init__(self) -> None:
        self.segments = []
    
    def read(self,filename:str):
        self.segments.append(FormatSegment())
        self.segments.append(FactSegment())
        self.segments.append(FactSegment())
        self.segments.append(FactSegment())

    def reduce_noise(self):
        for segment in self.segments:
            segment.reduce_noise()
    
    def add_reverb(self):
        for segment in self.segments:
            segment.add_reverb()

    def normalize(self):
        for segment in self.segments:
            segment.normalize()

file = WavFile()
file.read('test')
file.add_reverb()