# app.py
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Page configuration
st.set_page_config(
    page_title="Mobile Price Predictor",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .main-header h1 {
        color: white;
        margin: 0;
        font-size: 2.5rem;
    }
    .main-header p {
        color: #f0f0f0;
        margin: 0.5rem 0 0 0;
        font-size: 1.2rem;
    }
    .input-section {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 4px solid #667eea;
    }
    .section-title {
        color: #333;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #667eea;
    }
    .prediction-result {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-top: 2rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        width: 100%;
        margin-top: 1rem;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Load model and scaler
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

@st.cache_resource
def load_scaler():
    with open("scaler.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()
scaler = load_scaler()

# Header
st.markdown("""
<div class="main-header">
    <h1>📱 Mobile Phone Price Predictor</h1>
    <p>Get instant price range predictions based on phone specifications</p>
</div>
""", unsafe_allow_html=True)

# Create three columns for better layout
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="input-section"><div class="section-title">📋 Basic Specifications</div>', unsafe_allow_html=True)
    battery_power = st.number_input("🔋 Battery Power (mAh)", min_value=500, max_value=6000, step=50, value=1500)
    clock_speed = st.number_input("⚡ Clock Speed (GHz)", min_value=0.5, max_value=3.0, step=0.1, value=1.5)
    ram = st.number_input("💾 RAM (MB)", min_value=256, max_value=16000, step=256, value=4000)
    int_memory = st.number_input("💿 Internal Memory (GB)", min_value=2, max_value=512, step=1, value=64)
    n_cores = st.number_input("🖥️ Processor Cores", min_value=1, max_value=8, step=1, value=4)
    mobile_wt = st.number_input("⚖️ Mobile Weight (g)", min_value=50, max_value=300, step=1, value=150)
    m_dep = st.number_input("📏 Mobile Depth (cm)", min_value=0.1, max_value=1.0, step=0.01, value=0.8)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="input-section"><div class="section-title">📸 Camera & Display</div>', unsafe_allow_html=True)
    pc = st.number_input("📷 Primary Camera (MP)", min_value=0, max_value=32, step=1, value=12)
    fc = st.number_input("🤳 Front Camera (MP)", min_value=0, max_value=20, step=1, value=5)
    px_height = st.number_input("📐 Pixel Height", min_value=0, max_value=3000, step=10, value=1200)
    px_width = st.number_input("📐 Pixel Width", min_value=0, max_value=3000, step=10, value=800)
    sc_h = st.number_input("📱 Screen Height (cm)", min_value=5, max_value=25, step=1, value=15)
    sc_w = st.number_input("📱 Screen Width (cm)", min_value=2, max_value=15, step=1, value=8)
    talk_time = st.number_input("📞 Talk Time (hours)", min_value=2, max_value=30, step=1, value=10)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="input-section"><div class="section-title">🔗 Connectivity Features</div>', unsafe_allow_html=True)
    blue = st.selectbox("🔵 Bluetooth", [0, 1], format_func=lambda x: "✅ Yes" if x == 1 else "❌ No", index=1)
    wifi = st.selectbox("📶 WiFi", [0, 1], format_func=lambda x: "✅ Yes" if x == 1 else "❌ No", index=1)
    four_g = st.selectbox("📡 4G Support", [0, 1], format_func=lambda x: "✅ Yes" if x == 1 else "❌ No", index=1)
    three_g = st.selectbox("📡 3G Support", [0, 1], format_func=lambda x: "✅ Yes" if x == 1 else "❌ No", index=1)
    dual_sim = st.selectbox("📋 Dual SIM", [0, 1], format_func=lambda x: "✅ Yes" if x == 1 else "❌ No", index=0)
    touch_screen = st.selectbox("👆 Touch Screen", [0, 1], format_func=lambda x: "✅ Yes" if x == 1 else "❌ No", index=1)
    st.markdown('</div>', unsafe_allow_html=True)

# Prediction section
st.markdown("<br>", unsafe_allow_html=True)
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])

with col_btn2:
    if st.button("🔮 Predict Price Range", key="predict_btn"):
        # Create input array
        input_data = np.array([[battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory,
                                m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram,
                                sc_h, sc_w, talk_time, three_g, touch_screen, wifi]])
        
        # Make prediction
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)[0]
        
        # Define price ranges with colors and details
        price_dict = {
            0: ("💚 Low Cost", "$0 - $150", "Perfect for basic usage", "#28a745"),
            1: ("💙 Medium Cost", "$151 - $400", "Great balance of features and price", "#007bff"),
            2: ("💜 High Cost", "$401 - $800", "Premium features and performance", "#6f42c1"),
            3: ("🧡 Very High Cost", "$801+", "Flagship with cutting-edge technology", "#fd7e14")
        }
        
        category, price_range, description, color = price_dict[prediction]
        
        # Display result with enhanced styling
        st.markdown(f"""
        <div class="prediction-result">
            <h2 style="margin: 0; font-size: 2rem;">{category}</h2>
            <h3 style="margin: 0.5rem 0; font-size: 1.5rem; opacity: 0.9;">{price_range}</h3>
            <p style="margin: 0; font-size: 1.1rem; opacity: 0.8;">{description}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Additional insights
        st.markdown("### 📊 Specification Summary")
        col_summary1, col_summary2 = st.columns(2)
        
        with col_summary1:
            st.info(f"""
            **Performance Score:**
            - RAM: {ram} MB
            - Processor: {n_cores} cores @ {clock_speed} GHz
            - Storage: {int_memory} GB
            """)
            
        with col_summary2:
            st.info(f"""
            **Camera & Display:**
            - Primary Camera: {pc} MP
            - Front Camera: {fc} MP
            - Resolution: {px_width} x {px_height}
            """)
