## Exercise 1: Age Calculator
from datetime import date
birth = date.fromisoformat(input("Birthdate YYYY-MM-DD: "))
today = date.today()
age = today - birth
years = age.days // 365
months = (age.days % 365) // 30
days = (age.days % 365) % 30
print(f"{years} years, {months} months, {days} days")

## Exercise 2: Days Until Next Birthday
from datetime import date
birth = date.fromisoformat(input("Birthdate YYYY-MM-DD: "))
today = date.today()
next_birth = date(today.year, birth.month, birth.day)
if next_birth < today:
    next_birth = date(today.year + 1, birth.month, birth.day)
days = (next_birth - today).days
print(days)

## Exercise 3: Meeting Scheduler
from datetime import datetime, timedelta
current = datetime.fromisoformat(input("Current datetime YYYY-MM-DDTHH:MM: "))
hours, mins = map(int, input("Duration hours minutes: ").split())
end = current + timedelta(hours=hours, minutes=mins)
print(end)

## Exercise 4: Timezone Converter
from datetime import datetime
from pytz import timezone
dt_str = input("Datetime YYYY-MM-DDTHH:MM: ")
current_tz = timezone(input("Current TZ: "))
target_tz = timezone(input("Target TZ: "))
dt = datetime.fromisoformat(dt_str)
dt_current = current_tz.localize(dt)
dt_target = dt_current.astimezone(target_tz)
print(dt_target)

## Exercise 5: Countdown Timer
import time
from datetime import datetime
target = datetime.fromisoformat(input("Future datetime: "))
while True:
    now = datetime.now()
    if now >= target:
        print("Time up!")
        break
    remaining = target - now
    print(remaining)
    time.sleep(1)

## Exercise 6: Email Validator
import re
email = input("Email: ")
if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
    print("Valid")
else:
    print("Invalid")

## Exercise 7: Phone Number Formatter
phone = input("Phone: ").strip()
phone = re.sub(r"\D", "", phone)
if len(phone) == 10:
    print(f"({phone[:3]}) {phone[3:6]}-{phone[6:]}")
else:
    print("Invalid")

## Exercise 8: Password Strength Checker
password = input("Password: ")
if len(password) >= 8 and re.search(r"[A-Z]", password) and re.search(r"[a-z]", password) and re.search(r"\d", password):
    print("Strong")
else:
    print("Weak")

## Exercise 9: Word Finder
text = "sample text with word and word again"
word = input("Word: ")
occurrences = [m.start() for m in re.finditer(word, text)]
print(occurrences)

## Exercise 10: Date Extractor
import re
text = input("Text: ")
dates = re.findall(r"\d{4}-\d{2}-\d{2}", text)  # simple YYYY-MM-DD
print(dates)
