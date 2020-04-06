"""
Author: Yilmaz Guleryuz yilmazg@uio.no

UiO IN5410 Assignment-01
Demand Response Management - Optimisation

Part.1) We have a simple household that only has three appliances: a washing machine, an EV and a dishwasher.
We assume the time-of-Use (ToU) pricing scheme: 1NOK/KWh for peak hour and 0.5NOK/KWh for off-peak hours.
Peak hours are in the range of 5:00pm- 8:00pm while all other timeslots are off-peak hours.
Design the strategy to use these appliances to have minimum energy cost.

Note: We need a strategy, not just the amount of the minimal energy cost.
For example, you may need to consider some exemplary questions.
Is it reasonable to use all three appliances at the same time, e.g., 2:00am which has the low energy price?
How should we distribute the power load more reasonably in the timeline?

Solution:
Using Python & PuLP package to solve this problem, see code with inline comments
"""

# import all packages from PuLP, see https://coin-or.github.io/pulp/index.html
from pulp import *

#x_ev = LpVariable('x_ev', 1, 4, LpInteger)
#y_wash = LpVariable('y_wash', 1, 4, LpInteger)
#z_dish = LpVariable('z_dish', 1, 4, LpInteger)
#price_i = LpVariable('price_i', 1, 4)

appliances = ['EV', 'WASH', 'DISH']
# kWh per appliance
app_kwh = {
    'EV': 9.9,
    'WASH': 1.94,
    'DISH': 1.44
}
cost = {
    'offpeak': 0.5,
    'peak': 1
}
# -> optimal total_cost <= 6.64NOK in off-peak hours (0.5nok/kwh)

# peak hours: 17:00-20:00 -> 1NOK/kWh
# off-peak hours: ... -> 0.5NOK/kWh
prices = {}
h = 1
while h <= 24:
    if 17 <= h <= 20:
        prices[str(h)] = 1
    else:
        prices[str(h)] = 0.5
    h = h + 1

# define the problem
drm_problem = LpProblem("DRM_Three_Appliances", LpMinimize)

app_vars = LpVariable.dict("App", appliances, 0)
price_vars = LpVariable.dict("Prices", prices)#, (sum(app_kwh.values())))

"""
...constraints...
ev1 + ev2 + ev3 + ev4 = 9.9 kwh (total consumption per day)
ev1 <= 4.95
ev2 <= 4.95

wash1 + wash2 + wash3 + wash4 = 1.94 kwh (total consumption per day)
wash1 <= 0.97
wash2 <= 0.97

dish1 + dish2 = 1.44 kwh (total consumption per day)
dish1 <= 0.72
dish2 <= 0.72
"""
ev_per_hour = app_kwh['EV']/2 #4.95
ev1 = LpVariable("EV_PerHour1", 0)
ev2 = LpVariable("EV_PerHour2", 0)
wash_per_hour = app_kwh['WASH']/2 #0.97
wash1 = LpVariable("WASH_PerHour1", 0)
wash2 = LpVariable("WASH_PerHour2", 0)
dish_per_hour = app_kwh['DISH']/2 #0.72
dish1 = LpVariable("DISH_PerHour1", 0)
dish2 = LpVariable("DISH_PerHour2", 0)

# The objective function is added to the 'problem' first
#drm_problem += ev1*ev_per_hour + ev2*ev_per_hour \
#               + wash1*wash_per_hour + wash2*wash_per_hour \
#               + dish1*dish_per_hour + dish2*dish_per_hour, "Total consumption of all appliances"

drm_problem += cost['offpeak']*ev1 + cost['offpeak']*ev2 \
               + cost['offpeak']*wash1 + cost['offpeak']*wash2 \
               + cost['offpeak']*dish1 + cost['offpeak']*dish2, "Total_Cost_of_Appliances"

# constraints
drm_problem += cost['offpeak']*ev1 + cost['offpeak']*ev2 <= 4.95, "EV_CostRequirement"
drm_problem += cost['offpeak']*wash1 + cost['offpeak']*wash2 <= 0.97, "WASH_CostRequirement"
drm_problem += cost['offpeak']*dish1 + cost['offpeak']*dish2 <= 0.72, "DISH_CostRequirement"

#drm_problem += lpSum([(sum([wash_per_hour, dish_per_hour, ev_per_hour])) * prices[i] for i in prices]) <= 6.64

#drm_problem += lpSum([(sum(app_kwh.values())) * prices[i] for i in prices]) <= 6.64
#drm_problem += lpSum([app_kwh[i] * app_vars[i] for i in appliances]), "kWh_per_appliance"
#drm_problem += lpSum([app_vars[i] for i in appliances]), "ConsumptionSum"


# (optional) The problem data is written to an .lp file
drm_problem.writeLP("drm_3appliances.lp")

# The problem is solved using PuLP's choice of Solver
drm_problem.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[drm_problem.status])

# Each of the variables is printed with it's resolved optimum value
for prob_var in drm_problem.variables():
    print(prob_var.name, "=", prob_var.varValue)

# The optimised objective function value is printed to the screen
print("Total ... = ", value(drm_problem.objective))
