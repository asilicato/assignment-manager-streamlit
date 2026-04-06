import streamlit as st
import json
from pathlib import Path
from datetime import datetime, date
import pandas as pd

st.set_page_config(
    page_title="Excused Absence App",
    layout="wide",
    initial_sidebar_state="expanded"
)

json_path_requests = Path("requests.json")

default_requests = [
    {
        "request_id": "01121212",
        "status": "Pending",
        "course_id": "011101",
        "student_email": "jsmith@university.edu",
        "absence_date": "2026-03-25",
        "submitted_timestamp": "2026-03-19 08:30:00",
        "excuse_type": "Medical",
        "explanation": "I have a scheduled doctor's appointment that I cannot reschedule.",
        "instructor_note": ""
    }
]

# Load data
if json_path_requests.exists():
    with open(json_path_requests, "r", encoding="utf-8") as f:
        requests = json.load(f)
else:
    requests = default_requests
    with open(json_path_requests, "w", encoding="utf-8") as f:
        json.dump(requests, f, indent=4)

# Fix old records that are missing fields
updated = False
for i, request in enumerate(requests):
    if "request_id" not in request:
        request["request_id"] = f"{i+1:06d}"
        updated = True
    if "instructor_note" not in request:
        request["instructor_note"] = ""
        updated = True

if updated:
    with open(json_path_requests, "w", encoding="utf-8") as f:
        json.dump(requests, f, indent=4)

# Session state
if "page" not in st.session_state:
    st.session_state["page"] = "dashboard"

if "selected_request" not in st.session_state:
    st.session_state["selected_request"] = None

# Sidebar
st.sidebar.title("Navigation")

if st.sidebar.button("Dashboard", use_container_width=True):
    st.session_state["page"] = "dashboard"

if st.sidebar.button("Request", use_container_width=True):
    st.session_state["page"] = "request"

# Dashboard Page
if st.session_state["page"] == "dashboard":
    st.title("Excused Absences")

    total_requests = len(requests)
    pending_requests = sum(1 for r in requests if r["status"] == "Pending")

    spacer, metric1, metric2 = st.columns([5, 1.5, 1.5])

    with metric1:
        st.metric("Count", total_requests)

    with metric2:
        st.metric("Pending", pending_requests)

    st.markdown("---")

    filter_col1, filter_col2 = st.columns([3, 1.2])

    with filter_col1:
        search_email = st.text_input("Search by student Email")

    with filter_col2:
        status_filter = st.selectbox(
            "Status",
            ["All", "Pending", "Approved", "Cancelled"]
        )

    filtered_requests = requests.copy()

    if search_email:
        filtered_requests = [
            r for r in filtered_requests
            if search_email.lower() in r["student_email"].lower()
        ]

    if status_filter != "All":
        filtered_requests = [
            r for r in filtered_requests
            if r["status"] == status_filter
        ]

    left_col, right_col = st.columns([3.2, 1.4])

    with left_col:
        if filtered_requests:
            df = pd.DataFrame(filtered_requests)

            display_df = df[
                [
                    "request_id",
                    "status",
                    "course_id",
                    "student_email",
                    "absence_date",
                    "submitted_timestamp",
                    "excuse_type",
                    "explanation"
                ]
            ]

            event = st.dataframe(
                display_df,
                use_container_width=True,
                hide_index=True,
                on_select="rerun",
                selection_mode="single-row"
            )

            if event.selection.rows:
                selected_index = event.selection.rows[0]
                st.session_state["selected_request"] = filtered_requests[selected_index]
        else:
            st.info("No matching requests found.")

    with right_col:
        st.subheader("Selected Request Details")

        selected_request = st.session_state["selected_request"]

        if selected_request is not None:
            st.markdown(f"**{selected_request['status']}**")
            st.write(selected_request["student_email"])
            st.write(selected_request["course_id"])
            st.write(selected_request["absence_date"])
            st.write(selected_request["submitted_timestamp"])
            st.write(selected_request["excuse_type"])
            st.write(selected_request["explanation"])

            st.markdown("### Update Request")

            status_options = ["Pending", "Approved", "Cancelled"]
            current_status_index = status_options.index(selected_request["status"])

            new_status = st.selectbox(
                "Update Status",
                status_options,
                index=current_status_index,
                key="dashboard_status_select"
            )

            new_note = st.text_area(
                "Instructor Note",
                value=selected_request["instructor_note"],
                key="dashboard_instructor_note_textarea"
            )

            btn1, btn2 = st.columns(2)

            with btn1:
                if st.button("Save Update", use_container_width=True):
                    for request in requests:
                        if request["request_id"] == selected_request["request_id"]:
                            request["status"] = new_status
                            request["instructor_note"] = new_note
                            break

                    with open(json_path_requests, "w", encoding="utf-8") as f:
                        json.dump(requests, f, indent=4)

                    st.success("Request updated successfully.")
                    st.session_state["selected_request"] = None
                    st.rerun()

            with btn2:
                if st.button("Clear Selection", use_container_width=True):
                    st.session_state["selected_request"] = None
                    st.rerun()

        else:
            st.info("Select a row from the table to view details.")

# Request Page
elif st.session_state["page"] == "request":
    st.title("Excused Absence Request")

    with st.form("excused_absence_form"):
        student_email = st.text_input("Student Email")
        absence_date = st.date_input("Absence Date", value=date.today())
        excuse_type = st.selectbox(
            "Excuse Type",
            ["Medical", "University Competitions", "Other"]
        )
        explanation = st.text_area("Student Explanation / Reason")

        submit_request = st.form_submit_button("Submit Request")

        if submit_request:
            new_request = {
                "request_id": datetime.now().strftime("%H%M%S%f"),
                "status": "Pending",
                "course_id": "011101",
                "student_email": student_email,
                "absence_date": absence_date.strftime("%Y-%m-%d"),
                "submitted_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "excuse_type": excuse_type,
                "explanation": explanation,
                "instructor_note": ""
            }

            requests.append(new_request)

            with open(json_path_requests, "w", encoding="utf-8") as f:
                json.dump(requests, f, indent=4)

            st.success("Excused absence request submitted successfully.")
            st.session_state["page"] = "dashboard"
            st.rerun()

