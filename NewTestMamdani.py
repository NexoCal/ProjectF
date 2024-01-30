import skfuzzy as skf
import numpy as np
import matplotlib.pyplot as plt
from membershipGroup import membershipGroup
from mamdaniSolver import MamdaniInference

MamdaniSystem = MamdaniInference()

Umur = ['T1','T2','T3','T4','T5','T6']
Tinggi = ['SS','S','NH','H']
Berat = ['SU','U','I','PRO']
OutPut = ['SW','SW','W','W','SW','W','G','G','W','G','G','G','OB','OV','PRO','G']
counter = 0

for i in Umur:
    for j in Tinggi:
        for k in Berat:
            tmp = [i,j,k]
            MamdaniSystem.addRule(tmp,OutPut[counter])
            counter += 1
            if counter == 16:
                counter = 0

MamdaniSystem.showRules()

# Age Membership
domainU = np.arange(0.,24.1,0.1)
AgeMembership = membershipGroup()

AgeMembership.add_member('T1',domainU,[0.,0.,1.,3.])
AgeMembership.add_member('T2',domainU,[1.,3.,4.,6.])
AgeMembership.add_member('T3',domainU,[4.,6.,7.,9.])
AgeMembership.add_member('T4',domainU,[7.,9.,10.,12.])
AgeMembership.add_member('T5',domainU,[10.,12.,15.,18.])
AgeMembership.add_member('T6',domainU,[15.,18.,21.,24.])

# AgeMembership.show_plot(domainU)
# AgeMembership.show_capture_member()
# AgeMembership.show_fuzzy_point()

# Height Membership
domainT = np.arange(40.,70.,0.1)
HeightMembership = membershipGroup()

HeightMembership.add_member('SS',domainT,[0.,0.,44.,55.])
HeightMembership.add_member('S',domainT,[44.,55.,57.,59.])
HeightMembership.add_member('NH',domainT,[57.,59.,65.5,67.6])
HeightMembership.add_member('H',domainT,[65.5,67.6,100,100])

# HeightMembership.show_plot(domainT)
# HeightMembership.show_capture_member()
# HeightMembership.show_fuzzy_point()

# Weigth Membership
domainB = np.arange(1.,10.,0.1)
WeightMembership = membershipGroup()

WeightMembership.add_member('SU',domainB,[0.,0.,2.1,4.4])
WeightMembership.add_member('U',domainB,[2.1,4.4,5.,5.7])
WeightMembership.add_member('I',domainB,[5.,5.7,8.,9.])
WeightMembership.add_member('PO',domainB,[8.,9.,10,10])

# WeightMembership.show_plot(domainB)
# WeightMembership.show_capture_member()
# WeightMembership.show_fuzzy_point()

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

def fuzzyInterp(Age, Height, Weight):
    AgeMembership.captureInterp(Age, domainU)
    # AgeMembership.fuzzy_points.pop()
    AgeMembership.show_fuzzy_point()

    HeightMembership.captureInterp(Height, domainT)
    HeightMembership.show_fuzzy_point()
    
    WeightMembership.captureInterp(Weight, domainB)
    WeightMembership.show_fuzzy_point()
    

if __name__ == "__main__":
    fuzzyInterp(0, 50, 3.9)


    MamdaniSystem.evaluateRules(AgeMembership.getCapturedMember(), HeightMembership.getCapturedMember(), WeightMembership.getCapturedMember())
    print(MamdaniSystem.captured_output)

    ScoreList = MamdaniSystem.getFuzzyScore(AgeMembership.fuzzy_points, HeightMembership.fuzzy_points, WeightMembership.fuzzy_points, OutputMembership)
    print(ScoreList)

    MamdaniSystem.ProjectFuzzyScoreToOutput(ScoreList, OutputMembership)