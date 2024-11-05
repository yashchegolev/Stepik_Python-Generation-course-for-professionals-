from datetime import datetime, date, timedelta
my_date = datetime.strptime(input(), '%d.%m.%Y')
print((my_date - timedelta(hours=24)).strftime('%d.%m.%Y'))
print((my_date + timedelta(hours=24)).strftime('%d.%m.%Y'))
