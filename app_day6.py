import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import uuid
import time

json_file = Path("users.json")
users = []
if json_file.exists():
    with open(json_file, "r") as f:
        users = json.load(f)
        

#login

st.set_page_config(page_title="Course Manager", layout="centered")
st.title("Course Manager App")

users= [
    {"id":"1",
     "email":" admin@school.edu",
     "password":"ABC123",
     "role":"admin",
     "registered_at":",,,"}
]

st.subheader("Log In")
with st.container(border=True):
    email_input = st.text_input("Email", key="login_email")
    password_input = st.text_input("Password", type="password", key="login_password")
    
    if st.button("Log In", type="primary", use_container_width=True):
        with st.spinner("Logging in..."):
            time.sleep(2) # Fake backend delay
            
            # Find user
            found_user = None
            for user in users:
                if user["email"].strip().lower() == email_input.strip().lower() and user["password"] == password_input:
                    found_user = user
                    break
            
            if found_user:
                st.success(f"Welcome back, {found_user['email']}!")
                time.sleep(2)
                st.rerun()
            else:
                st.error("Invalid credentials")


# Registration 
st.subheader("New Instructor Account")
with st.container(border=True):
    new_email = st.text_input("Email Address", key="reg_email")
    new_password = st.text_input("Password", type="password", key="reg_password")
    
    if st.button("Create Account"):
        with st.spinner("Creating account..."):
            time.sleep(2) # Fake backend delay
            # ... (Assume validation logic here) ...
            users.append({
                "id": str(uuid.uuid4()),
                "email": new_email,
                "password": new_password,
                "role": "Instructor"
            })
            #with open(json_file, "w") as f:
               #json.dump(users, f, indent=4)
            st.success("Account created!")
            st.rerun()

st.write("---")
st.dataframe(users)