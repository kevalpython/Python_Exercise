"""
Difference between start time and end time
"""

from datetime import datetime, timedelta

import intervals as I

START_TIME = datetime(2024, 5, 18, 6, 4)
END_TIME = datetime(2024, 5, 21, 6, 5)

if START_TIME < END_TIME:
    total_time = I.empty()
    current_time = START_TIME

    while current_time < END_TIME:
        day_start = current_time.replace(hour=6, minute=0, second=0)
        day_end = current_time.replace(hour=23, minute=59, second=59)
        current_time = max(current_time, day_start)  # Simplified line

        interval_start = max(current_time, day_start)
        interval_end = min(END_TIME, day_end)

        if interval_start < interval_end:
            total_time |= I.closedopen(interval_start, interval_end)

        current_time = day_start + timedelta(days=1)

    TOTAL_SECONDS = sum(
        (i.upper - i.lower).total_seconds() for i in total_time
    )  # Simplified total seconds calculation
    TOTAL_HOURS = TOTAL_SECONDS / 3600
    print(f"Total hours : {TOTAL_HOURS:.2f}")
else:
    print("Please make sure that start time is greater than end time.")
