#!/usr/bin/env python3
"""
Simple test script for the Medical Tourism India API
"""

import requests
import json
import time

BASE_URL = "http://localhost:8000"

def test_api():
    print("🏥 Testing Medical Tourism India API")
    print("=" * 50)
    
    # Test 1: API Status
    print("\n1. Testing API Status...")
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API Status: {data['message']} (v{data['version']})")
        else:
            print(f"❌ API Status Error: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ API Connection Error: {e}")
        return False
    
    # Test 2: Get Procedures
    print("\n2. Testing Procedures Endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api/procedures")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Found {len(data['procedures'])} procedures:")
            for proc in data['procedures']:
                print(f"   - {proc['name']} (ID: {proc['id']})")
        else:
            print(f"❌ Procedures Error: {response.status_code}")
    except Exception as e:
        print(f"❌ Procedures Error: {e}")
    
    # Test 3: Get Hospitals
    print("\n3. Testing Hospitals Endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api/hospitals")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Found {len(data['hospitals'])} hospitals")
        else:
            print(f"❌ Hospitals Error: {response.status_code}")
    except Exception as e:
        print(f"❌ Hospitals Error: {e}")
    
    # Test 4: Get Travel Info
    print("\n4. Testing Travel Info Endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api/travel")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Travel info loaded successfully")
            print(f"   - Visa cost: {data['visa_cost']}")
            print(f"   - Flight cost: {data['flight_average_cost']}")
        else:
            print(f"❌ Travel Info Error: {response.status_code}")
    except Exception as e:
        print(f"❌ Travel Info Error: {e}")
    
    # Test 5: Filter Hospitals by Procedure
    print("\n5. Testing Hospital Filtering...")
    try:
        response = requests.get(f"{BASE_URL}/api/hospitals?procedure=heart-bypass")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Found {len(data['hospitals'])} hospitals for heart bypass")
        else:
            print(f"❌ Hospital Filter Error: {response.status_code}")
    except Exception as e:
        print(f"❌ Hospital Filter Error: {e}")
    
    # Test 6: Get Specific Procedure
    print("\n6. Testing Specific Procedure...")
    try:
        response = requests.get(f"{BASE_URL}/api/procedures/heart-bypass")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Heart Bypass Procedure Details:")
            print(f"   - U.S. Cost: {data['us_cost_range']}")
            print(f"   - India Cost: {data['india_cost_range']}")
            print(f"   - Savings: {data['savings_percentage']}")
        else:
            print(f"❌ Specific Procedure Error: {response.status_code}")
    except Exception as e:
        print(f"❌ Specific Procedure Error: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 API Testing Complete!")
    print("\nTo test the frontend:")
    print("1. Open frontend/index.html in your browser")
    print("2. Or visit http://localhost:8000/docs for API documentation")
    
    return True

if __name__ == "__main__":
    # Wait a moment for server to start
    print("Waiting for server to start...")
    time.sleep(2)
    test_api() 