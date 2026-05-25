# Calendar Tool Sequences

## Tools (10)
| Tool | Purpose |
|------|---------|
| `list_calendars` | Available calendars |
| `list_events` | Events in range |
| `create_event` | Book meeting |
| `update_event` | Reschedule/modify |
| `delete_event` | Cancel event |
| `find_free_time` | Free/busy lookup |
| `rsvp_event` | Accept/decline |
| `get_event` | Event details |
| `search_events` | Search by text |
| `list_attendees` | Who's invited |

## Sequence: Schedule Meeting (2-3 calls)
```
1. find_free_time(attendees: ["sarah@co.com", "tom@co.com"], duration: 30, range: "next_5_days")
   → [{start: "2025-01-20T10:00", end: "2025-01-20T10:30"}, {start: "2025-01-20T14:00", ...}]
2. [User picks slot]
3. create_event(title: "Deal Review — Acme", start: "2025-01-20T10:00", end: "2025-01-20T10:30", attendees: [...], description: "Discuss proposal feedback")
```

## Sequence: View Today (1 call)
```
list_events(calendar: "primary", start: "today 00:00", end: "today 23:59")
→ [{title: "Standup", time: "9:00"}, {title: "Client call", time: "14:00"}, ...]
```
