import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="BrandDrop Prototype", page_icon="✨", layout="centered")

# --- CUSTOM CSS (LUXURY DARK MODE) ---
st.markdown("""
    <style>
    /* Main background and text */
    .stApp {
        background-color: #121212;
        color: #ffffff;
    }
    /* Headers */
    h1, h2, h3 {
        color: #C5837C !important; /* Rose Gold */
        font-family: 'Helvetica Neue', sans-serif;
    }
    /* Cards */
    div.stExpander {
        background-color: #1e1e1e !important;
        border: 1px solid #333 !important;
        border-radius: 10px !important;
    }
    /* Buttons */
    .stButton>button {
        background-color: #C5837C;
        color: white;
        border-radius: 20px;
        border: none;
        width: 100%;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #a86c66;
        color: white;
    }
    /* Success Message */
    .stSuccess {
        background-color: rgba(197, 131, 124, 0.2) !important;
        color: #C5837C !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE (DATABASE SIMULATION) ---
if 'passport_stamps' not in st.session_state:
    st.session_state.passport_stamps = ["🛍️ Dubai Explorer (Level 1)"]

# --- NAVIGATION ---
st.sidebar.title("BrandDrop.")
st.sidebar.caption("📍 Dubai, UAE")
page = st.sidebar.radio("Menu", ["✨ Discover", "⭐ My Passport"])

# --- PAGE: DISCOVER ---
if page == "✨ Discover":
    st.title("Discover Experiences")
    st.write("Where brands compete for your attention through experiences.")
    
    # Filters
    category = st.radio("Filters:", ["All", "Cosmetics", "Fashion", "Fragrance"], horizontal=True)
    
    st.divider()

    # Experience Card 1
    if category in ["All", "Cosmetics"]:
        st.image("https://images.unsplash.com/photo-1596462502278-27bfdc403348?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", use_container_width=True)
        st.subheader("Fenty Beauty Glow Masterclass")
        st.caption("📍 Fashion Avenue, Dubai Mall • Today, 4 PM")
        st.write("Join the exclusive masterclass and test unreleased highlighters before they hit the market.")
        
        if st.button("Reserve Spot - Fenty", key="btn_fenty"):
            if "💄 Beauty Insider" not in st.session_state.passport_stamps:
                st.session_state.passport_stamps.append("💄 Beauty Insider")
            st.success("Spot Reserved! QR Code sent to your email. Passport stamp unlocked!")

    st.write("") # Spacing

    # Experience Card 2
    if category in ["All", "Fashion"]:
        st.image("https://images.unsplash.com/photo-1490481651871-ab68de25d43d?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", use_container_width=True)
        st.subheader("Dior Secret Pop-up & Mystery Gift")
        st.caption("📍 Mall of the Emirates • Tomorrow, 10 AM")
        st.write("Find the hidden pop-up to unlock a mystery luxury gift and a limited-edition tote.")
        
        if st.button("Reserve Spot - Dior", key="btn_dior"):
            if "👗 Fashion Icon" not in st.session_state.passport_stamps:
                st.session_state.passport_stamps.append("👗 Fashion Icon")
            st.success("Spot Reserved! QR Code sent to your email. Passport stamp unlocked!")

# --- PAGE: PASSPORT ---
elif page == "⭐ My Passport":
    st.title("My Experience Passport")
    st.write("Complete experiences to unlock VIP tiers and exclusive rewards.")
    
    st.divider()
    
    st.subheader("Unlocked Achievements")
    if not st.session_state.passport_stamps:
        st.write("You haven't attended any experiences yet. Go discover some!")
    else:
        for stamp in st.session_state.passport_stamps:
            # Display stamps like a gamified checklist
            st.markdown(f"### {stamp}")
            st.progress(100)
    
    st.divider()
    
    st.subheader("Locked Achievements")
    st.markdown("🔒 **Sneaker Hunter** (0/3 Launches Attended)")
    st.progress(0)
    st.markdown("🔒 **Coffee Connoisseur** (1/5 Tastings Attended)")
    st.progress(20)
