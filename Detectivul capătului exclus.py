from enum import Enum
class Z(Enum):
    LUNI = 1
    MARTI = 2
    MIERCURI = 3
    JOI = 4
    VINERI = 5
    SAMBATA = 6
    DUMINICA = 7

C=Z.DUMINICA
print(list(range(1, 8)))
print(bool(Z.DUMINICA.value == 7))