#!/usr/bin/env python3
"""Find optimal meeting slots respecting timezones and working hours."""
import json, sys
from datetime import datetime, timedelta

WORKING_HOURS = (9, 17)  # 9 AM - 5 PM

def find_slots(data):
    duration_min = data.get("duration", 30)
    attendee_tzs = data.get("timezones", ["UTC"])
    days_ahead = data.get("days_ahead", 5)
    
    slots = []
    now = datetime.now()
    for day in range(1, days_ahead + 1):
        date = now + timedelta(days=day)
        if date.weekday() >= 5:  # skip weekends
            continue
        for hour in range(WORKING_HOURS[0], WORKING_HOURS[1]):
            # Check if hour works for all timezones
            works_for_all = True
            for tz_offset in [int(tz) for tz in attendee_tzs if tz.lstrip('-').isdigit()]:
                local_hour = hour + tz_offset
                if local_hour < WORKING_HOURS[0] or local_hour >= WORKING_HOURS[1]:
                    works_for_all = False
                    break
            if works_for_all:
                slots.append({"date": date.strftime("%Y-%m-%d"), "time": f"{hour:02d}:00", "duration": duration_min})
    return {"slots": slots[:5], "total_found": len(slots)}

if __name__ == "__main__":
    print(json.dumps(find_slots(json.loads(sys.argv[1])), indent=2))
