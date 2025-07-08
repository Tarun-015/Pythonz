import streamlit as st

st.title("Esports Monetization Simulator")

role = st.selectbox("Who are you?", ["-- Select --", "Creator", "Sponsor", "Startup", "Organizer"])

if role == "Creator":
    views = st.number_input("Monthly Views")
    subs = st.number_input("Subscribers")
    engagement = st.slider("Engagement (%)", 1, 20, 7)
    # Show earning estimate
elif role == "Sponsor":
    budget = st.number_input("Your Budget")
    region = st.selectbox("Target Region", ["India", "NA", "Europe"])
    # Show sponsor ROI
elif role == "Startup":
    game = st.text_input("Target Game")
    model = st.radio("Business Model", ["Ad-based", "Freemium", "Merch"])
    # Show revenue forecast
elif role == "Organizer":
    prize_pool = st.number_input("Prize Pool")
    teams = st.number_input("No. of Teams")
    entry_fee = st.number_input("Entry Fee per Team")
    # Show ROI for event
