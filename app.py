import base64
import streamlit as st
import pandas as pd
import altair as alt

from modules.classifier import classify_asset
from modules.clustering import get_priority
from modules.risk import calculate_risk, risk_level
from modules.encryption import encrypt_data

st.set_page_config(
    page_title="AI Digital Legacy Guardian",
    page_icon="🔐",
    layout="wide"
)

DATA_PATH = "assets.csv"


def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def load_assets(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def set_background_image(image_path: str):
    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    background_style = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)


load_css()
set_background_image("images/bg.jpg")

st.markdown("<div class='main-header'>🔐 AI Digital Legacy Guardian</div>", unsafe_allow_html=True)

st.markdown("<div class='sub-header'>Secure AI-based Digital Asset Protection System</div>", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Asset Analyzer", "Digital Will", "Encryption Center", "Reports"]
)

st.sidebar.markdown("---")
st.sidebar.write("ML: SVM + KMeans")
st.sidebar.write("Security: AES Encryption")

assets_df = load_assets(DATA_PATH)

if page == "Dashboard":

    st.subheader("Dashboard")

    category_counts = (
        assets_df["category"]
        .value_counts()
        .reindex(["Financial", "Legal", "Social", "Personal"], fill_value=0)
        .reset_index()
    )
    category_counts.columns = ["Category", "Count"]

    total_assets = int(assets_df.shape[0])
    critical_assets = int(
        category_counts.loc[category_counts["Category"].isin(["Financial", "Legal"]), "Count"].sum()
    )
    protected_assets = int(
        category_counts.loc[category_counts["Category"].isin(["Social", "Personal"]), "Count"].sum()
    )
    security_score = max(65, min(100, int(95 - (critical_assets / max(total_assets, 1)) * 20)))

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Assets", f"{total_assets}")
    col2.metric("Critical Assets", f"{critical_assets}")
    col3.metric("Protected Assets", f"{protected_assets}")
    col4.metric("Security Score", f"{security_score}%")

    st.markdown("#### Asset category distribution")
    bar_chart = alt.Chart(category_counts).mark_bar(
        cornerRadiusTopRight=14,
        cornerRadiusBottomRight=14,
        opacity=0.92
    ).encode(
        x=alt.X("Count:Q", title="Number of assets"),
        y=alt.Y("Category:N", sort=["Financial", "Legal", "Social", "Personal"], title=None),
        color=alt.Color(
            "Category:N",
            scale=alt.Scale(range=["#7dd3fc", "#38bdf8", "#60a5fa", "#818cf8"]),
            legend=None
        ),
        tooltip=["Category", "Count"]
    ).properties(height=340)

    st.altair_chart(bar_chart, width="stretch")
    st.progress(min(100, security_score))
    
    if total_assets > 0:
        st.caption(f"✓ Dashboard showing data for {total_assets} analyzed assets.")

elif page == "Asset Analyzer":

    st.subheader("AI Asset Analyzer")

    text = st.text_area("Enter Asset Description")

    if st.button("Analyze"):

        if text.strip() == "":
            st.warning("Enter something")
        else:

            category, confidence = classify_asset(text)
            priority = get_priority(category)
            risk = calculate_risk(text)
            level = risk_level(risk)

            st.success(f"Category: {category}")
            st.info(f"Confidence: {confidence}%")
            st.warning(f"Priority: {priority}")
            st.error(f"Risk Score: {risk}%")
            st.write(f"Risk Level: {level}")

            report = f"""
Category: {category}
Confidence: {confidence}%
Priority: {priority}
Risk: {risk}%
Level: {level}
"""

            st.download_button("Download Report", report)

            report = f"""
Category: {category}
Confidence: {confidence}%
Priority: {priority}
Risk: {risk}%
Level: {level}
"""

            st.download_button("Download Report", report)

elif page == "Digital Will":

    st.subheader("Digital Will Generator")

    name = st.text_input("Nominee Name")
    asset = st.text_input("Asset Name")

    if st.button("Generate"):

        doc = f"""
Digital Will

Nominee: {name}
Asset: {asset}

Status: Approved
"""

        st.text_area("Result", doc, height=200)
        st.download_button("Download Will", doc)

elif page == "Encryption Center":

    st.subheader("AES Encryption")

    data = st.text_area("Enter Sensitive Data")

    if st.button("Encrypt"):

        if data.strip() == "":
            st.warning("Enter data first")
        else:

            key, encrypted = encrypt_data(data)

            st.code(key)
            st.code(encrypted)

elif page == "Reports":

    st.subheader("System Report")

    report = """
AI Digital Legacy Guardian Report

Assets Protected: 17
Critical Assets: 8
Security Score: 87%

ML: SVM + KMeans
Encryption: AES
"""

    st.text_area("Report", report, height=250)
    st.download_button("Download Report", report)

st.markdown("---")
st.markdown("<div style='text-align:center;'>AI Digital Legacy Guardian © 2026</div>", unsafe_allow_html=True)