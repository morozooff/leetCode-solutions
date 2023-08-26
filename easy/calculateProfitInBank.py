def totalMoney(n: int) -> int:
    def calculate_money_for_current_week(week, full_days):
        start_with = week + 1
        profit = sum(range(start_with, start_with + full_days))
        return profit

    full_weeks = n // 7
    non_full_week = n % 7
    base_profit = 0
    if full_weeks != 0:
        base_profit = calculate_money_for_current_week(0, 7)
    full_profit = 0

    for week in range(full_weeks):
        full_profit += base_profit + 7 * week

    full_profit += calculate_money_for_current_week(full_weeks, non_full_week)

    return full_profit


print(totalMoney(4))