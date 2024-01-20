# Read Me

## Update
Alright getting the hang of it, MembershipGroup Class is already set and go problem now is on the
Mamdani Solver. using Max - Min Inference method, antecedent will use OR logic while the consequence use
AND logic.

source : https://www.mathworks.com/help/fuzzy/fuzzy-inference-process.html

Defuzzy will use centroid method

Main problem:

- How the rules will work
- Getting the fuzzy point out of membershipGroup and how to use it

Note:
Might have to rebuild MamdaniSolver from start since it's a mess of a code

## Progress
Mamdani Solver 

## Desc
Currently MembershipGroup Class is for membership and are now separated from MamdaniSolver Class which capture the output membership
to solve it later

planning on merging them into one class after i get the solver working since as for right now it can only create rules and capturing
output member

also code a bit messy might tidy it up after everything is set

also also the code is still too specific so i might generalize it


## Class
### MembershipGroup Class
this class is responsible for membership ploting and ect

it has this attribute and fucntion:
- add_membership(String, np.arange, list) : adding membership (detect triat amd traps membership)
- interp(input,np.arange) : use for fuzzification and capturing which member triggered it
- show_plot(np.arange) : show all membership in a plot
- show_captured_member : show all membership that give fuzzy value > 0.0

### MamdaniSolver
Currently working on it