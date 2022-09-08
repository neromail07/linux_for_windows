time = int(input('Укажите продолжительность в секундах: '))

min = 60
hour = 3600
day = 86400

if time < min:
    print(f'{time} sec')
elif time >= min and time < hour:
    res_min = time // min
    res_sec = time % min
    print(f'{res_min} min,{res_sec} sec')
elif time >= hour and time < day:
    res_hour = time // hour
    time = time % hour
    res_min = time // min
    res_sec = time % min
    print(f'{res_hour} hours,{res_min} min,{res_sec} sec')
elif time >= day :
    res_day = time // day
    time = time % day
    res_hour = time // hour
    time = time % hour
    res_min = time // min
    res_sec = time % min
    print(f'{res_day} day,{res_hour} hours,{res_min} min,{res_sec} sec')
