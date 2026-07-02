import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="BrandDrop Prototype", page_icon="✨", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    /* Main background and text */
    .stApp { background-color: #121212; color: #ffffff; }
    
    h1 { font-family: 'Times New Roman', Times, serif !important; color: #C5837C !important; font-size: 2.5rem !important; }
    h2, h3 { color: #C5837C !important; font-family: 'Helvetica Neue', sans-serif; }
    
    /* Buttons */
    .stButton>button { background-color: #C5837C; color: white; border-radius: 20px; border: none; width: 100%; font-weight: bold; transition: 0.3s; }
    .stButton>button:hover { background-color: #a86c66; color: white; border: 1px solid white; }
    
    /* Square Stat Cards (Profile) */
    .stat-square {
        background-color: #f8f9fa;
        border-radius: 12px;
        padding: 20px 10px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        margin-bottom: 15px;
    }
    .stat-square h2 { color: #1e1e2f !important; font-size: 28px; margin: 10px 0; font-family: 'Arial', sans-serif;}
    .stat-square p { color: #6c757d; font-size: 12px; margin: 0; font-weight: bold;}
    
    /* Global Stats Bar */
    .global-stats-bar {
        background: linear-gradient(90deg, #e0f7fa 0%, #b2ebf2 100%);
        border-radius: 15px;
        padding: 20px;
        display: flex;
        justify-content: space-around;
        text-align: center;
        margin: 40px 0 20px 0;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    .global-stats-bar div { display: flex; flex-direction: column; align-items: center; }
    .global-stats-bar h3 { color: #112233 !important; margin: 0; font-size: 24px; }
    .global-stats-bar p { color: #546e7a; margin: 0; font-size: 13px; font-weight: 500;}
    
    /* Futuristic Passport Cards */
    .cyber-card {
        background: linear-gradient(145deg, #1a1a2e 0%, #16213e 100%);
        border: 1px solid #0f3460;
        box-shadow: 0 0 15px rgba(197, 131, 124, 0.2);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        color: #fff;
        transition: transform 0.3s;
    }
    .cyber-card:hover { transform: translateY(-5px); box-shadow: 0 0 20px rgba(197, 131, 124, 0.5); }
    .cyber-card .glow-icon { font-size: 40px; text-shadow: 0 0 15px #C5837C; margin-bottom: 10px;}
    
    /* Footer */
    .brand-footer {
        background-color: #26C6DA; /* Cyan background matching image */
        padding: 30px 20px;
        text-align: center;
        border-radius: 15px;
        margin-top: 50px;
    }
    .brand-footer h2 { margin: 0; font-family: 'Helvetica', sans-serif; font-size: 28px; }
    .brand-footer .brand-text { color: #111111; font-weight: 900;}
    .brand-footer .drop-text { color: #FF5252; font-weight: 900;}
    .brand-footer .tagline { color: #444; font-size: 15px; margin: 10px 0; font-weight: 500;}
    .brand-footer .copyright { color: #666; font-size: 12px; margin: 0;}
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if 'passport_stamps' not in st.session_state:
    st.session_state.passport_stamps = ["🛍️ Dubai Explorer", "💄 Beauty Insider"]
if 'points' not in st.session_state:
    st.session_state.points = 450
if 'experiences' not in st.session_state:
    st.session_state.experiences = 3

# --- HELPER COMPONENTS ---
def render_footer():
    st.markdown("""
        <div class="global-stats-bar">
            <div><h3>5,247</h3><p>Total Users</p></div>
            <div><h3>287</h3><p>Active Brands</p></div>
            <div><h3>1,432</h3><p>Experiences Created</p></div>
            <div><h3>4.7</h3><p>Avg. Rating</p></div>
        </div>
        <div class="brand-footer">
            <h2><span class="brand-text">Brand</span><span class="drop-text">Drop</span></h2>
            <p class="tagline">Discover. Experience. Earn. — Where brands come to life.</p>
            <p class="copyright">© 2026 BrandDrop. All rights reserved. UAE's First Consumer Experience Marketplace.</p>
        </div>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
st.sidebar.title("BrandDrop.")
st.sidebar.caption("📍 Dubai, UAE")
# Reordered to make Discover the default landing page
page = st.sidebar.radio("Navigation", [
    "✨ Discover", 
    "👤 My Profile", 
    "🤝 Consumer Clubs",
    "⭐ Passport & Rewards", 
    "📖 About BrandDrop"
])

# ==========================================
# PAGE 1: DISCOVER (LANDING PAGE)
# ==========================================
if page == "✨ Discover":
    st.title("Discover")
    st.write("Where brands compete for your attention through experiences.")
    
    st.markdown('<div style="background-color:#C5837C;color:white;padding:4px 10px;border-radius:12px;font-size:12px;font-weight:bold;display:inline-block;margin-bottom:10px;">🌟 FEATURED THIS WEEK</div>', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1555529771-835f59fc5efe?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80", use_container_width=True)
    st.subheader("Charlotte Tilbury: The Magic Oasis")
    st.caption("📍 Burj Park, Downtown Dubai • Friday, 6 PM - 10 PM")
    if st.button("Reserve VIP Access", key="featured"):
        st.success("VIP Access Confirmed!")
    
    st.divider()
    st.write("### Trending Near You")
    
    # Grid of experiences
    c1, c2 = st.columns(2)
    with c1:
        st.image("https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80", use_container_width=True)
        st.markdown("**Nike Air Max Scavenger Hunt**")
        st.caption("Dubai Design District")
        st.button("Join Hunt", key="nike")
        
        st.image("https://images.unsplash.com/photo-1596462502278-27bfdc403348?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80", use_container_width=True)
        st.markdown("**Fenty Beauty Masterclass**")
        st.caption("Dubai Mall")
        st.button("Reserve Spot", key="fenty")

    with c2:
        st.image("https://images.unsplash.com/photo-1511920170033-f8396924c348?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80", use_container_width=True)
        st.markdown("**Nespresso Secret Tasting**")
        st.caption("City Walk")
        st.button("Get Invite", key="nespresso")
        
        st.image("https://images.unsplash.com/photo-1490481651871-ab68de25d43d?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80", use_container_width=True)
        st.markdown("**Dior Mystery Gift Drop**")
        st.caption("Mall of the Emirates")
        st.button("Claim Drop", key="dior")
        
    render_footer()

# ==========================================
# PAGE 2: USER PROFILE
# ==========================================
elif page == "👤 My Profile":
    st.title("My Profile")
    
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image("https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=300&q=80", width=120)
    with c2:
        st.subheader("Aisha Al Mansoori")
        st.write("🌟 **Status:** Gold Member")
        st.write("📍 Dubai, UAE")

    st.write("") # spacing
    
    # Square Interactive Stats (Mirroring the image)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f'<div class="stat-square"><div>🎯</div><h2>{st.session_state.experiences}</h2><p>Experiences Attended</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="stat-square"><div>🏆</div><h2>{st.session_state.points}</h2><p>Total Points Earned</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="stat-square"><div>📗</div><h2>{len(st.session_state.passport_stamps)}/8</h2><p>Passport Stamps</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="stat-square"><div>🔥</div><h2>8</h2><p>Available Experiences</p></div>', unsafe_allow_html=True)

    st.divider()
    st.write("### Upcoming Reservations")
    st.success("🎟️ **Dior Secret Pop-up** - Tomorrow, 10:00 AM @ Mall of the Emirates")
    
    render_footer()

# ==========================================
# PAGE 3: CONSUMER CLUBS
# ==========================================
elif page == "🤝 Consumer Clubs":
    st.title("Consumer Clubs")
    st.write("Join niche communities to get highly targeted event invites.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.image("https://images.unsplash.com/photo-1552346154-21d32810baa3?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80", use_container_width=True)
        st.markdown("### 👟 Sneakerhead Hub")
        st.caption("Early access to drops and streetwear pop-ups.")
        st.button("Join Club", key="c_sneak")
        
        st.write("")
        st.image("https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80", use_container_width=True)
        st.markdown("### 💎 Luxury Lounge")
        st.caption("Private viewing rooms and VIP galas.")
        st.button("Joined", disabled=True, key="c_lux")
        
        st.write("")
        st.image("https://images.unsplash.com/photo-1550745165-9bc0b252726f?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80", use_container_width=True)
        st.markdown("### 🎮 Tech & Gaming")
        st.caption("Console launches, VR experiences, and tournaments.")
        st.button("Join Club", key="c_tech")

    with c2:
        st.image("https://images.unsplash.com/photo-1497935586351-b67a49e012bf?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80", use_container_width=True)
        st.markdown("### ☕ Coffee Connoisseurs")
        st.caption("Secret menu tastings and barista workshops.")
        st.button("Join Club", key="c_coffee")
        
        st.write("")
        st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80", use_container_width=True)
        st.markdown("### 🧘‍♀️ Wellness Collective")
        st.caption("Beach yoga and organic food tastings.")
        st.button("Join Club", key="c_well")
        
        st.write("")
        st.image("https://images.unsplash.com/photo-1504674900247-0877df9cc836?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80", use_container_width=True)
        st.markdown("### 🍣 Foodies Club")
        st.caption("Restaurant soft-openings and tasting menus.")
        st.button("Join Club", key="c_food")
        
    render_footer()

# ==========================================
# PAGE 4: PASSPORT & REWARDS
# ==========================================
elif page == "⭐ Passport & Rewards":
    st.title("Digital Passport")
    st.write("Your futuristic ledger of real-world brand interactions.")
    
    # Futuristic Grid
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="cyber-card">
            <div class="glow-icon">💄</div>
            <h3 style="color:white !important; margin:0;">Beauty Insider</h3>
            <p style="color:#aaa; font-size:12px;">Level 2 Unlocked</p>
            <div style="background:#333; height:4px; width:100%; margin-top:10px; border-radius:2px;">
                <div style="background:#C5837C; height:4px; width:100%; border-radius:2px; box-shadow: 0 0 10px #C5837C;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="cyber-card">
            <div class="glow-icon">🛍️</div>
            <h3 style="color:white !important; margin:0;">Dubai Explorer</h3>
            <p style="color:#aaa; font-size:12px;">Level 1 Unlocked</p>
            <div style="background:#333; height:4px; width:100%; margin-top:10px; border-radius:2px;">
                <div style="background:#C5837C; height:4px; width:100%; border-radius:2px; box-shadow: 0 0 10px #C5837C;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    st.divider()
    
    st.title("Rewards Network")
    st.write(f"Balance: **{st.session_state.points}** points")
    
    st.markdown("#### 🎟️ AED 100 Sephora Digital Gift Card")
    st.caption("Cost: 1,000 pts")
    st.button("Insufficient Points", disabled=True)
            
    st.markdown("#### ☕ Free Coffee at % Arabica")
    st.caption("Cost: 200 pts")
    if st.button("Redeem Reward"):
        st.success("Access Code Generated: BRND-DROP-882")
        
    render_footer()

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
    st.write("### Community Voices")
    
    # Generic User Testimonials
    st.success("""
    *"I used to hate targeted ads on Instagram. Now I check BrandDrop every weekend to see what cool pop-ups are happening around the city. Earning points for attending is just a bonus!"*
    
    — **Aisha M., BrandDrop User**
    """)
    
    st.info("""
    *"Such a cool concept. I joined the Sneakerhead Hub and got early access to a drop at Dubai Design District that I wouldn't have known about otherwise."*
    
    — **Khalid A., Dubai Resident**
    """)
    
    st.success("""
    *"Finally, an app that actually rewards you for doing fun things instead of just giving you 5% off coupon codes."*
    
    — **Fatima S., University Student**
    """)
    
    render_footer()
