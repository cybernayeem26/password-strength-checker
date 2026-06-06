import streamlit as st
import re

# ---------------- UI CONFIG ----------------
st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔐",
    layout="centered"
)

# ---------------- HACKER STYLE CSS ----------------
st.markdown("""
<style>
body {
    background-color: #0d0d0d;
    color: #00ff00;
}

.stApp {
    background-color: #0d0d0d;
}

h1, h2, h3 {
    color: #00ff00;
    text-align: center;
    font-family: "Courier New";
}

.stTextInput > div > div > input {
    background-color: black;
    color: #00ff00;
    border: 1px solid #00ff00;
}

.stButton > button {
    background-color: black;
    color: #00ff00;
    border: 1px solid #00ff00;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #00ff00;
    color: black;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOGIC ----------------
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Weak length detected")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Missing uppercase layer")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Missing lowercase layer")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Missing numeric signature")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Missing special characters")

    return score, feedback

# ---------------- UI ----------------
st.title("🔐 PASSWORD SECURITY SCANNER")
st.write("Enter password to analyze security level")

password = st.text_input("Enter Password", type="password")

if st.button("SCAN SYSTEM"):
    score, feedback = check_password_strength(password)

    st.write("### SECURITY ANALYSIS:")

    if score <= 2:
        st.error("⚠ SYSTEM STATUS: BREACHED (WEAK PASSWORD)")
    elif score == 3 or score == 4:
        st.warning("⚡ SYSTEM STATUS: MODERATE SECURITY")
    else:
        st.success("🛡 SYSTEM STATUS: HIGH SECURITY")

    st.write(f"Security Score: {score}/5")

    if feedback:
        st.write("### Threat Analysis Report:")
        for f in feedback:
            st.write("•", f)