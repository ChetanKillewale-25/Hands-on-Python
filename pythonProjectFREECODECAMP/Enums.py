# BASICALLY ENUMS ARE THE ONLY WAY TO CREATE CONSTANTS IN PYTHON

from enum import Enum
#   ENUMS ARE THE READABLE NAME THAT ARE BOUND TO CONSTANT VALUES
class State(Enum):

    INACTIVE=0
    ACTIVE=1

print(State.ACTIVE)
print(State.ACTIVE.value)
print(State(1))
print(State['ACTIVE'])
print(State['ACTIVE'].value)
print(list(State))
print(len(State))

"""
THESE ARE ALL THE METHODS FOR ACCESSING ENUMS
"""