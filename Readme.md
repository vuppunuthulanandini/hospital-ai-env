
# Hospital Resource Optimization Environment

## Description
This environment simulates hospital resource allocation.

## Actions
- assign_doctors
- allocate_beds
- prioritize_critical

## Endpoints
- POST /reset
- POST /step
- GET /state

## Run Locally
uvicorn app.main:app --reload