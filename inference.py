
import requests
import os

API = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")

print("[START]")

state = requests.post(f"{API}/reset").json()

for i in range(5):
    action = {
        "assign_doctors": 6,
        "allocate_beds": 8,
        "prioritize_critical": True
    }

    res = requests.post(f"{API}/step", json=action).json()

    print(f"[STEP] {i} | reward={res['reward']}")

print("[END]")