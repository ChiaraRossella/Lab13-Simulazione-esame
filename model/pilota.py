from dataclasses import dataclass

@dataclass
class Pilota:
    driverId:int
    surname: str

    def __hash__(self):
        return hash(self.driverId)

    def __eq__(self, other):
        return self.driverId== other.driverId

    def __str__(self):
        return self.surname