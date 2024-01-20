import skfuzzy as skf
import numpy as np
import matplotlib.pyplot as plt
from membershipGroup import membershipGroup
from mamdaniSolver import mamdaniSolver

Temp = membershipGroup()
Humid = membershipGroup()
ControlSystem = membershipGroup()

domainTemp = np.arange(0.,50.5,0.5)
domainHumid = np.arange(0.,100.5,0.5)
domainSystem = np.arange(18.,33.5,0.5)

Temp.add_member('Low',domainTemp,[0.,0.,18.,27.])
Temp.add_member('Medium',domainTemp,[18.,27.,34.,41.])
Temp.add_member('High',domainTemp,[34.,41.,50.5,50.5])

# Temp.show_plot(domainTemp)

Humid.add_member('Low',domainHumid,[0.,0.,20.,40.])
Humid.add_member('Medium',domainHumid,[20.,40.,60.,80.])
Humid.add_member('High',domainHumid,[60.,80.,100.5,100.5])

# Humid.show_plot(domainHumid)

ControlSystem.add_member('Decrease',domainSystem,[18.,18.,24.,27])
ControlSystem.add_member('Increase',domainSystem,[25.,28.,33.5,33.5])

# ControlSystem.show_plot(domainSystem)

# let say Temp = 25 and Humid = 34
TempScore = 25
HumidityScore = 34

Temp.interp(TempScore,domainTemp)
Temp.show_fuzzy_point()

Humid.interp(HumidityScore,domainHumid)
Humid.show_fuzzy_point()

