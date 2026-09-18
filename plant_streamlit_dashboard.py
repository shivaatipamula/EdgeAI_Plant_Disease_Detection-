import streamlit as st
import numpy as np
import cv2
import time
import os
from PIL import Image
import io

# Import local database
try:
    from disease_info import DISEASE_INFO, CLASS_NAMES
except ImportError:
    st.error("Error: Could not import disease_info.py. Make sure it is in the same directory.")

# Page config
st.set_page_config(
    page_title="SmartCrop Leaf Diagnostics",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom premium CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    .main-title {
        color: #1e5631;
        font-weight: 700;
        font-size: 2.8rem;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        color: #4c9a2a;
        font-weight: 400;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255, 255, 255, 0.85) !important;
        border: 1px solid rgba(224, 242, 225, 1) !important;
        border-radius: 16px !important;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.05) !important;
        backdrop-filter: blur(4px) !important;
        -webkit-backdrop-filter: blur(4px) !important;
        margin-bottom: 20px !important;
    }
    div[data-testid="stVerticalBlockBorderWrapper"] > div {
        padding: 24px !important;
    }
    .metric-card {
        background: #f4fbf7;
        border: 1px solid #d0f0db;
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        transition: transform 0.2s ease-in-out;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
    }
    .metric-val {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1b5e20;
        margin: 5px 0;
    }
    .metric-lbl {
        font-size: 0.85rem;
        font-weight: 600;
        color: #666;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .badge {
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        display: inline-block;
        color: white;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .badge-none { background-color: #2e7d32; }
    .badge-low { background-color: #1565c0; }
    .badge-medium { background-color: #ef6c00; }
    .badge-high { background-color: #c62828; }
    .badge-veryhigh { background-color: #4e0d0d; }
    
    /* Custom tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #f1f8f3;
        border-radius: 8px 8px 0 0;
        padding: 10px 18px;
        color: #2e7d32;
        font-weight: 600;
        border: 1px solid #e0f2e1;
        border-bottom: none;
    }
    .stTabs [aria-selected="true"] {
        background-color: #2e7d32 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Helper function to load model
@st.cache_resource
def load_model(model_path):
    try:
        import ai_edge_litert.interpreter as litert
        interpreter = litert.Interpreter(model_path=model_path)
    except ImportError:
        try:
            import tflite_runtime.interpreter as tflite
            interpreter = tflite.Interpreter(model_path=model_path)
        except ImportError:
            import tensorflow as tf
            interpreter = tf.lite.Interpreter(model_path=model_path)
            
    interpreter.allocate_tensors()
    return interpreter

# Path setup
MODEL_PATH = "plant_disease_model_quant.tflite"

# Ensure model exists in local workspace
if not os.path.exists(MODEL_PATH):
    # Fallback search path
    alternative_path = "C:/Users/shiva/Downloads/plant_disease_model_quant.tflite"
    if os.path.exists(alternative_path):
        MODEL_PATH = alternative_path

# Main Logic
st.markdown("<h1 class='main-title'>🌿 SmartCrop Leaf Diagnostics</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>TensorFlow Lite powered real-time plant disease diagnostic suite for sustainable farming.</p>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/color/144/sprout.png", width=80)
    st.markdown("## Diagnostic Dashboard")
    st.markdown("Identify crop infections, assess severity, and instantly discover organic & chemical treatment options.")
    
    st.markdown("---")
    st.markdown("### 🤖 Model Info")
    st.info(
        f"**Engine**: TensorFlow Lite\n\n"
        f"**Model File**: `plant_disease_model_quant.tflite`\n\n"
        f"**Classes**: 38 Categories\n\n"
        f"**Input Size**: 224 x 224 x 3\n\n"
        f"**Dtype**: float32"
    )
    
    st.markdown("### 🛠️ Technology Stack")
    st.markdown(
        "- **Framework**: Streamlit\n"
        "- **Inference**: LiteRT (`ai-edge-litert`)\n"
        "- **Computer Vision**: OpenCV, Pillow\n"
        "- **Diagnostics**: Custom Expert Database"
    )
    
    st.markdown("---")
    st.markdown("<small>© 2026 SmartBridge </small>", unsafe_allow_html=True)

# Main layout split into two columns: Left for Upload/Input, Right for Diagnostic results
col1, col2 = st.columns([1, 1], gap="large")

# State variable to hold prediction result
prediction_ready = False

with col1:
    with st.container(border=True):
        st.subheader("📤 Crop Leaf Image Upload")
        
        # Drag-and-drop file uploader
        uploaded_file = st.file_uploader(
            "Drag and drop or select an image of a plant leaf (supported format: JPG, JPEG, PNG)",
            type=["jpg", "jpeg", "png"]
        )
        
        if uploaded_file is not None:
            # Display uploaded image beautifully
            image = Image.open(uploaded_file).convert("RGB")
            st.image(image, caption="Uploaded Leaf Image", use_container_width=True)
            
            # Run diagnostics button
            run_btn = st.button("🔍 Run Instant Diagnostic", type="primary", use_container_width=True)
        else:
            st.info("Please upload a leaf image to begin diagnostic analysis.")
            run_btn = False

# Action on button press
if (uploaded_file is not None) and (run_btn or "last_uploaded" not in st.session_state or st.session_state.last_uploaded != uploaded_file.name):
    # Store filename in session state to avoid running on every reload
    st.session_state.last_uploaded = uploaded_file.name
    
    with st.spinner("Analyzing leaf with TensorFlow Lite inference engine..."):
        try:
            # Load model
            interpreter = load_model(MODEL_PATH)
            input_details = interpreter.get_input_details()
            output_details = interpreter.get_output_details()
            
            # Start timer
            start_time = time.time()
            
            # Image Preprocessing
            img_resized = image.resize((224, 224))
            img_array = np.array(img_resized, dtype=np.float32) / 255.0
            input_data = np.expand_dims(img_array, axis=0)
            
            # Set tensor and run inference
            interpreter.set_tensor(input_details[0]['index'], input_data)
            interpreter.invoke()
            
            # Get outputs
            output_data = interpreter.get_tensor(output_details[0]['index'])[0]
            
            # Argmax
            class_id = np.argmax(output_data)
            confidence = output_data[class_id]
            
            # Latency
            latency = (time.time() - start_time) * 1000
            
            # Result class name
            predicted_class = CLASS_NAMES[class_id]
            
            # Store in session state
            st.session_state.prediction = {
                "class": predicted_class,
                "confidence": confidence,
                "latency": latency,
                "image": image,
                "class_id": class_id
            }
            prediction_ready = True
            
        except Exception as e:
            st.error(f"Inference Error: {e}")
            st.info("Please verify that the TFLite model exists at path: " + MODEL_PATH)

# Check if prediction is already stored in session state
if "prediction" in st.session_state:
    prediction_ready = True

with col2:
    if prediction_ready:
        pred_data = st.session_state.prediction
        predicted_label = pred_data["class"]
        confidence = pred_data["confidence"]
        latency = pred_data["latency"]
        image = pred_data["image"]
        
        info = DISEASE_INFO.get(predicted_label, {})
        
        with st.container(border=True):
            st.subheader("📊 Analysis Output")
            
            # Display metric cards side by side
            m_col1, m_col2 = st.columns(2)
            with m_col1:
                st.markdown(
                    f"<div class='metric-card'>"
                    f"<div class='metric-lbl'>Prediction Confidence</div>"
                    f"<div class='metric-val'>{confidence:.2%}</div>"
                    f"</div>",
                    unsafe_allow_html=True
                )
            with m_col2:
                st.markdown(
                    f"<div class='metric-card'>"
                    f"<div class='metric-lbl'>Inference Latency</div>"
                    f"<div class='metric-val'>{latency:.2f} ms</div>"
                    f"</div>",
                    unsafe_allow_html=True
                )
                
            st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
            
            # Formatted Display Name
            clean_name = predicted_label.replace("___", " — ").replace("_", " ")
            st.markdown(f"### Diagnosis: **{clean_name}**")
            
            # Severity Badge
            severity = info.get("severity", "None")
            badge_class = f"badge-{severity.lower().replace(' ', '')}"
            st.markdown(f"Severity: <span class='badge {badge_class}'>{severity}</span>", unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Tabs for details
            tab_titles = [
                "📋 Overview", 
                "🦠 Cause", 
                "🔍 Symptoms", 
                "💊 Chemical Treatment", 
                "🌿 Organic Treatment", 
                "🌱 Prevention", 
                "🌦️ Weather", 
                "💧 Irrigation", 
                "🌾 Fertilizer"
            ]
            tabs = st.tabs(tab_titles)
            
            with tabs[0]:
                st.markdown("#### Disease Overview")
                if "healthy" in predicted_label.lower():
                    st.success("The analyzed leaf appears to be healthy and shows no visible signs of infection.")
                    st.write("Ensure regular crop scouting and maintenance as preventative measures.")
                else:
                    st.warning(f"An infection of **{clean_name}** has been diagnosed on the plant leaf.")
                    st.write(f"This leaf shows patterns consistent with {info.get('cause', 'unknown causes')}. Please refer to the treatment tabs for management options.")
            
            with tabs[1]:
                st.markdown("#### Primary Cause")
                st.markdown(f"**Description**: {info.get('cause', 'N/A')}")
                
            with tabs[2]:
                st.markdown("#### Symptoms")
                symptoms = info.get("symptoms", [])
                if symptoms:
                    for sym in symptoms:
                        st.markdown(f"- {sym}")
                else:
                    st.write("No specific symptoms logged.")
                    
            with tabs[3]:
                st.markdown("#### Chemical Treatment Options 💊")
                chem = info.get("chemical_treatment", [])
                if chem:
                    for c in chem:
                        st.markdown(f"- {c}")
                else:
                    st.write("No chemical treatment necessary or listed.")
                    
            with tabs[4]:
                st.markdown("#### Organic Treatment Options 🌿")
                org = info.get("organic_treatment", [])
                if org:
                    for o in org:
                        st.markdown(f"- {o}")
                else:
                    st.write("No organic treatment necessary or listed.")
                    
            with tabs[5]:
                st.markdown("#### Prevention Guidelines 🌱")
                prev = info.get("prevention", [])
                if prev:
                    for p in prev:
                        st.markdown(f"- {p}")
                else:
                    st.write("No prevention guidelines listed.")
                    
            with tabs[6]:
                st.markdown("#### Favorable Weather Conditions 🌦️")
                st.markdown(f"{info.get('weather', 'N/A')}")
                
            with tabs[7]:
                st.markdown("#### Irrigation Recommendations 💧")
                st.markdown(f"{info.get('irrigation', 'N/A')}")
                
            with tabs[8]:
                st.markdown("#### Recommended Fertilization 🌾")
                st.markdown(f"{info.get('fertilizer', 'N/A')}")
        
        # Download Section
        with st.container(border=True):
            st.subheader("📥 Export Diagnostics & Report")
            
            down_col1, down_col2 = st.columns(2)
            
            # 1. Annotated Image generation
            with down_col1:
                try:
                    # Convert PIL image to cv2
                    cv_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                    h, w, _ = cv_img.shape
                    
                    # Dynamic banner based on image size
                    banner_h = int(h * 0.12) if h > 300 else 40
                    overlay = cv_img.copy()
                    
                    # Select banner color based on severity
                    banner_color = (46, 125, 50)  # Green for None
                    if severity == "Low":
                        banner_color = (192, 101, 21) # Blue (BGR format: 21, 101, 192)
                    elif severity == "Medium":
                        banner_color = (0, 108, 239)  # Orange (BGR format: 0, 108, 239)
                    elif severity == "High":
                        banner_color = (40, 40, 198)  # Red (BGR: 40, 40, 198)
                    elif severity == "Very High":
                        banner_color = (13, 13, 78)   # Dark Red (BGR: 13, 13, 78)
                        
                    cv2.rectangle(overlay, (0, h - banner_h), (w, h), banner_color, -1)
                    cv2.addWeighted(overlay, 0.7, cv_img, 0.3, 0, cv_img)
                    
                    # Text overlay
                    display_label = predicted_label.replace("___", " — ").replace("_", " ")
                    text = f"{display_label} ({confidence:.1%})"
                    font_scale = max(0.4, w / 700.0)
                    thickness = max(1, int(w / 500.0))
                    
                    (t_w, t_h), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
                    tx = int((w - t_w) / 2)
                    ty = int(h - (banner_h - t_h) / 2)
                    
                    cv2.putText(cv_img, text, (tx, ty), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)
                    
                    # Convert back to bytes
                    is_success, buffer = cv2.imencode(".png", cv_img)
                    io_buf = io.BytesIO(buffer)
                    
                    st.download_button(
                        label="🖼️ Download Annotated Image",
                        data=io_buf.getvalue(),
                        file_name=f"diagnosed_{predicted_label.lower()}.png",
                        mime="image/png",
                        use_container_width=True
                    )
                except Exception as ex:
                    st.error(f"Could not generate annotated image: {ex}")
                    
            # 2. Text Diagnosis Report generation
            with down_col2:
                try:
                    report_content = f"""==================================================
              SMARTCROP DIAGNOSTIC REPORT
==================================================
Date generated      : {time.strftime('%Y-%m-%d %H:%M:%S')}
Crop & Disease Class: {clean_name}
Severity Rating     : {severity}
Model Confidence    : {confidence:.2%}
Inference Latency   : {latency:.2f} ms
--------------------------------------------------

1. PRIMARY CAUSE:
   {info.get('cause', 'N/A')}

2. CLINICAL SYMPTOMS:
"""
                    for sym in info.get("symptoms", []):
                        report_content += f"   - {sym}\n"
                        
                    report_content += "\n3. ORGANIC TREATMENT MANAGEMENT:\n"
                    for org_tr in info.get("organic_treatment", []):
                        report_content += f"   - {org_tr}\n"
                        
                    report_content += "\n4. CHEMICAL TREATMENT MANAGEMENT:\n"
                    for chem_tr in info.get("chemical_treatment", []):
                        report_content += f"   - {chem_tr}\n"
                        
                    report_content += "\n5. PREVENTION PROTOCOLS:\n"
                    for prev_pr in info.get("prevention", []):
                        report_content += f"   - {prev_pr}\n"
                        
                    report_content += f"""
6. AGRO-METEOROLOGICAL & IRRIGATION ADVISORY:
   - Weather   : {info.get('weather', 'N/A')}
   - Irrigation: {info.get('irrigation', 'N/A')}
   - Fertilizer: {info.get('fertilizer', 'N/A')}
--------------------------------------------------
Report compiled automatically by SmartCrop Edge AI.
=================================================="""

                    st.download_button(
                        label="📄 Download Diagnosis Report",
                        data=report_content,
                        file_name=f"diagnostic_report_{predicted_label.lower()}.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                except Exception as ex:
                    st.error(f"Could not generate text report: {ex}")
        
    else:
        # Display instructions if no image is run
        st.info("👈 Upload leaf photo and click 'Run Instant Diagnostic' to view results.")
