import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

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
    st.image("https://via.placeholder.com/800x400.png?text=Farmers+at+Work", caption="Supporting resilient farming communities")

# Crop Monitoring Section
elif section == "Crop Monitoring":
    st.header("📊 Real-Time Crop Monitoring")
    st.markdown("Monitor soil moisture, crop health, and pest risks with AI-driven insights.")
    
    # Generate and display mock data
    crop_data = generate_crop_data()
    
    # Filters
    region = st.selectbox("Select Region", ["All"] + list(crop_data["Region"].unique()))
    if region != "All":
        crop_data = crop_data[crop_data["Region"] == region]
    
    # Visualizations
    st.subheader("Soil Moisture Trend")
    fig_moisture = px.line(crop_data, x="Date", y="Soil_Moisture (%)", title="Soil Moisture Over Time")
    st.plotly_chart(fig_moisture)
    
    st.subheader("Crop Health Score")
    fig_health = px.line(crop_data, x="Date", y="Crop_Health_Score", title="Crop Health Score Over Time")
    st.plotly_chart(fig_health)
    
    st.subheader("Pest Risk Analysis")
    fig_pest = px.bar(crop_data, x="Date", y="Pest_Risk (%)", title="Pest Risk Over Time")
    st.plotly_chart(fig_pest)
    
    # Summary Stats
    st.subheader("Summary Statistics")
    st.write(crop_data.describe())

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
st.markdown("Built with ❤️ by Swetanshu| Powered by Larrchatt assosiations")