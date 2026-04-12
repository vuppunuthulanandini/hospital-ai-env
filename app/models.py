
from pydantic import BaseModel

class Action(BaseModel):
    assign_doctors: int
    allocate_beds: int
    prioritize_critical: bool

class State(BaseModel):
    available_doctors: int
    available_beds: int
    critical_patients: int
    normal_patients: int
    waiting_time: int