---
layout: default
title: "Find and Fix Springshell"
parent: Important Announcements
nav_order: 2
---

# Find and Fix Springshell

This page and the [Sonatype blog post](https://blog.sonatype.com/new-0-day-spring-framework-vulnerability-confirmed) are updated with the latest information

News broke on March 30, 2022, of a new vulnerability, dubbed "Springshell / Spring4shell" in the community, as a new, previously unknown security vulnerability.

Sonatype deep-dive data research has confirmed that this serious vulnerability affects the **spring-beans** and **spring** artifacts under the [following conditions](https://spring.io/blog/2022/03/31/spring-framework-rce-early-announcement) :

- JDK >=9 is being used.
- The application is deployed as a .war (as opposed to a Spring Boot executable jar)

Anyone using software built on Spring—a large population of enterprise Java software—is possibly affected. This vulnerability has been added to Sonatype data as SONATYPE-2022-1764 and given the designation CVE-2022-22965 with a CVSS Score of 9.8

**Note:** The SONATYPE-2022-1764 issue is a duplicate of CVE-2022-22965, as Sonatype reported this issue before a CVE ID was officially released.

Spring has released patched versions 5.3.18 and 5.2.20 as well as remediated versions of Spring Boot, available on Maven Central. We recommend an immediate upgrade.

## Select a Sonatype Solution

Sonatype Lifecycle - find and fix the Springshell vulnerability across applications

Sonatype Repository Firewall - find if Springshell exists in your repository and prevent future downloads of vulnerable versions of Springshell

Nexus Repository - find if Springshell exists in your repository

### Sonatype Lifecycle

The following information helps Sonatype Lifecycle users find and fix Springshell vulnerabilities.

#### How do I know if my applications are affected by the Springshell vulnerability (CVE-2022-22965)?

**I have scanned my application(s) since March 30, 2022**

Your Dashboard results will show the most recent violations. The Dashboard is displayed by default when you log into Lifecycle. You can also access it by clicking the Dashboard icon on the left navbar.

Click the Filter button to adjust your results. For example, you can filter by security threat severity. Large organizations with lots of scanned apps should set the Age filter to *Past 7 Days* or *Past 24 hours* to find the components to review.

Click an application on the Applications screen to review the Report. The Report Details will show you the policy violations and the exact Spring components found. Look for policy violations that flag components with the IDs *spring-beans* and *spring-core*.

**I have not scanned my application(s) since March 30, 2022**

You will need to initiate a scan to get up-to-date violation information. Violations found for these applications before March 30, 2022, will not include the Springshell vulnerability because Sonatype's research was not yet complete.

You can trigger a scan by making any commit or build to your application. Alternatively, you can trigger a rescan via the Lifecycle UI:

1. Navigate to *Applications* in the left sidebar
2. Click on the application name to view application details
3. Click the *Rescan* button to manually trigger a new scan

Once the scan completes, follow the instructions above for reviewing Dashboard and Report results.

#### How do I remediate Springshell vulnerabilities in my applications?

The remediation for Springshell depends on your specific Spring Framework setup:

1. **If you're using Spring Framework directly**: Upgrade to Spring Framework 5.3.18+ or 5.2.20+ 
2. **If you're using Spring Boot**: Upgrade to Spring Boot 2.5.12+ or 2.6.6+
3. **For applications that cannot immediately upgrade**: Consider implementing workarounds such as:
   - Switching from .war deployment to Spring Boot executable jar deployment
   - Implementing additional input validation and access controls
   - Using web application firewalls to filter malicious requests

#### Email Notifications

Email notifications from the IQ Server are automatically sent to recipients when a policy alert occurs. The email contains information about the application and violation and provides a link to the full results for further investigation.

### Sonatype Repository Firewall

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

### Nexus Repository

The following information helps Nexus Repository users identify if Springshell exists in your repository.

**Use Repository Health Check**

## Are Sonatype products vulnerable?

Sonatype conducted an audit of our applications, and we determined that Sonatype products are not affected by the Spring4shell vulnerability.

## Resources

- Sonatype Blog: [New Spring Framework RCE Vulnerability Confirmed - What to do?](https://blog.sonatype.com/new-0-day-spring-framework-vulnerability-confirmed)
- For further assistance, contact your Customer Success representative or log a support ticket.
