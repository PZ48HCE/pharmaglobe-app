import google.generativeai as genai
import os
import med_database

# Helper to check if API key exists in environment
def get_env_api_key():
    return os.environ.get("GEMINI_API_KEY", "")

def get_gemini_client(api_key=None):
    """Initializes and returns the generative model if a valid key is provided."""
    key = api_key or get_env_api_key()
    if not key:
        return None
    try:
        genai.configure(api_key=key)
        # Use gemini-2.5-flash as the default standard model
        model = genai.GenerativeModel('gemini-2.5-flash')
        return model
    except Exception as e:
        print(f"Error initializing Gemini: {e}")
        return None

# ==================== PERSONA SYSTEM PROMPTS ====================

HEALTH_SYSTEM_PROMPT = """
You are "Aegis", a professional AI Health Consultant for the PharmaGlobe app.
Your goal is to help users discuss general health problems, understand mild symptoms, suggest appropriate daily-use over-the-counter (OTC) medicines, and offer health guidelines.

Strict Guidelines:
1. ALWAYS start or end your response with a clear medical disclaimer:
   "Disclaimer: I am an AI, not a doctor. This advice is for informational purposes only. Please consult a qualified healthcare provider or pharmacist before taking any medication, especially if you have pre-existing conditions, are pregnant, or experience severe symptoms."
2. Suggest appropriate OTC medicines based on standard medical guidelines. If the user mentions a location (e.g. Japan, USA, India, UK), try to recommend the corresponding local brand names from the PharmaGlobe curated database (e.g., Loxonin S or EVE Quick in Japan, Tylenol or Advil in the US, Dolo 650 in India, Panadol in the UK).
3. Always ask clarifying questions if the symptoms are vague, and list common warnings (e.g., drowsiness, stomach irritation).
4. Emphasize when symptoms require immediate medical attention (e.g., high fever, severe chest pain, shortness of breath).
"""

DEV_SYSTEM_PROMPT = """
You are the Lead Developer and Architect of the PharmaGlobe application.
Your goal is to explain the frontend and backend architecture of the app to the user, help them understand the codebase, and guide them in writing code to extend the app.

Technical Details of PharmaGlobe:
- Frontend: Streamlit (Python) utilizing custom HTML embedding and custom CSS overrides (style.css) for a premium dark glassmorphic design.
- Local Database (med_database.py): A structured list of dictionaries containing daily-use OTC medicines mapped to countries, categories, uses, dosages, and Amazon/Boots shopping links.
- OpenFDA (openfda_helper.py): Pulls live US drug labels (brand, generic, warnings, uses, dosage) via HTTP requests.
- Barcode Decoder (barcode_helper.py): Uses OpenCV's BarcodeDetector and QRCodeDetector to extract codes from images (camera or uploaded file). UPCs are resolved via UPCitemdb and linked to local/OpenFDA data.
- Validation Suite (validate_app.py): Performs automated logic assertions.

Always be technical, clear, and provide code snippets when helping the user write or refactor code.
"""

# ==================== LOCAL FALLBACK RESPONDER ====================

def get_local_fallback_response(persona, message):
    """Provides a smart keyword-based local response if no Gemini API Key is configured."""
    msg = message.lower()
    
    disclaimer = (
        "\n\n*⚠️ Disclaimer: I am an AI Assistant operating in offline fallback mode. "
        "This advice is for informational purposes only. Please consult a qualified doctor before taking any medicine.*"
    )
    
    if persona == "🩺 AI Health Consultant":
        # Check symptoms & locations
        symptom = None
        matched_meds = []
        
        # Determine symptom category
        if any(w in msg for w in ["pain", "headache", "toothache", "muscle", "fever", "cramp"]):
            symptom = "Pain & Fever"
            category = "Pain Reliever"
        elif any(w in msg for w in ["cold", "flu", "cough", "sore throat", "runny nose", "phlegm"]):
            symptom = "Cold & Flu Symptoms"
            category = "Cold & Flu"
        elif any(w in msg for w in ["stomach", "acid", "heartburn", "bloating", "digestion", "nausea", "reflux"]):
            symptom = "Stomach & Acid Issues"
            category = "Digestive Health"
        elif any(w in msg for w in ["allergy", "allergic", "sneeze", "itch", "hay fever"]):
            symptom = "Allergies"
            category = "Allergy"
        else:
            category = None
            
        # Determine country
        country = None
        if "japan" in msg:
            country = "Japan"
        elif "usa" in msg or "america" in msg or "us" in msg:
            country = "USA"
        elif "india" in msg:
            country = "India"
        elif "uk" in msg or "britain" in msg or "england" in msg:
            country = "UK"
            
        if category:
            matched_meds = med_database.get_medicines_by_filters(country=country, category=category)
            
        if matched_meds:
            med_list_str = "\n".join([f"- **{m['name']}** ({m['generic_name']}): {', '.join(m['uses'][:2])}. Typical Price: {m['price']}" for m in matched_meds])
            loc_str = f" in **{country}**" if country else ""
            return (
                f"Hello! It sounds like you are asking about symptoms relating to **{symptom}**{loc_str}.\n\n"
                f"Here are some common over-the-counter (OTC) options from our regional database:\n{med_list_str}\n\n"
                f"**General Guidelines:**\n"
                f"- Read the dosing labels carefully.\n"
                f"- Avoid taking multiple medicines containing the same active ingredient (e.g. paracetamol/acetaminophen) to prevent overdose.\n"
                f"- Take pain relievers with food if you have a sensitive stomach."
                f"{disclaimer}"
            )
        else:
            return (
                f"Hello! I am operating in local fallback mode. I can assist with queries about pain, fever, cold, stomach upset, or allergy symptoms.\n\n"
                f"To get more detailed symptom discussions and personalized suggestions, **please configure your Gemini API Key in the sidebar**!\n"
                f"In the meantime, you can browse all regional OTC listings directly in the **🗺️ Regional Directory** tab."
                f"{disclaimer}"
            )
            
    else:  # Developer Assistant Persona
        if any(w in msg for w in ["frontend", "app", "ui", "streamlit"]):
            return (
                "### Frontend Architecture (Streamlit)\n"
                "PharmaGlobe uses a Streamlit frontend configured in `app.py`. The design matches a modern dark-mode layout with custom styling:\n"
                "1. **Layout**: Defined in `app.py` using `st.set_page_config(layout='wide')` to support side-by-side grids.\n"
                "2. **Styling**: Overridden globally via `style.css` which injects a dark violet gradient background, glassmorphism borders (`backdrop-filter`), and customized category badges.\n"
                "3. **State Management**: Streamlit's `st.session_state` is utilized to hold navigation and persistent chat messages."
            )
        elif any(w in msg for w in ["backend", "db", "database", "med"]):
            return (
                "### Backend & Local Database\n"
                "The backend of PharmaGlobe relies on three custom helpers:\n"
                "1. `med_database.py`: Houses curated OTC medicines for Japan, UK, USA, and India. Functions like `search_local_medicines()` handle name and symptom lookups.\n"
                "2. `openfda_helper.py`: Queries the official OpenFDA Label and NDC directories over HTTPS. It parses details like `indications_and_usage` and `warnings`.\n"
                "3. `barcode_helper.py`: Integrates OpenCV to detect barcodes and matches them to products using the UPCitemdb catalog API."
            )
        elif any(w in msg for w in ["barcode", "scan", "opencv"]):
            return (
                "### Barcode Scanner Mechanism\n"
                "The barcode scanner logic is located in `barcode_helper.py`:\n"
                "1. **Image Capture**: Streamlit captures an image via file uploader or camera input.\n"
                "2. **OpenCV Decoding**: The image is converted to a BGR numpy array. `cv2.barcode.BarcodeDetector()` scans for EAN/UPC barcodes. `cv2.QRCodeDetector()` acts as a fallback.\n"
                "3. **Resolution Chain**: Decoded codes are checked against OpenFDA. If not found, they query the global UPCitemdb registry to get the product name, which is then mapped back to local database equivalents."
            )
        else:
            return (
                "### PharmaGlobe Codebase Overview\n"
                "I am the Dev Assistant. Here are the core files in this project:\n"
                "- `app.py`: Main Streamlit app UI containing page tabs.\n"
                "- `med_database.py`: Curated regional medicines mapping.\n"
                "- `openfda_helper.py`: Live FDA drug label search wrapper.\n"
                "- `barcode_helper.py`: OpenCV barcode reader & UPC catalog lookups.\n"
                "- `style.css`: Custom CSS styling for glassmorphic elements.\n"
                "- `validate_app.py`: Logic verification script.\n\n"
                "Ask me about: **frontend**, **backend**, or **barcode scanning** to see detailed explanations! "
                "For interactive, AI-generated coding help, **configure your Gemini API Key in the sidebar**."
            )

# ==================== MAIN CHAT GENERATION ====================

def generate_chat_response(persona, chat_history, user_message, api_key=None):
    """
    Generates a response from the AI assistant.
    If the API key is active, queries Gemini. Otherwise, runs local fallback logic.
    
    chat_history: list of dicts, e.g. [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]
    """
    model = get_gemini_client(api_key)
    
    if not model:
        # Fallback to smart rule-based offline engine
        return get_local_fallback_response(persona, user_message)
        
    # Build the prompt structure including system instructions
    system_instruction = HEALTH_SYSTEM_PROMPT if persona == "🩺 AI Health Consultant" else DEV_SYSTEM_PROMPT
    
    # Format the chat history into a structured prompt for Gemini
    formatted_chat = []
    # System instruction context
    formatted_chat.append(f"System Instructions: {system_instruction}")
    
    # Add history
    for msg in chat_history[-6:]:  # Keep context window focused on last 6 messages
        role_label = "User" if msg["role"] == "user" else "Assistant"
        formatted_chat.append(f"{role_label}: {msg['content']}")
        
    # Add new message
    formatted_chat.append(f"User: {user_message}\nAssistant:")
    
    full_prompt = "\n\n".join(formatted_chat)
    
    try:
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        print(f"Gemini generation error: {e}")
        return f"Error communicating with Gemini API: {e}. Falling back to offline engine:\n\n" + get_local_fallback_response(persona, user_message)
