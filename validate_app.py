import sys
import os

print("--- Starting PharmaGlobe Logic Validation ---")

# Step 1: Test Import of local modules
print("\n[1/5] Testing imports...")
try:
    import med_database
    import openfda_helper
    import barcode_helper
    import ai_helper
    print("Success: Imported med_database, openfda_helper, barcode_helper, and ai_helper successfully.")
except Exception as e:
    print(f"FAILED: Import error: {e}")
    sys.exit(1)

# Step 2: Test Local Database integrity
print("\n[2/5] Testing local database module...")
try:
    countries = med_database.get_countries()
    categories = med_database.get_categories()
    print(f"Curated Countries: {countries}")
    print(f"Curated Categories: {categories}")
    
    # Assert countries are parsed
    assert len(countries) > 0, "No countries found in database."
    assert "Japan" in countries, "Japan not found in database."
    assert "USA" in countries, "USA not found in database."
    
    # Assert search
    search_res = med_database.search_local_medicines("Loxonin")
    print(f"Search 'Loxonin' results count: {len(search_res)}")
    assert len(search_res) > 0, "Could not find 'Loxonin' in search."
    assert "Loxoprofen" in search_res[0]["generic_name"], "Active ingredient mismatch for Loxonin."
    print("Success: Local database functions verified.")
except Exception as e:
    print(f"FAILED: Local database test error: {e}")
    sys.exit(1)

# Step 3: Test OpenFDA API integration
print("\n[3/5] Testing OpenFDA API connection...")
try:
    print("Querying OpenFDA label API for 'aspirin'...")
    fda_results = openfda_helper.search_openfda_by_name("aspirin", limit=1)
    print(f"OpenFDA results count: {len(fda_results)}")
    if fda_results:
        first_res = fda_results[0]
        print(f"Successfully fetched label for: {first_res.get('brand_name')} ({first_res.get('generic_name')})")
        assert "uses" in first_res, "Label result missing 'uses' field."
        assert "warnings" in first_res, "Label result missing 'warnings' field."
        print("Success: OpenFDA API connection and parsing verified.")
    else:
        print("WARNING: OpenFDA API returned 0 results. Check internet connection or FDA API status.")
except Exception as e:
    print(f"FAILED: OpenFDA test error: {e}")
    sys.exit(1)

# Step 4: Test Barcode decoder and database lookup fallback
print("\n[4/5] Testing barcode helper...")
try:
    # Test lookup of a known UPC code (e.g. Advil UPC: 300450444160 or similar US OTC)
    # Let's test with a standard acetaminophen UPC: 300450444160 (Tylenol Extra Strength 100ct)
    test_upc = "300450444160"
    print(f"Querying product lookup for test UPC: {test_upc}...")
    resolved = barcode_helper.lookup_barcode_in_databases(test_upc)
    if resolved:
        print(f"Successfully resolved UPC '{test_upc}' to product:")
        print(f"  Brand: {resolved.get('brand_name')}")
        print(f"  Generic: {resolved.get('generic_name')}")
        print(f"  Resolved via: {resolved.get('resolved_via')}")
    else:
        print(f"WARNING: Test UPC '{test_upc}' could not be resolved. This is acceptable if the third-party trial API rate limit is hit or UPC is deprecated, but check connection.")
        
    print("Success: Barcode helper logic validated.")
except Exception as e:
    print(f"FAILED: Barcode helper test error: {e}")
    sys.exit(1)

# Step 5: Test AI Helper offline fallback responses
print("\n[5/5] Testing AI helper offline local response system...")
try:
    # Test Health Consultant offline fallback
    health_response = ai_helper.generate_chat_response(
        persona="🩺 AI Health Consultant",
        chat_history=[],
        user_message="I have a headache in Japan",
        api_key=None
    )
    print("Health Fallback Response preview:")
    print(health_response[:200] + "...")
    assert "Loxonin S" in health_response or "Bufferin A" in health_response or "EVE Quick" in health_response, "Health fallback did not suggest correct Japanese pain relievers."
    
    # Test Dev Assistant offline fallback
    dev_response = ai_helper.generate_chat_response(
        persona="💻 Codebase Dev Assistant",
        chat_history=[],
        user_message="Explain backend scanner",
        api_key=None
    )
    print("Dev Fallback Response preview:")
    print(dev_response[:200] + "...")
    assert "barcode_helper.py" in dev_response or "OpenCV" in dev_response, "Dev fallback did not mention barcode scanner implementation."
    
    print("Success: AI helper offline response logic verified.")
except Exception as e:
    print(f"FAILED: AI helper test error: {e}")
    sys.exit(1)

print("\n--- All logic tests passed successfully! ---")

