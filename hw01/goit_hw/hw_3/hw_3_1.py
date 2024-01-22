import datetime
def get_days_from_today(date):
    date_now = datetime.datetime.today()
    date_from = datetime.datetime.strptime(date, "%Y-%m-%d")
    return date_now.toordinal() - date_from.toordinal()
print(get_days_from_today("2022-02-24"))