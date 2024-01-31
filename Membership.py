import skfuzzy as skf
import numpy as np
import matplotlib.pyplot as plt
from membershipGroup import membershipGroup

# Age Membership
domainAge = np.arange(0.,24.1,0.1)
AgeMembership = membershipGroup()

AgeMembership.add_member('T1',domainAge,[0.,0.,1.,3.])
AgeMembership.add_member('T2',domainAge,[1.,3.,4.,6.])
AgeMembership.add_member('T3',domainAge,[4.,6.,7.,9.])
AgeMembership.add_member('T4',domainAge,[7.,9.,10.,12.])
AgeMembership.add_member('T5',domainAge,[10.,12.,15.,18.])
AgeMembership.add_member('T6',domainAge,[15.,18.,21.,24.])

# AgeMembership.show_plot(domainAge)
# AgeMembership.show_capture_member()
# AgeMembership.show_fuzzy_point()

# Height Membership

#=====[T1 HeightMembership]=====#
domainHeightT1 = np.arange(40.,70.,0.1)
HeightMembershipT1 = membershipGroup()

HeightMembershipT1.add_member('SS',domainHeightT1,[0.,0.,44.,55.])
HeightMembershipT1.add_member('S',domainHeightT1,[44.,55.,57.,59.])
HeightMembershipT1.add_member('NH',domainHeightT1,[57.,59.,65.5,67.6])
HeightMembershipT1.add_member('H',domainHeightT1,[65.5,67.6,100,100])


#=====[T2 HeightMembership]=====#
domainHeightT2 = np.arange(56.6,75.,0.1)
HeightMembershipT2 = membershipGroup()

HeightMembershipT2.add_member('SS',domainHeightT2,[0.,0.,57.6,55.])
HeightMembershipT2.add_member('S',domainHeightT2,[57.6,55.,57.,59.])
HeightMembershipT2.add_member('NH',domainHeightT2,[57.,59.,72.,74.])
HeightMembershipT2.add_member('H',domainHeightT2,[72.,74.,100,100])


#=====[T3 HeightMembership]=====#
domainHeightT3 = np.arange(61.7,79.7,0.1)
HeightMembershipT3 = membershipGroup()

HeightMembershipT3.add_member('SS',domainHeightT3,[0.,0.,62.7,65.2])
HeightMembershipT3.add_member('S',domainHeightT3,[62.7,65.2,67.5,70.])
HeightMembershipT3.add_member('NH',domainHeightT3,[67.5,70.,76.5,78.7])
HeightMembershipT3.add_member('H',domainHeightT3,[76.5,78.7,100,100])


#=====[T4 HeightMembership]=====#
domainHeightT4 = np.arange(65.4,84.,0.1)
HeightMembershipT4 = membershipGroup()

HeightMembershipT4.add_member('SS',domainHeightT4,[0.,0.,66.4,68.6])
HeightMembershipT4.add_member('S',domainHeightT4,[66.4,68.6,71.,73.])
HeightMembershipT4.add_member('NH',domainHeightT4,[71.,73.,80.5,82.9])
HeightMembershipT4.add_member('H',domainHeightT4,[80.5,82.9,100,100])


#=====[T5 HeightMembership]=====#
domainHeightT5 = np.arange(68.6,91.4,0.1)
HeightMembershipT5 = membershipGroup()

HeightMembershipT5.add_member('SS',domainHeightT5,[0.,0.,69.6,74.2])
HeightMembershipT5.add_member('S',domainHeightT5,[69.6,74.2,76.9,79.6])
HeightMembershipT5.add_member('NH',domainHeightT5,[76.9,79.6,87.7,90.4])
HeightMembershipT5.add_member('H',domainHeightT5,[87.7,90.4,100,100])


#=====[T6 HeightMembership]=====#
domainHeightT6 = np.arange(64.,98.,0.1)
HeightMembershipT6 = membershipGroup()

HeightMembershipT6.add_member('SS',domainHeightT6,[0.,0.,75.,78.7])
HeightMembershipT6.add_member('S',domainHeightT6,[75.,78.7,81.7,84.4])
HeightMembershipT6.add_member('NH',domainHeightT6,[81.7,84.4,93.9,97.])
HeightMembershipT6.add_member('H',domainHeightT6,[93.9,97.,100,100])



# Weigth Membership
domainWeightT1 = np.arange(1.,10.,0.1)
WeightMembershipT1 = membershipGroup()

WeightMembershipT1.add_member('SU',domainWeightT1,[0.,0.,2.1,4.4])
WeightMembershipT1.add_member('U',domainWeightT1,[2.1,4.4,5.,5.7])
WeightMembershipT1.add_member('I',domainWeightT1,[5.,5.7,8.,9.])
WeightMembershipT1.add_member('PO',domainWeightT1,[8.,9.,10,10])

domainWeightT2 = np.arange(6.,12.,0.1)
WeightMembershipT2 = membershipGroup()

WeightMembershipT2.add_member('SU',domainWeightT2,[0.,0.,4.9,5.7])
WeightMembershipT2.add_member('U',domainWeightT2,[4.9,5.7,6.4,7.1])
WeightMembershipT2.add_member('I',domainWeightT2,[6.4,7.1,9.8,10.9])
WeightMembershipT2.add_member('PO',domainWeightT2,[9.8,10.9,12,12])

domainWeightT3 = np.arange(7.,13.3,0.1)
WeightMembershipT3 = membershipGroup()

WeightMembershipT3.add_member('SU',domainWeightT3,[0.,0.,5.9,6.4])
WeightMembershipT3.add_member('U',domainWeightT3,[5.9,6.4,7.1,8.])
WeightMembershipT3.add_member('I',domainWeightT3,[7.1,8.,11.,12.3])
WeightMembershipT3.add_member('PO',domainWeightT3,[11.,12.3,10,10])

domainWeightT4 = np.arange(7.6,14.3,0.1)
WeightMembershipT4 = membershipGroup()

WeightMembershipT4.add_member('SU',domainWeightT4,[0.,0.,6.6,6.9])
WeightMembershipT4.add_member('U',domainWeightT4,[6.6,6.9,7.7,8.6])
WeightMembershipT4.add_member('I',domainWeightT4,[7.7,8.6,12.,13.3])
WeightMembershipT4.add_member('PO',domainWeightT4,[12.,13.3,14.3,14.3])

domainWeightT5 = np.arange(8.,16.3,0.1)
WeightMembershipT5 = membershipGroup()

WeightMembershipT5.add_member('SU',domainWeightT5,[0.,0.,7.1,7.8])
WeightMembershipT5.add_member('U',domainWeightT5,[7.1,7.8,8.8,9.8])
WeightMembershipT5.add_member('I',domainWeightT5,[8.8,9.8,13.7,15.3])
WeightMembershipT5.add_member('PO',domainWeightT5,[13.7,15.3,16.3,16.3])

domainWeightT6 = np.arange(9.,18.,0.1)
WeightMembershipT6 = membershipGroup()

WeightMembershipT6.add_member('SU',domainWeightT6,[0.,0.,8.,8.6])
WeightMembershipT6.add_member('U',domainWeightT6,[8.,8.6,9.7,10.8])
WeightMembershipT6.add_member('I',domainWeightT6,[9.7,10.8,15.3,17.1])
WeightMembershipT6.add_member('PO',domainWeightT6,[15.3,17.1,18,18])


# Output Membership
domainO = np.arange(1,11.,0.1)
OutputMembership = membershipGroup()

OutputMembership.add_member('SW',domainO,[1.,1.,1.9,2.2])
OutputMembership.add_member('W',domainO,[1.9,2.2,3.3,4.3])
OutputMembership.add_member('G',domainO,[3.3,4.3,5.3,6.4])
OutputMembership.add_member('PRO',domainO,[5.3,6.4,7.5,8.7])
OutputMembership.add_member('OV',domainO,[7.5,8.7,9.,10.2])
OutputMembership.add_member('OB',domainO,[9.,10.2,11.,11.])

# OutputMembership.show_plot(domainO)
# OutputMembership.show_capture_member()
# OutputMembership.show_fuzzy_point()