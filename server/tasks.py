
def easy_task(state):
    return 1.0 if state["normal_patients"] < 5 else 0.0

def medium_task(state):
    return 1.0 if state["critical_patients"] < 2 else 0.0

def hard_task(state):
    return 1.0 if state["critical_patients"] == 0 else 0.0