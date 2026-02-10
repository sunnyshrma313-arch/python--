import streamlit as st

# Page config
st.set_page_config(page_title="Happy Birthday Mom!", page_icon="🎂")

# --- HEADER SECTION ---
st.balloons()
st.title("🎂 Happy Birthday, Mom!")
st.header("The World's Best Mother ❤️")

# --- IMAGE SECTION ---
st.image("https://via.placeholder.com/700x400", caption="A beautiful memory of us") 

# --- PERSONAL MESSAGE ---
st.subheader("A Special Message for You:")
st.write("""
Mom, thank you for everything you do. You are the heart of our home 
and my biggest inspiration. I built this website just to show you 
how much you mean to me!
""")

st.divider() # Yeh wahi line hai jo aapne screenshot mein dekhi, ye sirf ek partition line hai design ke liye.

# --- INTERACTIVE BUTTON ---
if st.button('Click for a Surprise!'):
    st.snow()
    st.success("You are loved more than words can say!")
    st.write("✨ 🎈 ✨ 🎈 ✨ 🎈 ✨")

# --- REASONS LIST ---
with st.expander("Click to see 5 reasons why you're the best"):
    st.write("1. Your infinite patience.")
    # Aapka special message yahan perfect format mein hai:
    st.write("2. Mom, you made me capable enough to do all this for you and ensured I became well-educated.")
    st.write("3. Your laugh is contagious.")
    st.write("4. You always know how to make me feel better.")
    st.write("5. You're my best friend.")

st.markdown("---")
st.caption("Created with ❤️ by your favorite child.")
