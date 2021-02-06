"""Accepts time in seconds and convert it to hr, min, secs"""
sec_min = 60
sec_hr = 60 * sec_min
sec = int(input("Enter seconds: "))

hours = sec // sec_hr #Hours
sec %= sec_hr #Remaining seconds
minute = sec // sec_min
sec %= sec_min
if hours > 0: #print hours at all
    print(hours, end='')
    if hours == 1:
        print(" hour ", end='')
    else:
        print(" hours ", end='')
if minute > 0:
    print(minute, end='')
    if minute == 1:
        print(" minute ", end='')
    else:
        print(" minutes ", end='')

if sec > 0 or (hours == 0 and minute == 0 and sec == 0):
    print(sec, end='')
    if sec == 1:
        print(" second", end='')
    else:
        print(" seconds", end='')

print()
