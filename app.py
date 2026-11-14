import streamlit as st

from eligibility import check_eligibility, parse_age

st.set_page_config(page_title="Voting Eligibility System", page_icon="🗳️")

if "history" not in st.session_state:
    st.session_state.history = []

st.title("🗳️ Voting Eligibility System")
st.caption(
    "A person is eligible to vote if age is 18 or more and the person is an "
    "Indian citizen. A valid age is a whole number from 0 to 120."
)

with st.form("voter_form", clear_on_submit=True):
    name = st.text_input("Name")
    age_text = st.text_input("Age")
    citizen = st.radio("Indian citizen?", ["y", "n"], horizontal=True,
                       format_func=lambda v: "Yes (y)" if v == "y" else "No (n)")
    submitted = st.form_submit_button("Check eligibility")

if submitted:
    if not name.strip():
        st.error("Please enter a name.")
    else:
        try:
            age = parse_age(age_text)
        except ValueError as err:
            st.error(str(err))
        else:
            eligible, reasons, years_left = check_eligibility(age, citizen == "y")
            name = name.strip()
            if eligible:
                st.success(f"{name} is eligible to vote.")
            else:
                st.warning(f"{name} is not eligible to vote.")
                st.write("**Reason:** " + " ".join(reasons))
                if years_left:
                    st.write(f"Years left to become eligible: {years_left}")
            st.session_state.history.append(
                {"Name": name, "Age": age,
                 "Citizen": "Yes" if citizen == "y" else "No",
                 "Result": "Eligible" if eligible else "Not eligible"}
            )

history = st.session_state.history
checked = len(history)
eligible_count = sum(1 for h in history if h["Result"] == "Eligible")

st.divider()
c1, c2, c3 = st.columns(3)
c1.metric("Voters checked", checked)
c2.metric("Eligible", eligible_count)
c3.metric("Not eligible", checked - eligible_count)

if history:
    st.dataframe(history, use_container_width=True, hide_index=True)
    if st.button("Reset"):
        st.session_state.history = []
        st.rerun()