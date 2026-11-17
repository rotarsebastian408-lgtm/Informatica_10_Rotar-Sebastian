from enum import Enum
class Club(Enum):
    ROBOTICA = 1 
    ARTA = 2
    SPORT = 3
cod=int(input("Introduceti codul clubului (1-ROBOTICA, 2-ARTA, 3-SPORT): "))
Club = Club(cod)
print(Club)
print(cod==Club.ROBOTICA.value)
