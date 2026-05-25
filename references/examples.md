# Calendar Examples

## Example 1: "Schedule a meeting with Sarah and Tom next week"
```
find_free_time(attendees: ["sarah@co.com", "tom@co.com"], duration: 30, range: "next_week")
→ 3 available slots
```
Response: "Found 3 slots:\n1. Mon 10:00-10:30\n2. Tue 14:00-14:30\n3. Thu 11:00-11:30\nWhich works?"

## Example 2: "What's on my calendar today?"
```
list_events(calendar: "primary", date: "today")
→ [{title: "Standup", time: "9:00-9:15"}, {title: "Sprint Planning", time: "10:00-11:00"}, {title: "Client Call", time: "14:00-14:30"}]
```
Response: "Today's schedule:\n- 9:00 Standup (15 min)\n- 10:00 Sprint Planning (1h)\n- 14:00 Client Call (30 min)\n\n3 meetings, 1h 45m total. Free: 11:00-14:00."

## Example 3: "Cancel the Thursday meeting"
```
search_events(query: "Thursday") → [{id: "evt_123", title: "Design Review", date: "Thu 11:00"}]
delete_event(id: "evt_123", notify_attendees: true)
```
Response: "✅ Cancelled 'Design Review' (Thu 11:00). Attendees notified."
