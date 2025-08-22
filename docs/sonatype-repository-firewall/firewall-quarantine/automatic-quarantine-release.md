---
layout: default
title: "Automatic Quarantine Release"
parent: Firewall Quarantine
nav_order: 1
---

# Automatic Quarantine Release

Set the frequently the Repository Firewall checks components quarantined in the past 14 days for updated metadata.

Scheduling interval (in minutes) for Automatic Quarantine Release. The minimum value supported is `30` minutes.

Property: `automaticQuarantineReleaseTimeIntervalInMinutes`

Default: 60

```
curl -u admin:admin123 -X PUT -H "Content-Type: application/json" -d '{"automaticQuarantineReleaseTimeIntervalInMinutes": 120 }' http://localhost:8070/api/v2/config

curl -u admin:admin123 -X GET "https://localhost:8070/api/v2/config?property=automaticQuarantineReleaseTimeIntervalInMinutes"
```
