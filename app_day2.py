import streamlit as st

st.title("Course Management Apps")
st.header("Assignment")
st.subheader("Assignments Manager")

next_assignment_id_number=3

tab1, tab2, tab3= st.tabs(["View Assignments", "Add new Assignments", "Update an Assignment"])





st.divider()

assignments=[
    {    "id":"HW1",
        "title":"Introduction to Database",
        "description": "basics of database design",
        "points":100,
        "type":"homework"},
    
    {
        "id": "HW2",
        "title":"Normalization",
        "description": "Normalize the table design",
        "points":100,
        "type":"lab"}
]

# Add new assignment 
st.markdown("# Add New Assignment")

#input
title= st.text_input("Title", placeholder="ex. Homework 1", help="This is the name of the assignment")

description=st.text_area("Description", placeholder="ex. database design....")
due_date=st.date_input("Due Date")
assignments_type=st.radio("Type",["Homework","Lab"])
#assignments_type2=st.selectbox("Type",["Homework","Lab"])
#if assignments_type2 == "Other":
#assignments_type2=st.text_input("Assignment Type")

#assignment_type3= st.checkbox("Assignment Type")

#labs=st.checkbox("Lab")

with st.expander("Assignment Preview",expanded=True):
    st.markdown("## Live Preview")
    st.markdown(f"Title: {title}")

btn_save=st.button("Save", use_container_width=100, disabled=False)

import time 

import json
from pathlib import Path 

json_path=Path("assignments.json")


if btn_save:
    with st.spinner("Saving the Assignment"):
        time.sleep(5)
        if title=='':
            st.warning("Enter Assignment Title")
        else:
             #Create a new assignment 
            new_assignment_id="HW_" +str(next_assignment_id_number)
            next_assignment_id_number +=1
            
            assignments.append(
                {"id": new_assignment_id,
                 "title": title,
                 "description": description,
                   "points": 100,
                   "type": assignments_type})


            with json_path.open("w",encoding="utf-8") as f:
                json.dump(assignments,f)
            
            st.success("Assignment is recorded!")
            st.dataframe(assignments)
