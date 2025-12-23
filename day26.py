def calculate_fine(date_returned, date_due):
    day_returned, month_returned, year_returned = date_returned
    day_due, month_due, year_due = date_due

    if year_returned > year_due:
        return 10000
    elif year_returned == year_due:
        if month_returned > month_due:
            return 500 * (month_returned - month_due)
        elif month_returned == month_due:
            if day_returned > day_due:
                return 15 * (day_returned - day_due)

    return 0

date_returned = list(map(int, input().strip().split()))
date_due = list(map(int, input().strip().split()))
print(calculate_fine(date_returned, date_due))