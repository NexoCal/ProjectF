import skfuzzy as skf
import numpy as np
import matplotlib.pyplot as plt
from membershipGroup import membershipGroup

# Height Membership

#=====[T1 HeightMembership]=====#
domainHeightT1 = np.arange(40.,70.,0.1)
HeightMembershipT1 = membershipGroup()

HeightMembershipT1.add_member('SS',domainHeightT1,[0.,0.,44.,55.])
HeightMembershipT1.add_member('S',domainHeightT1,[44.,55.,57.,59.])
HeightMembershipT1.add_member('NH',domainHeightT1,[57.,59.,65.5,67.6])
HeightMembershipT1.add_member('H',domainHeightT1,[65.5,67.6,100,100])


#=====[T2 HeightMembership]=====#
domainHeightT2 = np.arange(54.6,75.,0.1)
HeightMembershipT2 = membershipGroup()

HeightMembershipT2.add_member('SS',domainHeightT2,[0.,0.,55.,57.6])
HeightMembershipT2.add_member('S',domainHeightT2,[55.,57.,57.6,59.])
HeightMembershipT2.add_member('NH',domainHeightT2,[57.6,59.,72.,74.])
HeightMembershipT2.add_member('H',domainHeightT2,[72.,74.,100,100])


#=====[T3 HeightMembership]=====#
domainHeightT3 = np.arange(0.0,79.7,0.1)
HeightMembershipT3 = membershipGroup()

HeightMembershipT3.add_member('SS',domainHeightT3,[0.,0.,62.7,65.2])
HeightMembershipT3.add_member('S',domainHeightT3,[62.7,65.2,67.5,70.])
HeightMembershipT3.add_member('NH',domainHeightT3,[67.5,70.,76.5,78.7])
HeightMembershipT3.add_member('H',domainHeightT3,[76.5,78.7,100,100])


#=====[T4 HeightMembership]=====#
domainHeightT4 = np.arange(2.0,84.,0.1)
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

#=====[T1 WeightMembership]=====#
domainWeightT1 = np.arange(1.,6.,0.1)
WeightMembershipT1 = membershipGroup()

WeightMembershipT1.add_member('SU',domainWeightT1,[0.,0.,1.9,2.2])
WeightMembershipT1.add_member('U',domainWeightT1,[1.9,2.2,2.5,2.8])
WeightMembershipT1.add_member('I',domainWeightT1,[2.5,2.8,3.9,4.7])
WeightMembershipT1.add_member('PO',domainWeightT1,[3.9,4.7,6,6])


#=====[T2 WeightMembership]=====#
domainWeightT2 = np.arange(4.,12.,0.1)
WeightMembershipT2 = membershipGroup()

WeightMembershipT2.add_member('SU',domainWeightT2,[0.,0.,4.9,5.7])
WeightMembershipT2.add_member('U',domainWeightT2,[4.9,5.7,6.4,7.1])
WeightMembershipT2.add_member('I',domainWeightT2,[6.4,7.1,9.8,10.9])
WeightMembershipT2.add_member('PO',domainWeightT2,[9.8,10.9,12,12])


#=====[T3 WeightMembership]=====#
domainWeightT3 = np.arange(5.,13.3,0.1)
WeightMembershipT3 = membershipGroup()

WeightMembershipT3.add_member('SU',domainWeightT3,[0.,0.,5.9,6.4])
WeightMembershipT3.add_member('U',domainWeightT3,[5.9,6.4,7.1,8.])
WeightMembershipT3.add_member('I',domainWeightT3,[7.1,8.,11.,12.3])
WeightMembershipT3.add_member('PO',domainWeightT3,[11.,12.3,13.3,13.3])


#=====[T4 WeightMembership]=====#
domainWeightT4 = np.arange(0.0,14.3,0.1)
WeightMembershipT4 = membershipGroup()

WeightMembershipT4.add_member('SU',domainWeightT4,[0.,0.,6.6,6.9])
WeightMembershipT4.add_member('U',domainWeightT4,[6.6,6.9,7.7,8.6])
WeightMembershipT4.add_member('I',domainWeightT4,[7.7,8.6,12.,13.3])
WeightMembershipT4.add_member('PO',domainWeightT4,[12.,13.3,14.3,14.3])


#=====[T5 WeightMembership]=====#
domainWeightT5 = np.arange(6.,16.3,0.1)
WeightMembershipT5 = membershipGroup()

WeightMembershipT5.add_member('SU',domainWeightT5,[0.,0.,7.1,7.8])
WeightMembershipT5.add_member('U',domainWeightT5,[7.1,7.8,8.8,9.8])
WeightMembershipT5.add_member('I',domainWeightT5,[8.8,9.8,13.7,15.3])
WeightMembershipT5.add_member('PO',domainWeightT5,[13.7,15.3,16.3,16.3])


#=====[T6 WeightMembership]=====#
domainWeightT6 = np.arange(7.,18.,0.1)
WeightMembershipT6 = membershipGroup()

WeightMembershipT6.add_member('SU',domainWeightT6,[0.,0.,8.,8.6])
WeightMembershipT6.add_member('U',domainWeightT6,[8.,8.6,9.7,10.8])
WeightMembershipT6.add_member('I',domainWeightT6,[9.7,10.8,15.3,17.1])
WeightMembershipT6.add_member('PO',domainWeightT6,[15.3,17.1,18,18])


# Output Membership

#=====[T1 OutputMembership]=====#
domainOT1 = np.arange(1,11.,0.1)
OutputMembershipT1 = membershipGroup()

OutputMembershipT1.add_member('SW',domainOT1,[1.,1.,1.9,2.2])
OutputMembershipT1.add_member('W',domainOT1,[1.9,2.2,3.3,4.3])
OutputMembershipT1.add_member('G',domainOT1,[3.3,4.3,5.3,6.4])
OutputMembershipT1.add_member('PRO',domainOT1,[5.3,6.4,7.5,8.7])
OutputMembershipT1.add_member('OV',domainOT1,[7.5,8.7,9.,10.2])
OutputMembershipT1.add_member('OB',domainOT1,[9.,10.2,11.,11.])


#=====[T2 OutputMembership]=====#
domainOT2 = np.arange(3,13.,0.1)
OutputMembershipT2 = membershipGroup()

OutputMembershipT2.add_member('SW',domainOT2,[3.,3.,4.1,5.1])
OutputMembershipT2.add_member('W',domainOT2,[4.1,5.1,5.8,7.])
OutputMembershipT2.add_member('G',domainOT2,[5.8,7.,7.4,7.9])
OutputMembershipT2.add_member('PRO',domainOT2,[7.4,7.9,9.2,10.5])
OutputMembershipT2.add_member('OV',domainOT2,[9.2,10.5,11.,12.1])
OutputMembershipT2.add_member('OB',domainOT2,[11.,12.1,13.,13.])


#=====[T3 OutputMembership]=====#
domainOT3 = np.arange(4.2,14.2,0.1)
OutputMembershipT3 = membershipGroup()

OutputMembershipT3.add_member('SW',domainOT3,[4.2,4.2,5.2,6.1])
OutputMembershipT3.add_member('W',domainOT3,[5.2,6.1,6.7,7.9])
OutputMembershipT3.add_member('G',domainOT3,[6.7,7.9,8.2,8.6])
OutputMembershipT3.add_member('PRO',domainOT3,[8.2,8.6,10.1,11.6])
OutputMembershipT3.add_member('OV',domainOT3,[10.1,11.6,12.,13.2])
OutputMembershipT3.add_member('OB',domainOT3,[12.,13.2,14.2,14.2])


#=====[T4 OutputMembership]=====#
domainOT4 = np.arange(5,15.2,0.1)
OutputMembershipT4 = membershipGroup()

OutputMembershipT4.add_member('SW',domainOT4,[5.,5.,5.9,6.9])
OutputMembershipT4.add_member('W',domainOT4,[5.9,6.9,7.4,8.4])
OutputMembershipT4.add_member('G',domainOT4,[7.4,8.4,9.1,9.6])
OutputMembershipT4.add_member('PRO',domainOT4,[9.1,9.6,11.1,12.5])
OutputMembershipT4.add_member('OV',domainOT4,[11.1,12.5,13.,14.2])
OutputMembershipT4.add_member('OB',domainOT4,[13.,14.2,15.2,15.2])


#=====[T5 OutputMembership]=====#
domainOT5 = np.arange(5.6,17.4,0.1)
OutputMembershipT5 = membershipGroup()

OutputMembershipT5.add_member('SW',domainOT5,[5.6,5.6,6.6,7.6])
OutputMembershipT5.add_member('W',domainOT5,[6.6,7.6,8.3,9.5])
OutputMembershipT5.add_member('G',domainOT5,[8.3,9.5,9.8,10.8])
OutputMembershipT5.add_member('PRO',domainOT5,[9.8,10.8,12.5,14.3])
OutputMembershipT5.add_member('OV',domainOT5,[12.5,14.3,15.,16.4])
OutputMembershipT5.add_member('OB',domainOT5,[15.,16.4,17.4,17.4])


#=====[T6 OutputMembership]=====#
domainOT6 = np.arange(6.5,19.5,0.1)
OutputMembershipT6 = membershipGroup()

OutputMembershipT6.add_member('SW',domainOT6,[6.5,6.5,7.5,8.5])
OutputMembershipT6.add_member('W',domainOT6,[7.5,8.5,9.1,10.4])
OutputMembershipT6.add_member('G',domainOT6,[9.1,10.4,11.,12.1])
OutputMembershipT6.add_member('PRO',domainOT6,[11.,12.1,13.9,16.])
OutputMembershipT6.add_member('OV',domainOT6,[13.9,16.,17.,18.5])
OutputMembershipT6.add_member('OB',domainOT6,[17.,18.5,19.5,19.5])