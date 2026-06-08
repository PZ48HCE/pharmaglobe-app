import streamlit as st
from PIL import Image
import os
import med_database
import openfda_helper
import barcode_helper
import ai_helper

# Set Page Config
st.set_page_config(
    page_title="PharmaGlobe - Global Medicine Directory",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
def local_css(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning(f"CSS file {file_name} not found.")

local_css("style.css")

# Helper to render category badges
def get_category_badge_html(category):
    cat_lower = category.lower()
    if "pain" in cat_lower or "fever" in cat_lower:
        return f'<span class="category-badge badge-pain">{category}</span>'
    elif "cold" in cat_lower or "cough" in cat_lower or "flu" in cat_lower:
        return f'<span class="category-badge badge-cold">{category}</span>'
    elif "digest" in cat_lower or "stomach" in cat_lower or "acid" in cat_lower or "heartburn" in cat_lower:
        return f'<span class="category-badge badge-digestive">{category}</span>'
    elif "allergy" in cat_lower or "rhinitis" in cat_lower:
        return f'<span class="category-badge badge-allergy">{category}</span>'
    else:
        return f'<span class="category-badge badge-default">{category}</span>'

# Render a card for medicine details
def render_medicine_card(med, index=0):
    category = med.get("category", "General Medicine")
    badge_html = get_category_badge_html(category)
    
    country = med.get("country", "")
    country_html = f'<div class="country-badge">📍 {country}</div>' if country else ""
    
    uses_list = med.get("uses", [])
    uses_html = ""
    if isinstance(uses_list, list):
        uses_html = ", ".join(uses_list)
    else:
        uses_html = str(uses_list)
        
    benefits_list = med.get("benefits", [])
    benefits_html = ""
    if isinstance(benefits_list, list):
        benefits_html = " ".join([f"<li>{b}</li>" for b in benefits_list])
    else:
        benefits_html = f"<li>{benefits_list}</li>"
        
    warnings_list = med.get("warnings", [])
    warnings_html = ""
    if isinstance(warnings_list, list):
        warnings_html = "".join([f"<li>{w}</li>" for w in warnings_list])
    else:
        warnings_html = f"<li>{warnings_list}</li>"
        
    resolved_via = med.get("resolved_via", "")
    resolved_html = f'<div style="font-size: 0.75rem; color: rgba(20, 240, 200, 0.7); margin-bottom: 6px;">Resolved via: {resolved_via}</div>' if resolved_via else ""

    # Build card HTML
    card_html = f"""
    <div class="glass-card">
        {resolved_html}
        {country_html}
        <h3 style="margin: 0 0 6px 0; font-size: 1.35rem; font-family: 'Outfit'; color: #ffffff;">{med['name']}</h3>
        <div style="font-size: 0.9rem; color: rgba(255,255,255,0.6); margin-bottom: 12px; font-style: italic;">
            Active Ingredient: {med.get('generic_name', med.get('active_ingredients', 'Not Specified'))}
        </div>
        {badge_html}
        
        <div class="section-title">✨ Primary Uses</div>
        <div class="section-content">{uses_html}</div>
        
        {f'<div class="section-title">🌟 Benefits</div><div class="section-content" style="padding-left: 15px; margin: 0;"><ul style="margin:0; padding-left:15px;">{benefits_html}</ul></div>' if benefits_html else ''}
        
        <div class="section-title">📋 Dosage & Directions</div>
        <div class="section-content">{med.get('dosage', 'Refer to product package for details.')}</div>
        
        {f'<div class="section-title">🏥 Precautions</div><div class="section-content">{med["precautions"]}</div>' if med.get("precautions") and med["precautions"] != "No specific precautions listed." else ''}
        
        {f'<div class="price-tag" style="margin-top: 10px;">🏷️ {med["price"]}</div>' if med.get("price") else ''}
        
        {f'<div class="warnings-panel"><div class="warnings-title">⚠️ Warnings & Precautions</div><ul class="warnings-list">{warnings_html}</ul></div>' if warnings_html else ''}
        
        {f'<a href="{med["shop_link"]}" target="_blank" class="btn-action">🛒 Find Store / Shop Online</a>' if med.get("shop_link") else ''}
    </div>
    """
    return card_html

# Sidebar Header & Nav
with st.sidebar:
    st.markdown('<h1 class="app-title" style="font-size: 1.8rem; margin-bottom: 5px;"><span class="gradient-text">PharmaGlobe</span></h1>', unsafe_allow_html=True)
    st.markdown('<div style="font-size: 0.85rem; color: rgba(255,255,255,0.5); margin-bottom: 25px;">Global Medicine Lookup & Scanner</div>', unsafe_allow_html=True)
    
    st.markdown("### 🗺️ Select Location")
    countries = med.get_countries()
    selected_country = st.selectbox(
        "Browse regional daily-use medicines:",
        options=["Global (All)"] + countries
    )
    
    st.markdown("---")
    st.markdown("### 🧭 Navigation")
    menu = st.radio(
        "Go to page:",
        ["🗺️ Regional Directory", "🔍 Search & Compare", "📸 Barcode Scanner", "💬 AI Assistant"]
    )
    
    st.markdown("---")
    st.markdown("### 🔑 Gemini AI API")
    user_gemini_key = st.text_input(
        "Enter Gemini API Key:",
        type="password",
        help="Get a free key from Google AI Studio. If left blank, local fallback logic is used.",
        value=os.environ.get("GEMINI_API_KEY", "")
    )
    
    st.markdown("---")
    st.markdown("### ℹ️ App Information")
    st.markdown(
        """
        **PharmaGlobe** provides a comprehensive database of daily-use over-the-counter (OTC) medicines across different countries.
        
        Uses public **OpenFDA** and product barcode APIs for real-time drug label resolution.
        """
    )
    
    # Optional API Key input (hidden input style)
    api_key_status = "Inactive"
    if os.environ.get("FDA_API_KEY") or os.path.exists(".env"):
        api_key_status = "Active (Env)"
    st.markdown(f"**OpenFDA Key:** `{api_key_status}`")

# Header Area
st.markdown('<h1 style="margin-top:-20px;"><span class="gradient-text">PharmaGlobe Dashboard</span></h1>', unsafe_allow_html=True)

# ----------------- MENU: REGIONAL DIRECTORY -----------------
if menu == "🗺️ Regional Directory":
    st.markdown("### 🗺️ Local Daily-Use & Common OTC Medicines")
    st.markdown("Browse standard household over-the-counter medications based on your country. Helps you find local equivalents of medicines you use at home.")
    
    country_filter = None if selected_country == "Global (All)" else selected_country
    
    # Filter Categories
    categories = med.get_categories(country=country_filter)
    selected_category = st.tabs(["All Categories"] + categories)
    
    # Tab handling
    for i, tab in enumerate([st] + list(selected_category)):
        if i == 0:
            # First tab represents "All"
            continue
            
        current_cat = categories[i - 1]
        with selected_category[i - 1]:
            meds = med.get_medicines_by_filters(country=country_filter, category=current_cat)
            if not meds:
                st.info(f"No medicines curated for {selected_country} under category {current_cat}.")
            else:
                # Render in grid
                st.markdown('<div class="med-grid">', unsafe_allow_html=True)
                cols = st.columns(3)
                for idx, item in enumerate(meds):
                    with cols[idx % 3]:
                        st.markdown(render_medicine_card(item, idx), unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
    # If the user selected the first tab (or just viewing all in standard layout)
    if selected_country != "Global (All)" and not categories:
        st.info("Select a country from the sidebar to browse local medicines.")
    elif selected_country == "Global (All)":
        st.info("Browse medicines by selecting a specific country in the sidebar, or search for a product under the 'Search & Compare' tab.")
        
        # Display overall directory in grid
        meds = med.get_medicines_by_filters()
        st.markdown('<div class="med-grid">', unsafe_allow_html=True)
        cols = st.columns(3)
        for idx, item in enumerate(meds):
            with cols[idx % 3]:
                st.markdown(render_medicine_card(item, idx), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ----------------- MENU: SEARCH & COMPARE -----------------
elif menu == "🔍 Search & Compare":
    st.markdown("### 🔍 Global Medicine Search")
    st.markdown("Search across our local curated database or query the live **OpenFDA** database for detailed US FDA drug labels.")
    
    search_query = st.text_input("Enter drug name, active ingredient (e.g., Ibuprofen, Acetaminophen), or symptom (e.g., headache, fever):")
    
    search_source = st.radio(
        "Search source:",
        ["Curated Local Database", "OpenFDA Live Database (Official US labels)", "Both (Compare side-by-side)"],
        horizontal=True
    )
    
    if search_query:
        local_results = []
        fda_results = []
        
        if "Local" in search_source or "Both" in search_source:
            local_results = med.search_local_medicines(search_query)
            
        if "OpenFDA" in search_source or "Both" in search_source:
            with st.spinner("Searching official OpenFDA records..."):
                fda_results = openfda_helper.search_openfda_by_name(search_query, limit=3)
                
        # Rendering results
        if search_source == "Both (Compare side-by-side)":
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### Curated Regional Medicines")
                if not local_results:
                    st.info("No matching medicines in the local curated database.")
                else:
                    for idx, m in enumerate(local_results):
                        st.markdown(render_medicine_card(m, idx), unsafe_allow_html=True)
                        
            with col2:
                st.markdown("#### Live OpenFDA Drug Labels")
                if not fda_results:
                    st.info("No matching drug labels found in OpenFDA.")
                else:
                    for idx, m in enumerate(fda_results):
                        # Convert OpenFDA dictionary format to render card
                        m_card = {
                            "name": m["brand_name"],
                            "generic_name": m["generic_name"],
                            "category": m["product_type"],
                            "uses": [m["uses"]],
                            "dosage": m["dosage"],
                            "warnings": [m["warnings"]],
                            "precautions": m["precautions"],
                            "price": "",
                            "shop_link": f"https://www.amazon.com/s?k={m['brand_name']}",
                            "resolved_via": "OpenFDA API",
                            "country": "USA (FDA)"
                        }
                        st.markdown(render_medicine_card(m_card, idx + 100), unsafe_allow_html=True)
                        
        elif "Local" in search_source:
            st.markdown("#### Curated Regional Medicines")
            if not local_results:
                st.info("No matching medicines found in the curated database.")
            else:
                st.markdown('<div class="med-grid">', unsafe_allow_html=True)
                cols = st.columns(3)
                for idx, m in enumerate(local_results):
                    with cols[idx % 3]:
                        st.markdown(render_medicine_card(m, idx), unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
        else:  # OpenFDA only
            st.markdown("#### Live OpenFDA Drug Labels")
            if not fda_results:
                st.info("No matching drug labels found in OpenFDA.")
            else:
                st.markdown('<div class="med-grid">', unsafe_allow_html=True)
                cols = st.columns(3)
                for idx, m in enumerate(fda_results):
                    m_card = {
                        "name": m["brand_name"],
                        "generic_name": m["generic_name"],
                        "category": m["product_type"],
                        "uses": [m["uses"]],
                        "dosage": m["dosage"],
                        "warnings": [m["warnings"]],
                        "precautions": m["precautions"],
                        "price": "",
                        "shop_link": f"https://www.amazon.com/s?k={m['brand_name']}",
                        "resolved_via": "OpenFDA API",
                        "country": "USA (FDA)"
                    }
                    with cols[idx % 3]:
                        st.markdown(render_medicine_card(m_card, idx), unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

# ----------------- MENU: BARCODE SCANNER -----------------
elif menu == "📸 Barcode Scanner":
    st.markdown("### 📸 Barcode Scanner & Product Identifier")
    st.markdown("Upload a photo or capture a packaging barcode using your camera. PharmaGlobe will decode the barcode, lookup the product details, and link it to database records.")
    
    scan_method = st.radio(
        "Choose capture source:",
        ["Upload Barcode Image File", "Use Device Camera Input"],
        horizontal=True
    )
    
    img_file = None
    if scan_method == "Upload Barcode Image File":
        img_file = st.file_uploader("Upload an image of a barcode (PNG, JPG, JPEG):", type=["png", "jpg", "jpeg"])
    else:
        img_file = st.camera_input("Position the barcode clearly in the frame:")
        
    # Manual barcode lookup fallback option
    st.markdown("---")
    st.markdown("#### ⌨️ Manual Barcode Search")
    manual_barcode = st.text_input("If scanning fails, type the barcode number (UPC/EAN) manually here:")
    
    # Process scan or manual lookup
    barcode_to_lookup = None
    barcode_format = "Manual"
    
    if img_file is not None:
        try:
            image = Image.open(img_file)
            st.image(image, caption="Uploaded Image Preview", width=300)
            
            with st.spinner("Decoding barcode from image..."):
                code, code_type = barcode_helper.decode_barcode(image)
                
            if code:
                st.success(f"Successfully decoded barcode: `{code}` (Format: {code_type})")
                barcode_to_lookup = code
                barcode_format = code_type
            else:
                st.warning("Could not detect a clear barcode in the image. Please ensure the barcode is flat, well-lit, and in focus, or type it in the manual search below.")
        except Exception as e:
            st.error(f"Error reading image: {e}")
            
    elif manual_barcode:
        barcode_to_lookup = manual_barcode.strip()
        
    if barcode_to_lookup:
        st.markdown(f"### 🔍 Resolving details for code: `{barcode_to_lookup}`")
        with st.spinner("Searching product catalogs and medicine registries..."):
            resolved_product = barcode_helper.lookup_barcode_in_databases(barcode_to_lookup)
            
        if resolved_product:
            st.success("Product resolved successfully!")
            
            # Map values to rendering card
            card_data = {
                "name": resolved_product.get("brand_name", resolved_product.get("name", "Unknown Brand")),
                "generic_name": resolved_product.get("generic_name", "Unknown Active Ingredient"),
                "category": resolved_product.get("category", resolved_product.get("product_type", "OTC Medicine")),
                "country": resolved_product.get("country", "Global Database"),
                "uses": resolved_product.get("uses", "No usage information found."),
                "benefits": resolved_product.get("benefits", []),
                "dosage": resolved_product.get("dosage", "Refer to package guidelines."),
                "warnings": resolved_product.get("warnings", []),
                "precautions": resolved_product.get("precautions", ""),
                "price": resolved_product.get("price", ""),
                "shop_link": resolved_product.get("shop_link", ""),
                "resolved_via": resolved_product.get("resolved_via", "Barcode Resolution API")
            }
            
            # Make sure warnings and uses are parsed correctly for list/str types
            if isinstance(card_data["uses"], str):
                card_data["uses"] = [card_data["uses"]]
            if isinstance(card_data["warnings"], str):
                card_data["warnings"] = [card_data["warnings"]]
                
            # Render card
            st.markdown(render_medicine_card(card_data, index=999), unsafe_allow_html=True)
        else:
            st.error(f"Could not resolve barcode `{barcode_to_lookup}` in any database.")
            st.markdown("Would you like to search the web directly for this barcode?")
            st.markdown(f'<a href="https://www.google.com/search?q={barcode_to_lookup}" target="_blank" class="btn-action">🔍 Google Search Barcode</a>', unsafe_allow_html=True)

# ----------------- MENU: AI ASSISTANT -----------------
elif menu == "💬 AI Assistant":
    st.markdown("### 💬 AI Health & Dev Assistant")
    st.markdown("Engage with our AI agent to discuss health problems, suggest medicines, or learn about the frontend/backend architecture of this application.")
    
    # Selection of Persona
    persona = st.selectbox(
        "Choose AI Assistant Persona:",
        ["🩺 AI Health Consultant", "💻 Codebase Dev Assistant"]
    )
    
    # Select target session key based on persona
    chat_key = "health_chat" if persona == "🩺 AI Health Consultant" else "dev_chat"
    
    # Initialize history if empty
    if chat_key not in st.session_state:
        st.session_state[chat_key] = []
        # Add welcome message
        if persona == "🩺 AI Health Consultant":
            st.session_state[chat_key].append({
                "role": "assistant",
                "content": "Hello! I am your AI Health Consultant. How can I help you today? Please feel free to describe symptoms, ask about health problems, or ask for standard OTC medicine recommendations."
            })
        else:
            st.session_state[chat_key].append({
                "role": "assistant",
                "content": "Hello! I am the lead Developer of PharmaGlobe. I can explain the frontend architecture, backend database, OpenFDA API integration, OpenCV barcode scanner, or help you write code to extend the app."
            })
            
    # Clear chat option
    col_chat, col_clear = st.columns([6, 1])
    with col_clear:
        if st.button("🧹 Clear Chat", use_container_width=True):
            st.session_state[chat_key] = []
            st.rerun()
            
    # Display message history
    for msg in st.session_state[chat_key]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    # API key check indicator
    is_using_gemini = bool(user_gemini_key)
    api_badge = "🟢 Connected (Gemini API)" if is_using_gemini else "🟡 Offline Mode (Local Fallback)"
    st.caption(f"Status: {api_badge}")
    
    # Handle user message
    user_input = st.chat_input("Ask a question...")
    if user_input:
        # User message
        with st.chat_message("user"):
            st.markdown(user_input)
        st.session_state[chat_key].append({"role": "user", "content": user_input})
        
        # Assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = ai_helper.generate_chat_response(
                    persona=persona,
                    chat_history=st.session_state[chat_key][:-1],  # exclude current user input as it's passed separately
                    user_message=user_input,
                    api_key=user_gemini_key
                )
                st.markdown(response)
        st.session_state[chat_key].append({"role": "assistant", "content": response})
        st.rerun()

