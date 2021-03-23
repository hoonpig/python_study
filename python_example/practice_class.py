class Unit:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyhableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()

dropship = FlyhableUnit()