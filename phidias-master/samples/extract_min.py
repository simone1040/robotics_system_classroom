from phidias.Types  import *
from phidias.Main import *
from phidias.Lib import *

import random

class block(Belief): pass

class compute_min(Procedure):pass

def_vars("X","temp_min")

compute_min() / block(X) >> [compute_min(X)]
compute_min() >> [show_line("Estrazioni completate")]
compute_min(temp_min) / (block(X) & lt(X,temp_min)) >> [compute_min(X)]
compute_min(temp_min) >> [show_line("Number Exctracted:",temp_min),-block(temp_min),compute_min()]







# populate the KB
for i in range(1,10):
    PHIDIAS.assert_belief(block(random.uniform(0,50)))

# instantiate the engine
PHIDIAS.run()
# run the engine shell
PHIDIAS.shell(globals())