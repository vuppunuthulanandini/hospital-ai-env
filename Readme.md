environment
🏥 Hospital Resource Optimization Environment
Every second counts, every bed matters, and you're the one deciding who gets what — and when.

The Hospital Resource Optimization Environment throws an RL agent into the chaos of a busy hospital floor, where doctors, beds, and critical cases are all competing for the same limited resources. One wrong call and a critical patient waits too long. One smart allocation and the whole system runs smoother. This is triage, but the triage officer is your agent.

Built as a lightweight FastAPI service, it exposes a clean HTTP interface so any agent — Python, remote, or otherwise — can plug in and start making calls.

⚕️ What the agent controls
Action	What it does
assign_doctors	Route available doctors to patients or departments that need them
allocate_beds	Assign beds across wards based on current demand
prioritize_critical	Bump critical-condition patients to the front of the queue
Every decision ripples outward — assign doctors poorly and beds sit empty while a ward drowns; ignore a critical case and the cost shows up fast.

🔌 API Endpoints
Method	Endpoint	Purpose
POST	/reset	Start a fresh hospital state — new patients, new pressure
POST	/step	Submit an action and see how the hospital responds
GET	/state	Check the current state of the floor: beds, doctors, patients waiting
🚀 Run Locally
bash
uvicorn app.main:app --reload
Then point your agent (or curl, or Postman) at http://localhost:8000 and start making decisions.





