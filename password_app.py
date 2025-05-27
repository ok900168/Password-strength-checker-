import streamlit as st
import re

# Set page title and icon
st.set_page_config(page_title=" Password Strength Checker", page_icon="")

# Title
st.title(" Password Strength Checker")

# Description
st.markdown("""
-  At least **8 characters**
-  At least **1 uppercase** letter (A-Z)
-  At least **1 lowercase** letter (a-z)
-  At least **1 digit** (0-9)
-  At least **1 special character** (e.g., ! @ # $ %)
-  Not be a **common password**
""")

# Input field
password = st.text_input(" Enter your password", type="password")

# Common password list
COMMON_PASSWORDS = {"123456", "password", "12345678", "qwerty", "abc123", "letmein", "123456789" }

# Function to check password strength
def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[ @!#$%^&*()<>?/\\|}{~:]", password) is None
    common_password_error = password.lower() in COMMON_PASSWORDS

    errors = {
        "Too Short (<8 chars)": length_error,
        "Missing Digit": digit_error,
        "Missing Uppercase Letter": uppercase_error,
        "Missing Lowercase Letter": lowercase_error,
        "Missing Special Symbol": symbol_error,
        "Too Common": common_password_error
    }

    score = 6 - sum(errors.values())

    if score == 6:
        strength = "Strong "
    elif score >= 4:
        strength = "Moderate "
    else:
        strength = "Weak "

    return strength, errors

# Show results
if password:
    st.divider()
    strength, error_details = check_password_strength(password)
    st.subheader(f"Password Strength: **{strength}**")

    st.markdown("###  Check Breakdown")
    for issue, is_error in error_details.items():
        st.write(f"{'' if is_error else ''} {issue}")

    if strength != "Strong ":
        st.info("Try making your password longer and include a mix of upper/lowercase letters, digits, and special characters.")
