---
layout: default
title: "Sonatype Security Vulnerabilities"
parent: Sonatype Product Overview
nav_order: 5
---

# Sonatype Security Vulnerabilities

Sonatype knows that software security is critical in today’s interconnected world. We use robust tools and processes to ensure that our products are as safe as possible so that our customers can deploy them confidently.

## Our Security Practices

To ensure the security of our products, we use a comprehensive application security practice that includes transitive dependency analysis at multiple points in the SLDC, static analysis of application code, and automated and human review processes for all changes.

### Dependency Vulnerabilities

As with most modern software applications, Nexus Repository incorporates several open-source components as dependencies. Sonatype Lifecycle’s continuous monitoring capabilities regularly detect vulnerabilities in these components.

These may or may not be exploitable, depending upon both the nature of the vulnerability and how the components are used within our solutions. However, we consider all dependency vulnerabilities to be potentially exploitable through attack techniques such as vulnerability chaining. Therefore, our development teams upgrade the component to a non-vulnerable version as soon as possible. We make these upgrades available to our customers and users in later solution releases.

To benefit from this ongoing risk mitigation, we recommend our customers and users regularly update their Sonatype solutions to the most recent versions.

### Inquiring About a Dependency Vulnerability's Status

For concerns about a dependency vulnerability with unknown exploitability, we confirm whether we are aware of it and that it is queued for remediation as part of our normal development process.

For the protection of our customers and users, we do not disclose the exploitability of suspected vulnerabilities before they are remediated and we have released upgraded versions of our solutions.

## Reporting a Security Vulnerability

Sonatype responds to exploitable security vulnerabilities with the utmost urgency and follows a responsible disclosure and notification process to protect our users and customers.

To report a new vulnerability you discovered, follow the steps for reporting a security issue to [security@sonatype.com](mailto:security@sonatype.com) as detailed on our [Contact Us page](https://www.sonatype.com/contactus) .
