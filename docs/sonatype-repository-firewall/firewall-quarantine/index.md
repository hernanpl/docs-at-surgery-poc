---
layout: default
title: "Firewall Quarantine"
parent: Sonatype Repository Firewall
nav_order: 5
has_children: true
---

# Firewall Quarantine

When a requested component violates your open-source policy, the component is put into quarantine while returning an error message and linking the component details to the requester. While the component remains quarantined in the proxy repository, it may not be downloaded through that proxy repository.

Your security team reviews the violations of quarantined components from the Firewall Dashboard. When the organization determines the introduced risk is acceptable or the components are required by the development team, the violations may be waived and the components are made available for download again through the proxy repository.

Keep the following points in mind when using quarantine for Repository Firewall:

- Set critical policies to `FAIL` at the `PROXY` stage to quarantine components when they violate these policies. Disabling the Repository Firewall releases any quarantined components.
- Components already found in the proxy repository are audited but not quarantined. This is to avoid disruption to your build pipeline. Use Sonatype Lifecycle to manage the components used by your applications. Components that are deleted from the proxy and re-requested may end up in quarantine when they violate your policies.
- In some build environments, the logs only show a 403 error message for quarantined components without details on why. We recommend socializing expectations with your development teams so that they are not surprised when this happens.
- When the Repository Firewall service is unavailable and quarantine enabled, requests for new components are immediately placed in quarantine until they are evaluated and released. New components are not available for download unless the Repository Firewall is disabled on your proxy repository. Consult with Sonatype support before making this change as recovering your quarantined component may not be possible.

## Quarantine Configuration

Repository Firewall quarantines components when the policy violation action is set to `FAIL` at the `PROXY` stage. Changing the policy actions requires the `Policy Administrator` or `Owner` roles in the IQ Server.

### Actions on the Proxy Stage

These are the actions available at the proxy stage and how they are used.

- Quarantines any newly requested components that violate the policy.
- Trigger an email notification when new components that violate this policy are brought into your build environment.
- The default action, where violations are only displayed in the audit report.

## Viewing Quarantined Components

Quarantined components may be reviewed in the following locations:

- The Firewall Dashboard lists the quarantined components from all of your repositories in one place. Each component links you to the component in the Repository Results view. See [Repository Firewall Dashboard](#UUID-4439bba0-67dd-8d9f-3011-e58458a57f19)
- From the Firewall configuration page, you may view the audit repo for a proxy repository configured with Repository Firewall protection. See [Repository Results](#UUID-a08de187-0418-3468-53bf-8e5f864b06ef)
- Individual quarantined components may be viewed in the Quarantined Component View. This view is available when you request a quarantined component from the command line. See [Quarantined Component View](#UUID-1b1073ca-3e40-aece-85c3-b8d003588620)
- The REST API may be used to return a list of the quarantined components for reporting or automation in your third-party tooling. See [Firewall REST API](#UUID-d516f5b1-1573-aae2-7261-107d95f5fb67)

## Quarantine Remediation

A few approaches exist to remediate violations when a component has been quarantined.

## Release Quarantined Components

To release a component from quarantine you must waive the failing policy violations. Components are automatically released from quarantine when the failing violations are no longer open.

## Repository Firewall and Time-Based Waivers

When adding a waiver against failing policy violations for Repository Firewall, the waivers used to release the component should be scoped to either the repository from which they were quarantined or using a short-lived time-based waiver. Once the waiver expires, the component will again trigger the violation. However, since it is already in the repository, it will not be quarantined.

With time-based waivers, violations do not re-occur during the time window set on the waiver. Downloading the component while waivers are in place will not cause violations during the time window.

## Automatic Quarantine Release

With this feature, you may configure quarantined components to be released when components no longer have failing violations. Auto-release will monitor components quarantined in the last 14 days. When new information resolves the policy violation that caused the quarantine, the component is automatically released from quarantine.

After 14 days, the component may still be released manually. However, the value of releasing that component drops dramatically, since a different component may be in place, or the component is no longer required.

### Auto-Release Dashboard

The Auto-Release Dashboard displays an activity summary and components that have been auto-released from quarantine.

This view is accessed from the Firewall Dashboard.

![Auto-Release_Dashboard.png](/docs-at-surgery-poc/assets/images/uuid-78a46c7a-91b0-d267-034e-0e0078607554.png)

- Components auto-released from quarantine in the current month
- Components auto-released from quarantine in the current year
- Summary and configuration of policy condition types enabled for auto release from quarantine.
- These are the components that were auto-released from quarantine. Selecting a row will open the Component Information Panel for that component. These results do not include components that have been manually released from quarantine.

### Auto Release from Quarantine Configuration

The configuration for auto-releasing quarantined components is found on the Auto Release from Quarantine dashboard.

Modifying the auto-release functionality requires the `Edit IQ Elements` permission set at the `Repository Managers` access level.

![fw.dashboard_auto_release_config](/docs-at-surgery-poc/assets/images/uuid-b614713c-b530-aba5-2aa8-b367068e45c0.png)

### Auto-Release Task

The auto-release task runs hourly by default. The schedule interval can be configured using the following property of the Configuration REST API.

```
automaticQuarantineReleaseTimeIntervalInMinutes
```

The Re-Evaluate Repository option in the Repository Results screen will trigger the auto-release task to review quarantined components.

### Policy Condition Types Supporting Auto Release

Policy violations are triggered by conditions in the policy. The condition types are used to correlate to component information.

The policy condition types that can be enabled for monitoring with auto-release from quarantine are:

```
Integrity Rating
License
License Threat Group
Match State
Security Vulnerability Severity
Security Vulnerability Category
Security Vulnerability Custom Remediation
Security Vulnerability Custom CVSS 
Security Research Type
```

## Custom Quarantine Messages

Configure Repository Firewall to provide a custom quarantine message when a component request fails a Firewall policy. This message and the default Firewall quarantine messages are included in the command line output.

Use cases for the capability:

- Provide instructions on how to respond when components are quarantined during their builds.
- Using up to 500 characters the custom messages may contain a URL pointing to internal instructions
- For Repository Firewall release 165 or greater using Nexus Repository Pro version 3.58 or greater
- For Repository Firewall using JFrog Artifactory plugin 2.4.11 or greater

### Setting the quarantine message

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

### Getting the current message

Use a GET request to check the value of the property from the config API

```
curl -X GET -u admin:admin123 \
     "http://localhost:8070/api/v2/config?property=quarantinedItemCustomMessage"
```

### Deleting the custom message

Use a DELETE request to remove the message

```
curl -X DELETE -u admin:admin123 \
     "http://localhost:8070/api/v2/config?property=quarantinedItemCustomMessage"
```
