class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day} day {self.month} month {self.year} year"

    @classmethod
    def get_date(cls, dd_mm_yy):
        a, b, c = map(int, dd_mm_yy.split("-"))
        return cls(a, b, c)

    @staticmethod
    def validate(day, month, year):
        if 0 < day <= 31 and 0 < month <= 12 and 0 <= year <= 2022:
            print("valid date entry")
        else:
            print("invalid date entry")


data_1 = Data.get_date("22-12-2021")
print(data_1)
Data.validate(22, 12, 2021)
Data.validate(0, 11, 2021)
