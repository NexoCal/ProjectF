import skfuzzy as skf
import numpy as np
import matplotlib.pyplot as plt
from membershipGroup import membershipGroup
from mamdaniSolver import MamdaniInference
import MembershipBoy
import pandas as pd

# Age Membership
domainAge = np.arange(0.,25.1,0.1)
AgeMembership = membershipGroup()

AgeMembership.add_member('T1',domainAge,[0.,0.,1.,3.])
AgeMembership.add_member('T2',domainAge,[1.,3.,4.,6.])
AgeMembership.add_member('T3',domainAge,[4.,6.,7.,9.])
AgeMembership.add_member('T4',domainAge,[7.,9.,10.,12.])
AgeMembership.add_member('T5',domainAge,[10.,12.,15.,18.])
AgeMembership.add_member('T6',domainAge,[15.,18.,21.,24.1])

MamdaniSystem = MamdaniInference()

Umur = ['T1','T2','T3','T4','T5','T6']
Berat = ['SU','U','I','PO']
Tinggi = ['SS','S','NH','H']
OutPut = ['SW','SW','W','W','SW','W','G','G','W','G','G','G','OB','OV','PRO','PRO']
counter = 0

for i in Umur:
    for j in Berat:
        for k in Tinggi:
            tmp = [i,j,k]
            MamdaniSystem.addRule(tmp,OutPut[counter])
            counter += 1
            if counter == 16:
                counter = 0



def AgeCheck(Age: float):
    AgeMembership.captureInterp(Age, domainAge)
    AgeMembership.show_fuzzy_point()
    AgeMembership.show_plot(domainAge)

    return AgeMembership.getCapturedMember()


def fuzzyInterp(Height, Weight):
    
    WeightMembership.captureInterp(Weight, DomainWeight)
    WeightMembership.show_fuzzy_point()
    
    HeightMembership.captureInterp(Height, DomainHeight)
    HeightMembership.show_fuzzy_point()


AgeInput, WeightInput, HeightInput = map(float,input("Umur, Berat dan Tinggi: ").split(" "))

AgeOutput = AgeCheck(AgeInput)
for i in range(len(AgeOutput)):
    
    if AgeOutput[i] == 'T1':
        HeightMembership = MembershipBoy.HeightMembershipT1
        WeightMembership = MembershipBoy.WeightMembershipT1
        OutputMembership = MembershipBoy.OutputMembershipT1

        DomainHeight = MembershipBoy.domainHeightT1
        DomainWeight = MembershipBoy.domainWeightT1
        DomainOutput = MembershipBoy.domainOT1

    elif AgeOutput[i] == 'T2':
        HeightMembership = MembershipBoy.HeightMembershipT2
        WeightMembership = MembershipBoy.WeightMembershipT2
        OutputMembership = MembershipBoy.OutputMembershipT2

        DomainHeight = MembershipBoy.domainHeightT2
        DomainWeight = MembershipBoy.domainWeightT2
        DomainOutput = MembershipBoy.domainOT2

    elif AgeOutput[i] == 'T3':
        HeightMembership = MembershipBoy.HeightMembershipT3
        WeightMembership = MembershipBoy.WeightMembershipT3
        OutputMembership = MembershipBoy.OutputMembershipT3

        DomainHeight = MembershipBoy.domainHeightT3
        DomainWeight = MembershipBoy.domainWeightT3
        DomainOutput = MembershipBoy.domainOT3

    elif AgeOutput[i] == 'T4':
        HeightMembership = MembershipBoy.HeightMembershipT4
        WeightMembership = MembershipBoy.WeightMembershipT4
        OutputMembership = MembershipBoy.OutputMembershipT4

        DomainHeight = MembershipBoy.domainHeightT4
        DomainWeight = MembershipBoy.domainWeightT4
        DomainOutput = MembershipBoy.domainOT4

    elif AgeOutput[i] == 'T5':
        HeightMembership = MembershipBoy.HeightMembershipT5
        WeightMembership = MembershipBoy.WeightMembershipT5
        OutputMembership = MembershipBoy.OutputMembershipT5

        DomainHeight = MembershipBoy.domainHeightT5
        DomainWeight = MembershipBoy.domainWeightT5
        DomainOutput = MembershipBoy.domainOT5

    elif AgeOutput[i] == 'T6':
        HeightMembership = MembershipBoy.HeightMembershipT6
        WeightMembership = MembershipBoy.WeightMembershipT6
        OutputMembership = MembershipBoy.OutputMembershipT6

        DomainHeight = MembershipBoy.domainHeightT6
        DomainWeight = MembershipBoy.domainWeightT6
        DomainOutput = MembershipBoy.domainOT6

    
    fuzzyInterp(HeightInput, WeightInput)

    MamdaniSystem.evaluateRules([AgeOutput[i]], WeightMembership.getCapturedMember(), HeightMembership.getCapturedMember())
    print(MamdaniSystem.captured_output)

    ScoreList = MamdaniSystem.getFuzzyScore([AgeMembership.fuzzy_points[i]], WeightMembership.fuzzy_points, HeightMembership.fuzzy_points, OutputMembership)
    print(ScoreList)

    ProjectedChart = MamdaniSystem.ProjectFuzzyScoreToOutput(ScoreList, OutputMembership)

    MamdaniSystem.PlotProjected(ProjectedChart,DomainOutput)

    AggregatedChart = MamdaniSystem.aggregated(ProjectedChart)

    MamdaniSystem.PlotAggregated(AggregatedChart, DomainOutput)
    defuzzyResult = skf.defuzz(DomainOutput, AggregatedChart, 'centroid')

    print("Result:")
    print("Z Value:",defuzzyResult)
    OutputMembership.captureInterp(defuzzyResult, DomainOutput)
    OutputMembership.show_fuzzy_point()

    OutputInterp = OutputMembership.get_fuzzy_point()
    KeyOut = OutputMembership.getCapturedMember()
    OutputMembership.show_plot_withVal(DomainOutput,defuzzyResult,OutputInterp,KeyOut)
    print("")
    
    MamdaniSystem.captured_output = []