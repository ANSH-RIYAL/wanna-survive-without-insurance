# 🏥 Medical Tourism India - Setup Guide

## 🎯 Project Summary

This is a **lightweight Python backend API** for medical tourism to India, designed to help U.S. citizens navigate affordable healthcare options. The system provides comprehensive information about procedures, hospitals, travel logistics, and generates personalized medical tourism planners.

## ✅ What's Built

### **Backend API (FastAPI)**
- **4 Core Procedures**: Heart Bypass, Dental Implants, Spine Surgery, IVF
- **12 Hospitals**: Delhi area hospitals with detailed information
- **Cost Comparisons**: U.S. vs India pricing (80-95% savings)
- **Travel Information**: Visa, flights, accommodation, emergency contacts
- **Personalized Planners**: JSON-based planner generation

### **Data Structure**
- **Hospitals**: Contact info, specialties, accreditations, cost ranges
- **Procedures**: Step-by-step guides, requirements, risks, cost comparisons
- **Travel**: Visa requirements, flight costs, emergency contacts

### **API Endpoints**
- `GET /api/procedures` - List all procedures
- `GET /api/hospitals` - List hospitals (with filtering)
- `GET /api/travel` - Get travel information
- `POST /api/generate-planner` - Generate personalized planner
- `GET /api/stats` - Get API statistics

## 🚀 Quick Start

### **Option 1: Simple Setup (Recommended)**
```bash
# 1. Install dependencies
pip3 install -r requirements_simple.txt

# 2. Run the server
python3 app_simple.py

# 3. Test the API
python3 test_api.py

# 4. Open frontend
open frontend/index_simple.html
```

### **Option 2: Full Setup (with PDF generation)**
```bash
# 1. Install system dependencies (macOS)
brew install pango gdk-pixbuf libffi

# 2. Install Python dependencies
pip3 install -r requirements.txt

# 3. Run the server
python3 app.py

# 4. Test the API
python3 test_api.py
```

## 📁 Project Structure

```
wanna-survive-without-insurance/
├── app_simple.py              # Main API (simplified, no PDF)
├── app.py                     # Full API (with PDF generation)
├── requirements_simple.txt    # Dependencies (simplified)
├── requirements.txt           # Full dependencies
├── test_api.py               # API testing script
├── data/                     # JSON data files
│   ├── hospitals.json        # 12 hospitals in Delhi
│   ├── procedures.json       # 4 core procedures
│   └── travel.json          # Travel logistics
├── frontend/                 # Test frontend
│   ├── index_simple.html    # Simplified frontend
│   └── index.html           # Full frontend (with PDF)
└── README.md                # Project documentation
```

## 🔧 API Testing

### **Automated Test**
```bash
python3 test_api.py
```

### **Manual Testing**
1. **API Status**: `http://localhost:8000/`
2. **Procedures**: `http://localhost:8000/api/procedures`
3. **Hospitals**: `http://localhost:8000/api/hospitals`
4. **Travel Info**: `http://localhost:8000/api/travel`
5. **API Docs**: `http://localhost:8000/docs`

## 📊 Sample Data Included

### **Hospitals (12 total)**
- Apollo Hospital Delhi
- Fortis Escorts Heart Institute
- Max Super Speciality Hospital
- BLK Super Speciality Hospital
- Indraprastha Apollo Hospitals
- Safdarjung Hospital
- AIIMS Delhi
- Sir Ganga Ram Hospital
- Delhi Dental Centre
- Nova IVF Fertility
- Medanta The Medicity
- Artemis Hospital

### **Procedures (4 total)**
- **Heart Bypass**: $70k-$200k (US) vs $6k-$15k (India)
- **Dental Implants**: $20k-$50k (US) vs $2k-$8k (India)
- **Spine Surgery**: $50k-$150k (US) vs $5k-$12k (India)
- **IVF Treatment**: $15k-$30k (US) vs $2.5k-$6k (India)

## 🎨 Frontend Integration

### **For Replit Development**
The backend is designed to work with any frontend framework. Key integration points:

1. **API Base URL**: `http://localhost:8000/api`
2. **CORS**: Enabled for all origins (configure for production)
3. **Data Format**: JSON responses
4. **Error Handling**: Standard HTTP status codes

### **Example API Calls**
```javascript
// Get all procedures
fetch('http://localhost:8000/api/procedures')
  .then(response => response.json())
  .then(data => console.log(data.procedures));

// Get hospitals for specific procedure
fetch('http://localhost:8000/api/hospitals?procedure=heart-bypass')
  .then(response => response.json())
  .then(data => console.log(data.hospitals));

// Generate planner
fetch('http://localhost:8000/api/generate-planner', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    name: "John Doe",
    email: "john@example.com",
    procedure: "heart-bypass",
    travel_dates: "March 15-30, 2024",
    budget_range: "$10,000 - $15,000"
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

## 🚀 Deployment Options

### **Local Development**
```bash
python3 app_simple.py
```

### **Production (Render/Heroku)**
1. Create `Procfile`:
```
web: uvicorn app_simple:app --host 0.0.0.0 --port $PORT
```

2. Deploy with `requirements_simple.txt`

### **Docker (Optional)**
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements_simple.txt .
RUN pip install -r requirements_simple.txt
COPY . .
EXPOSE 8000
CMD ["python", "app_simple.py"]
```

## 🔒 Security & Privacy

- **No Data Storage**: All data is read-only from JSON files
- **No User Sessions**: Stateless API design
- **CORS Configuration**: Configure properly for production
- **Input Validation**: Pydantic models for data validation

## 🛠️ Customization

### **Adding New Data**
1. Edit JSON files in `data/` directory
2. Restart server to load changes
3. Test via API endpoints

### **Adding New Endpoints**
1. Add route functions in `app_simple.py`
2. Update data models if needed
3. Test with `test_api.py`

### **Modifying Data Structure**
1. Update Pydantic models in `app_simple.py`
2. Modify JSON files to match new structure
3. Update frontend to handle new data

## 📞 Support & Next Steps

### **Immediate Next Steps**
1. **Test the API**: Run `python3 test_api.py`
2. **Explore Frontend**: Open `frontend/index_simple.html`
3. **Review Data**: Check `data/` directory for sample data
4. **Plan Integration**: Design how Replit frontend will use the API

### **Future Enhancements**
- PDF generation (when WeasyPrint dependencies are resolved)
- Real-time flight data integration
- Hospital review system
- User testimonials
- Multi-language support

### **For Replit Integration**
1. **Backend**: Deploy to Render/Heroku using `app_simple.py`
2. **Frontend**: Build in Replit using the API endpoints
3. **Data Updates**: Modify JSON files and redeploy
4. **Testing**: Use the provided test scripts

---

## 🎉 Ready to Use!

The backend is **fully functional** and ready for frontend integration. The simplified version (`app_simple.py`) works without any system dependencies and provides all core functionality needed for the medical tourism platform.

**Key Features Working:**
- ✅ All API endpoints functional
- ✅ 12 hospitals with detailed information
- ✅ 4 procedures with cost comparisons
- ✅ Travel information and emergency contacts
- ✅ Personalized planner generation
- ✅ Frontend test interface
- ✅ Comprehensive test suite

**Ready for Replit Frontend Development!** 🚀 