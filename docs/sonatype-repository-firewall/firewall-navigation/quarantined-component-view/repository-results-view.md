---
layout: default
title: "Repository Results View"
parent: Quarantined Component View
nav_order: 1
---

# Repository Results View

The repository results page is an audit of a proxy repository configured with the Repository Firewall. This view lists all the components requested through the proxy and any violations found near the time the component was requested.

![Screenshot_2024-02-15_at_7_05_08_PM.png](/docs-at-surgery-poc/assets/images/uuid-849decb0-9296-f7d4-d2d6-39a6a0242beb.png)

## Repository Summary

The summary section contains metrics on the health and contents of the repository. Here you will find the total number of components, the number of violations that affect some of the components, and a spread of the severity of those violations. You will also see if any components have been quarantined and are blocked from downloading through the proxy.

### Re-evaluate Repository

Components are evaluated when they are first requested through the proxy repository. This allows for components with unacceptable risk to be quarantined before they are downloaded through the proxy.

The Repository Firewall capability [Automatic Quarantine Release](#UUID-fce7cb93-a2a2-7970-ac89-97dc14c9e891) automatically re-evaluates the components for 14 days after the first request to check for changes in any violations they may have. After which, components are not evaluated anymore to minimize load on the repository manager and IQ Server.

You may perform a re-evaluation of all the components within the repository by selecting the `Re-evaluate Repository` option in the upper right of this page. Keep in mind that the time to complete re-evaluation depends on the number of components in the repository and may introduce load on the server for repositories that have a large number of components. We recommend limiting how often this audit is done to avoid strain on production services or delaying new requests through the proxy.

## Repository Components

This table lists all the components in the proxy repository and their associated violations found as of their last evaluation. By default, the view is aggregated by components while only displaying the highest policy violation for that component.

- Select an individual component from the list to view the component's detail page.
- When the toggle is 'on', only the highest-threat violation is displayed for the component. Select the component to view all violations for the component.
- Components are released from quarantine by waiving the policy failing violations on the component. Waive the violations from the component details page. Once the failing violations have been waived, the components are released from quarantine.
- Results may be filtered by the match state and the violation status. All - no filter Exact - Components identifiable by Sonatype Unknown - Components unknown to Sonatype all/none - no filter Not Violating - components with no violations Open - violations not waived or remediated Quarantined - components that have been quarantined due to a failing violation Waived - violations that have been waived
- All - no filter Exact - Components identifiable by Sonatype Unknown - Components unknown to Sonatype
- All - no filter
- Exact - Components identifiable by Sonatype
- Unknown - Components unknown to Sonatype
- all/none - no filter Not Violating - components with no violations Open - violations not waived or remediated Quarantined - components that have been quarantined due to a failing violation Waived - violations that have been waived
- all/none - no filter
- Not Violating - components with no violations
- Open - violations not waived or remediated
- Quarantined - components that have been quarantined due to a failing violation
- Waived - violations that have been waived

## Viewing results in Nexus Repository

As developers request components from a proxy repository, Firewall audits them using the policies in the IQ Server. There are a couple of ways to navigate this report.

The IQ Policy Violations are summarized in the Nexus Repository Pro and detailed in IQ Server.

In Nexus Repository Pro 3, the audit results are summarized in the IQ Policy Violations column of the Repositories view.

This view is located in the Repository sub-menu of the Administration menu.

![91948187.png]({{ /assets/images/uuid-dec4a3c8-c4af-4da2-a5e3-dfdc83fdba9a.png)

The IQ Policy Violations column includes the following items:

- A count of components by their highest policy violation level.
- A count of quarantined components.
- A link to Repository Results on IQ Server.

The IQ Policy Violations column alerts you if there are any errors in the audit and quarantine process. If there is an error a red exclamation mark will appear to the right of the Repository Results along with a description of the error. Additional information will be available in the Nexus Repository logs.

Without permissions to the Repository Results view, the IQ Policy Violations column displays either `Audit Enabled` or `Quarantine Enabled` .
