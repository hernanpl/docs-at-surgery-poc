---
layout: default
title: "Sonatype Container Deployment – Nexus Repository"
parent: Sonatype Integrations
nav_order: 21
---

# Nexus Repository

The following information helps Nexus Repository users identify if Springshell exists in your repository.

**Use Repository Health Check**

## How do I determine if my organization is impacted by the latest vulnerability disclosure?

Repository Health Check (RHC) can audit component downloads from a given proxy repository. Users can view a report that contains all components, which have been previously downloaded to your Nexus Repository through that applicable proxy repository.

This report can be reviewed for any instance of Springshell. Users can also search for a particular Springshell component. In addition, the RHC report includes links to the associated CVE.

If this component is found, it indicates it was previously downloaded into your Nexus Repository. As a result, the component is available to applications with privileges to access that proxy repository. We recommend [reaching out to Sonatype Sales](https://www.sonatype.com/contactus) to trial the Sonatype Lifecycle solution.

## How should we remediate this issue?

First, we recommend deleting vulnerable versions of this component from your proxy repositories. If you're also a Firewall customer, review the information above to learn how Sonatype Repostiory Firewall can automatically quarantine vulnerable versions of this component.

If you do not have a means of blocking components from being reintroduced to your proxy repositories, you'll need to manually alert development teams to the danger.

Spring has released patched versions 5.3.18 and 5.2.20 available on Maven Central. We recommend an immediate upgrade.

## How can Repository Health Check (RHC) help with other known vulnerabilities?

Enabling RHC on all supported repository types provides insight into component downloads across your proxy repositories. In addition, the report includes trend analysis determined by month-to-month component downloads.
