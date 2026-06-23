
# Node Overflow

## Definition
Node overflow is the failure mode where service hubs cannot process arriving vehicles, fueling, charging, cleaning, maintenance, or turnaround operations.

## Trigger
- Excess vehicle concentration
- Charging or fueling congestion
- Maintenance overlap
- Cleaning delay
- Dispatch synchronization failure
- Limited berth capacity
- Energy supply limitation

## KPI Impact
- Node utilization ↑
- Waiting time ↑
- Turnaround time ↑
- Dispatch delay ↑
- Utilization ↓

## Collapse Chain
[[Node_Control]]
→ [[Node_Overflow]]
→ [[Queue_Saturation]]
→ [[Fleet_Imbalance]]
→ [[Dispatch_Collapse]]

## Recovery Control
- Switch node
- Balance queue
- Reallocate fleet
- Prioritize turnaround
- Reschedule maintenance
- Restrict new dispatch into saturated node

## Related
- [[Service_Hub_Control]]
- [[Queue_Saturation]]
- [[Energy_Shortage]]
- [[Fleet_Imbalance]]
- [[Trips_Feasibility]]

```
