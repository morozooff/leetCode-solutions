class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        weekday_value = {
            '0': 'Thursday',
            '1': 'Friday',
            '2': 'Saturday',
            '3': 'Sunday',
            '4': 'Monday',
            '5': 'Tuesday',
            '6': 'Wednesday'
        }
        bissextile_flag = 0

        diff = year - 1971
        leap_days = diff // 4
        kare_remain = diff % 4

        if kare_remain == 1:
            bissextile_flag = 1
        elif kare_remain >= 2:
            leap_days += 1

        if year == 2100:
            bissextile_flag = 0

        days_before_current_year = diff*365 + leap_days

        days_before_current_month = 0
        for current_month in range(month - 1):
            if current_month == 1:
                days_before_current_month += 28 + bissextile_flag
            elif current_month == 7:
                days_before_current_month += 31
            elif current_month > 7:
                if current_month % 2 == 0:
                    days_before_current_month += 30
                elif current_month % 2 == 1:
                    days_before_current_month += 31
            elif current_month % 2 == 0:
                days_before_current_month += 31
            elif current_month % 2 == 1:
                days_before_current_month += 30

        days_before_date = days_before_current_year + days_before_current_month + day
        remainder = days_before_date%7
        return weekday_value[str(remainder)]


day = 30
month = 9
year = 2100

