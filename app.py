import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="BrandDrop Prototype", page_icon="✨", layout="wide")

# --- SESSION STATE FOR NAVIGATION & REWARDS ---
if 'current_page' not in st.session_state:
    st.session_state.current_page = "✨ Discover"
if 'claimed_coffee' not in st.session_state:
    st.session_state.claimed_coffee = False
if 'claimed_sephora' not in st.session_state:
    st.session_state.claimed_sephora = False

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: #ffffff; }
    h1 { font-family: 'Times New Roman', Times, serif !important; color: #C5837C !important; font-size: 2.5rem !important; }
    h2, h3 { color: #C5837C !important; font-family: 'Helvetica Neue', sans-serif; }
    
    /* Buttons */
    .stButton>button { background-color: #C5837C; color: white; border-radius: 20px; border: none; font-weight: bold; transition: all 0.3s ease; width: 100%;}
    .stButton>button:hover { background-color: #a86c66; transform: scale(1.02); }
    
    /* Profile Stats */
    .stat-square { background-color: #1e1e1e; border: 1px solid #333; border-radius: 12px; padding: 20px 10px; text-align: center; margin-bottom: 15px;}
    .stat-square h2 { color: #fff !important; font-size: 28px; margin: 10px 0; font-family: 'Arial', sans-serif;}
    .stat-square p { color: #888; font-size: 12px; margin: 0; font-weight: bold;}
    
    /* Passport Progress Cards */
    .stamp-card { background: linear-gradient(135deg, #2a1b3d 0%, #4a1942 100%); border-radius: 12px; padding: 15px; margin-bottom: 15px; border: 1px solid #C5837C; }
    .stamp-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
    .stamp-title { background: #5c3c92; padding: 5px 12px; border-radius: 20px; font-size: 14px; font-weight: bold; color: white; }
    .stamp-status { font-size: 12px; color: #ffb7b2; font-weight: bold; }
    .progress-track { background: #eee; height: 8px; border-radius: 4px; width: 100%; overflow: hidden; margin-bottom: 5px; }
    .progress-fill { background: #d32f2f; height: 100%; border-radius: 4px; }
    .progress-text { font-size: 11px; color: #ccc; }
    
    /* Reward Box Styling */
    .reward-gold {
        background: linear-gradient(135deg, #BF953F, #FCF6BA, #B38728, #FBF5B7);
        color: #111; padding: 20px; border-radius: 12px; margin-bottom: 10px;
        box-shadow: 0 4px 15px rgba(218, 165, 32, 0.3); font-weight: 900;
        display: flex; justify-content: space-between; align-items: center;
    }
    .reward-locked {
        background: repeating-linear-gradient(45deg, #1a1a1a, #1a1a1a 10px, #222 10px, #222 20px);
        color: #666; padding: 20px; border-radius: 12px; margin-bottom: 15px;
        border: 2px solid #333; position: relative; overflow: hidden;
    }
    .reward-locked::after {
        content: '⛓️ 🔒 ⛓️'; position: absolute; right: 20px; top: 50%;
        transform: translateY(-50%); font-size: 24px; letter-spacing: 5px; opacity: 0.7;
    }
    
    /* About Page Specifics */
    .about-card { background-color: #fce4ec; border-radius: 15px; padding: 20px; margin-bottom: 20px; color: #333; }
    .about-card h3 { color: #d81b60 !important; margin-top: 0;}
    .team-card { background-color: white; border-radius: 15px; padding: 20px; color: #333;}
    .team-card h3 { color: #1a237e !important; }
    .team-member { background-color: #3949ab; color: white; padding: 5px 15px; border-radius: 5px; margin-bottom: 8px; display: inline-block; width: 100%; font-weight: bold; }
    
    /* Footer */
    .brand-footer { background-color: #1e1e1e; padding: 30px 20px; text-align: center; border-radius: 15px; margin-top: 50px; border-top: 2px solid #333;}
    .brand-footer h2 { margin: 0; font-family: 'Helvetica', sans-serif; font-size: 28px; color: white !important;}
    .brand-footer .drop-text { color: #E91E63; font-weight: 900;}
    .brand-footer .tagline { color: #aaa; font-size: 15px; margin: 10px 0;}
    .brand-footer .copyright { color: #666; font-size: 12px; margin: 0;}
    </style>
""", unsafe_allow_html=True)

def render_footer():
    st.markdown("""
        <div class="brand-footer">
            <h2>Brand<span class="drop-text">Drop</span></h2>
            <p class="tagline">Discover. Experience. Earn. — Where brands come to life.</p>
            <p class="copyright">© 2026 BrandDrop. All rights reserved. UAE's First Consumer Experience Marketplace.</p>
        </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION LOGIC ---
try:
    st.sidebar.image("logo.jpeg", use_container_width=True)
except:
    st.sidebar.title("BrandDrop.")
st.sidebar.caption("📍 Dubai, UAE")

pages = ["✨ Discover", "👤 My Profile", "🤝 Consumer Clubs", "⭐ Passport & Rewards", "💬 Testimonials", "📖 About BrandDrop", "🔔 Notifications"]
try:
    idx = pages.index(st.session_state.current_page)
except ValueError:
    idx = 0

page = st.sidebar.radio("Navigation", pages, index=idx)

# Sync radio selection with session state
if page != st.session_state.current_page:
    st.session_state.current_page = page
    st.rerun()

st.sidebar.divider()

# Clickable Notification Button in Sidebar
if st.sidebar.button("🔔 3 New Notifications", type="primary"):
    st.session_state.current_page = "🔔 Notifications"
    st.rerun()
    
st.sidebar.markdown("<div style='text-align:center; color:#888; font-size:12px; margin-top:20px;'>📱 v2.0.0<br>🇦🇪 Made in UAE</div>", unsafe_allow_html=True)

# ==========================================
# PAGE 1: DISCOVER 
# ==========================================
if st.session_state.current_page == "✨ Discover":
    st.title("Discover Experiences")
    st.write("Browse real-world brand activations across the UAE.")
    
    events = [
        ("Charlotte Tilbury Oasis", "Burj Park", "💄 Beauty", "https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=500&q=80"), 
        ("Nike Air Max Drop", "D3", "👟 Fashion", "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=500&q=80"), 
        ("Nespresso Tasting", "City Walk", "☕ F&B", "https://images.unsplash.com/photo-1511920170033-f8396924c348?w=500&q=80"), 
        ("Dior Mystery Gift", "MOE", "👗 Luxury", "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=500&q=80"),
        ("Apple Vision Pro Demo", "Dubai Mall", "💻 Tech", "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=500&q=80"), 
        ("Porsche Track Day", "Autodrome", "🏎️ Auto", "https://images.unsplash.com/photo-1511919884226-fd3cad34687c?w=500&q=80"),
        ("Banaras Artisanal Showcase", "Alserkal", "🧵 Heritage", "https://images.unsplash.com/photo-1605814518731-863a35f29910?w=500&q=80"), 
        ("Packaged Foods Expo", "WTC", "🍱 F&B", "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=500&q=80"),
        ("Chanel Pop-up", "Kite Beach", "💎 Luxury", "https://images.unsplash.com/photo-1555529771-835f59fc5efe?w=500&q=80"), 
        ("Sephora VIP Night", "Dubai Mall", "💄 Beauty", "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=500&q=80"),
        ("Supply Chain Expo", "DIFC", "⚙️ B2B/Tech", "https://images.unsplash.com/photo-1586528116311-ad8ed7c663c0?w=500&q=80"), 
        ("Red Bull Gaming", "JBR", "🎮 Gaming", "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=500&q=80"),
        ("Adidas Run Club", "Marina", "🏃 Fitness", "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=500&q=80"), 
        ("Samsung Galaxy Launch", "Bluewaters", "📱 Tech", "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=500&q=80"),
        ("Lego Family Build", "Festival City", "🧸 Family", "https://images.unsplash.com/photo-1511895426328-dc8714191300?w=500&q=80")
    ]
    
    col1, col2, col3 = st.columns(3)
    for i, (name, loc, tag, img) in enumerate(events):
        with [col1, col2, col3][i % 3]:
            with st.container(border=True):
                st.image(img, use_container_width=True)
                st.markdown(f"**{name}**")
                st.caption(f"📍 {loc} | {tag}")
                
                # Interactive Popover for Reservation
                with st.popover("Reserve Slot", use_container_width=True):
                    st.write(f"🗓️ **Next Slot:** Tomorrow, 6:00 PM")
                    st.write(f"📍 {loc}")
                    if st.button("Confirm", key=f"conf_{i}", use_container_width=True):
                        st.success(f"Confirmed! Ref Code: BRND-{1045+i}X")

    render_footer()

# ==========================================
# PAGE 2: USER PROFILE
# ==========================================
elif st.session_state.current_page == "👤 My Profile":
    st.title("My Profile")
    
    # Notification Banner
    if st.button("🔔 You have 3 pending reward claims! Click to view.", type="primary", use_container_width=True):
        st.session_state.current_page = "🔔 Notifications"
        st.rerun()
        
    st.write("")
    
    c1, c2 = st.columns([1, 3])
    with c1:
         st.image("https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=300&q=80", width=150)
    with c2:
        st.subheader("Aisha Al Mansoori")
        st.write("🌟 **Status:** Gold Member")
        st.write("📞 +971 50 123 4567 | 📧 aisha.m@branddrop.ae")
        
        b1, b2, b3 = st.columns(3)
        b1.button("⚙️ Settings")
        b2.button("🖼️ Change Pic")
        b3.button("🚪 Sign Out")

    st.write("")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="stat-square"><div>🎯</div><h2>3</h2><p>Experiences Attended</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-square"><div>🏆</div><h2>1250</h2><p>Total Points Earned</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="stat-square"><div>📗</div><h2>1/8</h2><p>Passport Stamps</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="stat-square"><div>🔥</div><h2>8</h2><p>Available Experiences</p></div>', unsafe_allow_html=True)

    with st.expander("Privacy & Account Settings"):
        st.write("Notifications: **ON**")
        st.write("Location Services: **ON**")

    render_footer()

# ==========================================
# PAGE 3: CONSUMER CLUBS
# ==========================================
elif st.session_state.current_page == "🤝 Consumer Clubs":
    st.title("Consumer Clubs")
    st.write("Join 12 exclusive communities tailored to your interests.")
    
    # Updated image links to guarantee they render
    clubs = [
        ("👟 Sneakerhead Hub", "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=500&q=80"),
        ("🧘‍♀️ Wellness Collective", "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=500&q=80"), 
        ("🐾 Pet Lovers", "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=500&q=80"), 
        ("☕ Coffee Connoisseurs", "https://images.unsplash.com/photo-1497935586351-b67a49e012bf?w=500&q=80"), 
        ("🏎️ Auto Enthusiasts", "https://images.unsplash.com/photo-1511919884226-fd3cad34687c?w=500&q=80"), 
        ("🍼 Parents Club", "https://images.unsplash.com/photo-1511895426328-dc8714191300?w=500&q=80"), 
        ("🎮 Tech & Gaming", "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=500&q=80"), 
        ("🍣 Foodies Club", "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=500&q=80"), 
        ("💎 Luxury Lounge", "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=500&q=80"), 
        ("💄 Beauty Insiders", "https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=500&q=80"), 
        ("🎨 Art & Design", "https://images.unsplash.com/photo-1460661419201-fd4cecdf8a8b?w=500&q=80"), 
        ("✈️ Travel Explorers", "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=500&q=80")
    ]
    
    cols = st.columns(3)
    for i, (club_name, img_url) in enumerate(clubs):
        with cols[i % 3]:
            st.image(img_url, use_container_width=True)
            st.info(club_name)
            st.button("Join", key=f"club_{i}")

    render_footer()

# ==========================================
# PAGE 4: PASSPORT & REWARDS
# ==========================================
elif st.session_state.current_page == "⭐ Passport & Rewards":
    st.title("My Experience Passport")
    
    c1, c2, c3 = st.columns(3)
    c1.markdown("<div style='background:#1e1e1e; padding:20px; border-radius:10px; text-align:center;'>📗<h3>3</h3><p style='color:#888;'>Total Experiences</p></div>", unsafe_allow_html=True)
    c2.markdown("<div style='background:#1e1e1e; padding:20px; border-radius:10px; text-align:center;'>🏆<h3>1/8</h3><p style='color:#888;'>Stamps Unlocked</p></div>", unsafe_allow_html=True)
    c3.markdown("<div style='background:#1e1e1e; padding:20px; border-radius:10px; text-align:center;'>⭐<h3>1250</h3><p style='color:#888;'>Total Points</p></div>", unsafe_allow_html=True)
    
    st.divider()
    st.subheader("✨ Your Passport Stamps")
    
    stamps = [
        ("Coffee Explorer", 7, 10), ("Beauty Insider", 4, 5),
        ("Food Adventurer", 3, 10), ("Tech Enthusiast", 2, 5),
        ("Fitness Fanatic", 1, 5), ("Sneaker Hunter", 3, 3),
        ("Luxury Seeker", 2, 5), ("Dubai Explorer", 1, 5)
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
    
    # Interactive Rewards Logic
    if not st.session_state.claimed_coffee:
        st.markdown("""
            <div class="reward-gold">
                <div>
                    <h4 style="margin:0; color:#111;">☕ % Arabica Free Coffee</h4>
                    <span style="font-size:14px;">Cost: 200 pts | Status: Claimable</span>
                </div>
                <div style="font-size:30px;">✨</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Claim Coffee Reward"):
            st.session_state.claimed_coffee = True
            st.rerun()

    if not st.session_state.claimed_sephora:
        st.markdown("""
            <div class="reward-gold">
                <div>
                    <h4 style="margin:0; color:#111;">🎟️ AED 50 Sephora Voucher</h4>
                    <span style="font-size:14px;">Cost: 400 pts | Status: Claimable</span>
                </div>
                <div style="font-size:30px;">✨</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Claim Sephora Voucher"):
            st.session_state.claimed_sephora = True
            st.rerun()
            
    # Always display standard locked rewards
    st.markdown("""
        <div class="reward-locked">
            <h4 style="margin:0; color:#888;">🚢 VIP Yacht Party - Marina</h4>
            <span style="font-size:14px;">Requires 5,000 pts</span>
        </div>
        
        <div class="reward-locked">
            <h4 style="margin:0; color:#888;">👗 Dubai Fashion Week Invite</h4>
            <span style="font-size:14px;">Requires 3,000 pts</span>
        </div>
    """, unsafe_allow_html=True)

    # If any reward is claimed, show a NEW locked reward at the bottom
    if st.session_state.claimed_coffee or st.session_state.claimed_sephora:
        st.markdown("""
            <div class="reward-locked">
                <h4 style="margin:0; color:#888;">🏎️ F1 Abu Dhabi Paddock Pass</h4>
                <span style="font-size:14px;">Requires 10,000 pts</span>
            </div>
        """, unsafe_allow_html=True)

    render_footer()

# ==========================================
# PAGE 5: TESTIMONIALS
# ==========================================
elif st.session_state.current_page == "💬 Testimonials":
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
elif st.session_state.current_page == "📖 About BrandDrop":
    st.markdown("""
        <div style="background: linear-gradient(135deg, #1a237e 0%, #C5837C 100%); padding: 30px; border-radius: 15px; margin-bottom: 20px;">
            <h1 style="color: white !important; margin:0;">About Brand<span style="color:#E91E63;">Drop</span></h1>
            <p style="color: #eee; font-size: 16px;">UAE's First Consumer Experience Marketplace<br>
            <i>Where brands compete for attention through experiences, not advertisements.</i></p>
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

    render_footer()

# ==========================================
# PAGE 7: NOTIFICATIONS
# ==========================================
elif st.session_state.current_page == "🔔 Notifications":
    st.title("🔔 Your Notifications")
    st.write("Stay updated on your rewards, club invites, and event reminders.")
    
    st.success("✨ **Reward Unlocked:** You have enough points to claim a Free Coffee at % Arabica!")
    st.success("✨ **Reward Unlocked:** You have enough points to claim an AED 50 Sephora Voucher!")
    st.info("🎟️ **Upcoming Event:** Don't forget your Dior Mystery Gift drop tomorrow at 10:00 AM at Mall of the Emirates.")
    st.warning("⭐ **Passport Update:** You are just 1 event away from unlocking the 'Dubai Explorer' stamp.")
    st.info("🤝 **Club Invite:** You've been exclusively invited to the 'Sneakerhead Hub' VIP launch at D3.")
    st.error("🔥 **Trending Now:** The Charlotte Tilbury Oasis event is 90% full. Reserve your spot now!")
    st.success("🏆 **Milestone Reached:** Congratulations! You just crossed 1,000 lifetime points.")
    st.info("🎁 **Surprise Drop:** Check the Discover page for a hidden Nespresso tasting event added today.")
    
    st.divider()
    if st.button("⬅️ Back to Discover", type="primary"):
        st.session_state.current_page = "✨ Discover"
        st.rerun()
        
    render_footer()
