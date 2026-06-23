from pathlib import Path
import json

BASE = Path("C:/Obsidian/UrbanOS_Operation_Control")

runtime_data = {
    "runtime_operation": {
        "status": "active",
        "synchronization": True,
        "collapse_state": "normal"
    },

    "fleet_operation": {
        "queue_time": 12,
        "fleet_idle_ratio": 0.18,
        "dispatch_success_rate": 0.97
    },

    "service_hub": {
        "hydrogen_queue": 3,
        "turnaround_time": 18,
        "node_utilization": 0.82
    },

    "vehicle": {
        "latency_ms": 42,
        "control_stability": 0.96,
        "odd_status": "inside"
    },

    "business": {
        "revenue": 12800000,
        "cost": 8300000,
        "contribution": 4500000
    }
}

output = BASE / "runtime_data" / "runtime_state.json"

with open(output, "w", encoding="utf-8") as f:
    json.dump(runtime_data, f, indent=2)

print("runtime_state.json exported.")