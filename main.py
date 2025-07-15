import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestClassifier
from PIL import Image
import io

# Set page configuration
st.set_page_config(page_title="AgriEmpower: Smart Farming Solutions", layout="wide")

# Mock data for crop monitoring
def generate_crop_data():
    dates = [datetime.now() - timedelta(days=x) for x in range(30)]
    data = {
        "Date": dates,
        "Soil_Moisture (%)": np.random.uniform(20, 80, 30),
        "Crop_Health_Score": np.random.uniform(50, 100, 30),
        "Pest_Risk (%)": np.random.uniform(5, 40, 30),
        "Region": ["North", "South", "East", "West"] * 7 + ["North", "South"]
    }
    return pd.DataFrame(data)

# Mock data for soil prediction
def generate_soil_data():
    data = {
        "Soil_Moisture": np.random.uniform(20, 80, 100),
        "pH": np.random.uniform(5.5, 7.5, 100),
        "Nitrogen": np.random.uniform(10, 50, 100),
        "Phosphorus": np.random.uniform(5, 30, 100),
        "Potassium": np.random.uniform(10, 40, 100),
        "Fertility": np.random.choice(["Low", "Medium", "High"], 100)
    }
    return pd.DataFrame(data)

# Mock soil fertility prediction model
def train_soil_model():
    soil_data = generate_soil_data()
    X = soil_data[["Soil_Moisture", "pH", "Nitrogen", "Phosphorus", "Potassium"]]
    y = soil_data["Fertility"]
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)
    return model

# Mock crop image analysis
def analyze_crop_image(image):
    # Placeholder logic for crop condition (simulating ML model)
    # In a real app, this would use a trained CNN model
    pixel_data = np.array(image.convert("RGB"))
    brightness = pixel_data.mean()
    if brightness > 150:
        return "Healthy", "Crop appears vibrant and well-maintained."
    elif brightness > 100:
        return "Stressed", "Crop shows signs of stress, possibly due to water or nutrient deficiency."
    else:
        return "Failure", "Crop shows severe damage, likely due to pests or disease."

# Mock data for government schemes
schemes_data = {
    "Scheme_Name": ["PM-KISAN", "Crop Insurance", "Soil Health Card", "Kisan Credit Card"],
    "Description": [
        "Income support of ₹6,000 per year for farmers",
        "Insurance coverage for crop failure due to natural calamities",
        "Free soil testing and nutrient recommendations",
        "Low-interest credit for farming needs"
    ],
    "Eligibility": [
        "Small and marginal farmers",
        "All farmers growing notified crops",
        "All farmers",
        "Farmers aged 18-75"
    ],
    "Apply_Link": [
        "https://pmkisan.gov.in",
        "https://pmfby.gov.in",
        "https://soilhealth.dac.gov.in",
        "https://www.kisancard.in"
    ]
}

# Mock data for mental health resources
mental_health_resources = {
    "Resource_Name": ["Kisan Helpline", "Mental Health NGO", "Community Support Group"],
    "Contact": ["1800-123-4567", "contact@ngo.org", "localgroup@community.in"],
    "Description": [
        "24/7 helpline for farmer distress",
        "Counseling and support for farmers",
        "Local meetups for peer support"
    ]
}

# App Header
st.title("🌾 AgriEmpower: Empowering Farmers for a Sustainable Future")
st.markdown("""
Welcome to **AgriEmpower**, a platform designed to support farmers with real-time crop monitoring, 
access to government schemes, mental health resources, and community-driven solutions.
""")

# Sidebar for navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Home", "Crop Monitoring", "Government Schemes", "Mental Health Support", "Community Reporting"])

# Home Section
if section == "Home":
    st.header("Empowering Agriculture")
    st.markdown("""
    AgriEmpower bridges the gap between technology and farming communities. Explore features like:
    - **Real-time Crop Monitoring**: AI-driven insights from satellite and soil data.
    - **Government Schemes**: Access subsidies and support programs.
    - **Mental Health Support**: Resources to address farmer distress.
    - **Community Reporting**: Share and track local agricultural challenges.
    """)
    st.image(r"img/p.png", caption="Supporting resilient farming communities")

# Crop Monitoring Section
elif section == "Crop Monitoring":
    st.header("📊 Real-Time Crop Monitoring")
    st.markdown("Monitor soil, crops, and pest risks with AI-driven insights and satellite imagery.")
    
    # Tabs for different monitoring features
    tab1, tab2, tab3, tab4 = st.tabs(["Soil Analysis", "Crop Trends", "Satellite View", "Crop Image Analysis"])
    
    # Tab 1: Soil Analysis
    with tab1:
        st.subheader("Soil Fertility Prediction")
        st.markdown("Enter soil parameters to predict fertility.")
        model = train_soil_model()
        
        with st.form("soil_form"):
            moisture = st.slider("Soil Moisture (%)", 20.0, 80.0, 50.0)
            ph = st.slider("pH", 5.5, 7.5, 6.5)
            nitrogen = st.slider("Nitrogen (ppm)", 10.0, 50.0, 30.0)
            phosphorus = st.slider("Phosphorus (ppm)", 5.0, 30.0, 15.0)
            potassium = st.slider("Potassium (ppm)", 10.0, 40.0, 25.0)
            submitted = st.form_submit_button("Predict Fertility")
            
            if submitted:
                input_data = [[moisture, ph, nitrogen, phosphorus, potassium]]
                prediction = model.predict(input_data)[0]
                st.success(f"Predicted Soil Fertility: **{prediction}**")
    
    # Tab 2: Crop Trends
    with tab2:
        st.subheader("Crop Health Trends")
        crop_data = generate_crop_data()
        region = st.selectbox("Select Region", ["All"] + list(crop_data["Region"].unique()))
        if region != "All":
            crop_data = crop_data[crop_data["Region"] == region]
        
        st.subheader("Soil Moisture Trend")
        fig_moisture = px.line(crop_data, x="Date", y="Soil_Moisture (%)", title="Soil Moisture Over Time")
        st.plotly_chart(fig_moisture)
        
        st.subheader("Crop Health Score")
        fig_health = px.line(crop_data, x="Date", y="Crop_Health_Score", title="Crop Health Score Over Time")
        st.plotly_chart(fig_health)
        
        st.subheader("Pest Risk Analysis")
        fig_pest = px.bar(crop_data, x="Date", y="Pest_Risk (%)", title="Pest Risk Over Time")
        st.plotly_chart(fig_pest)
        
        st.subheader("Summary Statistics")
        st.write(crop_data.describe())
    
    # Tab 3: Satellite View
    with tab3:
        st.subheader("Satellite Imagery View")
        st.markdown("View mock satellite imagery of crop regions.")
        st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="Mock Satellite View of Farmland")
        
        # Mock geospatial data for regions
        geo_data = pd.DataFrame({
            "Region": ["North", "South", "East", "West"],
            "Latitude": [28.7041, 15.9129, 22.5726, 19.0760],
            "Longitude": [77.1025, 79.7400, 88.3639, 72.8777],
            "Crop_Health_Score": [85, 70, 65, 90]
        })
        fig_geo = px.scatter_mapbox(geo_data, lat="Latitude", lon="Longitude", size="Crop_Health_Score",
                                    color="Crop_Health_Score", hover_name="Region",
                                    mapbox_style="open-street-map", zoom=3)
        st.plotly_chart(fig_geo)
    
    # Tab 4: Crop Image Analysis
    with tab4:
        st.subheader("Crop Image Analysis")
        st.markdown("Upload an image of your crop to detect its condition.")
        uploaded_file = st.file_uploader("Choose a crop image", type=["jpg", "png"])
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Crop Image", use_column_width=True)
            condition, description = analyze_crop_image(image)
            st.write(f"**Crop Condition**: {condition}")
            st.write(f"**Description**: {description}")

# Government Schemes Section
elif section == "Government Schemes":
    st.header("🏛️ Government Schemes & Subsidies")
    st.markdown("Explore available government schemes to support your farming needs.")
    
    schemes_df = pd.DataFrame(schemes_data)
    for _, row in schemes_df.iterrows():
        with st.expander(row["Scheme_Name"]):
            st.markdown(f"""
            **Description**: {row["Description"]}  
            **Eligibility**: {row["Eligibility"]}  
            **Apply**: [Click Here]({row["Apply_Link"]})
            """)

# Mental Health Support Section
elif section == "Mental Health Support":
    st.header("🧠 Mental Health Resources")
    st.markdown("Access resources to support mental well-being for farmers.")
    
    resources_df = pd.DataFrame(mental_health_resources)
    for _, row in resources_df.iterrows():
        with st.expander(row["Resource_Name"]):
            st.markdown(f"""
            **Description**: {row["Description"]}  
            **Contact**: {row["Contact"]}
            """)

# Community Reporting Section
elif section == "Community Reporting":
    st.header("🌍 Community-Driven Reporting")
    st.markdown("Report local agricultural challenges and share knowledge with your community.")
    
    with st.form("report_form"):
        issue = st.text_area("Describe the Issue (e.g., pest outbreak, drought, etc.)")
        location = st.text_input("Location")
        severity = st.slider("Severity (1-10)", 1, 10, 5)
        submitted = st.form_submit_button("Submit Report")
        
        if submitted:
            st.success(f"Report submitted: {issue} in {location} (Severity: {severity})")
    
    # Mock community reports
    st.subheader("Recent Community Reports")
    mock_reports = [
        {"Issue": "Pest outbreak in wheat fields", "Location": "Punjab", "Severity": 7, "Date": "2025-07-10"},
        {"Issue": "Drought conditions", "Location": "Rajasthan", "Severity": 9, "Date": "2025-07-08"}
    ]
    reports_df = pd.DataFrame(mock_reports)
    st.dataframe(reports_df)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ by Swetanshu | Powered by Streamlit")
