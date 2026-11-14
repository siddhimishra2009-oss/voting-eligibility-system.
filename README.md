# 🗳️ Voting Eligibility System

**PS No. 25** | Programming Fundamentals and Logic Building Using Python (RU-100-01-00021)
Rungta International Skills University, School of Computer Science and Engineering (B.Tech CSE with AI and ML, in association with IBM)

A Python program that takes a person's name, age and citizenship, checks whether the person is eligible to vote, gives the reason when not eligible, and lets you check more voters in a loop. It comes as a **console app** (the assignment version) and a **Streamlit web app**.

**Rule:** a person is eligible if age is 18 or more **and** the person is an Indian citizen. A valid age is a whole number from 0 to 120.

**Concepts:** Conditions, Functions, Exceptions

## Project structure

```
voting-eligibility-system/
├── app.py                # Streamlit web app
├── eligibility.py        # core logic (check_eligibility, parse_age)
├── console_app.py        # single-file console version
├── tests/
│   └── test_eligibility.py
├── requirements.txt
└── README.md
```

## How to run

```bash
pip install -r requirements.txt

# Web app
streamlit run app.py

# Console version
python console_app.py

# Tests
python -m unittest discover tests
```

## Test cases

| # | Input | Expected output |
|---|-------|-----------------|
| 1. Normal | Aman, 25, y | Aman is eligible to vote. |
| 2. Boundary | (a) Neha, 18, y; (b) Ravi, 17, y | (a) Neha is eligible to vote. (b) Ravi is not eligible to vote. Years left to become eligible: 1 |
| 3. Invalid | Amit; age abc, -5, then 30; y | Invalid input. Enter a whole number. / Invalid age. Age must be between 0 and 120. / Amit is eligible to vote. |
| 4. Different | Riya, 30, n | Riya is not eligible to vote. Reason: Not an Indian citizen. Voters checked: 1 \| Eligible: 0 \| Not eligible: 1 |

## Future enhancements

- Save voter records in a file or SQLite database
- Take date of birth and calculate age automatically
- Voter ID verification
- Export results to CSV or PDF

- live app:https://voting-eligibility-system-siddhi.streamlit.app/
## Author

Name: SIDDHI MISHRA | RU Id: RU-26-02309
