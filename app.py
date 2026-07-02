import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="BrandDrop Prototype", page_icon="✨", layout="centered")

# --- CUSTOM CSS (LUXURY DARK MODE & TIMES NEW ROMAN) ---
st.markdown("""
    <style>
    /* Main background and text */
    .stApp {
        background-color: #121212;
        color: #ffffff;
    }
    
    /* Times New Roman for Main Headings */
    h1 {
        font-family: 'Times New Roman', Times, serif !important;
        color: #C5837C !important; /* Rose Gold */
        font-size: 2.5rem !important;
    }
    
    /* Helvetica for Subheadings to keep it modern */
    h2, h3 {
        color: #C5837C !important;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* Cards and Expanders */
    div.stExpander, div.css-1r6slb0, div.css-12oz5g7 {
        background-color: #1e1e1e !important;
        border: 1px solid #333 !important;
        border-radius: 10px !important;
        padding: 15px;
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #C5837C;
        color: white;
        border-radius: 20px;
        border: none;
        width: 100%;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #a86c66;
        color: white;
        border: 1px solid white;
    }
    
    /* Featured Badge */
    .featured-badge {
        background-color: #C5837C;
        color: white;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE (DATABASE SIMULATION) ---
if 'passport_stamps' not in st.session_state:
    st.session_state.passport_stamps = ["🛍️ Dubai Explorer (Level 1)"]
if 'points' not in st.session_state:
    st.session_state.points = 1250
if 'clubs' not in st.session_state:
    st.session_state.clubs = ["💄 Beauty Club"]

# --- NAVIGATION ---
st.sidebar.title("BrandDrop.")
st.sidebar.caption("📍 Dubai, UAE")
page = st.sidebar.radio("Navigation", [
    "👤 My Profile", 
    "✨ Discover", 
    "🤝 Consumer Clubs",
    "⭐ Passport & Rewards", 
    "📖 About BrandDrop"
])

# ==========================================
# PAGE 1: USER PROFILE (LOGGED IN VIEW)
# ==========================================
if page == "👤 My Profile":
    st.title("My Profile")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=300&q=80", width=120)
    with col2:
        st.subheader("Aisha Al Mansoori")
        st.write("🌟 **Status:** Gold Member")
        st.write(f"🪙 **Points Balance:** {st.session_state.points}")
    
    st.divider()
    
    st.write("### Active Memberships")
    for club in st.session_state.clubs:
        st.info(f"Member of: **{club}**")
        
    st.write("### Upcoming Reservations")
    st.success("🎟️ **Dior Secret Pop-up** - Tomorrow, 10:00 AM @ Mall of the Emirates")

# ==========================================
# PAGE 2: DISCOVER
# ==========================================
elif page == "✨ Discover":
    st.title("Discover")
    st.write("Where brands compete for your attention through experiences.")
    
    # FEATURED EXPERIENCE
    st.markdown('<div class="featured-badge">🌟 FEATURED THIS WEEK</div>', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1555529771-835f59fc5efe?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80", use_container_width=True)
    st.subheader("Charlotte Tilbury: The Magic Oasis")
    st.caption("📍 Burj Park, Downtown Dubai • Friday, 6 PM - 10 PM")
    st.write("Step into a magical immersive oasis. First 50 attendees unlock the exclusive 'Glow Guru' passport stamp and a full-size mystery product.")
    if st.button("Reserve VIP Access (500 pts)", key="featured"):
        st.success("VIP Access Confirmed! Check your profile for the QR ticket.")
    
    st.divider()
    
    # STANDARD EXPERIENCES
    st.write("### Trending Near You")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1596462502278-27bfdc403348?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80", use_container_width=True)
        st.markdown("**Fenty Masterclass**")
        st.caption("Dubai Mall • Today")
        if st.button("Reserve", key="fenty"):
            st.session_state.passport_stamps.append("💄 Beauty Insider")
            st.success("Reserved!")
            
    with col2:
        st.image("https://images.unsplash.com/photo-1490481651871-ab68de25d43d?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80", use_container_width=True)
        st.markdown("**Dior Mystery Gift**")
        st.caption("Mall of the Emirates • Tomorrow")
        if st.button("Reserve", key="dior"):
            st.session_state.passport_stamps.append("👗 Fashion Icon")
            st.success("Reserved!")

# ==========================================
# PAGE 3: CONSUMER CLUBS
# ==========================================
elif page == "🤝 Consumer Clubs":
    st.title("Clubs")
    st.write("Join niche communities to get highly targeted event invites. No spam, just what you love.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 👟 Sneakerhead Hub")
        st.write("Early access to drops, trading events, and streetwear pop-ups.")
        if st.button("Join Club", key="sneaker"):
            if "👟 Sneakerhead Hub" not in st.session_state.clubs:
                st.session_state.clubs.append("👟 Sneakerhead Hub")
                st.success("Joined!")
                
        st.markdown("### ☕ Coffee Connoisseurs")
        st.write("Secret menu tastings, barista workshops, and farm-to-cup events.")
        if st.button("Join Club", key="coffee"):
            if "☕ Coffee Connoisseurs" not in st.session_state.clubs:
                st.session_state.clubs.append("☕ Coffee Connoisseurs")
                st.success("Joined!")

    with col2:
        st.markdown("### 💎 Luxury Lounge")
        st.write("Private viewing rooms, high-jewelry exhibitions, and VIP galas.")
        if st.button("Join Club", key="luxury"):
            if "💎 Luxury Lounge" not in st.session_state.clubs:
                st.session_state.clubs.append("💎 Luxury Lounge")
                st.success("Joined!")
                
        st.markdown("### 🧘‍♀️ Wellness Collective")
        st.write("Beach yoga, activewear launches, and organic food tastings.")
        if st.button("Join Club", key="wellness"):
            if "🧘‍♀️ Wellness Collective" not in st.session_state.clubs:
                st.session_state.clubs.append("🧘‍♀️ Wellness Collective")
                st.success("Joined!")

# ==========================================
# PAGE 4: PASSPORT & REWARDS
# ==========================================
elif page == "⭐ Passport & Rewards":
    st.title("My Passport")
    
    st.subheader("Unlocked Achievements")
    for stamp in set(st.session_state.passport_stamps):
        st.markdown(f"### {stamp}")
        st.progress(100)
        
    st.divider()
    
    st.title("Rewards Center")
    st.write(f"You have **{st.session_state.points}** points to spend.")
    
    st.markdown("#### 🎟️ AED 100 Sephora Gift Card")
    st.caption("Cost: 1,000 pts")
    if st.button("Redeem Gift Card"):
        if st.session_state.points >= 1000:
            st.session_state.points -= 1000
            st.success("Redeemed! Check your email.")
        else:
            st.error("Not enough points.")
            
    st.markdown("#### ☕ Free Coffee at % Arabica")
    st.caption("Cost: 200 pts")
    if st.button("Redeem Coffee"):
        if st.session_state.points >= 200:
            st.session_state.points -= 200
            st.success("Redeemed! QR Code generated.")
        else:
            st.error("Not enough points.")

# ==========================================
# PAGE 5: ABOUT BRANDDROP
# ==========================================
elif page == "📖 About BrandDrop":
    st.title("About Us")
    st.write("**The UAE's First Consumer Experience Marketplace.**")
    st.write("""
    We believe traditional marketing is broken. Consumers skip ads, and influencers are losing trust. 
    At BrandDrop, we replace interruptions with interactions. We are where brands come to life.
    """)
    
    st.divider()
    
    st.write("### What People Are Saying")
    
    st.info("""
    *"BrandDrop changed how we launch products in Dubai. Instead of paying for billboard impressions, we had 300 highly engaged beauty lovers physically test our new foundation on day one."*
    
    — **Sarah K., Marketing Director at leading Cosmetics Brand**
    """)
    
    st.success("""
    *"I used to hate targeted ads on Instagram. Now I check BrandDrop every weekend to see what cool pop-ups are happening around the city. Earning points for attending is just a bonus!"*
    
    — **Aisha M., BrandDrop User**
    """)
    
    st.divider()
    st.write("📍 Headquartered in Dubai, UAE.")
    st.write("📧 partner@branddrop.ae")
