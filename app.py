import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="BrandDrop Prototype", page_icon="✨", layout="centered")

# --- CUSTOM CSS (ANIMATIONS & LAYOUTS) ---
st.markdown("""
    <style>
    /* Main background and text */
    .stApp { background-color: #121212; color: #ffffff; }
    h1 { font-family: 'Times New Roman', Times, serif !important; color: #C5837C !important; font-size: 2.5rem !important; }
    h2, h3 { color: #C5837C !important; font-family: 'Helvetica Neue', sans-serif; }
    
    /* Buttons */
    .stButton>button { background-color: #C5837C; color: white; border-radius: 20px; border: none; width: 100%; font-weight: bold; transition: all 0.3s ease; }
    .stButton>button:hover { background-color: #a86c66; color: white; transform: scale(1.02); }
    
    /* Profile Stat Squares */
    .stat-square {
        background-color: #1e1e1e; border: 1px solid #333; border-radius: 12px; padding: 20px 10px;
        text-align: center; margin-bottom: 15px; transition: transform 0.3s ease;
    }
    .stat-square:hover { transform: translateY(-5px); border-color: #C5837C; }
    .stat-square h2 { color: #fff !important; font-size: 28px; margin: 10px 0; font-family: 'Arial', sans-serif;}
    .stat-square p { color: #888; font-size: 12px; margin: 0; font-weight: bold;}
    
    /* Global Stats Bar (Interactive) */
    .global-stats-bar {
        background: linear-gradient(90deg, #e0f7fa 0%, #b2ebf2 100%);
        border-radius: 15px; padding: 20px; display: flex; justify-content: space-around;
        text-align: center; margin: 40px 0 20px 0; box-shadow: 0 4px 15px rgba(0,0,0,0.4);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .global-stats-bar:hover { transform: translateY(-5px) scale(1.02); box-shadow: 0 10px 25px rgba(38, 198, 218, 0.4); }
    .global-stats-bar div { display: flex; flex-direction: column; align-items: center; }
    .global-stats-bar h3 { color: #112233 !important; margin: 0; font-size: 24px; }
    .global-stats-bar p { color: #546e7a; margin: 0; font-size: 13px; font-weight: bold;}
    
    /* Futuristic Passport Cards (Morphing/Pulsing) */
    @keyframes pulseGlow {
        0% { box-shadow: 0 0 10px rgba(197, 131, 124, 0.2); transform: scale(1); }
        50% { box-shadow: 0 0 25px rgba(197, 131, 124, 0.6); transform: scale(1.03); }
        100% { box-shadow: 0 0 10px rgba(197, 131, 124, 0.2); transform: scale(1); }
    }
    .cyber-card {
        background: linear-gradient(145deg, #1a1a2e 0%, #16213e 100%);
        border: 1px solid #C5837C; border-radius: 15px; padding: 20px; text-align: center; color: #fff;
        animation: pulseGlow 4s infinite ease-in-out;
    }
    .cyber-card .glow-icon { font-size: 40px; text-shadow: 0 0 15px #C5837C; margin-bottom: 10px;}
    
    /* Footer */
    .brand-footer {
        background-color: #26C6DA; padding: 30px 20px; text-align: center; border-radius: 15px; margin-top: 50px;
    }
    .brand-footer h2 { margin: 0; font-family: 'Helvetica', sans-serif; font-size: 28px; }
    .brand-footer .brand-text { color: #111111; font-weight: 900;}
    .brand-footer .drop-text { color: #FF5252; font-weight: 900;}
    .brand-footer .tagline { color: #222; font-size: 15px; margin: 10px 0; font-weight: bold;}
    .brand-footer .copyright { color: #444; font-size: 12px; margin: 0;}
    
    /* About Page Specifics */
    .about-card {
        background-color: #fce4ec; border-radius: 15px; padding: 20px; margin-bottom: 20px; color: #333;
    }
    .about-card h3 { color: #d81b60 !important; margin-top: 0;}
    .team-card { background-color: white; border-radius: 15px; padding: 20px; color: #333;}
    .team-card h3 { color: #1a237e !important; }
    .team-member {
        background-color: #3949ab; color: white; padding: 5px 15px; border-radius: 5px; margin-bottom: 8px; display: inline-block; width: 100%; font-weight: bold;
    }
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
        <div class="brand-footer">
            <h2><span class="brand-text">Brand</span><span class="drop-text">Drop</span></h2>
            <p class="tagline">Discover. Experience. Earn. — Where brands come to life.</p>
            <p class="copyright">© 2026 BrandDrop. All rights reserved. UAE's First Consumer Experience Marketplace.</p>
        </div>
    """, unsafe_allow_html=True)

# --- NAVIGATION & LOGO ---
try:
    st.sidebar.image("logo.jpeg", use_container_width=True)
except:
    st.sidebar.title("BrandDrop.")
st.sidebar.caption("📍 Dubai, UAE")

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
    
    c1, c2 = st.columns(2)
    with c1:
        st.image("https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80", use_container_width=True)
        st.markdown("**Nike Air Max Scavenger Hunt**")
        st.caption("Dubai Design District")
        st.button("Join Hunt", key="nike")
        
    with c2:
        st.image("https://images.unsplash.com/photo-1511920170033-f8396924c348?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80", use_container_width=True)
        st.markdown("**Nespresso Secret Tasting**")
        st.caption("City Walk")
        st.button("Get Invite", key="nespresso")
        
    # STATS BAR ONLY ON DISCOVER PAGE
    st.markdown("""
        <div class="global-stats-bar">
            <div><h3>5,247</h3><p>Total Users</p></div>
            <div><h3>287</h3><p>Active Brands</p></div>
            <div><h3>1,432</h3><p>Experiences Created</p></div>
            <div><h3>4.7</h3><p>Avg. Rating</p></div>
        </div>
    """, unsafe_allow_html=True)

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
        st.write("📞 +971 50 123 4567")
        st.write("📧 aisha.m@branddrop.ae")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("⚙️ Settings")
    with col2:
        st.button("🖼️ Change Pic")
    with col3:
        st.button("🚪 Sign Out")

    st.write("") 
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f'<div class="stat-square"><div>🎯</div><h2>{st.session_state.experiences}</h2><p>Experiences Attended</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="stat-square"><div>🏆</div><h2>{st.session_state.points}</h2><p>Total Points Earned</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="stat-square"><div>📗</div><h2>{len(st.session_state.passport_stamps)}/8</h2><p>Passport Stamps</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="stat-square"><div>🔥</div><h2>8</h2><p>Available Experiences</p></div>', unsafe_allow_html=True)

    with st.expander("Privacy & Account Settings"):
        st.write("Notifications: **ON**")
        st.write("Location Services: **ON**")
        st.write("Data Sharing: **OFF**")

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
        st.button("Join Club", key="c_sneak")
        
        st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80", use_container_width=True)
        st.markdown("### 🧘‍♀️ Wellness Collective")
        st.button("Join Club", key="c_well")
        
        st.image("https://images.unsplash.com/photo-1583337130417-3346a1be7dee?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80", use_container_width=True)
        st.markdown("### 🐾 Pet Lovers")
        st.button("Join Club", key="c_pet")

    with c2:
        st.image("https://images.unsplash.com/photo-1497935586351-b67a49e012bf?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80", use_container_width=True)
        st.markdown("### ☕ Coffee Connoisseurs")
        st.button("Join Club", key="c_coffee")
        
        st.image("https://images.unsplash.com/photo-1511919884226-fd3cad34687c?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80", use_container_width=True)
        st.markdown("### 🏎️ Auto Enthusiasts")
        st.button("Join Club", key="c_auto")
        
        st.image("https://images.unsplash.com/photo-1511895426328-dc8714191300?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80", use_container_width=True)
        st.markdown("### 🍼 Parents Club")
        st.button("Join Club", key="c_parent")

# ==========================================
# PAGE 4: PASSPORT & REWARDS
# ==========================================
elif page == "⭐ Passport & Rewards":
    st.title("Digital Passport")
    st.write("Your futuristic ledger of real-world brand interactions.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="cyber-card">
            <div class="glow-icon">💄</div>
            <h3 style="color:white !important; margin:0;">Beauty Insider</h3>
            <p style="color:#aaa; font-size:12px;">Level 2 Unlocked</p>
            <div style="background:#333; height:4px; width:100%; margin-top:10px; border-radius:2px;">
                <div style="background:#C5837C; height:4px; width:100%; border-radius:2px;"></div>
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
                <div style="background:#C5837C; height:4px; width:100%; border-radius:2px;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    st.divider()
    
    st.title("Rewards Network")
    st.write(f"Balance: **{st.session_state.points}** points")
    
    st.markdown("#### 🚢 VIP Yacht Party Access - Dubai Marina")
    st.caption("Cost: 5,000 pts")
    st.button("Insufficient Points", disabled=True, key="r1")
    
    st.markdown("#### 👗 Exclusive Fashion Week Invite")
    st.caption("Cost: 3,000 pts")
    st.button("Insufficient Points", disabled=True, key="r2")
            
    st.markdown("#### ☕ Free Coffee at % Arabica")
    st.caption("Cost: 200 pts")
    if st.button("Redeem Reward", key="r3"):
        st.success("Access Code Generated: BRND-DROP-882")

# ==========================================
# PAGE 5: ABOUT BRANDDROP
# ==========================================
elif page == "📖 About BrandDrop":
    # Layout replicating images 3 & 4
    st.markdown("""
        <div style="background: linear-gradient(135deg, #1a237e 0%, #d81b60 100%); padding: 30px; border-radius: 15px; margin-bottom: 20px;">
            <h1 style="color: white !important; font-family: 'Arial', sans-serif !important; font-size: 36px !important; margin:0;">About BrandDrop</h1>
            <p style="color: #eee; font-size: 16px; margin-top: 5px;">UAE's First Consumer Experience Marketplace<br>
            <i>Where brands compete for attention through experiences, not advertisements</i></p>
        </div>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns([1.5, 1])
    
    with c1:
        st.markdown("""
            <div class="about-card">
                <h3>🎯 Our Mission</h3>
                <p>BrandDrop is revolutionizing how brands connect with consumers in the UAE. We're replacing traditional advertising with real-world experiences that create meaningful connections and measurable engagement.</p>
            </div>
            
            <h3 style="color:#ff5252 !important;">❌ The Problem We Solve</h3>
            <ul style="color:#ddd;">
                <li>Consumers skip ads and ignore influencer promotions</li>
                <li>Brands waste budget on activations without measuring ROI</li>
                <li>Exciting brand experiences are scattered across multiple platforms</li>
                <li>No single platform exists for discovering brand experiences</li>
            </ul>
            
            <h3 style="color:#69f0ae !important;">✅ Our Solution</h3>
            <ul style="color:#ddd;">
                <li>Single platform for discovering, booking, and engaging</li>
                <li>Measurable engagement instead of just impressions</li>
                <li>Experience Passport with achievements and rewards</li>
                <li>Real-time analytics for brands to track performance</li>
            </ul>
            
            <h3 style="color:#40c4ff !important;">🇦🇪 Why UAE?</h3>
            <ul style="color:#ddd;">
                <li>Retail- and mall-driven culture</li>
                <li>Frequent product launches and brand activations</li>
                <li>Large tourism volumes & digitally connected population</li>
                <li>Strong government support for innovation</li>
            </ul>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
            <div class="team-card" style="margin-bottom: 20px; background-color: #fce4ec;">
                <h3 style="color:#d81b60 !important;">📊 Quick Stats</h3>
                <p style="display:flex; justify-content:space-between;"><b>👥 Users</b> <span>5,000+</span></p>
                <p style="display:flex; justify-content:space-between;"><b>🏢 Brands</b> <span>200+</span></p>
                <p style="display:flex; justify-content:space-between;"><b>🎯 Experiences</b> <span>500+</span></p>
                <p style="display:flex; justify-content:space-between;"><b>⭐ Avg. Rating</b> <span>4.7</span></p>
            </div>
            
            <div class="team-card">
                <h3>👨‍💻 Development Team</h3>
                <div class="team-member">Mr. Ronit Kapoor</div>
                <div class="team-member">Mr. Syed Ali Kavish Abdi</div>
                <div class="team-member">Ms. Shania Mehta</div>
                <div class="team-member">Ms. Vyomika Mugdha</div>
                <div class="team-member">Mr. Krishna Sharma</div>
                <div class="team-member">Mr. Khushil Sharma</div>
                <hr>
                <p style="font-size:12px; color:#666; margin:0;">Built with ❤️ by the SP Jain Global team in Dubai, UAE.<br>© 2026 BrandDrop</p>
            </div>
        """, unsafe_allow_html=True)

# CALL FOOTER AT THE VERY END (APPLIES TO ALL PAGES)
render_footer()
