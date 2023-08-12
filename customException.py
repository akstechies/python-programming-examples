class CustomError(Exception):
    def __init__(self, message):
        self.message = message

def calculate_age(year_born):
    current_year = 2023
    if year_born > current_year:
        raise CustomError("Invalid year of birth")
    return current_year - year_born

try:
    age = calculate_age(2050)
    print("Age:", age)
except CustomError as e:
    print("Error:", e.message)
