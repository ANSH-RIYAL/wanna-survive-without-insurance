# 🏥 Medical Tourism India - Backend API

A comprehensive backend API for medical tourism to India, helping U.S. citizens navigate affordable healthcare options.

## 🎯 Project Overview

This backend provides:
- **4 Core Procedures**: Heart Bypass, Dental Implants, Spine Surgery, IVF
- **Hospital Directory**: 12+ hospitals in Delhi area with detailed information
- **Cost Comparisons**: U.S. vs India pricing with 80-95% savings
- **Step-by-Step Guides**: Complete process from diagnosis to recovery
- **Travel Information**: Visa, flights, accommodation, emergency contacts
- **PDF Generator**: Personalized medical tourism planners

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd wanna-survive-without-insurance
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the backend server**
```bash
python app.py
```

4. **Test the API**
- Open `frontend/index.html` in your browser
- Or visit `http://localhost:8000/docs` for interactive API documentation

## 📁 Project Structure

```
wanna-survive-without-insurance/
├── app.py                 # Main FastAPI application
├── requirements.txt       # Python dependencies
├── data/                 # JSON data files
│   ├── hospitals.json    # Hospital directory
│   ├── procedures.json   # Procedure information
│   └── travel.json       # Travel logistics
├── frontend/             # Simple test frontend
│   └── index.html        # HTML test interface
└── README.md            # This file
```

## 🔌 API Endpoints

### Core Endpoints
- `GET /` - API status and version
- `GET /api/procedures` - List all procedures
- `GET /api/procedures/{id}` - Get specific procedure details
- `GET /api/hospitals` - List hospitals (with optional filtering)
- `GET /api/hospitals/{id}` - Get specific hospital details
- `GET /api/travel` - Get travel information
- `POST /api/generate-planner` - Generate personalized PDF planner

### Query Parameters
- `GET /api/hospitals?procedure=heart-bypass` - Filter hospitals by procedure
- `GET /api/hospitals?location=Delhi` - Filter hospitals by location

## 📊 Data Structure

### Procedures
Each procedure includes:
- Cost comparison (U.S. vs India)
- Step-by-step process
- Requirements and risks
- Duration and recovery time

### Hospitals
Each hospital includes:
- Contact information
- Specialties and procedures
- Accreditations
- Estimated cost ranges

### Travel Information
- Visa requirements and costs
- Flight and accommodation costs
- Emergency contacts
- Useful links

## 🎨 Frontend Integration

The backend is designed to work with any frontend framework. The test frontend (`frontend/index.html`) demonstrates:

- API connection testing
- Data display
- PDF generation
- Form handling

## 🔧 Development

### Adding New Data
1. Edit the JSON files in the `data/` directory
2. Restart the server to load new data
3. Test via the API endpoints

### Customizing PDF Templates
The PDF generation uses Jinja2 templates in `app.py`. Modify the `html_template` variable to customize the PDF output.

### Adding New Endpoints
1. Add new route functions in `app.py`
2. Update data models if needed
3. Test with the frontend or API docs

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production (Render/Heroku)
1. Create a `Procfile`:
```
web: uvicorn app:app --host 0.0.0.0 --port $PORT
```

2. Deploy to your preferred platform

## 📝 Sample Data

The backend comes with sample data for:

### Hospitals (12 total)
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

### Procedures (4 total)
- Heart Bypass Surgery
- Dental Implants
- Spine Surgery
- IVF Treatment

## 🔒 Privacy & Security

- No user data is stored permanently
- PDF generation is temporary
- All data is read-only from JSON files
- CORS enabled for frontend integration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For questions or issues:
- Check the API documentation at `http://localhost:8000/docs`
- Review the test frontend for usage examples
- Open an issue in the repository

## 📄 License

This project is open source and available under the MIT License.

---

**Note**: This is a backend API for medical tourism information. It does not provide medical advice. Users should consult with healthcare professionals for medical decisions.
