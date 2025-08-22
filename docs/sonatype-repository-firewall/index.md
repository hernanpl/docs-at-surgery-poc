---
layout: default
title: "Sonatype Repository Firewall"
nav_order: 5
has_children: true
---

# Sonatype Repository Firewall

The following information helps Repository Firewall users identify if Springshell exists in your repository and prevent future downloads of vulnerable versions of Springshell.

How do I determine if my organization is impacted by the latest vulnerability disclosure?

Repository Firewall can audit component downloads from a given proxy repository (Java, .NET, npm, Python). You can view a report that contains all components that have been previously downloaded to your Nexus Repository through that applicable proxy repository.

This report can be reviewed for any instance of Springshell, and you can search for a particular Springshell component. In addition, the Firewall results include Sonatype-curated vulnerability information—for this CVE and others—only available to Sonatype Firewall and Lifecycle customers.

If this component is found, it indicates it was previously downloaded into your Nexus Repository. As a result, the component is available to applications with privileges to access that proxy repository. If you have numerous applications to analyze, we recommend [reaching out to Sonatype Sales](https://www.sonatype.com/contactus) to trial the Sonatype Lifecycle solution.

How should we remediate this issue?

First, we recommend deleting vulnerable versions of this component from your proxy repos. Firewall's quarantine feature can block vulnerable versions from being reintroduced into your proxy repos. Set your security policies for severities 9 and 10 to Fail at the Proxy stage.

Spring has released patched versions 5.3.18 and 5.2.20 available on Maven Central. We recommend an immediate upgrade.

**Note:** Sonatype Repository Firewall will not block the spring-beans component if it is already in your repository unless you first delete the component.

How can Firewall help with other known vulnerabilities?

In addition to auditing component downloads, Sonatype Repository Firewall is designed to quarantine component download requests based on policy configuration. You can configure the policy to quarantine new component downloads for known vulnerable versions of any component based on any range of criticality.
