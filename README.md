# Read Me

## Update
Alright all is set now just to make it work for T2 till T6

source : https://www.mathworks.com/help/fuzzy/fuzzy-inference-process.html

Defuzzy will use centroid method

To Do:
- Clean up the code and optimize it

Note:
NewMamdaniTest is the one using custom made class

## Progress
Optimizing and Cleaning up

## Desc
Currently MembershipGroup Class is for membership and are now separated from MamdaniSolver Class which capture the output membership
to solve it later

planning on merging them into one class after i get the solver working since as for right now it can only create rules and capturing
output member

also code a bit messy might tidy it up after everything is set

also also the code is still too specific so i might generalize it


## Class
### membershipGroup Class
this class is responsible for membership ploting and ect

it has this attribute and function:

Attribute:
- captured_member : where captured membership is stored after using captureInterp function
- member : where added member is stored
- fuzzy_points : where captured membership is stored after using captureInterp function

Function:
- add_member(self,membername : str, domain_space, point : list )
- interp(self,value : int, domain_space)
- captureInterp(self,value : int, domain_space)
- show_plot(self,domian_space)
- show_capture_member(self)
- show_fuzzy_point(self)
- getCapturedMember(self)

### mamdaniSolver
This class is responsible for mamdani inference

it has this attribute and function:

Attribute:
- rules : where all the rules is stored
- captured_output : where output rule is stored adter using evaluateRules function

Function:
- addRule(self,x: list, y: str)
- showRules()
- evaluateRules(self, Age: list, Height: list, Weight: list)
- getFuzzyScore(self,Age: list, Height: list, Weight: list, Output: membershipGroup)
- ProjectFuzzyScoreToOutput(self, ListofFuzzyScore: list, OutputMembership: membershipGroup)
- PlotProjected(self, Projected: list, OutputDomain)
- aggregated(self, Projected: list)
- PlotAggregated(self, aggregated, domain)
