class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def extract_date(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        return cls(f"{day}-{month}-{year}")

    @staticmethod
    def validate_date(date_str):
        day, month, year = map(int, date_str.split('-'))
        if day < 1 or day > 31:
            return False
        if month < 1 or month > 12:
            return False
        if year < 1900 or year > 2023:
            return False
        return True


date_string = "24-04-2023"

if Date.validate_date(date_string):
    date_obj = Date.extract_date(date_string)
    print(date_obj.date)  # выведет "26-5-2021"
else:
    print("Некорректная дата")
