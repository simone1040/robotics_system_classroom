from phidias.Types import *
from phidias.Main import *
from phidias.Lib import *

class free(Belief): pass

class Alloca(Procedure): pass

class InitialPositionLeft(SingletonBelief): pass
class InitialPositionRight(SingletonBelief): pass

class SeatRimanenti(SingletonBelief):pass

class ProcedureAlloc(Procedure):pass


class lastInsert(SingletonBelief):pass #0 sinistra a ,  1 sinistra b ,2 destra a ,3 destra b


def_vars('X','Y','Z','N')
Alloca(N) /(SeatRimanenti(X) & eq(X,0)) >> [show_line("Tutti i posti sono stati occupati")]
Alloca(N) / (SeatRimanenti(X) & geq(X,N) & gt(N,0)) >> [ProcedureAlloc(N)]
Alloca(N) / (eq(N,0)) >> [show_line("Posti Allocati")]
Alloca(N) >> [show_line("Non mi è possibile allocare ",N," posti")]


ProcedureAlloc(N) / (InitialPositionLeft(X) & SeatRimanenti(Z) & lastInsert(Y) & eq(Y,3) & free(X,'a')) >> [
    -free(X,'a'),show_line("Inserito posto:(",X,"a)"),"Y = 0",+lastInsert(Y),"Z = Z-1",+SeatRimanenti(Z),"N = N -1",Alloca(N)]

ProcedureAlloc(N) / (InitialPositionLeft(X) & SeatRimanenti(Z) & lastInsert(Y) & eq(Y,0) & free(X,'b')) >> [
    -free(X,'b'),show_line("Inserito posto:(",X,"b)"),"X = X - 1",+InitialPositionLeft(X),"Y = Y + 1",+lastInsert(Y),"Z = Z-1",+SeatRimanenti(Z),"N = N -1",Alloca(N)]


ProcedureAlloc(N) / (InitialPositionRight(X) & SeatRimanenti(Z) & lastInsert(Y) & eq(Y,1) & free(X,'a')) >> [
    -free(X,'a'),show_line("Inserito posto:(",X,"a)"),"Y = Y + 1",+lastInsert(Y),"Z = Z-1",+SeatRimanenti(Z),"N = N -1",Alloca(N)]

ProcedureAlloc(N) / (InitialPositionRight(X) & SeatRimanenti(Z) & lastInsert(Y) & eq(Y,2) & free(X,'b')) >> [
    -free(X,'b'),show_line("Inserito posto:(",X,"b)"),"X = X + 1",+InitialPositionRight(X),"Y = Y + 1",+lastInsert(Y),"Z = Z-1",+SeatRimanenti(Z),"N = N -1",Alloca(N)]





c = 0
for i in ['a','b']:
    for y in range(2,35):
        PHIDIAS.assert_belief(free(y,i))
        c+=1
PHIDIAS.assert_belief(SeatRimanenti(c))

PHIDIAS.assert_belief(InitialPositionLeft(18))
PHIDIAS.assert_belief(InitialPositionRight(19))
PHIDIAS.assert_belief(lastInsert(3))




# instantiate the engine
PHIDIAS.run()
# run the engine shell
PHIDIAS.shell(globals())
