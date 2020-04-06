# uio_assignment_drm
UiO IN5410 Assignment-01: Demand Response Management - Optimisation

```
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
```
