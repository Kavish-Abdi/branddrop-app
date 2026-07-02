import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="BrandDrop Prototype", page_icon="✨", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: #ffffff; }
    h1 { font-family: 'Times New Roman', Times, serif !important; color: #C5837C !important; font-size: 2.5rem !important; }
    h2, h3 { color: #C5837C !important; font-family: 'Helvetica Neue', sans-serif; }
    
    /* Buttons */
    .stButton>button { background-color: #C5837C; color: white; border-radius: 20px; border: none; font-weight: bold; transition: all 0.3s ease; width: 100%;}
    .stButton>button:hover { background-color: #a86c66; transform: scale(1.02); }
    
    /* Passport Progress Cards (Matching Pic 3) */
    .stamp-card {
        background: linear-gradient(135deg, #2a1b3d 0%, #4a1942 100%);
        border-radius: 12px; padding: 15px; margin-bottom: 15px; border: 1px solid #C5837C;
    }
    .stamp-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
    .stamp-title { background: #5c3c92; padding: 5px 12px; border-radius: 20px; font-size: 14px; font-weight: bold; color: white; }
    .stamp-status { font-size: 12px; color: #ffb7b2; font-weight: bold; }
    .progress-track { background: #eee; height: 8px; border-radius: 4px; width: 100%; overflow: hidden; margin-bottom: 5px; }
    .progress-fill { background: #d32f2f; height: 100%; border-radius: 4px; }
    .progress-text { font-size: 11px; color: #ccc; }
    
    /* Achievements (Matching Pic 4) */
    .achieve-unlocked {
        background: linear-gradient(90deg, #ff4081 0%, #f50057 100%);
        border-radius: 10px; padding: 15px; margin-bottom: 10px; color: white; display: flex; justify-content: space-between;
    }
    .achieve-locked {
        background: rgba(255,255,255,0.1); border-radius: 10px; padding: 15px; margin-bottom: 10px; color: #888; display: flex; justify-content: space-between;
    }
    
    /* Footer */
    .brand-footer { background-color: #1e1e1e; padding: 30px 20px; text-align: center; border-radius: 15px; margin-top: 50px; border-top: 2px solid #333;}
    .brand-footer h2 { margin: 0; font-family: 'Helvetica', sans-serif; font-size: 28px; color: white !important;}
    .brand-footer .drop-text { color: #E91E63; font-weight: 900;} /* Pink Drop */
    .brand-footer .tagline { color: #aaa; font-size: 15px; margin: 10px 0;}
    .brand-footer .copyright { color: #666; font-size: 12px; margin: 0;}
    </style>
""", unsafe_allow_html=True)

# --- HELPER: FOOTER ---
def render_footer():
    st.markdown("""
        <div class="brand-footer">
            <h2>Brand<span class="drop-text">Drop</span></h2>
            <p class="tagline">Discover. Experience. Earn. — Where brands come to life.</p>
            <p class="copyright">© 2026 BrandDrop. All rights reserved. UAE's First Consumer Experience Marketplace.</p>
        </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
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
    "💬 Testimonials",
    "📖 About BrandDrop"
])

st.sidebar.divider()
st.sidebar.button("🔔 3 New Notifications", key="side_notif", type="primary")
st.sidebar.markdown("<div style='text-align:center; color:#888; font-size:12px; margin-top:20px;'>📱 v2.0.0<br>🇦🇪 Made in UAE</div>", unsafe_allow_html=True)


# ==========================================
# PAGE 1: DISCOVER 
# ==========================================
if page == "✨ Discover":
    st.title("Discover Experiences")
    st.write("Browse real-world brand activations across the UAE.")
    
    events = [
        ("Charlotte Tilbury Oasis", "Burj Park", "💄 Beauty"), ("Nike Air Max Drop", "D3", "👟 Fashion"), 
        ("Nespresso Tasting", "City Walk", "☕ F&B"), ("Dior Mystery Gift", "MOE", "👗 Luxury"),
        ("Apple Vision Pro Demo", "Dubai Mall", "💻 Tech"), ("Porsche Track Day", "Autodrome", "🏎️ Auto"),
        ("Banaras Artisanal Showcase", "Alserkal", "🧵 Heritage"), ("Packaged Foods Expo", "WTC", "🍱 F&B"),
        ("Chanel Pop-up", "Kite Beach", "💎 Luxury"), ("Sephora VIP Night", "Dubai Mall", "💄 Beauty"),
        ("Supply Chain Automation Demo", "DIFC", "⚙️ B2B/Tech"), ("Red Bull Gaming", "JBR", "🎮 Gaming"),
        ("Adidas Run Club", "Marina", "🏃 Fitness"), ("Samsung Galaxy Launch", "Bluewaters", "📱 Tech"),
        ("Lego Family Build", "Festival City", "🧸 Family")
    ]
    
    col1, col2, col3 = st.columns(3)
    for i, (name, loc, tag) in enumerate(events):
        with [col1, col2, col3][i % 3]:
            with st.container(border=True):
                st.markdown(f"**{name}**")
                st.caption(f"📍 {loc} | {tag}")
                st.button("Reserve", key=f"evt_{i}")

    render_footer()

# ==========================================
# PAGE 2: USER PROFILE
# ==========================================
elif page == "👤 My Profile":
    st.title("My Profile")
    st.button("🔔 You have 3 pending reward claims! Click to view.", type="primary", use_container_width=True)
    st.write("")
    
    c1, c2 = st.columns([1, 3])
    with c1:
         st.image("https://api.dicebear.com/7.x/avataaars/svg?seed=Aisha", width=150)
    with c2:
        st.subheader("Aisha Al Mansoori")
        st.write("🌟 **Status:** Gold Member")
        st.write("📞 +971 50 123 4567 | 📧 aisha.m@branddrop.ae")
        st.button("⚙️ Account Settings")
        st.button("🚪 Sign Out")

    render_footer()

# ==========================================
# PAGE 3: CONSUMER CLUBS
# ==========================================
elif page == "🤝 Consumer Clubs":
    st.title("Consumer Clubs")
    st.write("Join 12 exclusive communities tailored to your interests.")
    
    clubs = [
        "👟 Sneakerhead Hub", "🧘‍♀️ Wellness Collective", "🐾 Pet Lovers", "☕ Coffee Connoisseurs", 
        "🏎️ Auto Enthusiasts", "🍼 Parents Club", "🎮 Tech & Gaming", "🍣 Foodies Club", 
        "💎 Luxury Lounge", "💄 Beauty Insiders", "🎨 Art & Design", "✈️ Travel Explorers"
    ]
    
    cols = st.columns(3)
    for i, club in enumerate(clubs):
        with cols[i % 3]:
            st.info(club)
            st.button("Join", key=f"club_{i}")

    render_footer()

# ==========================================
# PAGE 4: PASSPORT & REWARDS
# ==========================================
elif page == "⭐ Passport & Rewards":
    st.title("My Experience Passport")
    
    # Stats row (Matching Pic 2)
    c1, c2, c3 = st.columns(3)
    c1.markdown("<div style='background:#1e1e1e; padding:20px; border-radius:10px; text-align:center;'>📗<h3>3</h3><p style='color:#888;'>Total Experiences</p></div>", unsafe_allow_html=True)
    c2.markdown("<div style='background:#1e1e1e; padding:20px; border-radius:10px; text-align:center;'>🏆<h3>2/8</h3><p style='color:#888;'>Stamps Unlocked</p></div>", unsafe_allow_html=True)
    c3.markdown("<div style='background:#1e1e1e; padding:20px; border-radius:10px; text-align:center;'>⭐<h3>450</h3><p style='color:#888;'>Total Points</p></div>", unsafe_allow_html=True)
    
    st.divider()
    st.subheader("✨ Your Passport Stamps")
    
    # Progress bars (Matching Pic 3)
    stamps = [
        ("Coffee Explorer", 7, 10), ("Beauty Insider", 4, 5),
        ("Food Adventurer", 3, 10), ("Tech Enthusiast", 2, 5),
        ("Fitness Fanatic", 1, 5), ("Sneaker Hunter", 3, 3),
        ("Luxury Seeker", 2, 5), ("Dubai Explorer", 5, 5)
    ]
    
    col1, col2 = st.columns(2)
    for i, (name, curr, total) in enumerate(stamps):
        pct = int((curr/total)*100)
        status = "✅ Unlocked" if curr == total else f"🔒 {curr}/{total}"
        fill_color = "#4caf50" if curr == total else "#d32f2f"
        
        html = f"""
        <div class="stamp-card">
            <div class="stamp-header">
                <span class="stamp-title">{name}</span>
                <span class="stamp-status">{status}</span>
            </div>
            <div class="progress-track"><div class="progress-fill" style="width: {pct}%; background: {fill_color};"></div></div>
            <span class="progress-text">{curr}/{total} completed</span>
        </div>
        """
        with [col1, col2][i % 2]:
            st.markdown(html, unsafe_allow_html=True)
            
    st.divider()
    st.subheader("🏆 Reward Catalog")
    
    # Claimable Rewards
    st.success("**[CLAIMABLE]** ☕ % Arabica Free Coffee (Cost: 200 pts)")
    st.success("**[CLAIMABLE]** 🎟️ AED 50 Sephora Voucher (Cost: 400 pts)")
    
    # Locked Rewards
    st.error("**[LOCKED]** 🚢 VIP Yacht Party - Marina (Requires 5,000 pts)")
    st.error("**[LOCKED]** 👗 Dubai Fashion Week Invite (Requires 3,000 pts)")
    st.error("**[LOCKED]** 🏎️ Porsche Track Day Pass (Requires 10,000 pts)")

    render_footer()

# ==========================================
# PAGE 5: TESTIMONIALS
# ==========================================
elif page == "💬 Testimonials":
    st.title("Community Voices")
    st.write("See what users and brands are saying about BrandDrop.")
    
    reviews = [
        ("Sarah K.", "Marketing Director", "⭐⭐⭐⭐⭐", "BrandDrop completely changed our product launch strategy. Real engagement over empty clicks."),
        ("Aisha M.", "Coffee Lover", "⭐⭐⭐⭐⭐", "I've discovered 4 new independent cafes this month just through the app's treasure hunts!"),
        ("Khalid A.", "Sneakerhead", "⭐⭐⭐⭐", "Got early access to the new Jordan drop. The passport system makes shopping feel like a game."),
        ("Fatima S.", "University Student", "⭐⭐⭐⭐⭐", "Finally an app that rewards you for attending cool events instead of just giving generic coupons."),
        ("Omar T.", "Tech Enthusiast", "⭐⭐⭐⭐", "The Vision Pro demo event was incredibly well organized. Points hit my account instantly."),
        ("Priya R.", "Fashion Influencer", "⭐⭐⭐⭐⭐", "I tell all my followers to use BrandDrop. The VIP access rewards are actually worth it."),
        ("Dr. Hansel D.", "Business Strategist", "⭐⭐⭐⭐⭐", "A brilliant application of Blue Ocean Strategy in the retail space. Highly disruptive.")
    ]
    
    for name, role, stars, text in reviews:
        with st.chat_message("user"):
            st.write(f"**{name}** ({role}) - {stars}")
            st.write(f"*{text}*")
            
    st.divider()
    st.subheader("Share Your Experience")
    with st.form("feedback_form"):
        st.text_input("Your Name")
        st.text_input("Your Role (e.g., Coffee Lover, Brand Manager)")
        st.slider("Rating", 1, 5, 5)
        st.text_area("Your Testimonial")
        st.form_submit_button("Submit Feedback", type="primary")

    render_footer()

# ==========================================
# PAGE 6: ABOUT BRANDDROP
# ==========================================
elif page == "📖 About BrandDrop":
    st.markdown("""
        <div style="background: linear-gradient(135deg, #1a237e 0%, #C5837C 100%); padding: 30px; border-radius: 15px; margin-bottom: 20px;">
            <h1 style="color: white !important; margin:0;">About Brand<span style="color:#E91E63;">Drop</span></h1>
            <p style="color: #eee; font-size: 16px;">UAE's First Consumer Experience Marketplace<br>
            <i>Where brands compete for attention through experiences, not advertisements.</i></p>
        </div>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns([1.5, 1])
    with c1:
        st.subheader("🎯 Our Mission")
        st.write("Replacing traditional advertising with real-world experiences that create meaningful connections and measurable engagement.")
        
        st.subheader("❌ The Problem")
        st.write("Consumers skip ads. Brands waste money on unmeasurable activations. Experiences are scattered.")
        
        st.subheader("✅ Our Solution")
        st.write("A single platform for discovering experiences, building a digital passport, and driving real-time B2B analytics.")
        
    with c2:
        with st.container(border=True):
            st.subheader("👨‍💻 Development Team")
            st.write("• Mr. Ronit Kapoor\n• Mr. Syed Ali Kavish Abdi\n• Ms. Shania Mehta\n• Ms. Vyomika Mugdha\n• Mr. Krishna Sharma\n• Mr. Khushil Sharma")
            st.caption("Built with ❤️ by the SP Jain Global team in Dubai, UAE.")

    render_footer()
