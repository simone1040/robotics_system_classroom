#
#
#

from phidias.Types import *
from phidias.Main import *
from phidias.Lib import *

class ora(Procedure): pass
class mezzora(Procedure): pass
class reset(Procedure): pass
class InsertCoin(Procedure):pass
class verifyPayament(Procedure):pass

class Money(SingletonBelief): pass

class DueEuro(SingletonBelief):pass
class UnEuro(SingletonBelief):pass
class cinquantaCent(SingletonBelief):pass
class ventiCent(SingletonBelief):pass
class dieciCent(SingletonBelief):pass

class RestituisciMonete(Procedure):pass

class time_lock(SingletonBelief):pass


def_vars("N","X","Z")

ora() / (Money(X) & time_lock(N) & eq(N,1)) >> [show_line("Non è possibile inserire ulteriore tempo una volta iniziato il pagamento")]
ora() / Money(X) >> ["X = X + 100",+Money(X),show_line("Inserire ",X ," Cent")]


mezzora() / (Money(X) & time_lock(N) & eq(N,1)) >> [show_line("Non è possibile inserire ulteriore tempo una volta iniziato il pagamento")]
mezzora() / Money(X) >> ["X = X + 50",+Money(X),show_line("Inserire ",X ," Cent")]


reset() / (Money(X) & time_lock(N) & eq(N,1)) >> [show_line("Inizio Procedura restituzione monete"),RestituisciMonete()]
reset() / Money(X) >> ["X = 0",+Money(X),show_line("Valore resettato")]


#Restituzione Monete

RestituisciMonete() / (DueEuro(X) & gt(X,0) ) >> ["X = X -1",+DueEuro(X),show_line("moneta da 200 cent emessa"),
                                                             RestituisciMonete()]


RestituisciMonete() / (UnEuro(X) & gt(X,0) ) >> ["X = X -1",+UnEuro(X),show_line("moneta da 100 cent emessa"),
                                                            RestituisciMonete()]


RestituisciMonete() / (cinquantaCent(X) & gt(X,0) ) >> ["X = X -1",+cinquantaCent(X),show_line("moneta da 50 cent emessa"),
                                                             RestituisciMonete()]

RestituisciMonete() / (ventiCent(X) & gt(X,0) ) >> ["X = X -1",+ventiCent(X),show_line("moneta da 20 cent emessa"),
                                                             RestituisciMonete()]

RestituisciMonete() / (dieciCent(X) & gt(X,0) ) >> ["X = X -1",+dieciCent(X),show_line("moneta da 20 cent emessa"),
                                                             RestituisciMonete()]

RestituisciMonete() >> [show_line("Credito restituito"),+Money(0),+time_lock(0)]



verifyPayament() / (Money(N) &  eq(N,0)) >> [show_line("Pagamento effettuato correttamente"),+DueEuro(0),+UnEuro(0),+cinquantaCent(0),+ventiCent(0),+dieciCent(0),+time_lock(0)]
verifyPayament() / (Money(N) &  lt(N,0)) >> [show_line("Pagamento effettuato correttamente, La macchina non eroga resto"),+Money(0),+DueEuro(0),+UnEuro(0),+cinquantaCent(0),+ventiCent(0),+dieciCent(0),+time_lock(0)]
verifyPayament() / (Money(N) &  gt(N,0)) >> [show_line("Moneta inserita correttamente, Inserire :",N)]



#Inserimento Monete
InsertCoin(N)  / (Money(X) & eq(X,0) ) >> [show_line("Nessuna tariffa selezionata,moneta restituita")]
InsertCoin(N) / (Money(X) & eq(N,200) & DueEuro(Z) ) >> [+time_lock(1),"X = X - 200",+Money(X),"Z = Z + 1",+DueEuro(Z),verifyPayament()]
InsertCoin(N)  / (Money(X) & eq(N,100) & UnEuro(Z) ) >> [+time_lock(1),"X = X - 100",+Money(X),"Z = Z + 1",+UnEuro(Z),verifyPayament()]
InsertCoin(N) / (Money(X) & eq(N,50) & cinquantaCent(Z) ) >> [+time_lock(1),"X = X - 50",+Money(X),"Z = Z + 1",+cinquantaCent(Z),verifyPayament()]
InsertCoin(N) / (Money(X) & eq(N,20) & ventiCent(Z) ) >> [+time_lock(1),"X = X - 20",+Money(X),"Z = Z + 1",+ventiCent(Z),verifyPayament()]
InsertCoin(N)  / (Money(X) & eq(N,10) & dieciCent(Z) ) >> [+time_lock(1),"X = X - 10",+Money(X),"Z = Z + 1",+dieciCent(Z),verifyPayament()]
InsertCoin(N) >> [show_line("Taglio non esistente")]



PHIDIAS.assert_belief(Money(0))
PHIDIAS.assert_belief(DueEuro(0))
PHIDIAS.assert_belief(UnEuro(0))
PHIDIAS.assert_belief(cinquantaCent(0))
PHIDIAS.assert_belief(ventiCent(0))
PHIDIAS.assert_belief(dieciCent(0))
PHIDIAS.assert_belief(time_lock(0))

# instantiate the engine
PHIDIAS.run()
# run the engine shell
PHIDIAS.shell(globals())





