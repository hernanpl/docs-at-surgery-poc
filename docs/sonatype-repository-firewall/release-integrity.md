---
layout: default
title: "Release Integrity"
parent: Sonatype Repository Firewall
nav_order: 9
---

# Release Integrity

New releases of open-source components introduce high risk to your build pipeline as they may hide malware, critical security vulnerabilities, or unapproved licenses.

Release Integrity is a collection of features in the Repository Firewall that protect you from intentionally harmful components.

- Machine Learning (ML) system for identifying potentially malicious releases
- Repository Firewall blocks dangerous releases by default
- Protect your build pipeline from software supply chain attacks

- Firewall automatically releases components from quarantine that no longer have failing violations
- Automatically release suspicious components deemed safe by the Sonatype Research team
- Reduce costs of assessing components coming into your build environment

- Configure your repository manager to only deliver versions without failing policy violations
- This keeps new versions from breaking your builds or disrupting development

## Release Integrity

When an open-source component or new version is published, Sonatype’s AI and Machine Learning tools analyze the release and flag it when detecting unusual release behavior. Typical releases are assigned a normal rating while flagged components are sent to the Sonatype Research team for detailed review. During this review, components are assigned a Suspicious Integrity Rating to be temporarily quarantined. Components discovered with dangerous behavior are labeled Malicious and left in quarantine. Components have their Integrity Rating updated to Normal after passing the review process.

**Note:** The Integrity-Rating policy is automatically created when the Repository Firewall license is installed. This operation only occurs once, even if the license is installed again. The Integrity-Rating policy is configured to guard against malicious components. This feature is designed to be used along with Repository Firewall's [Automatic Quarantine Release](#UUID-fce7cb93-a2a2-7970-ac89-97dc14c9e891) to allow components re-assigned a normal integrity rating to be released without intervention by security teams.

## Enable Automatic Release

Automatically releasing components from quarantine keeps your environment running smoothly and reduces the needed effort managing components. We recommend allowing Automatic Release for Integrity Rating Policy Condition type and match state at a minimum.

See

## Integrity-Rating Policy

The Integrity-Rating Policy looks at a component's Release Integrity Score and creates violations for components with *Pending* or *Suspicious* values. These statuses are given to new components when Sonatype's machine-learning tools find anything suspicious or unusual in the release.

### Managing the Integrity-Rating Policy

The Integrity-Rating Policy is set using the following constraints. The action is set to Fail on the Proxy stage.

- Pending integrity rating - is in violation if the following is true: `Integrity Rating` is `Pending`
- Suspicious integrity rating - is in violation if the following is true: `Integrity Rating` is `Suspicious`

## Security Malicious Policy

The Security-Malicious policy is also triggered when a component is found to be malicious. This information is from the `Security Vulnerability Category` and is labeled `Malicious Code` .

![iq-policy-release-integrity](/docs-at-surgery-poc/assets/images/uuid-9f4dcb0e-de2e-1bb3-2eb7-6d280ef8f5db.png)

## Sample Malicious Components

The Sonatype data team maintains sample malicious components for [npm](https://www.npmjs.com/package/@sonatype/policy-demo) , [maven](https://central.sonatype.com/artifact/org.sonatype/maven-policy-demo/1.0.0) , and [python](https://pypi.org/project/python-policy-demo/) projects to use in testing the Integrity Rating policy with the Repository Firewall. These components are not vulnerable in any way but will result in policy violations when used in an application analysis or when requested through the Repository Firewall.
