# Curated Local Medicine Database for PharmaGlobe

MEDICINE_DATABASE = [
    # --- JAPAN ---
    {
        "name": "Loxonin S (ロキソニンS)",
        "generic_name": "Loxoprofen Sodium Hydrate",
        "category": "Pain Reliever",
        "country": "Japan",
        "uses": ["Headaches", "Menstrual cramps", "Toothaches", "Fever reduction", "Joint pain"],
        "benefits": ["Highly effective pain relief", "Fast-acting formula", "Gentle on the stomach compared to some older NSAIDs"],
        "dosage": "Adults (15+): Take 1 tablet up to 2 times a day. If symptoms persist, a 3rd dose may be taken. Avoid taking on an empty stomach. Space doses at least 4 hours apart.",
        "warnings": [
            "Do not take if under 15 years old.",
            "Do not take if you have stomach ulcers, severe kidney, liver, or heart issues.",
            "Avoid if you have asthma triggered by aspirin or other NSAIDs.",
            "Consult a doctor if pregnant or breastfeeding."
        ],
        "price": "¥650 - ¥800 (12 tablets)",
        "shop_link": "https://www.amazon.co.jp/s?k=ロキソニンS"
    },
    {
        "name": "Bufferin A (バファリンA)",
        "generic_name": "Aspirin (Acetylsalicylic Acid)",
        "category": "Pain Reliever",
        "country": "Japan",
        "uses": ["Headaches", "Fever reduction", "Muscle pain", "Toothache", "Shoulder stiffness pain"],
        "benefits": ["Dual-action formula with Dibuffer HT to protect the stomach lining", "Fast absorption", "Contains no sleep-inducing ingredients"],
        "dosage": "Adults (15+): 2 tablets per dose, up to 2 times a day. Space doses at least 6 hours apart. Take with water, preferably not on an empty stomach.",
        "warnings": [
            "Do not give to children under 15 years old (risk of Reye's syndrome).",
            "Do not take if you are within 12 weeks of delivery (pregnancy).",
            "Avoid alcohol while taking this medication.",
            "Consult a doctor if taking blood thinners."
        ],
        "price": "¥800 - ¥1,200 (40 tablets)",
        "shop_link": "https://www.amazon.co.jp/s?k=バファリンA"
    },
    {
        "name": "EVE Quick (イブクイック)",
        "generic_name": "Ibuprofen + Allylisopropylacetylurea + Anhydrous Caffeine",
        "category": "Pain Reliever",
        "country": "Japan",
        "uses": ["Severe headaches", "Fever reduction", "Menstrual pain", "Sore throat pain"],
        "benefits": ["Specially formulated for fast headache relief", "Contains magnesium oxide to speed up absorption and protect stomach"],
        "dosage": "Adults (15+): 2 tablets per dose, up to 3 times a day. Space doses at least 4 hours apart. Avoid taking on an empty stomach.",
        "warnings": [
            "Do not take if under 15 years old.",
            "May cause drowsiness; do not drive or operate machinery after taking.",
            "Avoid taking other cold medicines or sedatives concurrently.",
            "Limit use if you have history of asthma."
        ],
        "price": "¥900 - ¥1,400 (40 tablets)",
        "shop_link": "https://www.amazon.co.jp/s?k=イブクイック"
    },
    {
        "name": "Pabron Gold A (パブロンゴールドA)",
        "generic_name": "Guaifenesin + Dihydrocodeine Phosphate + Acetaminophen + Chlorpheniramine Maleate",
        "category": "Cold & Flu",
        "country": "Japan",
        "uses": ["Cough", "Sputum/Phlegm", "Sore throat", "Runny nose", "Fever", "Chills", "Muscle ache"],
        "benefits": ["All-in-one multi-symptom cold relief", "Clears phlegm and suppresses coughing", "Very popular standard household cold medicine"],
        "dosage": "Adults (15+): 1 packet of fine granules or 3 tablets, 3 times a day, within 30 minutes after meals.",
        "warnings": [
            "Do not give to children under 12 years old.",
            "Causes drowsiness. Do not drive or operate machinery.",
            "Contains codeine; use with caution. Do not use long-term.",
            "Avoid alcohol and other sedatives."
        ],
        "price": "¥1,300 - ¥1,800 (44 packets / 210 tablets)",
        "shop_link": "https://www.amazon.co.jp/s?k=パブロンゴールドA"
    },
    {
        "name": "Ohta's Isan (太田胃散)",
        "generic_name": "Herbal stomachic blend (Cinnamon, Fennel, Nutmeg) + Antacids (Sodium Bicarbonate, Calcium Carbonate)",
        "category": "Digestive Health",
        "country": "Japan",
        "uses": ["Heartburn", "Stomach upset", "Overeating/drinking", "Indigestion", "Loss of appetite"],
        "benefits": ["Traditional Japanese medicine trusted for over 140 years", "Natural aromatic herbs refresh the stomach", "Fast relief from acid reflux and bloating"],
        "dosage": "Adults (15+): 1 spoonful of powder or 1 sachet, 3 times a day, after or between meals.",
        "warnings": [
            "Do not give to infants under 8 years old.",
            "Contains sodium; consult doctor if on a low-salt diet.",
            "Do not use if you have severe kidney disease.",
            "Avoid long-term continuous use (limit to 2 weeks unless directed)."
        ],
        "price": "¥900 - ¥1,300 (140g powder)",
        "shop_link": "https://www.amazon.co.jp/s?k=太田胃散"
    },
    {
        "name": "Allegra FX (アレグラFX)",
        "generic_name": "Fexofenadine Hydrochloride",
        "category": "Allergy",
        "country": "Japan",
        "uses": ["Allergic rhinitis", "Hay fever (pollen allergy)", "Sneezing", "Runny/stuffy nose", "Itchy eyes"],
        "benefits": ["Non-drowsy antihistamine", "Does not impair performance or concentration", "Works 24 hours with twice-daily dosing"],
        "dosage": "Adults (15+): 1 tablet, twice a day (morning and evening) with water.",
        "warnings": [
            "Do not use for children under 15 (for under 15, look for 'Allegra FX Junior').",
            "Do not take with erythromycin or ketoconazole without consulting a doctor.",
            "Avoid taking with seasonal fruit juices (grapefruit, apple, orange) as they reduce absorption."
        ],
        "price": "¥1,800 - ¥2,400 (28 tablets)",
        "shop_link": "https://www.amazon.co.jp/s?k=アレグラFX"
    },

    # --- USA ---
    {
        "name": "Tylenol Extra Strength",
        "generic_name": "Acetaminophen (Paracetamol)",
        "category": "Pain Reliever",
        "country": "USA",
        "uses": ["Headaches", "Muscle aches", "Backache", "Minor arthritis pain", "Common cold fever reduction"],
        "benefits": ["Aspirin-free pain relief", "Gentle on the stomach", "Safe for individuals with stomach ulcers"],
        "dosage": "Adults & Children 12+: Take 2 caplets every 6 hours while symptoms last. Do not exceed 6 caplets (3000 mg) in 24 hours.",
        "warnings": [
            "Severe liver damage may occur if you take more than the maximum daily amount or consume 3+ alcoholic drinks daily while using.",
            "Do not use with any other drug containing acetaminophen.",
            "Stop use if pain worsens or lasts more than 10 days."
        ],
        "price": "$9.00 - $13.00 (100 caplets)",
        "shop_link": "https://www.amazon.com/s?k=Tylenol+Extra+Strength"
    },
    {
        "name": "Advil / Motrin",
        "generic_name": "Ibuprofen",
        "category": "Pain Reliever",
        "country": "USA",
        "uses": ["Headaches", "Toothaches", "Backache", "Menstrual cramps", "Fever reduction", "Minor arthritis pain"],
        "benefits": ["Effective anti-inflammatory", "Relieves pain at the site of inflammation", "Coated tablets are easy to swallow"],
        "dosage": "Adults & Children 12+: Take 1 tablet every 4 to 6 hours while symptoms persist. If pain/fever does not respond to 1 tablet, 2 tablets may be used. Do not exceed 6 tablets in 24 hours.",
        "warnings": [
            "May cause severe allergic reactions (hives, facial swelling, asthma).",
            "NSAID warning: Increases risk of heart attack, stroke, and stomach bleeding.",
            "Take with food or milk if stomach upset occurs."
        ],
        "price": "$8.00 - $12.00 (100 tablets)",
        "shop_link": "https://www.amazon.com/s?k=Advil+Ibuprofen"
    },
    {
        "name": "DayQuil Cold & Flu",
        "generic_name": "Acetaminophen + Dextromethorphan HBr + Phenylephrine HCl",
        "category": "Cold & Flu",
        "country": "USA",
        "uses": ["Nasal congestion", "Cough", "Sore throat", "Minor aches and pains", "Fever"],
        "benefits": ["Non-drowsy daytime relief", "Multi-symptom control", "Available in liquid caps or liquid form"],
        "dosage": "Adults & Children 12+: Take 2 LiquiCaps with water every 4 hours. Do not exceed 4 doses (8 LiquiCaps) in 24 hours.",
        "warnings": [
            "Liver damage hazard: Contains Acetaminophen. Do not combine with Tylenol or other cold products.",
            "Do not use if you are currently taking a monoamine oxidase inhibitor (MAOI).",
            "Stop use if you get nervous, dizzy, or sleepless."
        ],
        "price": "$12.00 - $16.00 (24 LiquiCaps)",
        "shop_link": "https://www.amazon.com/s?k=DayQuil"
    },
    {
        "name": "Pepto-Bismol",
        "generic_name": "Bismuth Subsalicylate",
        "category": "Digestive Health",
        "country": "USA",
        "uses": ["Heartburn", "Indigestion", "Nausea", "Upset stomach", "Diarrhea"],
        "benefits": ["5-symptom rapid relief", "Coats stomach lining to soothe irritation", "Antidiarrheal and antimicrobial action"],
        "dosage": "Adults & Children 12+: 30 mL (1 dose) or 2 chewable tablets every 1/2 to 1 hour as needed. Do not exceed 8 doses in 24 hours.",
        "warnings": [
            "Contains salicylate (aspirin relative). Do not give to children/teenagers who have or are recovering from chickenpox or flu (Reye's syndrome risk).",
            "May cause a temporary, harmless darkening of the tongue and/or stool.",
            "Do not take if you have ulcers or bleeding problems."
        ],
        "price": "$7.00 - $10.00 (12 oz liquid)",
        "shop_link": "https://www.amazon.com/s?k=Pepto-Bismol"
    },
    {
        "name": "Claritin 24 Hour",
        "generic_name": "Loratadine",
        "category": "Allergy",
        "country": "USA",
        "uses": ["Runny nose", "Sneezing", "Itchy, watery eyes", "Itching of the nose or throat due to hay fever"],
        "benefits": ["24-hour relief", "Guaranteed non-drowsy antihistamine", "Indoor and outdoor allergy protection"],
        "dosage": "Adults & Children 6+: Take one 10 mg tablet daily. Do not take more than 1 tablet in 24 hours.",
        "warnings": [
            "Consumers with liver or kidney disease should consult a doctor before use.",
            "Do not use if you have had an allergic reaction to loratadine.",
            "Keep out of reach of children."
        ],
        "price": "$18.00 - $25.00 (30 tablets)",
        "shop_link": "https://www.amazon.com/s?k=Claritin+Loratadine"
    },

    # --- INDIA ---
    {
        "name": "Dolo 650",
        "generic_name": "Paracetamol (Acetaminophen)",
        "category": "Pain Reliever",
        "country": "India",
        "uses": ["High fever reduction", "Headache", "Body ache", "Toothache", "Post-vaccination fever"],
        "benefits": ["Highly trusted for fever control", "Broadly prescribed by doctors in India", "Cost-effective relief"],
        "dosage": "Adults: 1 tablet (650 mg) every 4-6 hours as needed. Do not exceed 4 tablets (2600 mg) in 24 hours.",
        "warnings": [
            "Do not consume with alcohol (risk of severe liver damage).",
            "Avoid taking other medications containing paracetamol simultaneously.",
            "Consult a doctor if fever lasts more than 3 days."
        ],
        "price": "₹30 - ₹40 (15 tablets strip)",
        "shop_link": "https://www.netmeds.com/catalogsearch/result?q=Dolo+650"
    },
    {
        "name": "Combiflam",
        "generic_name": "Ibuprofen + Paracetamol",
        "category": "Pain Reliever",
        "country": "India",
        "uses": ["Muscle pain", "Joint inflammation", "Dental pain", "Fever", "Rheumatoid arthritis discomfort"],
        "benefits": ["Dual active formula targets pain and swelling simultaneously", "Rapid onset of action", "Popular painkiller in India"],
        "dosage": "Adults: 1 tablet 2 to 3 times a day after meals. Do not take on an empty stomach.",
        "warnings": [
            "Increased risk of stomach ulcers and gastrointestinal bleeding.",
            "Do not use if allergic to ibuprofen or paracetamol.",
            "Not recommended for patients with asthma or active stomach ulcers."
        ],
        "price": "₹45 - ₹55 (20 tablets strip)",
        "shop_link": "https://www.netmeds.com/catalogsearch/result?q=Combiflam"
    },
    {
        "name": "Digene Gel / Tablets",
        "generic_name": "Magnesium Hydroxide + Aluminium Hydroxide + Simethicone",
        "category": "Digestive Health",
        "country": "India",
        "uses": ["Acidity", "Heartburn", "Gas bloating", "Indigestion", "Stomach heaviness"],
        "benefits": ["Quick-acting antacid action", "Simethicone relieves gas bubbles and pressure", "Sugar-free formula available in multiple flavors (Mint, Orange, Mixed Fruit)"],
        "dosage": "Adults: Chew 2 to 4 tablets after meals or take 2-4 teaspoons (10-20ml) of liquid gel.",
        "warnings": [
            "Do not take more than the recommended dose.",
            "Patients with kidney disease should consult a doctor (risk of magnesium buildup).",
            "Do not use continuously for more than 2 weeks."
        ],
        "price": "₹120 - ₹150 (200ml syrup / 15 tablets)",
        "shop_link": "https://www.netmeds.com/catalogsearch/result?q=Digene"
    },
    {
        "name": "Eno Powder",
        "generic_name": "Svarjiksara (Sodium Bicarbonate) + Nimbukamra (Citric Acid)",
        "category": "Digestive Health",
        "country": "India",
        "uses": ["Acid reflux", "Heartburn", "Stomach bloating", "Sour stomach"],
        "benefits": ["Starts working in 6 seconds", "Effervescent action neutralizes acid instantly", "Comes in single-use sachets for portability"],
        "dosage": "Adults: Dissolve 1 sachet (5g) or 1 teaspoon of powder in a glass of water (approx. 150ml) and drink immediately. Repeat after 2-3 hours if needed. Max 2 doses per day.",
        "warnings": [
            "Contains high sodium; avoid if you have high blood pressure or are on a low-sodium diet.",
            "Do not take for more than 14 consecutive days.",
            "Not recommended for children under 12 years."
        ],
        "price": "₹80 - ₹100 (100g bottle / ₹9 per sachet)",
        "shop_link": "https://www.netmeds.com/catalogsearch/result?q=Eno"
    },
    {
        "name": "Cetzip / Cetzine",
        "generic_name": "Cetirizine Hydrochloride",
        "category": "Allergy",
        "country": "India",
        "uses": ["Runny nose", "Allergic skin conditions (hives, itching)", "Sneezing", "Watery eyes", "Dust or pet allergy"],
        "benefits": ["Effective 24-hour relief", "Very common OTC antihistamine", "Reduces allergy swelling and redness"],
        "dosage": "Adults: 1 tablet (10 mg) once daily, preferably at bedtime as it may cause mild drowsiness.",
        "warnings": [
            "May cause drowsiness; avoid driving or operating heavy machinery.",
            "Do not consume alcohol while taking cetirizine.",
            "Consult doctor if you have kidney or liver impairment."
        ],
        "price": "₹18 - ₹25 (10 tablets strip)",
        "shop_link": "https://www.netmeds.com/catalogsearch/result?q=Cetzine"
    },

    # --- UK ---
    {
        "name": "Panadol Advance",
        "generic_name": "Paracetamol",
        "category": "Pain Reliever",
        "country": "UK",
        "uses": ["Headaches", "Migraines", "Backache", "Cold & flu fever reduction", "Toothache", "Period pain"],
        "benefits": ["Optizorb technology dissolves up to 5 times faster than standard paracetamol", "Gentle on stomach", "Suitable for elderly patients"],
        "dosage": "Adults (12+): Take 1-2 tablets every 4 to 6 hours as needed. Do not exceed 8 tablets (4g) in 24 hours.",
        "warnings": [
            "Never exceed the maximum dose (paracetamol toxicity risk).",
            "Do not take other paracetamol-containing products simultaneously.",
            "Consult a doctor if pain lasts more than 3 days or fever persists."
        ],
        "price": "£2.50 - £4.00 (16 tablets)",
        "shop_link": "https://www.boots.com/sitesearch?searchTerm=Panadol"
    },
    {
        "name": "Nurofen",
        "generic_name": "Ibuprofen",
        "category": "Pain Reliever",
        "country": "UK",
        "uses": ["Headaches", "Migraines", "Backache", "Muscular pain", "Dental pain", "Fever reduction"],
        "benefits": ["Targeted pain relief", "Reduces inflammation", "Available in liquid capsules for faster absorption"],
        "dosage": "Adults & Children 12+: Take 1 or 2 tablets with water up to 3 times a day as required. Space doses at least 4 hours apart. Max 6 tablets in 24 hours.",
        "warnings": [
            "Do not take if you have a stomach ulcer, perforation, or bleeding.",
            "May trigger asthma attacks in sensitive individuals.",
            "Take with a glass of water, ideally with or after food."
        ],
        "price": "£2.00 - £3.50 (16 tablets)",
        "shop_link": "https://www.boots.com/sitesearch?searchTerm=Nurofen"
    },
    {
        "name": "Gaviscon Double Action",
        "generic_name": "Sodium Alginate + Sodium Bicarbonate + Calcium Carbonate",
        "category": "Digestive Health",
        "country": "UK",
        "uses": ["Heartburn", "Acid indigestion", "Reflux symptoms after meals or during pregnancy"],
        "benefits": ["Forms a protective raft over stomach contents to block acid", "Neutralizes excess acid", "Safe for use during pregnancy and breastfeeding"],
        "dosage": "Adults & Children 12+: Take 10-20ml (two to four 5ml spoonfuls) of liquid or chew 2-4 tablets after meals and at bedtime.",
        "warnings": [
            "Contains sodium and calcium. Consult doctor if on restricted sodium/calcium diets.",
            "Do not take within 2 hours of taking other medicines (as it can affect absorption).",
            "If symptoms persist after 7 days, consult your doctor."
        ],
        "price": "£6.00 - £8.50 (300ml liquid)",
        "shop_link": "https://www.boots.com/sitesearch?searchTerm=Gaviscon"
    },
    {
        "name": "Piriteze / Piri Allergy",
        "generic_name": "Cetirizine Hydrochloride",
        "category": "Allergy",
        "country": "UK",
        "uses": ["Hay fever", "Skin allergies (hives, itchiness)", "Pet allergies", "Dust mite allergy", "Mould spore allergy"],
        "benefits": ["Once-a-day allergy relief", "Relieves both nasal and ocular allergy symptoms", "Max strength non-drowsy formulation (relative to older antihistamines)"],
        "dosage": "Adults & Children 6+: Take 1 tablet daily with a glass of water.",
        "warnings": [
            "May cause drowsiness in some users; avoid driving if affected.",
            "Consult a pharmacist if you have kidney problems.",
            "Avoid excessive alcohol intake while using."
        ],
        "price": "£4.50 - £7.00 (30 tablets)",
        "shop_link": "https://www.boots.com/sitesearch?searchTerm=Piriteze"
    }
]

def get_countries():
    """Returns unique list of countries in the database."""
    return sorted(list(set(med["country"] for med in MEDICINE_DATABASE)))

def get_categories(country=None):
    """Returns unique list of categories, optionally filtered by country."""
    if country:
        return sorted(list(set(med["category"] for med in MEDICINE_DATABASE if med["country"] == country)))
    return sorted(list(set(med["category"] for med in MEDICINE_DATABASE)))

def get_medicines_by_filters(country=None, category=None):
    """Filter medicines by country and/or category."""
    results = MEDICINE_DATABASE
    if country:
        results = [med for med in results if med["country"].lower() == country.lower()]
    if category:
        results = [med for med in results if med["category"].lower() == category.lower()]
    return results

def search_local_medicines(query):
    """Search local database for medicine matching query in name, generic_name, uses, or category."""
    if not query:
        return []
    query = query.lower()
    results = []
    for med in MEDICINE_DATABASE:
        if (query in med["name"].lower() or 
            query in med["generic_name"].lower() or 
            query in med["category"].lower() or 
            any(query in use.lower() for use in med["uses"])):
            results.append(med)
    return results
