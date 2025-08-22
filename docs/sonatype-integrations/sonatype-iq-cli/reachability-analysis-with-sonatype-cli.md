---
layout: default
title: "Reachability Analysis with Sonatype CLI"
parent: Sonatype IQ CLI
nav_order: 1
---

# Reachability Analysis with Sonatype CLI

You can configure Sonatype CLI to perform [Reachability Analysis](#UUID-bffb3d6e-1a0b-5607-518a-3dcdc88508c2) , which can detect method signatures in your application code that contain components with potentially exploitable security vulnerabilities. Policy violations occurring due to these vulnerable components are labeled as `Reachable` and can be viewed on the application report.

**Note:** Supported Languages [Reachability Analysis](#UUID-bffb3d6e-1a0b-5607-518a-3dcdc88508c2) currently supports Java only.

By including [an additional parameter in the CLI command](#UUID-6b69b7b1-858f-e58a-e010-beb4fdff9cdf_section-idm4591846617011234159137652215) you can enable the Reachability Analysis feature. The scan process will then analyze all application and dependency Java (or any JVM language) binaries located in the scan target. This allows you to detect reachable vulnerabilities, even in proprietary components within your application.

Reachability Analysis requires a JVM CLI and does not work with native CLI installations.

## Permissions Required

The Sonatype CLI user should have the *Evaluate Applications* permissions to scan applications with Reachability Analysis.

## Using Reachability Analysis in Sonatype CLI

On first execution, if Reachability Analysis detects a component (belonging to the Maven ecosystem) that has a vulnerable method signature, the application report will show a policy violation with `Reachable` status.

![Reachable_Violation.png](/assets/images/uuid-8cd56a17-baac-e91f-72ba-4136c77c26f7.png)

You can prioritize the remediation of this violation.
