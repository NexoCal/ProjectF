import skfuzzy as skf
import numpy as np
import matplotlib.pyplot as plt
from membershipGroup import membershipGroup


class mamdaniSolver:
    def __init__(self):
        self.membershipGroupList = []
        self.rules = []
        self.captured_output = []

    def addMemberGroup(self,member : membershipGroup):
        self.membershipGroupList.append(member)

    def showMembershipGroup(self):
        for i in self.membershipGroupList:
            i.show_capture_member()
    
    def showMemberFuzzyPoint(self):
        for i in self.membershipGroupList:
            i.show_fuzzy_point()
    

    def add_rules(self,v1 : list,v2 : str):
        rule = {}
        rule[v2] = v1
        self.rules.append(rule)

    def capture_output_member_manual(self,x : list, y : list, z : list):
        ordering = []

        if len(x) == 2 and len(y) == 2 and len(z) == 2:

            for i in range(len(x)):
                for j in range(len(y)):
                    for k in range(len(z)):
                        temp = [x[i], y[j], z[k]]
                        ordering.append(temp)

        elif len(x) == 2 and len(y) == 2 and len(z) == 1:

            for i in range(len(x)):
                for j in range(len(y)):
                    for k in range(len(z)):
                        temp = [x[i], y[j], z[k]]
                        ordering.append(temp)

        elif len(x) == 2 and len(y) == 1 and len(z) == 2:

            for i in range(len(x)):
                for j in range(len(y)):
                    for k in range(len(z)):
                        temp = [x[i], y[j], z[k]]
                        ordering.append(temp)

        elif len(x) == 1 and len(y) == 2 and len(z) == 2:

            for i in range(len(x)):
                for j in range(len(y)):
                    for k in range(len(z)):
                        temp = [x[i], y[j], z[k]]
                        ordering.append(temp)

        elif len(x) == 1 and len(y) == 2 and len(z) == 1:

            for i in range(len(x)):
                for j in range(len(y)):
                    for k in range(len(z)):
                        temp = [x[i], y[j], z[k]]
                        ordering.append(temp)

        elif len(x) == 1 and len(y) == 1 and len(z) == 2:

            for i in range(len(x)):
                for j in range(len(y)):
                    for k in range(len(z)):
                        temp = [x[i], y[j], z[k]]
                        ordering.append(temp)

        elif len(x) == 1 and len(y) == 1 and len(z) == 1:

           for i in range(len(x)):
                for j in range(len(y)):
                    for k in range(len(z)):
                        temp = [x[i], y[j], z[k]]
                        ordering.append(temp)

        for rule in self.rules:
            key = list(rule)
            check = list(rule.values())
            for seq in ordering:
                if seq == check[0]:
                    self.captured_output.append(key[0])

    def capture_output_member(self):
        ordering = []
        x = self.membershipGroupList[0].getCapturedMember()
        y = self.membershipGroupList[1].getCapturedMember()
        z = self.membershipGroupList[2].getCapturedMember()

        cap = set(())

        if len(x) == 2 and len(y) == 2 and len(z) == 2:

            for i in range(len(x)):
                for j in range(len(y)):
                    for k in range(len(z)):
                        temp = [x[i], y[j], z[k]]
                        ordering.append(temp)

        elif len(x) == 2 and len(y) == 2 and len(z) == 1:

            for i in range(len(x)):
                for j in range(len(y)):
                    for k in range(len(z)):
                        temp = [x[i], y[j], z[k]]
                        ordering.append(temp)

        elif len(x) == 2 and len(y) == 1 and len(z) == 2:

            for i in range(len(x)):
                for j in range(len(y)):
                    for k in range(len(z)):
                        temp = [x[i], y[j], z[k]]
                        ordering.append(temp)

        elif len(x) == 1 and len(y) == 2 and len(z) == 2:

            for i in range(len(x)):
                for j in range(len(y)):
                    for k in range(len(z)):
                        temp = [x[i], y[j], z[k]]
                        ordering.append(temp)

        elif len(x) == 1 and len(y) == 2 and len(z) == 1:

            for i in range(len(x)):
                for j in range(len(y)):
                    for k in range(len(z)):
                        temp = [x[i], y[j], z[k]]
                        ordering.append(temp)

        elif len(x) == 1 and len(y) == 1 and len(z) == 2:

            for i in range(len(x)):
                for j in range(len(y)):
                    for k in range(len(z)):
                        temp = [x[i], y[j], z[k]]
                        ordering.append(temp)

        elif len(x) == 1 and len(y) == 1 and len(z) == 1:

           for i in range(len(x)):
                for j in range(len(y)):
                    for k in range(len(z)):
                        temp = [x[i], y[j], z[k]]
                        ordering.append(temp)

        for rule in self.rules:
            key = list(rule)
            check = list(rule.values())
            for seq in ordering:
                if seq == check[0]:
                    cap.add(key[0])

        for i in cap:
            self.captured_output.append(i)
