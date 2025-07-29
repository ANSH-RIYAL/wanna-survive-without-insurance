from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import json
import os
from datetime import datetime
import weasyprint
from jinja2 import Template
import tempfile

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
    """Generate personalized PDF planner"""
    
    # Get procedure details
    procedure = next((p for p in procedures_data if p["id"] == planner.procedure), None)
    if not procedure:
        raise HTTPException(status_code=404, detail="Procedure not found")
    
    # Get relevant hospitals
    relevant_hospitals = [h for h in hospitals_data if planner.procedure in h.get("procedures", [])]
    
    # Create HTML template
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Medical Tourism Planner - {{planner.name}}</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .header { text-align: center; border-bottom: 2px solid #333; padding-bottom: 20px; }
            .section { margin: 30px 0; }
            .section h2 { color: #2c5aa0; border-bottom: 1px solid #ccc; padding-bottom: 10px; }
            .cost-comparison { background: #f5f5f5; padding: 20px; border-radius: 5px; }
            .hospital-list { margin: 20px 0; }
            .hospital-item { border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 5px; }
            .emergency { background: #fff3cd; border: 1px solid #ffeaa7; padding: 15px; border-radius: 5px; }
            .steps { margin: 20px 0; }
            .step { margin: 10px 0; padding: 10px; background: #f8f9fa; border-left: 4px solid #007bff; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Medical Tourism Planner</h1>
            <p>Generated for: {{planner.name}} ({{planner.email}})</p>
            <p>Procedure: {{procedure.name}}</p>
            <p>Travel Dates: {{planner.travel_dates}}</p>
            <p>Generated on: {{generated_date}}</p>
        </div>

        <div class="section">
            <h2>Cost Comparison</h2>
            <div class="cost-comparison">
                <h3>{{procedure.name}}</h3>
                <p><strong>U.S. Cost:</strong> {{procedure.us_cost_range}}</p>
                <p><strong>India Cost:</strong> {{procedure.india_cost_range}}</p>
                <p><strong>Savings:</strong> {{procedure.savings_percentage}}</p>
                <p><strong>Duration in India:</strong> {{procedure.duration_in_india}}</p>
                <p><strong>Recovery Time:</strong> {{procedure.recovery_time}}</p>
            </div>
        </div>

        <div class="section">
            <h2>Step-by-Step Process</h2>
            <div class="steps">
                {% for step in procedure.steps %}
                <div class="step">
                    <h4>Step {{loop.index}}: {{step.title}}</h4>
                    <p>{{step.description}}</p>
                    {% if step.link %}
                    <p><strong>Link:</strong> <a href="{{step.link}}">{{step.link}}</a></p>
                    {% endif %}
                </div>
                {% endfor %}
            </div>
        </div>

        <div class="section">
            <h2>Recommended Hospitals</h2>
            <div class="hospital-list">
                {% for hospital in relevant_hospitals %}
                <div class="hospital-item">
                    <h3>{{hospital.name}}</h3>
                    <p><strong>Location:</strong> {{hospital.location}}</p>
                    <p><strong>Address:</strong> {{hospital.address}}</p>
                    <p><strong>Phone:</strong> {{hospital.phone}}</p>
                    <p><strong>Email:</strong> {{hospital.email}}</p>
                    <p><strong>Website:</strong> <a href="{{hospital.website}}">{{hospital.website}}</a></p>
                    <p><strong>Estimated Cost:</strong> {{hospital.estimated_cost_range}}</p>
                    <p><strong>Accreditations:</strong> {{hospital.accreditations|join(', ')}}</p>
                </div>
                {% endfor %}
            </div>
        </div>

        <div class="section">
            <h2>Travel Information</h2>
            <p><strong>Visa Cost:</strong> {{travel_info.visa_cost}}</p>
            <p><strong>Processing Time:</strong> {{travel_info.processing_time}}</p>
            <p><strong>Average Flight Cost:</strong> {{travel_info.flight_average_cost}}</p>
            <p><strong>Accommodation Cost:</strong> {{travel_info.accommodation_cost_range}}</p>
        </div>

        <div class="section">
            <h2>Emergency Contacts</h2>
            <div class="emergency">
                {% for contact_type, contact_info in travel_info.emergency_contacts.items() %}
                <p><strong>{{contact_type}}:</strong> {{contact_info}}</p>
                {% endfor %}
            </div>
        </div>

        <div class="section">
            <h2>Requirements & Risks</h2>
            <h3>Requirements:</h3>
            <ul>
                {% for req in procedure.requirements %}
                <li>{{req}}</li>
                {% endfor %}
            </ul>
            
            <h3>Risks:</h3>
            <ul>
                {% for risk in procedure.risks %}
                <li>{{risk}}</li>
                {% endfor %}
            </ul>
        </div>
    </body>
    </html>
    """
    
    # Render template
    template = Template(html_template)
    html_content = template.render(
        planner=planner,
        procedure=procedure,
        relevant_hospitals=relevant_hospitals,
        travel_info=travel_data,
        generated_date=datetime.now().strftime("%B %d, %Y")
    )
    
    # Generate PDF
    pdf = weasyprint.HTML(string=html_content).write_pdf()
    
    # Save to temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(pdf)
        tmp_file_path = tmp_file.name
    
    return FileResponse(
        tmp_file_path,
        media_type="application/pdf",
        filename=f"medical_tourism_planner_{planner.name.replace(' ', '_')}.pdf"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 