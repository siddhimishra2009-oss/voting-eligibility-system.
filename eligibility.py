MIN_AGE = 0
MAX_AGE = 120
VOTING_AGE = 18


def parse_age(text):
    try:
        age = int(str(text).strip())
    except ValueError:
        raise ValueError("Invalid input. Enter a whole number.")
    if age < MIN_AGE or age > MAX_AGE:
        raise ValueError("Invalid age. Age must be between 0 and 120.")
    return age


def check_eligibility(age, is_citizen):
    reasons = []
    years_left = 0
    if age >= VOTING_AGE and is_citizen:
        return True, reasons, years_left
    elif age < VOTING_AGE and not is_citizen:
        years_left = VOTING_AGE - age
        reasons = ["Under 18 years of age.", "Not an Indian citizen."]
    elif age < VOTING_AGE:
        years_left = VOTING_AGE - age
        reasons = ["Under 18 years of age."]
    else:
        reasons = ["Not an Indian citizen."]
    return False, reasons, years_left