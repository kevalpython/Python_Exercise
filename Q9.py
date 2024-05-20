from datetime import datetime, timedelta
import intervals as I

start_time = datetime(2024, 5, 18, 6, 4)  
end_time = datetime(2024, 5, 21, 6, 5)
    
if start_time < end_time:

    total_time = I.empty()
    current_time = start_time

    while current_time < end_time:
        day_start = current_time.replace(hour=6, minute=0, second=0)
        day_end = current_time.replace(hour=23, minute=59, second=59)
        if current_time < day_start:
            current_time = day_start
        
        interval_start = max(current_time, day_start)
        interval_end = min(end_time, day_end)
    
        if interval_start < interval_end:
            total_time |= I.closedopen(interval_start, interval_end)
    
        current_time = day_start + timedelta(days=1)
    
    total_seconds = 0
    for i in total_time:
        total_seconds += (i.upper - i.lower).total_seconds()
        
    total_hours = total_seconds / 3600
    print(f"Total hours : {total_hours:.2f}")
else:
    print("Please make sure that start time is greater than end time.")