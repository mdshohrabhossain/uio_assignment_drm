\* DRM_Three_Appliances *\
Minimize
Total_Cost_of_Appliances: 0.5 DISH_PerHour1 + 0.5 DISH_PerHour2
 + 0.5 EV_PerHour1 + 0.5 EV_PerHour2 + 0.5 WASH_PerHour1 + 0.5 WASH_PerHour2
Subject To
DISH_CostRequirement: 0.5 DISH_PerHour1 + 0.5 DISH_PerHour2 <= 0.72
EV_CostRequirement: 0.5 EV_PerHour1 + 0.5 EV_PerHour2 <= 4.95
WASH_CostRequirement: 0.5 WASH_PerHour1 + 0.5 WASH_PerHour2 <= 0.97
_dummy: __dummy = 0
_C1: __dummy <= -86.32
_C2: __dummy <= -86.32
Bounds
__dummy = 0
End
