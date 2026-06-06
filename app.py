import streamlit as st
import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters")

    return score, feedback


st.title("🔐 Password Strength Checker (Cybersecurity Project)")

password = st.text_input("Enter your password", type="password")

if st.button("Check Strength"):
    score, feedback = check_password_strength(password)

    st.write("### Result:")

    if score <= 2:
        st.error("Weak Password ❌")
    elif score == 3 or score == 4:
        st.warning("Medium Password ⚠️")
    else:
        st.success("Strong Password ✅")

    st.write("Score:", score, "/5")

    if feedback:
        st.write("### Suggestions:")
        for f in feedback:
            st.write("•", f)