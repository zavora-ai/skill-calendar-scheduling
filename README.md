# Calendar & Scheduling Skill

> Smart scheduling for AI agents — find free time across timezones, book meetings, manage events, and coordinate calendars via Google Calendar and Microsoft Graph.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--calendar-green)](https://github.com/zavora-ai/mcp-calendar)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

This skill orchestrates 10 calendar tools into **timezone-aware scheduling workflows** — ensuring meetings never double-book, always have a purpose, and respect working hours.

| Workflow | Tool Calls | What It Achieves |
|----------|-----------|------------------|
| Schedule Meeting | 2-3 | Check availability → present options → book |
| Find Free Time | 1 | Overlapping free slots across attendees |
| View Schedule | 1 | Today's agenda with gaps highlighted |
| Manage Events | 1-2 | Reschedule or cancel with notifications |

### Without this skill:
- Double-bookings because availability wasn't checked
- Meetings scheduled outside attendee's working hours
- No agenda or purpose in calendar invites
- Back-to-back meetings with no buffer time
- Timezone confusion for distributed teams

### With this skill:
- Always checks free/busy before creating events
- Respects working hours per timezone
- Every meeting has title + description + agenda
- 5-minute buffer enforced between meetings
- Times confirmed in each attendee's local timezone

## Installation

### Claude Code
```bash
git clone https://github.com/zavora-ai/skill-calendar-scheduling.git \
  ~/.skills/skills/calendar-scheduling
```

### ADK-Rust
```bash
cp -r calendar-scheduling /path/to/project/.skills/skills/
```

### Claude.ai
Download ZIP → Settings > Capabilities > Skills > Upload

## Requirements

**Required:**
- `mcp-calendar` server connected (Google Calendar or Microsoft Graph)

**Cross-MCP integrations:**
- `mcp-crm` — schedule customer meetings when deals advance
- `mcp-email` — send meeting follow-ups and summaries
- `mcp-itsm` — book change implementation windows
- `mcp-customer-service` — schedule check-ins for at-risk customers

## Folder Structure

```
calendar-scheduling/
├── SKILL.md                       # Decision tree + 4 workflows + scheduling rules
├── scripts/
│   └── find_slots.py              # Timezone-aware slot finder (working hours filter)
├── references/
│   ├── tool-sequences.md          # 10 tools with exact call patterns
│   ├── cross-mcp-workflows.md     # Calendar + CRM + ITSM + CS orchestration
│   └── examples.md                # 3 real scenarios with traces
├── README.md
└── LICENSE
```

## How It Works

### Decision Tree

```
User request arrives
├── "schedule", "book", "meeting"? → Find free time → Create event
├── "free", "available", "when can"? → Find overlapping slots
├── "what's on", "today", "agenda"? → List events for period
├── "reschedule", "cancel"? → Update or delete event
```

### Scheduling Rules (enforced automatically)

1. **Always check availability** before creating events
2. **Respect working hours** (9-17 in attendee's timezone)
3. **5-minute buffer** between back-to-back meetings
4. **Include purpose** — no mystery meetings
5. **Confirm timezone** when attendees span multiple zones

## Example

**User:** "Schedule a 30-min meeting with Sarah and Tom next week"

**Agent behavior:**
1. Calls `find_free_time` for both attendees (30 min, next 5 days)
2. Filters by working hours in both timezones
3. Presents top 3 options
4. On selection: creates event with title, attendees, description

**Result:**
```
Found 3 available slots:
1. Mon 10:00-10:30 (10 AM EAT / 8 AM CET)
2. Tue 14:00-14:30 (2 PM EAT / 12 PM CET)
3. Thu 11:00-11:30 (11 AM EAT / 9 AM CET)

Which works? I'll include a meeting description.
```

## Success Criteria

| Metric | Target |
|--------|--------|
| Trigger rate | 90% on scheduling queries |
| No double-bookings | Always check availability first |
| Timezone accuracy | Confirm times in attendee's local zone |
| Meeting quality | Every event has title + description |

## Scripts

### `find_slots.py`
Finds optimal meeting slots respecting timezones and working hours:
```bash
python scripts/find_slots.py '{"duration": 30, "timezones": ["3", "-1"], "days_ahead": 5}'
# → {"slots": [{"date": "2025-01-20", "time": "10:00"}, ...], "total_found": 8}
```

## MCP Server Compatibility

Designed for [mcp-calendar](https://github.com/zavora-ai/mcp-calendar):

| Capability | Tools |
|-----------|-------|
| Discovery | list_calendars |
| Events | list_events, get_event, create_event, update_event, delete_event, search_events |
| Scheduling | find_free_time |
| RSVPs | rsvp_event, list_attendees |

## Related Skills

- [skill-crm-customer-management](https://github.com/zavora-ai/skill-crm-customer-management) — Schedule on deal advance
- [skill-email-management](https://github.com/zavora-ai/skill-email-management) — Meeting follow-ups

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0

---

Part of the [ADK-Rust Enterprise](https://enterprise.adk-rust.com) skills ecosystem. Built with ❤️ by [Zavora AI](https://zavora.ai)
