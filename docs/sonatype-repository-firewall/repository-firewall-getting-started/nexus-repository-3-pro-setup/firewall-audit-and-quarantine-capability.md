---
layout: default
title: "Firewall Audit and Quarantine Capability"
parent: Nexus Repository 3 Pro Setup
nav_order: 1
---

# Firewall Audit and Quarantine Capability

The Repository Firewall configuration may be managed by setting the `Firewall: Audit and Quarantine` capability for each proxy repository that will need to be protected.

## Adding the Audit and Quarantine Capability

![Audit and Quarantine capability creation menu](/docs-at-surgery-poc/assets/images/uuid-b9ca76d0-a946-d9fb-ffe2-785b29148813.png)

The audit on the selected repository will automatically start. Nexus Repository connects to the IQ Server and evaluates the components within the selected repository against any associated policy.

## Disabling the Audit and Quarantine Capability

Disabling quarantine will release all quarantined components to your proxy repository. Previously quarantined components are not quarantined again. Only new components are evaluated for quarantine when quarantine is re-enabled.

To disable Audit and Quarantine:
