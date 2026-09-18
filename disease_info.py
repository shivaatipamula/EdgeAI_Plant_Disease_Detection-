# disease_info.py
# Detailed database for all 38 PlantVillage classes.

DISEASE_INFO = {
    # ==========================================================
    # APPLE
    # ==========================================================
    "Apple___Apple_scab": {
        "cause": "Fungal disease caused by Venturia inaequalis.",
        "symptoms": [
            "Olive-green velvety spots on leaves",
            "Dark lesions on fruits",
            "Premature leaf drop",
            "Reduced fruit quality"
        ],
        "chemical_treatment": [
            "Spray Captan fungicide.",
            "Apply Mancozeb at recommended dosage.",
            "Use Myclobutanil during severe infection."
        ],
        "organic_treatment": [
            "Spray neem oil every 7–10 days.",
            "Use sulfur-based organic fungicide.",
            "Remove infected leaves immediately."
        ],
        "prevention": [
            "Grow resistant apple varieties.",
            "Prune trees for better airflow.",
            "Collect and destroy fallen leaves.",
            "Avoid overhead irrigation."
        ],
        "severity": "Medium",
        "weather": "Cool (16–24°C) and humid weather favors infection.",
        "irrigation": "Avoid wetting the foliage. Prefer drip irrigation.",
        "fertilizer": "Balanced NPK (10-10-10) with sufficient potassium."
    },

    "Apple___Black_rot": {
        "cause": "Fungus Botryosphaeria obtusa.",
        "symptoms": [
            "Purple leaf spots",
            "Black fruit rot",
            "Cankers on branches",
            "Shriveled fruits"
        ],
        "chemical_treatment": [
            "Apply Captan fungicide.",
            "Spray Thiophanate-methyl.",
            "Copper fungicide before flowering."
        ],
        "organic_treatment": [
            "Prune infected branches.",
            "Apply neem oil.",
            "Maintain orchard sanitation."
        ],
        "prevention": [
            "Remove infected fruits.",
            "Prune dead wood.",
            "Improve air circulation.",
            "Maintain orchard hygiene."
        ],
        "severity": "High",
        "weather": "Warm and humid conditions.",
        "irrigation": "Avoid excessive watering.",
        "fertilizer": "High potassium fertilizer improves disease resistance."
    },

    "Apple___Cedar_apple_rust": {
        "cause": "Fungus Gymnosporangium juniperi-virginianae.",
        "symptoms": [
            "Bright orange leaf spots",
            "Yellow lesions",
            "Leaf drop",
            "Reduced fruit production"
        ],
        "chemical_treatment": [
            "Spray Myclobutanil.",
            "Apply Mancozeb.",
            "Use Propiconazole."
        ],
        "organic_treatment": [
            "Remove nearby cedar trees if possible.",
            "Neem oil spray.",
            "Sulfur fungicide."
        ],
        "prevention": [
            "Use resistant cultivars.",
            "Monitor during spring.",
            "Destroy infected leaves."
        ],
        "severity": "Medium",
        "weather": "Wet spring weather promotes infection.",
        "irrigation": "Use drip irrigation.",
        "fertilizer": "Balanced fertilizer with micronutrients."
    },

    "Apple___healthy": {
        "cause": "Healthy plant.",
        "symptoms": [
            "Healthy green leaves",
            "No visible disease",
            "Normal fruit development"
        ],
        "chemical_treatment": [
            "No chemical treatment required."
        ],
        "organic_treatment": [
            "Regular compost application."
        ],
        "prevention": [
            "Routine monitoring.",
            "Balanced nutrition.",
            "Proper pruning."
        ],
        "severity": "None",
        "weather": "Suitable growing conditions.",
        "irrigation": "Maintain regular watering schedule.",
        "fertilizer": "Balanced NPK fertilizer."
    },

    # ==========================================================
    # BLUEBERRY
    # ==========================================================
    "Blueberry___healthy": {
        "cause": "Healthy plant.",
        "symptoms": [
            "Dark green leaves",
            "Healthy stems",
            "Normal berry development"
        ],
        "chemical_treatment": [
            "No treatment required."
        ],
        "organic_treatment": [
            "Mulch using pine bark."
        ],
        "prevention": [
            "Maintain acidic soil.",
            "Regular pruning.",
            "Monitor pests."
        ],
        "severity": "None",
        "weather": "Cool to moderate climate.",
        "irrigation": "Keep soil consistently moist.",
        "fertilizer": "Ammonium sulfate for acidic soils."
    },

    # ==========================================================
    # CHERRY
    # ==========================================================
    "Cherry___Powdery_mildew": {
        "cause": "Fungal disease caused by Podosphaera clandestina.",
        "symptoms": [
            "White powdery coating",
            "Leaf curling",
            "Stunted shoots",
            "Poor fruit quality"
        ],
        "chemical_treatment": [
            "Apply Sulfur fungicide.",
            "Use Myclobutanil.",
            "Spray Potassium bicarbonate."
        ],
        "organic_treatment": [
            "Neem oil spray.",
            "Milk spray (10%).",
            "Prune infected shoots."
        ],
        "prevention": [
            "Increase air circulation.",
            "Avoid overcrowding.",
            "Monitor new shoots."
        ],
        "severity": "Medium",
        "weather": "Warm days with cool nights.",
        "irrigation": "Avoid overhead watering.",
        "fertilizer": "Balanced NPK with calcium."
    },

    "Cherry___healthy": {
        "cause": "Healthy plant.",
        "symptoms": [
            "Healthy foliage",
            "Strong branches",
            "Good flowering"
        ],
        "chemical_treatment": [
            "No treatment required."
        ],
        "organic_treatment": [
            "Use compost annually."
        ],
        "prevention": [
            "Regular pruning.",
            "Good irrigation.",
            "Balanced fertilization."
        ],
        "severity": "None",
        "weather": "Normal growing conditions.",
        "irrigation": "Deep watering during dry periods.",
        "fertilizer": "Balanced fruit-tree fertilizer."
    },

    # ==========================================================
    # CORN (MAIZE)
    # ==========================================================
    "Corn___Cercospora_leaf_spot": {
        "cause": "Fungal disease caused by Cercospora zeae-maydis.",
        "symptoms": [
            "Long narrow gray lesions",
            "Brown leaf spots",
            "Leaf drying",
            "Reduced photosynthesis"
        ],
        "chemical_treatment": [
            "Apply Azoxystrobin fungicide.",
            "Spray Pyraclostrobin.",
            "Use Propiconazole if disease is severe."
        ],
        "organic_treatment": [
            "Neem oil spray.",
            "Apply Trichoderma biofungicide.",
            "Remove infected leaves."
        ],
        "prevention": [
            "Practice crop rotation.",
            "Avoid dense planting.",
            "Use resistant hybrids.",
            "Destroy infected crop residues."
        ],
        "severity": "Medium",
        "weather": "Warm (25–30°C) with high humidity.",
        "irrigation": "Avoid excessive irrigation.",
        "fertilizer": "Balanced NPK with zinc."
    },

    "Corn___Common_rust": {
        "cause": "Fungus Puccinia sorghi.",
        "symptoms": [
            "Small reddish-brown pustules",
            "Yellow halos",
            "Premature leaf drying",
            "Reduced grain yield"
        ],
        "chemical_treatment": [
            "Apply Propiconazole.",
            "Spray Azoxystrobin.",
            "Use Mancozeb in early stages."
        ],
        "organic_treatment": [
            "Neem oil.",
            "Improve field sanitation.",
            "Remove infected leaves."
        ],
        "prevention": [
            "Plant resistant varieties.",
            "Maintain field hygiene.",
            "Avoid continuous maize cultivation."
        ],
        "severity": "Medium",
        "weather": "Cool to moderate temperatures with moisture.",
        "irrigation": "Avoid prolonged leaf wetness.",
        "fertilizer": "Nitrogen and potassium balanced fertilizer."
    },

    "Corn___Northern_Leaf_Blight": {
        "cause": "Fungus Exserohilum turcicum.",
        "symptoms": [
            "Large cigar-shaped lesions",
            "Gray-green spots",
            "Leaf blight",
            "Reduced grain production"
        ],
        "chemical_treatment": [
            "Spray Azoxystrobin.",
            "Apply Propiconazole.",
            "Use Pyraclostrobin."
        ],
        "organic_treatment": [
            "Apply compost tea.",
            "Use Trichoderma.",
            "Remove infected crop debris."
        ],
        "prevention": [
            "Crop rotation.",
            "Use resistant hybrids.",
            "Destroy infected residues."
        ],
        "severity": "High",
        "weather": "Cool humid weather (18–27°C).",
        "irrigation": "Avoid sprinkler irrigation.",
        "fertilizer": "Balanced NPK with micronutrients."
    },

    "Corn___healthy": {
        "cause": "Healthy crop.",
        "symptoms": [
            "Green leaves",
            "Strong stalk",
            "Healthy ear formation"
        ],
        "chemical_treatment": [
            "No treatment required."
        ],
        "organic_treatment": [
            "Use compost and organic manure."
        ],
        "prevention": [
            "Regular monitoring.",
            "Proper irrigation.",
            "Balanced fertilization."
        ],
        "severity": "None",
        "weather": "Normal growing conditions.",
        "irrigation": "Maintain adequate soil moisture.",
        "fertilizer": "NPK 20-20-20 with zinc."
    },

    # ==========================================================
    # GRAPE
    # ==========================================================
    "Grape___Black_rot": {
        "cause": "Fungus Guignardia bidwellii.",
        "symptoms": [
            "Brown circular spots",
            "Black shriveled berries",
            "Leaf lesions",
            "Fruit rot"
        ],
        "chemical_treatment": [
            "Apply Mancozeb.",
            "Spray Myclobutanil.",
            "Use Captan fungicide."
        ],
        "organic_treatment": [
            "Neem oil spray.",
            "Copper fungicide.",
            "Remove infected grapes."
        ],
        "prevention": [
            "Prune vines regularly.",
            "Destroy infected fruits.",
            "Improve air circulation."
        ],
        "severity": "High",
        "weather": "Warm humid weather.",
        "irrigation": "Use drip irrigation.",
        "fertilizer": "Balanced potassium-rich fertilizer."
    },

    "Grape___Esca": {
        "cause": "Complex fungal disease caused by Phaeomoniella species.",
        "symptoms": [
            "Tiger-striped leaves",
            "Wood decay",
            "Berry shriveling",
            "Sudden vine death"
        ],
        "chemical_treatment": [
            "Remove infected wood.",
            "Apply pruning wound protectants."
        ],
        "organic_treatment": [
            "Use Trichoderma products.",
            "Prune during dry weather."
        ],
        "prevention": [
            "Sanitize pruning tools.",
            "Avoid trunk injuries.",
            "Monitor older vines."
        ],
        "severity": "High",
        "weather": "Warm climate with vine stress.",
        "irrigation": "Avoid water stress.",
        "fertilizer": "Organic compost with potassium."
    },

    "Grape___Leaf_blight": {
        "cause": "Fungal infection causing leaf blight.",
        "symptoms": [
            "Brown leaf margins",
            "Drying leaves",
            "Reduced photosynthesis",
            "Leaf drop"
        ],
        "chemical_treatment": [
            "Apply Copper fungicide.",
            "Spray Mancozeb.",
            "Use Chlorothalonil."
        ],
        "organic_treatment": [
            "Neem oil.",
            "Remove infected leaves.",
            "Maintain vine sanitation."
        ],
        "prevention": [
            "Avoid overhead irrigation.",
            "Increase air circulation.",
            "Regular vineyard inspection."
        ],
        "severity": "Medium",
        "weather": "Warm and humid.",
        "irrigation": "Drip irrigation recommended.",
        "fertilizer": "Balanced NPK with magnesium."
    },

    "Grape___healthy": {
        "cause": "Healthy vine.",
        "symptoms": [
            "Healthy green leaves",
            "Normal bunch formation",
            "Good berry development"
        ],
        "chemical_treatment": [
            "No treatment required."
        ],
        "organic_treatment": [
            "Apply compost.",
            "Use mulch."
        ],
        "prevention": [
            "Routine monitoring.",
            "Proper pruning.",
            "Maintain irrigation schedule."
        ],
        "severity": "None",
        "weather": "Normal vineyard conditions.",
        "irrigation": "Regular drip irrigation.",
        "fertilizer": "Balanced grape fertilizer with potassium."
    },

    # ==========================================================
    # ORANGE
    # ==========================================================
    "Orange___Citrus_greening": {
        "cause": "Bacterial disease (Huanglongbing) caused by Candidatus Liberibacter spp.",
        "symptoms": [
            "Yellow shoots",
            "Blotchy mottled leaves",
            "Small, bitter fruits",
            "Premature fruit drop"
        ],
        "chemical_treatment": [
            "Control psyllid vectors using Imidacloprid.",
            "Apply systemic insecticides as recommended.",
            "No permanent cure for infected trees."
        ],
        "organic_treatment": [
            "Use neem oil against psyllids.",
            "Introduce natural predators like lady beetles.",
            "Remove infected branches."
        ],
        "prevention": [
            "Use certified disease-free seedlings.",
            "Control Asian citrus psyllids.",
            "Inspect orchard regularly."
        ],
        "severity": "Very High",
        "weather": "Warm tropical climate.",
        "irrigation": "Avoid drought stress.",
        "fertilizer": "Balanced NPK with Zinc, Magnesium and Iron."
    },

    # ==========================================================
    # PEACH
    # ==========================================================
    "Peach___Bacterial_spot": {
        "cause": "Bacteria Xanthomonas arboricola pv. pruni.",
        "symptoms": [
            "Dark angular leaf spots",
            "Shot holes",
            "Fruit lesions",
            "Twig cankers"
        ],
        "chemical_treatment": [
            "Copper fungicide.",
            "Oxytetracycline where permitted."
        ],
        "organic_treatment": [
            "Neem oil.",
            "Copper soap sprays."
        ],
        "prevention": [
            "Plant resistant cultivars.",
            "Avoid overhead irrigation.",
            "Prune infected branches."
        ],
        "severity": "High",
        "weather": "Warm rainy conditions.",
        "irrigation": "Use drip irrigation.",
        "fertilizer": "Balanced fertilizer with calcium."
    },

    "Peach___healthy": {
        "cause": "Healthy tree.",
        "symptoms": [
            "Healthy green foliage",
            "Normal fruit growth",
            "No disease symptoms"
        ],
        "chemical_treatment": [
            "No treatment required."
        ],
        "organic_treatment": [
            "Apply compost yearly."
        ],
        "prevention": [
            "Regular inspection.",
            "Maintain orchard hygiene."
        ],
        "severity": "None",
        "weather": "Suitable peach-growing conditions.",
        "irrigation": "Regular deep watering.",
        "fertilizer": "Fruit tree fertilizer rich in potassium."
    },

    # ==========================================================
    # PEPPER
    # ==========================================================
    "Pepper___Bacterial_spot": {
        "cause": "Xanthomonas campestris bacteria.",
        "symptoms": [
            "Small water-soaked spots",
            "Yellow halos",
            "Leaf drop",
            "Fruit lesions"
        ],
        "chemical_treatment": [
            "Copper-based bactericide.",
            "Copper + Mancozeb mixture."
        ],
        "organic_treatment": [
            "Neem oil.",
            "Copper soap spray."
        ],
        "prevention": [
            "Disease-free seeds.",
            "Crop rotation.",
            "Avoid wet foliage."
        ],
        "severity": "High",
        "weather": "Warm humid weather.",
        "irrigation": "Drip irrigation preferred.",
        "fertilizer": "Balanced NPK with Calcium."
    },

    "Pepper___healthy": {
        "cause": "Healthy plant.",
        "symptoms": [
            "Healthy leaves",
            "Healthy fruits",
            "Normal growth"
        ],
        "chemical_treatment": [
            "None required."
        ],
        "organic_treatment": [
            "Compost application."
        ],
        "prevention": [
            "Balanced fertilization.",
            "Regular monitoring."
        ],
        "severity": "None",
        "weather": "Suitable growing conditions.",
        "irrigation": "Regular watering.",
        "fertilizer": "Balanced vegetable fertilizer."
    },

    # ==========================================================
    # POTATO
    # ==========================================================
    "Potato___Early_blight": {
        "cause": "Fungus Alternaria solani.",
        "symptoms": [
            "Brown concentric rings",
            "Yellow leaf margins",
            "Leaf drying",
            "Reduced tuber yield"
        ],
        "chemical_treatment": [
            "Chlorothalonil.",
            "Mancozeb.",
            "Azoxystrobin."
        ],
        "organic_treatment": [
            "Neem oil.",
            "Compost tea.",
            "Copper fungicide."
        ],
        "prevention": [
            "Crop rotation.",
            "Destroy infected debris.",
            "Maintain proper spacing."
        ],
        "severity": "Medium",
        "weather": "Warm (24–29°C) with humidity.",
        "irrigation": "Avoid leaf wetness.",
        "fertilizer": "High potassium fertilizer."
    },

    "Potato___Late_blight": {
        "cause": "Phytophthora infestans.",
        "symptoms": [
            "Water-soaked lesions",
            "White fungal growth",
            "Rapid plant collapse",
            "Tuber rot"
        ],
        "chemical_treatment": [
            "Metalaxyl.",
            "Cymoxanil.",
            "Mancozeb."
        ],
        "organic_treatment": [
            "Copper fungicide.",
            "Destroy infected plants.",
            "Improve ventilation."
        ],
        "prevention": [
            "Use certified seed potatoes.",
            "Avoid excessive irrigation.",
            "Rotate crops."
        ],
        "severity": "Very High",
        "weather": "Cool (15–20°C), wet weather.",
        "irrigation": "Drip irrigation only.",
        "fertilizer": "Balanced NPK with extra potassium."
    },

    "Potato___healthy": {
        "cause": "Healthy crop.",
        "symptoms": [
            "Healthy leaves",
            "Strong stems",
            "Normal tuber development"
        ],
        "chemical_treatment": [
            "No treatment required."
        ],
        "organic_treatment": [
            "Organic compost."
        ],
        "prevention": [
            "Regular monitoring.",
            "Balanced nutrition."
        ],
        "severity": "None",
        "weather": "Suitable potato-growing conditions.",
        "irrigation": "Keep soil evenly moist.",
        "fertilizer": "Potato fertilizer rich in Potassium."
    },

    # ==========================================================
    # RASPBERRY (Added to complete 38 classes)
    # ==========================================================
    "Raspberry___healthy": {
        "cause": "Healthy plant.",
        "symptoms": [
            "Healthy green leaves",
            "Normal cane development",
            "No signs of disease or pests"
        ],
        "chemical_treatment": [
            "No chemical treatment required."
        ],
        "organic_treatment": [
            "Maintain organic mulch around the base.",
            "Apply compost in spring."
        ],
        "prevention": [
            "Plant in well-draining soil.",
            "Prune dead canes annually.",
            "Ensure full sun exposure."
        ],
        "severity": "None",
        "weather": "Grows best in cool to moderate climates.",
        "irrigation": "Deep watering once a week; avoid overhead watering.",
        "fertilizer": "Balanced organic compost or 10-10-10 fertilizer in early spring."
    },

    # ==========================================================
    # SOYBEAN (Added to complete 38 classes)
    # ==========================================================
    "Soybean___healthy": {
        "cause": "Healthy plant.",
        "symptoms": [
            "Vibrant green leaves",
            "Strong stems",
            "Healthy pod development"
        ],
        "chemical_treatment": [
            "No chemical treatment required."
        ],
        "organic_treatment": [
            "Incorporate organic matter into soil."
        ],
        "prevention": [
            "Crop rotation with corn or wheat.",
            "Use certified seed.",
            "Monitor for pests regularly."
        ],
        "severity": "None",
        "weather": "Warm and sunny conditions.",
        "irrigation": "Adequate soil moisture, especially during flowering and pod fill.",
        "fertilizer": "Typically doesn't need nitrogen if nodules are active; apply phosphorus and potassium as needed."
    },

    # ==========================================================
    # SQUASH (Added to complete 38 classes)
    # ==========================================================
    "Squash___Powdery_mildew": {
        "cause": "Fungal disease caused by Podosphaera xanthii.",
        "symptoms": [
            "White or gray powdery spots on leaves and stems",
            "Leaves turning yellow and brown",
            "Premature leaf death",
            "Stunted fruit growth"
        ],
        "chemical_treatment": [
            "Apply sulfur or copper-based fungicides.",
            "Use systemic fungicides like Myclobutanil.",
            "Spray potassium bicarbonate."
        ],
        "organic_treatment": [
            "Spray neem oil.",
            "Apply a diluted milk spray (40% milk, 60% water).",
            "Remove and destroy heavily infected leaves."
        ],
        "prevention": [
            "Plant resistant squash varieties.",
            "Provide wide spacing for air circulation.",
            "Avoid overhead irrigation.",
            "Grow in full sun."
        ],
        "severity": "Medium",
        "weather": "Warm, dry days with high relative humidity at night.",
        "irrigation": "Drip irrigation to keep leaves dry.",
        "fertilizer": "Avoid excessive nitrogen, which promotes susceptible tender growth."
    },

    # ==========================================================
    # STRAWBERRY (Added to complete 38 classes)
    # ==========================================================
    "Strawberry___Leaf_scorch": {
        "cause": "Fungus Diplocarpon earlianum.",
        "symptoms": [
            "Purplish spots on leaves that turn brown",
            "Leaves look scorched and dry",
            "Dark lesions on runners and stems",
            "Reduced plant vigor"
        ],
        "chemical_treatment": [
            "Apply protective fungicides like Captan or Mancozeb.",
            "Spray copper-based fungicides before flowering."
        ],
        "organic_treatment": [
            "Prune and destroy infected leaves.",
            "Apply organic copper soap spray.",
            "Mulch to prevent spore splashing."
        ],
        "prevention": [
            "Plant certified disease-free runners.",
            "Keep beds weed-free.",
            "Ensure good drainage.",
            "Renew planting bed every few years."
        ],
        "severity": "Medium",
        "weather": "Warm, wet, and humid conditions promote spore release.",
        "irrigation": "Water early in the day so foliage dries quickly; use drip irrigation.",
        "fertilizer": "Balanced fertilizer; avoid late-spring nitrogen which makes foliage tender."
    },

    "Strawberry___healthy": {
        "cause": "Healthy plant.",
        "symptoms": [
            "Lush green leaves",
            "Healthy runners",
            "Bright red, firm berries"
        ],
        "chemical_treatment": [
            "No chemical treatment required."
        ],
        "organic_treatment": [
            "Apply straw mulch.",
            "Feed with compost tea."
        ],
        "prevention": [
            "Regular weeding.",
            "Remove old leaves.",
            "Rotate crop site every 3-4 years."
        ],
        "severity": "None",
        "weather": "Cool to moderate sunny weather.",
        "irrigation": "Maintain consistent moisture, especially during fruit set.",
        "fertilizer": "Balanced organic fertilizer in early spring and post-harvest."
    },

    # ==========================================================
    # TOMATO
    # ==========================================================
    "Tomato___Bacterial_spot": {
        "cause": "Bacterial disease caused by Xanthomonas spp.",
        "symptoms": [
            "Small dark leaf spots",
            "Yellow halos around lesions",
            "Leaf drop",
            "Raised spots on fruits"
        ],
        "chemical_treatment": [
            "Spray Copper Hydroxide.",
            "Apply Copper + Mancozeb.",
            "Use bactericides as recommended."
        ],
        "organic_treatment": [
            "Neem oil spray.",
            "Copper soap.",
            "Remove infected leaves."
        ],
        "prevention": [
            "Use certified seeds.",
            "Practice crop rotation.",
            "Avoid overhead irrigation.",
            "Disinfect tools."
        ],
        "severity": "High",
        "weather": "Warm (24–30°C) with high humidity.",
        "irrigation": "Use drip irrigation.",
        "fertilizer": "Balanced NPK with Calcium."
    },

    "Tomato___Early_blight": {
        "cause": "Fungus Alternaria solani.",
        "symptoms": [
            "Brown concentric ring lesions",
            "Yellow leaves",
            "Lower leaves affected first",
            "Leaf drop"
        ],
        "chemical_treatment": [
            "Apply Chlorothalonil.",
            "Spray Mancozeb.",
            "Use Azoxystrobin."
        ],
        "organic_treatment": [
            "Neem oil.",
            "Copper fungicide.",
            "Compost tea."
        ],
        "prevention": [
            "Crop rotation.",
            "Remove infected debris.",
            "Improve air circulation."
        ],
        "severity": "Medium",
        "weather": "Warm humid weather.",
        "irrigation": "Avoid wet foliage.",
        "fertilizer": "Potassium-rich fertilizer."
    },

    "Tomato___Late_blight": {
        "cause": "Phytophthora infestans.",
        "symptoms": [
            "Large water-soaked lesions",
            "White fungal growth",
            "Rapid leaf death",
            "Fruit rot"
        ],
        "chemical_treatment": [
            "Metalaxyl.",
            "Cymoxanil.",
            "Mancozeb."
        ],
        "organic_treatment": [
            "Copper fungicide.",
            "Destroy infected plants.",
            "Improve field ventilation."
        ],
        "prevention": [
            "Use resistant varieties.",
            "Avoid excess irrigation.",
            "Maintain proper spacing."
        ],
        "severity": "Very High",
        "weather": "Cool wet weather (15–22°C).",
        "irrigation": "Drip irrigation recommended.",
        "fertilizer": "Balanced fertilizer with potassium."
    },

    "Tomato___Leaf_Mold": {
        "cause": "Fungus Passalora fulva.",
        "symptoms": [
            "Yellow leaf spots",
            "Olive-green mold underneath leaves",
            "Leaf curling",
            "Premature leaf drop"
        ],
        "chemical_treatment": [
            "Apply Chlorothalonil.",
            "Spray Copper fungicide.",
            "Use Mancozeb."
        ],
        "organic_treatment": [
            "Neem oil.",
            "Increase ventilation.",
            "Remove infected leaves."
        ],
        "prevention": [
            "Reduce greenhouse humidity.",
            "Improve air circulation.",
            "Avoid overhead watering."
        ],
        "severity": "Medium",
        "weather": "High humidity (>85%).",
        "irrigation": "Water at soil level.",
        "fertilizer": "Balanced NPK."
    },

    "Tomato___Septoria_leaf_spot": {
        "cause": "Fungus Septoria lycopersici.",
        "symptoms": [
            "Small circular spots",
            "Gray centers",
            "Black fungal dots",
            "Lower leaves die first"
        ],
        "chemical_treatment": [
            "Apply Mancozeb.",
            "Copper fungicide.",
            "Chlorothalonil."
        ],
        "organic_treatment": [
            "Neem oil.",
            "Remove infected leaves.",
            "Mulch around plants."
        ],
        "prevention": [
            "Crop rotation.",
            "Avoid splashing water.",
            "Destroy infected debris."
        ],
        "severity": "Medium",
        "weather": "Warm humid weather.",
        "irrigation": "Use drip irrigation.",
        "fertilizer": "Balanced fertilizer."
    },

    "Tomato___Spider_mites": {
        "cause": "Infestation by Two-spotted spider mites.",
        "symptoms": [
            "Tiny yellow speckles",
            "Fine webbing",
            "Leaf bronzing",
            "Leaf drop"
        ],
        "chemical_treatment": [
            "Apply Abamectin.",
            "Use Spiromesifen.",
            "Use approved miticides."
        ],
        "organic_treatment": [
            "Neem oil.",
            "Insecticidal soap.",
            "Release predatory mites."
        ],
        "prevention": [
            "Maintain humidity.",
            "Inspect leaf undersides.",
            "Avoid dusty conditions."
        ],
        "severity": "Medium",
        "weather": "Hot dry weather.",
        "irrigation": "Maintain adequate moisture.",
        "fertilizer": "Balanced nutrition."
    },

    "Tomato___Target_Spot": {
        "cause": "Fungus Corynespora cassiicola.",
        "symptoms": [
            "Brown circular spots",
            "Yellow leaf margins",
            "Fruit lesions",
            "Leaf drop"
        ],
        "chemical_treatment": [
            "Apply Azoxystrobin.",
            "Use Mancozeb.",
            "Copper fungicide."
        ],
        "organic_treatment": [
            "Neem oil.",
            "Remove infected foliage."
        ],
        "prevention": [
            "Crop rotation.",
            "Field sanitation.",
            "Proper plant spacing."
        ],
        "severity": "Medium",
        "weather": "Warm humid conditions.",
        "irrigation": "Avoid wet leaves.",
        "fertilizer": "Balanced NPK."
    },

    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "cause": "Tomato Yellow Leaf Curl Virus transmitted by whiteflies.",
        "symptoms": [
            "Yellow curled leaves",
            "Stunted growth",
            "Flower drop",
            "Poor fruit production"
        ],
        "chemical_treatment": [
            "Control whiteflies using Imidacloprid.",
            "Use insecticides as recommended."
        ],
        "organic_treatment": [
            "Neem oil spray.",
            "Yellow sticky traps.",
            "Remove infected plants."
        ],
        "prevention": [
            "Use resistant varieties.",
            "Control whiteflies.",
            "Use insect-proof netting."
        ],
        "severity": "Very High",
        "weather": "Warm tropical climate.",
        "irrigation": "Normal irrigation.",
        "fertilizer": "Balanced fertilizer with micronutrients."
    },

    "Tomato___Tomato_mosaic_virus": {
        "cause": "Tomato Mosaic Virus (ToMV).",
        "symptoms": [
            "Mosaic leaf pattern",
            "Leaf curling",
            "Stunted growth",
            "Reduced fruit quality"
        ],
        "chemical_treatment": [
            "No chemical cure available."
        ],
        "organic_treatment": [
            "Remove infected plants.",
            "Disinfect gardening tools.",
            "Control weeds."
        ],
        "prevention": [
            "Use virus-free seeds.",
            "Resistant cultivars.",
            "Wash hands before handling plants."
        ],
        "severity": "High",
        "weather": "Spreads under all weather conditions.",
        "irrigation": "Normal irrigation.",
        "fertilizer": "Balanced fertilizer."
    },

    "Tomato___healthy": {
        "cause": "Healthy tomato plant.",
        "symptoms": [
            "Healthy green leaves",
            "Strong stem",
            "Normal flowering",
            "Healthy fruits"
        ],
        "chemical_treatment": [
            "No treatment required."
        ],
        "organic_treatment": [
            "Apply compost.",
            "Use organic mulch."
        ],
        "prevention": [
            "Regular monitoring.",
            "Proper pruning.",
            "Balanced fertilization.",
            "Maintain irrigation schedule."
        ],
        "severity": "None",
        "weather": "Optimal growth at 20–28°C.",
        "irrigation": "Keep soil consistently moist.",
        "fertilizer": "Balanced tomato fertilizer rich in potassium and calcium."
    }
}

CLASS_NAMES = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Blueberry___healthy",
    "Cherry___Powdery_mildew",
    "Cherry___healthy",
    "Corn___Cercospora_leaf_spot",
    "Corn___Common_rust",
    "Corn___Northern_Leaf_Blight",
    "Corn___healthy",
    "Grape___Black_rot",
    "Grape___Esca",
    "Grape___Leaf_blight",
    "Grape___healthy",
    "Orange___Citrus_greening",
    "Peach___Bacterial_spot",
    "Peach___healthy",
    "Pepper___Bacterial_spot",
    "Pepper___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Raspberry___healthy",
    "Soybean___healthy",
    "Squash___Powdery_mildew",
    "Strawberry___Leaf_scorch",
    "Strawberry___healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy"
]
