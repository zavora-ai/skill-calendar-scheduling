# Calendar Cross-MCP Workflows

## Calendar + CRM: Deal Advance → Schedule Meeting
```
CRM: move_deal_stage(id: "d_123", stage: "Proposal")
CALENDAR: find_free_time(attendees: [rep, customer], duration: 30)
CALENDAR: create_event(title: "Proposal Review — Acme", attendees: [rep, customer])
CRM: create_activity(type: "meeting", subject: "Proposal review scheduled")
```

## Calendar + ITSM: Change Window
```
ITSM: open_change_request(title: "DB migration", window: "Sat 02:00")
CALENDAR: create_event(title: "CHG-001: DB Migration", start: "Sat 02:00", end: "Sat 04:00", attendees: [dba, oncall])
```

## Calendar + Customer Service: Check-in for At-Risk Customer
```
CS: assess_churn_risk(id: "cust_789") → {risk: "high"}
CALENDAR: find_free_time(attendees: [csm, customer])
CALENDAR: create_event(title: "Check-in: Customer Health Review")
```
