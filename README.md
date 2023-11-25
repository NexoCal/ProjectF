# Read Me
## Progress
Mamdani Solver

## Desc
Currently MembershipGroup Class is for membership and are now separated from MamdaniSolver Class which capture the output membership
to solve it later

planning on merging them into on class after i get the solver working since as for right now it can only create rules and capturing
output member

also code a bit messy might tidy it up after everything is set

also also the code is still to specific so might generalize it to


## Class
### MembershipGroup Class
this class is responsible for membership ploting and ect

it has this attribute and fucntion:
- add_membership(String, np.arange, list) : adding membership (detect triat amd traps membership)
- interp(input,np.arange) : use for fuzzification and capturing which member triggered it
- show_plot(np.range) : show all membership in a plot
- show_captured_member : show all membership that give fuzzy value > 0.0

### MamdaniSolver
Currently working on it