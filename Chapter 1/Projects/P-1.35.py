from random import randint
from datetime import datetime, timedelta

def random_birthdays(number_of_people):
    first_day_of_year = datetime(2017,1,1)
    return[first_day_of_year + timedelta(days=randint(0, 365))
    for _ in range(number_of_people)]

def determine_probality(number_of_people, run_amount = 1_000):
    dups_found = 0
    for _ in range(run_amount):
        birthdays = random_birthdays(number_of_people)
        duplicates = set(x for x in birthdays if birthdays.count(x) > 1)
        if len(duplicates) >= 1:
            dups_found += 1

    return dups_found/run_amount * 100

if __name__ == '__main__':
    msg = ("{people} Random people have a {chance:.1f}%"
    " chance of having a birthday on the same day")
    for people in (23, 100):
        print(msg.format(people = people,
         chance = determine_probality(people)))

#https://codecalamity.com/the-birthday-paradox-the-proof-is-in-the-python/#:~:text=the%20Birthday%20Paradox%20with%20some,is%20a%2099.9%20percent%20chance.