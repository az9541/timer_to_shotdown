import time
import os


def summ_time(hour, min):
    min_to_hours = min // 60
    new_min = min % 60
    hour += min_to_hours
    if hour >= 24:
        hour = abs(24 - hour)
    return hour, new_min


def pc_shotdown():
    hours_shotdown = int(input('Hours before shotdown: '))
    minutes_to_shotdown = int(input('Minutes before shotdown: '))
    shot_time = summ_time(hours_shotdown + time.gmtime().tm_hour + 5, time.gmtime().tm_min + minutes_to_shotdown)
    print('The computer will be turned off in {}H/{}M'.format(shot_time[0], shot_time[1]))

    while True:
        shotdown_hour_time = time.gmtime().tm_hour + 5
        if shotdown_hour_time >= 24:
            shotdown_hour_time = abs(24 - shotdown_hour_time)
        if shotdown_hour_time < shot_time[0]:
            time.sleep(60)
        else:
            if time.gmtime().tm_min < shot_time[1]:
                time.sleep(1)
            else:
                os.system("shutdown -s")
                break


pc_shotdown()
