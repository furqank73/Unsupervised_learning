import streamlit as st
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

# --- Load the model ---
@st.cache_resource
def load_model():
    with open('models.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

# --- Cluster Metadata ---
CLUSTER_INFO = {
    0: {"Income": "Medium", "Spending": "Medium", "Profile": "Balanced shoppers", "Strategy": "Cross-selling opportunities", "color": "#4e79a7"},
    1: {"Income": "High", "Spending": "High", "Profile": "Premium customers", "Strategy": "Retention and loyalty programs", "color": "#f28e2b"},
    2: {"Income": "Low", "Spending": "High", "Profile": "Impulse buyers", "Strategy": "Targeted promotions", "color": "#e15759"},
    3: {"Income": "Low", "Spending": "Low", "Profile": "Value-conscious", "Strategy": "Cost-effective offerings", "color": "#76b7b2"},
    4: {"Income": "High", "Spending": "Low", "Profile": "Selective buyers", "Strategy": "Conversion strategies", "color": "#59a14f"},
}

# --- Manual Scaler Setup (based on training data) ---
scaler = StandardScaler()
scaler.mean_ = np.array([40.0, 50.0])  # Replace with real training means
scaler.scale_ = np.array([20.0, 25.0])  # Replace with real training std devs

# --- Streamlit Page Configuration ---
st.set_page_config(page_title="Customer Segmentation", layout="wide")

# --- Header ---
st.markdown("""
    <h1 style='color:#4e79a7;'>Customer Segmentation Dashboard</h1>
    <p style='font-size:16px;'>Use income and spending behavior to identify customer segments and enhance marketing strategies.</p>
""", unsafe_allow_html=True)

# --- Layout: 3-Column Format ---
col_input, col_output, col_info = st.columns([1, 1.5, 1.5])

# --- Input Column ---
with col_input:
    st.subheader("Customer Input")
    income = st.slider("Annual Income (k$)", 0, 200, 40)
    spending = st.slider("Spending Score (1-100)", 0, 100, 50)

    if st.button("Predict Segment", type="primary", use_container_width=True):
        sample = np.array([[income, spending]])
        sample_scaled = scaler.transform(sample)
        kmeans = load_model()
        cluster_id = kmeans.predict(sample_scaled)[0]
        st.session_state.prediction = {
            "cluster": cluster_id,
            "income": income,
            "score": spending,
            "info": CLUSTER_INFO[cluster_id]
        }

# --- Output Column ---
with col_output:
    if "prediction" in st.session_state:
        pred = st.session_state.prediction
        st.subheader("Segmentation Result")

        st.markdown(f"""
        <div style="background-color:{pred['info']['color']}20; padding:20px; border-radius:10px; border-left:6px solid {pred['info']['color']}; margin-bottom:20px;">
            <h2 style="color:{pred['info']['color']}; margin-top:0;">Segment {pred['cluster']}: {pred['info']['Profile']}</h2>
            <p><b>Annual Income:</b> {pred['income']}k$<br>
               <b>Spending Score:</b> {pred['score']}/100<br>
               <b>Income Level:</b> {pred['info']['Income']}<br>
               <b>Spending Level:</b> {pred['info']['Spending']}</p>
        </div>
        """, unsafe_allow_html=True)

        st.subheader("Recommended Strategy")
        st.info(f"**{pred['info']['Strategy']}**")

        with st.expander("Segment Insights"):
            st.write(f"""
            **{pred['info']['Profile']} Characteristics:**
            - {pred['info']['Income']} income level
            - {pred['info']['Spending']} spending behavior
            - Respond well to {pred['info']['Strategy'].split()[0].lower()} strategies
            
            **Marketing Tips:**
            - Focus on {pred['info']['Strategy'].split()[0].lower()} campaigns
            - Customize offers to match this profile
            - Track behavioral changes regularly
            """)

# --- Info Column: Cluster Definitions ---
with col_info:
    st.subheader("Segment Definitions")
    for cluster_id, info in CLUSTER_INFO.items():
        st.markdown(f"""
        <div style="background-color:{info['color']}20; padding:12px; border-radius:8px; border-left:5px solid {info['color']}; margin-bottom:12px;">
            <h4 style="color:{info['color']}; margin-top:0;">Segment {cluster_id}: {info['Profile']}</h4>
            <p><b>Income:</b> {info['Income']}<br>
               <b>Spending:</b> {info['Spending']}<br>
               <b>Strategy:</b> {info['Strategy']}</p>
        </div>
        """, unsafe_allow_html=True)

# --- Footer ---
st.markdown("""---""")
st.caption("Customer Segmentation App • Built with Streamlit • v1.0")
