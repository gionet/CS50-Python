from datetime import datetime, date, timedelta
import inflect
import sys
import re

p = inflect.engine()

class Date:
    # def __init__(self, year, month, day):
    #     self.year = year
    #     self.month = month
    #     self.day = day

    @classmethod
    def lived_duration(cls, userInput):
        days = date.today() - datetime.strptime(userInput, '%Y-%m-%d').date()
        return days.days

    @staticmethod
    def convert_minutes(day_count):
        return day_count * 24 * 60

    # def __str__(self):
    #     return f"Year: {self.year}, Month: {self.month}, Day: {self.day}"

def main():
    get = get_dates()

    # converting into minutes
    minutes = Date.convert_minutes(get)

    # converting into words
    t = p.number_to_words(minutes)

    # removing 'and' word
    words = re.sub(r"\s\band\b\s", " ", t)
    print(f'{words.capitalize()} minutes')
    sys.exit(0)

def get_dates():
    userInput = input("Date of Birth: ")

    try:
        return Date.lived_duration(userInput)

    except ValueError as e:
        # print(e)
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
