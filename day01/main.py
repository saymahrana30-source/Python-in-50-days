"""
Day 1 — Profile Card Generator
Practices: variables, data types, type conversion, input/output, f-strings
"""


def get_user_info():
    """Collect basic info from the user and return it as a dict."""
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    city = input("Enter your city: ")
    height_cm = float(input("Enter your height in cm: "))

    return {
        "name": name,
        "age": age,
        "city": city,
        "height_cm": height_cm,
    }


def print_profile_card(info):
    """Print a formatted profile card using f-strings."""
    height_m = info["height_cm"] / 100

    print("\n" + "=" * 30)
    print("        PROFILE CARD")
    print("=" * 30)
    print(f"Name    : {info['name']}")
    print(f"Age     : {info['age']} years old")
    print(f"City    : {info['city']}")
    print(f"Height  : {info['height_cm']} cm ({height_m:.2f} m)")
    print("=" * 30)

    # A bit of type-based logic to practice bool/comparison too
    is_adult = info["age"] >= 18
    print(f"Adult   : {is_adult}")


if __name__ == "__main__":
    user_info = get_user_info()
    print_profile_card(user_info)
