#
#
#

from phidias.Types import *
from phidias.Main import *
from phidias.Lib import *


class Torre(Belief):
    pass

class last_tower(SingletonBelief):
    pass

class Cube(Belief):
    pass

class new_cube(Procedure):
    pass

class show_tower(Procedure):
    pass

class print_tower(Procedure):
    pass

class insert_cube(Procedure):
    pass


def_vars('X','Y','Z','T')


insert_cube(T,X) / (Torre(T,'bottom',Z)) >> [
    insert_cube(T,X,Z)
]
insert_cube(T,X) >> [
    +Torre(T,'bottom',X),
    +last_tower(T)
]

insert_cube(T,X,Z) / (Torre(T,Z,Y)) >> [
    insert_cube(T,X,Y)
]

insert_cube(T,X,Z) / (gt(X,Z)) >> [
    +Torre(T,Z,X)
]

insert_cube(T,X,Z) / (last_tower(Y) & leq(T,Y)) >> [
    "T=T+1",
    insert_cube(T,X)
]



new_cube(X) / (last_tower(Y) & gt(Y,0)) >> [insert_cube(1,X)]

new_cube(X) >> [
    +Torre(1,'bottom',X),
    +last_tower(1)
]

show_tower(X) / Torre(X,'bottom',Z) >> [
    show_line("Torre ",X, "  Elemento alla base : ",Z),
    print_tower(X,Z)
]

print_tower(X,Z) / Torre(X,Z,T) >> [
    show_line("Elemento Torre ",X," elemento sotto : ",Z," elemento sopra :",T),
    print_tower(X,T)
]

print_tower(X,Z) >> [
    show_line("Torre completamente stampata")
]



PHIDIAS.assert_belief(last_tower(0))

# instantiate the engine
PHIDIAS.run()
# run the engine shell
PHIDIAS.shell(globals())