import streamlit as st
import hashlib
import os

st.set_page_config(page_title="Login System", layout="centered")

# ------------- Helper Functions -------------

def make_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_hash(password, hashed_password):
    return make_hash(password) == hashed_password

def load_users():
    users = {}
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as f:
            for line in f:
                if ":" in line:
                    username, hashed = line.strip().split(":")
                    users[username] = hashed
    return users

def save_user(username, password):
    hashed = make_hash(password)
    with open("users.txt", "a") as f:
        f.write(f"{username}:{hashed}\n")

# ------------- Session State Setup -------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# ------------- Sidebar Menu -------------

menu = st.sidebar.radio("Menu", ["Login", "Sign Up"])

# ------------- Sign Up Section -------------

if menu == "Sign Up":
    st.header("📝 Create a New Account")
    new_user = st.text_input("Enter a username")
    new_pass = st.text_input("Create a password", type="password")
    confirm_pass = st.text_input("Confirm password", type="password")

    if st.button("Sign Up"):
        users = load_users()

        if new_user in users:
            st.error("❌ Username already exists. Try a different one.")
        elif new_pass != confirm_pass:
            st.error("❌ Passwords do not match.")
        elif new_user.strip() == "" or new_pass.strip() == "":
            st.warning("⚠️ Fields cannot be empty.")
        else:
            save_user(new_user, new_pass)
            st.success("✅ Account created successfully! Now go login.")
            st.balloons()

# ------------- Login Section -------------

elif menu == "Login":
    st.header("🔐 Login to Your Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        users = load_users()

        if username in users and verify_hash(password, users[username]):
            st.success(f"✅ Welcome, {username}!")
            st.session_state.logged_in = True
            st.session_state.username = username
        else:
            st.error("❌ Invalid username or password.")

# ------------- After Login -------------

if st.session_state.logged_in:
    st.sidebar.success(f"Logged in as {st.session_state.username}")
    st.markdown("### 🎉 You are now logged in.")
    st.info("Now you can build your dashboard, upload files, or track mood logs!")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.experimental_rerun()
