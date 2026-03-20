import streamlit as st
import json
from pathlib import Path
from datetime import datetime, date

st.set_page_config(page_title="Excused Absence App", layout="wide", initial_sidebar_state="expanded")

json_path_requests = Path("requests.json")

default_requests = [
    {   "request_id":"01121212",
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

#Loading the data
if json_path_requests.exists():
    with open(json_path_requests, "r", encoding="utf-8") as f:
        requests = json.load(f)
else:
    requests = default_requests
    with open(json_path_requests, "w", encoding="utf-8") as f:
        json.dump(requests, f, indent=4)


if "page" not in st.session_state:
    st.session_state["page"] = "dashboard"

if "selected_request" not in st.session_state:
    st.session_state["selected_request"] = None

#Building the Sidebar
st.sidebar.title("Navigation")

if st.sidebar.button("Excused Absence Dashboard"):
    st.session_state["page"] = "dashboard"

if st.sidebar.button("Excused Absence Request"):
    st.session_state["page"] = "request"


#Dashboard 
if st.session_state["page"] == "dashboard":
    st.title("Excused Absence Dashboard")

    col1, col2 = st.columns([3, 1])

    with col1:
        if len(requests) > 0:
            event = st.dataframe(
                requests,
                use_container_width=True,
                on_select="rerun",
                selection_mode="single-row"
            )

            if event.selection.rows:
                selected_index = event.selection.rows[0]
                st.session_state["selected_request"] = requests[selected_index]
        else:
            st.warning("No requests have been submitted yet.")

    with col2:
        st.metric("Total Requests", len(requests))

    if st.session_state["selected_request"] is not None:
        selected_request = st.session_state["selected_request"]

        st.markdown("---")
        st.subheader("Selected Request Details")

        st.write(f"**Status:** {selected_request['status']}")
        st.write(f"**Course ID:** {selected_request['course_id']}")
        st.write(f"**Student Email:** {selected_request['student_email']}")
        st.write(f"**Absence Date:** {selected_request['absence_date']}")
        st.write(f"**Submitted Timestamp:** {selected_request['submitted_timestamp']}")
        st.write(f"**Excuse Type:** {selected_request['excuse_type']}")
        st.write(f"**Student Explanation / Reason:** {selected_request['explanation']}")
        st.write(f"**Instructor Note:** {selected_request['instructor_note']}")

        st.markdown("---")
        st.subheader("Update Request")

        new_status = st.selectbox(
            "Update Status",
            ["Pending", "Cancelled", "Approved"],
            index=["Pending", "Cancelled", "Approved"].index(selected_request["status"]),
            key="dashboard_status_select"
        )

        new_note = st.text_area(
            "Instructor Note",
            value=selected_request["instructor_note"],
            key="dashboard_instructor_note_textarea"
        )

        col_update1, col_update2 = st.columns(2)

        with col_update1:
            if st.button("Save Update", key="dashboard_save_update_btn", use_container_width=True):
                for request in requests:
                    if (
                        request["student_email"] == selected_request["student_email"]
                        and request["submitted_timestamp"] == selected_request["submitted_timestamp"]
                    ):
                        request["status"] = new_status
                        request["instructor_note"] = new_note
                        break

                with open(json_path_requests, "w", encoding="utf-8") as f:
                    json.dump(requests, f, indent=4)

                st.success("Request updated successfully.")
                st.session_state["selected_request"] = None
                st.rerun()

        with col_update2:
            if st.button("Clear Selection", key="dashboard_clear_selection_btn", use_container_width=True):
                st.session_state["selected_request"] = None
                st.rerun()

# Request Form Page
elif st.session_state["page"] == "request":
    st.title("Excused Absence Request")

    with st.form("excused_absence_form"):
        student_email = st.text_input("Student Email", key="request_student_email_input")
        absence_date = st.date_input("Absence Date", value=date.today(), key="request_absence_date_input")
        excuse_type = st.selectbox(
            "Excuse Type",
            ["Medical", "University Competitions", "Other"],
            key="request_excuse_type_select"
        )
        explanation = st.text_area("Student Explanation / Reason", key="request_explanation_textarea")

        submit_request = st.form_submit_button("Submit Request")

        if submit_request:
            date_str = absence_date.strftime("%Y-%m-%d")

            new_request = {
                "request_id": datetime.now().strftime("%H%M%S%f"),
                "status": "Pending",
                "course_id": "011101",
                "student_email": student_email,
                "absence_date": date_str,
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


