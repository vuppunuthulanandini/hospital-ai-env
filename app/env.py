
import random

class HospitalEnv:
    def __init__(self):
        self.state = {}

    def reset(self):
        self.state = {
            "available_doctors": 10,
            "available_beds": 20,
            "critical_patients": random.randint(3, 8),
            "normal_patients": random.randint(10, 20),
            "waiting_time": 20
        }
        return {"state": self.state}

    def step(self, action):
        assign = action.get("assign_doctors", 5)
        beds = action.get("allocate_beds", 10)

        treated_critical = min(self.state["critical_patients"], assign)
        treated_normal = min(self.state["normal_patients"], beds)

        reward = (
            treated_critical * 0.5 +
            treated_normal * 0.2 -
            self.state["waiting_time"] * 0.01
        )

        reward = max(0, min(1, reward))

        # update state
        self.state["critical_patients"] -= treated_critical
        self.state["normal_patients"] -= treated_normal

        return {
            "state": self.state,
            "reward": reward,
            "done": False
        }

    def get_state(self):
        return self.state