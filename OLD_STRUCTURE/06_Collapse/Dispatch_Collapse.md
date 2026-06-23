# Dispatch Collapse

## Definition
Dispatch collapse is the failure mode where demand exists but fleet, route, node, energy, or ODD conditions cannot be resolved into executable trips.

## Trigger
- Matching rate decreases
- Dispatch success rate decreases
- Queue time increases
- Fleet imbalance occurs
- ODD restriction expands
- Energy supply becomes insufficient
- Node congestion blocks vehicle turnaround

## KPI Impact
- Dispatch success rate ↓
- Waiting time ↑
- Fleet idle ratio ↑
- Utilization ↓
- Trips ↓
- Revenue ↓

## Collapse Chain
[[Calendar_Demand]]
→ [[Matching_Control]]
→ [[Dispatch_Control]]
→ [[Queue_Saturation]]
→ [[Fleet_Imbalance]]
→ [[Trips_Feasibility]]

## Recovery Control
- Reallocate fleet
- Expand matching conditions
- Switch node
- Restrict demand intake
- Recalculate ETA
- Execute priority dispatch
- Reduce autonomy scope if ODD constraint is active

## Related
- [[Trips_Feasibility]]
- [[Queue_Saturation]]
- [[Fleet_Imbalance]]
- [[Energy_Shortage]]
- [[ODD_Constraint]]
- [[Node_Overflow]]