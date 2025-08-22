---
layout: default
title: "Custom Quarantine Messages"
parent: Firewall Quarantine
nav_order: 2
---

# Custom Quarantine Messages

Configure Repository Firewall to provide a custom quarantine message when a component request fails a Firewall policy. This message and the default Firewall quarantine messages are included in the command line output.

Use cases for the capability:

- Provide instructions on how to respond when components are quarantined during their builds.
- Using up to 500 characters the custom messages may contain a URL pointing to internal instructions
- For Repository Firewall release 165 or greater using Nexus Repository Pro version 3.58 or greater
- For Repository Firewall using JFrog Artifactory plugin 2.4.11 or greater

## Setting the quarantine message

Send a command to the to PUT a JSON object containing the quarantine message property.

```
quarantinedItemCustomMessage 
```

```
curl -X PUT -u admin:admin123 \
     -H "Content-Type: application/json" \
     -d '{"quarantinedItemCustomMessage": "Custom message http://domain.com/quarantine-guide"}' \
     "http://localhost:8070/api/v2/config"
```

## Getting the current message

Use a GET request to check the value of the property from the config API

```
curl -X GET -u admin:admin123 \
     "http://localhost:8070/api/v2/config?property=quarantinedItemCustomMessage"
```

## Deleting the custom message

Use a DELETE request to remove the message

```
curl -X DELETE -u admin:admin123 \
     "http://localhost:8070/api/v2/config?property=quarantinedItemCustomMessage"
```
