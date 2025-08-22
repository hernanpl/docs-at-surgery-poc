---
layout: default
title: "Find and Fix Log4j"
parent: Important Announcements
nav_order: 3
---

# Find and Fix Log4j

In December 2021, a zero-day Remote Code Execution [exploit was discovered in the component, log4j-core](https://blog.sonatype.com/a-new-0-day-log4j-vulnerability-discovered-in-the-wild) , the most popular Java logging framework. The log4j-core vulnerability ( [CVE-2021-44228](https://ossindex.sonatype.org/vulnerability/f0ac54b6-9b81-45bb-99a4-e6cb54749f9d) , a.k.a. Log4Shell) affects a massive number of applications and businesses. Essentially any application that contains a vulnerable version of log4j-core is exploitable.

**Note:** It has been determined that the fix for CVE-2021-44228 committed in v2.15 was insufficient in limiting nested message lookups in log4j. This resulted in [CVE-2021-45046](https://nvd.nist.gov/vuln/detail/CVE-2021-45046) —a Security High vulnerability on v2.15. In addition, a Denial-of-Service (DoS) vulnerability ( [CVE-2021-45105](https://nvd.nist.gov/vuln/detail/CVE-2021-45105) ) has been discovered in v2.16. It is recommended that all users upgrade to version 2.17.1.

## Select the Sonatype solution you wish to use

### Sonatype Lifecycle

The following information helps Lifecycle users find and fix log4j-core vulnerabilities. In addition, we've created a short video that walks you through this topic:

#### How do I know if my applications are affected by the log4j vulnerability (CVE-2021-44228)?

**I have scanned my application(s) since December 9, 2021**

Your Dashboard results will show the most recent violations. The Dashboard is displayed by default when you log into Lifecycle. You can also access it by clicking the Dashboard icon on the left navbar.

Click the Filter button to adjust your results. For example, you can filter by security threat severity. Large organizations with lots of scanned apps should set the Age filter to *Past 7 Days* or *Past 24 hours* to find the components to review.

Click an application on the Applications screen to review the Report. The Report Details will show you the policy violations and the exact log4j components found. Look for policy violations that flag components with the IDs *log4j-core* and *log4j-api*.

Alternatively, navigate to *Components* in the left sidebar. The Components screen will automatically show you a list of all the affected log4j components.

**I have not scanned my application(s) since December 9, 2021**

You will need to initiate a scan to get up-to-date violation information. Violations found for these applications before December 9, 2021, will not include the Log4Shell vulnerability because Sonatype's research was not yet complete.

You can trigger a scan by making any commit or build to your application. Alternatively, you can trigger a rescan via the Lifecycle UI:

1. Navigate to *Applications* in the left sidebar
2. Click on the application name to view application details
3. Click the *Rescan* button to manually trigger a new scan

Once the scan completes, follow the instructions above for reviewing Dashboard and Report results.

#### How do I remediate log4j vulnerabilities in my applications?

The remediation for Log4Shell depends on your specific log4j setup:

1. **If you're using log4j-core directly**: Upgrade to log4j-core 2.17.1 or later
2. **If you're using Spring Boot**: Upgrade to Spring Boot 2.5.8+ or 2.6.2+
3. **For applications that cannot immediately upgrade**: Consider implementing workarounds such as:
   - Removing the JndiLookup class from the log4j-core jar
   - Setting the system property `log4j2.formatMsgNoLookups=true`
   - Setting the `LOG4J_FORMAT_MSG_NO_LOOKUPS=true` environment variable

#### Email Notifications

Email notifications from the IQ Server are automatically sent to recipients when a policy alert occurs. The email contains information about the application and violation and provides a link to the full results for further investigation.

### Sonatype Repository Firewall

The following information helps Sonatype Repository Firewall users identify if log4j-core exists in your repository and prevent future downloads of vulnerable versions of log4j-core.

How do I determine if my organization is impacted by the latest vulnerability disclosure?

Repository Firewall can audit component downloads from a given proxy repository (Java, .NET, npm, Python). You can view a report that contains all components that have been previously downloaded to your Nexus Repository through that applicable proxy repository.

This report can be reviewed for any instance of log4j-core, and you can search for a particular log4j-core component. In addition, the Firewall results include Sonatype-curated vulnerability information—for this CVE and others—only available to Sonatype Firewall and Lifecycle customers.

If this component is found, it indicates it was previously downloaded into your Nexus Repository. As a result, the component is available to applications with privileges to access that proxy repository. To associate a component to a specific application, please visit Sonatype’s [Nexus Vulnerability Scanner (NVS)](https://www.sonatype.com/software-bill-of-materials) a no-cost scan tool. If you have numerous applications to analyze, we recommend [reaching out to Sonatype Sales](https://www.sonatype.com/contactus) to trial the Lifecycle solution.

**Note:** Repository Firewall will not block the log4j-core component if it is already in your repository.

How should we remediate this issue?

We recommend upgrading to a version of this component that is not vulnerable to this specific issue. The best option is to **upgrade** **** **to the newly released, non-vulnerable version immediately** . This is currently version [2.17.1](https://search.maven.org/artifact/org.apache.logging.log4j/log4j/2.17.1/pom) . However, given this is a fast-moving and fluid situation, there may be a newer version released as you are reading this guide.The fixed version for this issue was released by Apache and is [available via Maven Central](https://search.maven.org/) .

How can RepositoryFirewall help with other known vulnerabilities?

In addition to auditing component downloads, Firewall is designed to quarantine component download requests based on policy configuration. You can configure the policy to quarantine new component downloads for known vulnerable versions of any component based on any range of criticality.

### Nexus Repository

The following information helps Nexus Repository users identify if log4j-core exists in your repository.

Use the log4j Visualizer (Nexus Repository users)

## Additional Resources

- Sonatype resource: [Log4j Vulnerability Resource Center](https://www.sonatype.com/resources/log4j-vulnerability-resource-center)
- Sonatype blog: [FTC Warning in Wake of Log4j: Secure Your Software Supply Chain](https://blog.sonatype.com/ftc-warning-in-wake-of-log4j)
- Sonatype blog: [How Large Organizations Can Easily Scan for Log4j Vulnerabilities](https://blog.sonatype.com/how-large-organizations-can-easily-scan-for-log4j-vulnerabilities)
- Sonatype blog: [Critical New 0-day Vulnerability in Popular Log4j Library Discovered with Evidence of Mass Scanning for Affected Applications - Latest updates](https://blog.sonatype.com/a-new-0-day-log4j-vulnerability-discovered-in-the-wild)
- Sonatype blog: [Log4shell by the numbers- Why did CVE-2021-44228 set the Internet on Fire?](https://blog.sonatype.com/why-did-log4shell-set-the-internet-on-fire)
- Sign up for Sontype’s [log4j exploit explained webinar](https://www.sonatype.com/resources/webinar-q4-2021-log4j-exploit-explained)
- For more information, please see [Apache Log4j Security Vulnerabilities](https://logging.apache.org/log4j/2.x/security.html)
- For further assistance, please contact your Customer Success representative or log a [support ticket](https://support.sonatype.com/hc/en-us/sections/203012538-Product-Support-Overview) .
