import streamlit as st

st.title(" Course Manager")
st.header(" Course Management Dashboard")
st.caption("MISY350")
st.divider()


#Step 2 Defining Assignments 
assignments=[
    {
        "id":"HW1",
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

# Step 3 Add new Assignment Section (Inputs & Layout)
st.subheader("Add New Assignment")
with st.container(border=True):
   col1,col2=st.columns(2)
 
with col1:
    with st.container(border=True):
     st.markdown("## Assignment Details")
     title=st.text_input("Assignment title",placeholder="homework")
     description=st.text_input("Assignment Description")
     points=st.number_input("Points")
with col2:
   due_date=st.date_input("Due Date")
   type=st.radio("type",["Homework", "Lab"])



