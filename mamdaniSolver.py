import skfuzzy as skf
import numpy as np
import matplotlib.pyplot as plt
from membershipGroup import membershipGroup

class MamdaniInference:
    
    def __init__(self):
        self.rules = []
        self.captured_output = []
        
    def addRule(self,x: list, y: str):
        rule = {}
        rule[y] = x
        self.rules.append(rule)

    def showRules(self):
        for i in self.rules:
            print(i)
        #Show how many ruies in total
        print("Rules :", len(self.rules))

    def evaluateRules(self, Age: list, Height: list, Weight: list):
        antecedentList = []
        cap = []

        for i in range(len(Age)):
            for j in range(len(Height)):
                for k in range(len(Weight)):
                    antecedent = [Age[i], Height[j], Weight[k]]
                    antecedentList.append(antecedent)
                    
        for rule in self.rules:
            key = list(rule)
            check = list(rule.values())
            for seq in antecedentList:
                if seq == check[0]:
                    cap.append(key[0])

        for i in cap:
            self.captured_output.append(i)

    def getFuzzyScore(self,Age: list, Height: list, Weight: list, Output: membershipGroup):
        Dict = {}
        keyList = []
        scoreList = []

        AgeKey = []
        for i in Age:
            Dict.update(i)
            tmp = list(i.keys())
            AgeKey.append(tmp[0])
        keyList.append(AgeKey)

        HeightKey = []
        for i in Height:
            Dict.update(i)
            tmp = list(i.keys())
            HeightKey.append(tmp[0])
        keyList.append(HeightKey)
        
        WeightKey = []
        for i in Weight:
            Dict.update(i)
            tmp = list(i.keys())
            WeightKey.append(tmp[0])
        keyList.append(WeightKey)
        
        counter = 0
        for i in range(len(Height)):
            firstKey = keyList[1][i]
            for j in range(len(Weight)):
                secondKey = keyList[2][j]
                Score = np.fmax(Dict.get(firstKey),Dict.get(secondKey))
                scoreList.append({self.captured_output[counter]: Score})
                counter += 1
        return scoreList
    
    def ProjectFuzzyScoreToOutput(self, ListofFuzzyScore: list, OutputMembership: membershipGroup):
        SelectedMember = []

        for i in ListofFuzzyScore:
            tmpKey = list(i.keys())
            tmpKey = tmpKey[0]
            for j in OutputMembership.member:
                keyChecker = list(j.keys())
                keyChecker = keyChecker[0]
                if tmpKey == keyChecker:
                    SelectedMember.append(j)
                    continue
        
        
                
        

