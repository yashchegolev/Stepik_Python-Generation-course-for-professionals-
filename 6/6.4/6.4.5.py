import csv
from collections import namedtuple
from datetime import datetime

Friends = namedtuple('Friends', ['surname', 'name', 'meeting_date', 'meeting_time'] )

with open('6.4.5_meetings.csv', mode='r', encoding='utf-8') as file_in:
    rows = list(csv.reader(file_in))[1:]
    friends = []
    for row in rows:
        surname, name, meeting_date, meeting_time = row
        friends.append(Friends(surname, name, meeting_date, meeting_time))
result = sorted([friend._asdict() for friend in friends], key=lambda x: datetime.strptime(x['meeting_date'] + ' ' + x['meeting_time'], '%d.%m.%Y %H:%M'))
'''
print(*result, sep='\n')
'''
for friend in result:
    print(friend['surname'], friend['name'])
