class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def day_extract(cls, date):
        try:
            day, month, year = date.split("-")
            return cls(int(day), int(month), int(year))
        except Exception:
            print("Invalid data")

    @staticmethod
    def date_validation(date):
        day, month, year = date.split("-")
        day = int(day)
        month = int(month)
        year = int(year)
        if month > 12 or month <= 0:
            print("Invalid date:check month")
        if day <= 0:
            print("Invalid date:check day")
        if day > 30:
            if month == 4 or month == 6 or month == 9 or month == 11:
                print("Invalid date: check day")
        if day > 31:
            print("Invalid date: check day")
        if day > 29:
            if month == 2:
                print("Invalid date: check day")
        else:
            print(f"The current date is {day} - {month} - {year}")

Date.date_validation("31--2021")












