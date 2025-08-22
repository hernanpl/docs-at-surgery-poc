---
layout: default
title: "Nexus Repository 3 Pro Setup"
parent: Repository Firewall Getting Started
nav_order: 1
has_children: true
---

# Nexus Repository 3 Pro Setup

To set up Repository Firewall for your Nexus Repository, you need to connect to the Firewall server in Nexus Repository Administration and enable the Firewall capability on your proxy repositories.

Use the following steps for Nexus Repository 3 Pro:

**Note:** We recommend using a service account when connecting Nexus Repository to the IQ Server in production environments. Consider generating user tokens as an added layer of security. At a minimum, this account requires access to the `Evaluate Individual Components` permission at the `Repository Managers` level in IQ Server `Org and Policies` .

Leave the following configuration options blank unless directed by Sonatype support:

- *Properties, Connection Timeout*

## Firewall Audit and Quarantine Capability

The Repository Firewall configuration may be managed by setting the `Firewall: Audit and Quarantine` capability for each proxy repository that will need to be protected.

### Adding the Audit and Quarantine Capability

![Audit and Quarantine capability creation menu]({{ "/assets/images/uuid-b9ca76d0-a946-d9fb-ffe2-785b29148813.png)

The audit on the selected repository will automatically start. Nexus Repository connects to the IQ Server and evaluates the components within the selected repository against any associated policy.

### Disabling the Audit and Quarantine Capability

Disabling quarantine will release all quarantined components to your proxy repository. Previously quarantined components are not quarantined again. Only new components are evaluated for quarantine when quarantine is re-enabled.

To disable Audit and Quarantine:

## Firewall Results in Nexus Repository

The repository audit results are summarized in the `Firewall Report` column of the Repositories view in the Settings menu.

The Firewall Report column includes the following items:

- Count of components by their highest policy violation level
- Count of quarantined components
- Link to the results on the Firewall server

**Note:** When an issue occurs, a red exclamation mark and a description of the error appear in the Firewall Report column. Details of the error are available in the Nexus Repository log file.

### Access the report through the capabilities menu

You can access the results from the Capabilities submenu on the Settings menu if you have permission to add capabilities in the Nexus Repository.

### Grant privileges to view the summary results

Access to the detailed audit reports is managed in the Firewall server. In Nexus Repository, a summary of the repository results is displayed in the repository view of the settings panel. Access to this view is assigned to the Nexus Repository admin role by default, however, access can be granted to other users by assigning them the following privilege:

**Note:** Users without permission to the results summary will only see `Audit Enabled` or `Quarantine Enabled`

- `nx-repository-view—*-*-read`
- `nx-iq-violation-summary-read`
