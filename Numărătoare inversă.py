from enum import Enum
class Anotimp(Enum):
    PRIMAVARA=1
    VARA=2
    TOAMNA=3
    IARNA=4
C=Anotimp.PRIMAVARA
print(C.PRIMAVARA.name)
print(C.PRIMAVARA.value)