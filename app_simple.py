from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import json
import os
from datetime import datetime

app = FastAPI(title="Medical Tourism India API", version="1.0.0")

# CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data models
class Hospital(BaseModel):
    id: str
    name: str
    location: str
    address: str
    phone: str
    email: str
    website: str
    specialties: List[str]
    accreditations: List[str]
    procedures: List[str]
    estimated_cost_range: str
    rating: Optional[float] = None

class Procedure(BaseModel):
    id: str
    name: str
    description: str
    us_cost_range: str
    india_cost_range: str
    savings_percentage: str
    duration_in_india: str
    recovery_time: str
    steps: List[Dict[str, Any]]
    requirements: List[str]
    risks: List[str]

class TravelInfo(BaseModel):
    visa_requirements: List[str]
    visa_cost: str
    processing_time: str
    flight_average_cost: str
    accommodation_cost_range: str
    local_transport_cost: str
    emergency_contacts: Dict[str, str]

class UserPlanner(BaseModel):
    name: str
    email: str
    procedure: str
    travel_dates: str
    budget_range: str
    special_requirements: Optional[str] = None

# Data storage (in-memory for now, can be moved to JSON files)
hospitals_data = []
procedures_data = []
travel_data = {}

def load_data():
    """Load data from JSON files"""
    global hospitals_data, procedures_data, travel_data
    
    # Load hospitals data
    if os.path.exists("data/hospitals.json"):
        with open("data/hospitals.json", "r") as f:
            hospitals_data = json.load(f)
    
    # Load procedures data
    if os.path.exists("data/procedures.json"):
        with open("data/procedures.json", "r") as f:
            procedures_data = json.load(f)
    
    # Load travel data
    if os.path.exists("data/travel.json"):
        with open("data/travel.json", "r") as f:
            travel_data = json.load(f)

# Load data on startup
load_data()

@app.get("/")
async def root():
    return {"message": "Medical Tourism India API", "version": "1.0.0"}

@app.get("/api/hospitals")
async def get_hospitals(procedure: Optional[str] = None, location: Optional[str] = None):
    """Get hospitals with optional filtering"""
    filtered_hospitals = hospitals_data
    
    if procedure:
        filtered_hospitals = [h for h in filtered_hospitals if procedure in h.get("procedures", [])]
    
    if location:
        filtered_hospitals = [h for h in filtered_hospitals if location.lower() in h.get("location", "").lower()]
    
    return {"hospitals": filtered_hospitals}

@app.get("/api/hospitals/{hospital_id}")
async def get_hospital(hospital_id: str):
    """Get specific hospital details"""
    hospital = next((h for h in hospitals_data if h["id"] == hospital_id), None)
    if not hospital:
        raise HTTPException(status_code=404, detail="Hospital not found")
    return hospital

@app.get("/api/procedures")
async def get_procedures():
    """Get all procedures"""
    return {"procedures": procedures_data}

@app.get("/api/procedures/{procedure_id}")
async def get_procedure(procedure_id: str):
    """Get specific procedure details"""
    procedure = next((p for p in procedures_data if p["id"] == procedure_id), None)
    if not procedure:
        raise HTTPException(status_code=404, detail="Procedure not found")
    return procedure

@app.get("/api/travel")
async def get_travel_info():
    """Get travel information"""
    return travel_data

@app.post("/api/generate-planner")
async def generate_planner(planner: UserPlanner):
    """Generate personalized planner data (JSON format)"""
    
    # Get procedure details
    procedure = next((p for p in procedures_data if p["id"] == planner.procedure), None)
    if not procedure:
        raise HTTPException(status_code=404, detail="Procedure not found")
    
    # Get relevant hospitals
    relevant_hospitals = [h for h in hospitals_data if planner.procedure in h.get("procedures", [])]
    
    # Create planner data
    planner_data = {
        "user_info": {
            "name": planner.name,
            "email": planner.email,
            "travel_dates": planner.travel_dates,
            "budget_range": planner.budget_range,
            "special_requirements": planner.special_requirements
        },
        "procedure": procedure,
        "hospitals": relevant_hospitals,
        "travel_info": travel_data,
        "generated_date": datetime.now().strftime("%B %d, %Y"),
        "total_estimated_cost": {
            "procedure_cost": procedure["india_cost_range"],
            "travel_cost": travel_data["flight_average_cost"],
            "accommodation_cost": travel_data["accommodation_cost_range"],
            "visa_cost": travel_data["visa_cost"]
        }
    }
    
    return planner_data

@app.get("/api/stats")
async def get_stats():
    """Get API statistics"""
    return {
        "total_hospitals": len(hospitals_data),
        "total_procedures": len(procedures_data),
        "hospitals_by_location": {
            "Delhi": len([h for h in hospitals_data if "Delhi" in h["location"]]),
            "Gurgaon": len([h for h in hospitals_data if "Gurgaon" in h["location"]])
        },
        "procedures_available": [p["name"] for p in procedures_data]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 