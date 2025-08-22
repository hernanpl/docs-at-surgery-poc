---
layout: default
title: "SBOM Continuous Monitoring"
parent: Sonatype SBOM Manager
nav_order: 14
---

# SBOM Continuous Monitoring

Vulnerability and policy violations for an SBOM remain static after the initial analysis performed when importing SBOMs. Continuous Monitoring automatically checks the latest version of an application's SBOM for new violations on a nightly basis. Use this feature to alert you as to when your SBOMs have newly discovered vulnerabilities.

![sbm-continous-monitoring-configuration.png](/docs-at-surgery-poc/assets/images/uuid-2e3836d8-9415-d68c-1402-fce45936b72b.png)

**Note:** Continuous Monitoring for SBOM Manager uses the `Compliance` stage and functions independently from Lifecycle's monitoring configuration. Administrators need to enable Continuous Monitoring before the SBOM Manager reports newly discovered violations.

## Enabling Continuous Monitoring

Administrators may enable Continuous Monitoring from the Organizations view. We recommend setting the configuration at the Root Organization, however, this setting may be enabled at any level of the organization hierarchy.

![sbm-continous-monitoring-enable.png]({{ /assets/images/uuid-342bd5d0-6939-7e7e-89e2-b4f714f65cce.png)

- Navigate to the Organizations view
- From the center view, select the Continuous monitoring configuration
- Toggle the button from Disabled to Enabled
- Select Update

## Scheduling Continuous Monitoring

Continuous Monitoring starts at midnight for the hosting system. You can change the start time through the [Configuration REST API](#UUID-0fa6ca2c-1237-6aca-a4e6-ad4d074fd63f) .
