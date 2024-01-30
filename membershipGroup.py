import skfuzzy as skf
import numpy as np
import matplotlib.pyplot as plt

class membershipGroup:
    def __init__(self):
        self.captured_member = []
        self.member = []
        self.fuzzy_points = []

    def add_member(self,membername : str, domain_space, point : list ):

        if len(point) == 4:
            new_member = {}
            new_member[membername] = skf.trapmf(domain_space,point)
            self.member.append(new_member)
        elif len(point) == 3:
            new_member = dict(membername = skf.trimf(domain_space,point))
            self.member.append(new_member)


    def interp(self,value : int, domain_space):
        for variable in self.member:
            key = list(variable)
            checker = skf.interp_membership(domain_space,variable.get(key[0]),value)
            self.captured_member.append(variable)
            print({key[0]: checker}, end=" ")
        print("")

    def captureInterp(self,value : int, domain_space):
        for variable in self.member:
            key = list(variable)
            checker = skf.interp_membership(domain_space,variable.get(key[0]),value)

            if checker != 0.0:
                self.captured_member.append(variable)
                self.fuzzy_points.append({key[0]: checker})

    def show_plot(self,domian_space):
        for variable in self.member:
            key = list(variable)
            plt.plot(domian_space,variable.get(key[0]),linewidth=1.5)
            plt.fill_between(domian_space,variable.get(key[0]),alpha=0.2)
        plt.show()

    def show_capture_member(self):
        tmp = []
        for variable in self.captured_member:
            keys = list(variable)
            tmp.append(keys[0])

        print(tmp)

    def show_fuzzy_point(self):
        print(self.fuzzy_points)
    
    def getCapturedMember(self):
        tmp = []
        for variable in self.captured_member:
            keys = list(variable)
            tmp.append(keys[0])

        return tmp
    