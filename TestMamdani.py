import skfuzzy as skf
import numpy as np
import matplotlib.pyplot as plt
from membershipGroup import membershipGroup
from mamdaniSolverDeprecated import mamdaniSolver

Temp = membershipGroup()
Humid = membershipGroup()
ControlSystem = membershipGroup()

domainTemp = np.arange(0.,50.5,0.5)
domainHumid = np.arange(0.,100.5,0.5)
domainSystem = np.arange(0.,100.5,0.5)

Temp.add_member('Low',domainTemp,[0.,0.,18.,27.])
Temp.add_member('Medium',domainTemp,[18.,27.,34.,41.])
Temp.add_member('High',domainTemp,[34.,41.,50.5,50.5])

# Temp.show_plot(domainTemp)

Humid.add_member('Low',domainHumid,[0.,0.,20.,40.])
Humid.add_member('Medium',domainHumid,[20.,40.,60.,80.])
Humid.add_member('High',domainHumid,[60.,80.,100.5,100.5])

# Humid.show_plot(domainHumid)

ControlSystem.add_member('Decrease',domainSystem,[0.,0.,40.,60])
ControlSystem.add_member('Increase',domainSystem,[40.,60.,100.5,100.5])

# ControlSystem.show_plot(domainSystem)

# let say Temp = 25 and Humid = 34
TempScore = 22
HumidityScore = 30

Temp.interp(TempScore,domainTemp)
Temp.show_fuzzy_point()

Humid.interp(HumidityScore,domainHumid)
Humid.show_fuzzy_point()

lowScore = np.fmin(Temp.fuzzy_points[0].get('Low'),Humid.fuzzy_points[0].get('Low')) 
mediumScore = np.fmin(Temp.fuzzy_points[1].get('Medium'),Humid.fuzzy_points[1].get('Medium'))
highScore = np.fmin(Temp.fuzzy_points[2].get('High'),Humid.fuzzy_points[2].get('High'))

print(lowScore)
print(mediumScore)
print(highScore)

# print(ControlSystem.member[0])

activeLow = np.fmin(lowScore,ControlSystem.member[0].get('Decrease'))
activeHigh = np.fmin(mediumScore,ControlSystem.member[1].get('Increase'))

# print(activeLow)
# print(activeHigh)

# fig_scale_x = 1.5
# fig_scale_y = 1
# fig = plt.figure(figsize=(6.4 * fig_scale_x, 4.8 * fig_scale_y))
# row = 1
# col = 1

# plt.plot(row, col, 1)
# plt.title("Control Activation: Mamdani Inference Method")

# plt.plot(domainSystem, activeLow, label="Decrease", marker=".")
# plt.plot(domainSystem, activeHigh, label="Increase", marker=".")
# plt.legend(loc="upper left")

# plt.show()

# aggregatedControl = np.fmax(activeLow,activeHigh)

# plt.plot(row, col, 1)
# plt.title("Control Activation: Mamdani Inference Method")

# plt.plot(domainSystem, aggregatedControl, marker=".")

# plt.show()

# Control_centroid = skf.defuzz(domainSystem, aggregatedControl, 'centroid')
# print(Control_centroid)