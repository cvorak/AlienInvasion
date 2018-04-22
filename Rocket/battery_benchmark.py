import datetime as dt
"""Simple script that leaves battery info in 'timestamps.txt'"""

def format_duration(duration):
    duration = round(duration)
    hours = duration // 3600
    left = duration - hours * 3600
    minutes = left // 60
    left -= minutes * 60
    seconds = left
    return str(hours) + ":" + str(minutes) + ":" + str(seconds)

begin_time = dt.datetime.now()

while True:
    with open('timestamps.txt', 'w') as f_obj:
        current_time = dt.datetime.now()
        f_obj.write("Begin time: " + str(begin_time.time()) + "\n" + "End time: " + str(current_time.time()))
        
        # Calculate duration in seconds:
        duration = (current_time - begin_time).total_seconds()
        f_obj.write("\n\nBattery lasted for: " + format_duration(duration))






