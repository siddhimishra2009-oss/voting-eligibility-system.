def get_valid_age():
    while True:
        try:
            age = int(input("Age: ").strip())
        except ValueError:
            print("Invalid input. Enter a whole number.")
            continue
        if age < 0 or age > 120:
            print("Invalid age. Age must be between 0 and 120.")
            continue
        return age


def get_citizenship():
    while True:
        ans = input("Indian citizen (y/n): ").strip().lower()
        if ans in ("y", "n"):
            return ans == "y"
        print("Invalid input. Enter y or n.")


def check_eligibility(age, is_citizen):
    reasons = []
    years_left = 0
    if age >= 18 and is_citizen:
        return True, reasons, years_left
    elif age < 18 and not is_citizen:
        years_left = 18 - age
        reasons = ["Under 18 years of age.", "Not an Indian citizen."]
    elif age < 18:
        years_left = 18 - age
        reasons = ["Under 18 years of age."]
    else:
        reasons = ["Not an Indian citizen."]
    return False, reasons, years_left


def main():
    checked = eligible_count = not_eligible_count = 0

    while True:
        name = input("Name: ").strip()
        age = get_valid_age()
        is_citizen = get_citizenship()

        eligible, reasons, years_left = check_eligibility(age, is_citizen)
        checked += 1

        if eligible:
            eligible_count += 1
            print(f"{name} is eligible to vote.")
        else:
            not_eligible_count += 1
            print(f"{name} is not eligible to vote.")
            if age >= 18 or not is_citizen:
                print("Reason: " + " ".join(reasons))
            if years_left:
                print(f"Years left to become eligible: {years_left}")

        again = input("Check another voter? (y/n): ").strip().lower()
        if again != "y":
            break

    print(f"Voters checked: {checked} | Eligible: {eligible_count} "
          f"| Not eligible: {not_eligible_count}")


if __name__ == "__main__":
    main()