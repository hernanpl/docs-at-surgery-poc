---
layout: default
title: "Firewall Results in Nexus Repository"
parent: Nexus Repository 3 Pro Setup
nav_order: 2
---

# Firewall Results in Nexus Repository

The repository audit results are summarized in the `Firewall Report` column of the Repositories view in the Settings menu.

The Firewall Report column includes the following items:

- Count of components by their highest policy violation level
- Count of quarantined components
- Link to the results on the Firewall server

**Note:** When an issue occurs, a red exclamation mark and a description of the error appear in the Firewall Report column. Details of the error are available in the Nexus Repository log file.

## Access the report through the capabilities menu

You can access the results from the Capabilities submenu on the Settings menu if you have permission to add capabilities in the Nexus Repository.

## Grant privileges to view the summary results

Access to the detailed audit reports is managed in the Firewall server. In Nexus Repository, a summary of the repository results is displayed in the repository view of the settings panel. Access to this view is assigned to the Nexus Repository admin role by default, however, access can be granted to other users by assigning them the following privilege:

**Note:** Users without permission to the results summary will only see `Audit Enabled` or `Quarantine Enabled`

- `nx-repository-view—*-*-read`
- `nx-iq-violation-summary-read`
