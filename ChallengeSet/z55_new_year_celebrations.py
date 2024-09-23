'''You're a pretty busy billionaire, and you often fly your personal Private Jet to remote places. Usually travel doesn't
bother you, but this time you are unlucky: it's New Year's Eve, and since you have to fly halfway around the world, you'll
probably have to celebrate New Year's Day in mid-air!

Your course lies west of your current location and crosses several time zones. The pilot told you the exact schedule: it is
known that you will take off at takeOffTime, and in minutes[i] after takeoff you will cross the ith border between time
zones. After crossing each border you will have to set your wrist watch one hour earlier (every second matters to you, so
you can't let your watch show incorrect time). It is guaranteed that you won't cross the IDL (i.e. after crossing each time
zone border your current time will be set one hour back).

You've been thinking about this situation and realized that it might be a good opportunity to celebrate New Year's Day more
than once, i.e. each time your wrist watch shows 00:00. Assuming that you set your watch immediately after the border is
crossed, how many times will you be able to celebrate this New Year's Day with a nice bottle of champagne? Note that the
answer should include celebrations both in mid-air and on the ground (it doesn't matter if the plane landed in the last time
zone before the midnight or not, you'll not let the last opportunity to celebrate New Year slip through your fingers).

Example

For takeOffTime = "23:35" and minutes = [60, 90, 140],
the output should be
solution(takeOffTime, minutes) = 3.

Here is the list of events by the time zones:

initial time zone:
at 23:35 your flight starts;
at 00:00 you celebrate New Year for the first time;
at 00:35 (60 minutes after the take off) you cross the first border;
time zone -1:
at 23:35 you cross the border (00:35 by your initial time zone);
at 00:00 you celebrate New Year for the second time (01:00 by your initial time zone);
at 00:05 (90 minutes after the take off) you cross the second border;
time zone -2:
at 23:05 you cross the border;
at 23:55 (140 minutes after the take off) you cross another border;
time zone -3:
at 22:55 you cross the border;
at 00:00 you celebrate New Year for the third time.
Thus, the output should be 3. That's a lot of champagne!

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string takeOffTime

The take off time in the 24-hour format "HH:MM". It is guaranteed that the given time is valid. The "00:00" time corresponds
to the midnight of 31st of December / 1st of January.

Guaranteed constraints:
"00" ≤ HH ≤ "23",
"00" ≤ MM ≤ "59".

[input] array.integer minutes

A strictly increasing array of integers. minutes[i] stands for the number of minutes from the take off to crossing the ith
time zone border.

Guaranteed constraints:
0 ≤ minutes.length ≤ 20,
1 ≤ minutes[i] ≤ 1500.

[output] integer

The number of times you will be able to celebrate New Year's Day.'''
from datetime import datetime, timedelta

def f(t0, m):
    t0 = f"2024-01-01 {t0}" if t0 == "00:00" else f"2023-12-31 {t0}"
    date = datetime.strptime(t0, "%Y-%m-%d %H:%M")
    last_year, accu_time, c = date.year, 0, 0

    for i in m:
        i -= accu_time
        if date.hour == 0 and date.minute == 0: c += 1
        date += timedelta(minutes=i)
        if last_year < date.year: c += 1
        date -= timedelta(hours=1)
        last_year, accu_time = date.year, accu_time + i

    return c + (1 if date.year == 2023 or (date.hour == 0 and date.minute == 0) else 0)
