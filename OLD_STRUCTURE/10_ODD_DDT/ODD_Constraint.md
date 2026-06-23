
# ODD Constraint

## Definition
ODD constraint is the operational boundary that determines whether autonomous mobility can execute safely under current environment, route, traffic, weather, and system conditions.

## Trigger
- Weather deterioration
- Visibility reduction
- Communication latency
- Road condition change
- Sensor degradation
- Construction area
- Traffic abnormality

## KPI Impact
- Intervention rate ↑
- Latency ↑
- Dispatch restriction ↑
- Matching rate ↓
- Trips ↓

## Collapse Chain
[[ODD_Constraint]]
→ [[Dispatch_Restriction]]
→ [[Fleet_Imbalance]]
→ [[Queue_Saturation]]
→ [[Trips_Feasibility]]

## Recovery Control
- Restrict autonomy scope
- Re-route
- Switch to fallback operation
- Hold dispatch
- Stop execution
- Recalculate service availability

## Related
- [[Dispatch_Collapse]]
- [[DDT_Intervention]]
- [[Latency_Control]]
- [[Trips_Feasibility]]
- [[Safety_Margin]]
```
