---
layout: default
title: "Struts2 Frequently Asked Questions"
parent: Important Announcements
nav_order: 4
---

# Struts2 Frequently Asked Questions

An analysis of your applications will trigger a Security-High policy violation for the Struts2 vulnerability. If you are using Struts and did not have a violation raised, you can rest assured you are not affected.

- **Option 1** : Use the Dashboard components view as described in the article.
- **Option 2** : Use the Components view from the Lifecycle UI.
- **Option 3** : Use the REST API to search for the component. See the IQ Server REST API documentation for how to create a call. For example: org.apache.struts:struts2-rest-plugin:*:*:*

Upgrade the component to the newly released non-vulnerable version. Please reference the in-product security vulnerability information for additional details for mitigating the vulnerability exposure.

It is almost impossible to avoid zero-day vulnerabilities. There will always be a time gap between the zero-day discovery and public reporting. There is another time gap between the public release and the vulnerability appearing in evaluation results. Immediate notification is a key element for limiting potential impact. Sonatype is often aware in advance of a new vulnerability announcement, enabling us to provide notice within IQ Server prior to the issue being released publicly. In other instances, we must perform the issue identification and research after the issues are publicly released. In these cases, we strive to include the vulnerability in our data within a few hours of the announcement.

There are additional preventative measures that can be established within your development practices that will better prepare your organization for these situations and decrease your time to respond. Contact Customer Success to learn more about how Sonatype Lifecycle and associated best practices can help.

Sonatype Repository Firewall can audit component downloads from a given proxy repository (Java, .NET, npm, Python). Users can view a report that contains all components, which have been previously downloaded to your Nexus Repository through that applicable proxy repository.

This report can be reviewed for any instance of Struts. Users can search for a particular Struts component (E.g. org.apache.struts:struts2-rest-plugin:*). In addition, the Firewall results include Sonatype-curated vulnerability information - for this CVE and others - only available to Sonatype “Firewall” and “Lifecycle” customers.

If this component is found, it indicates it was previously downloaded into your Nexus Repository. As a result, the component is available to applications with privileges to access that proxy repository. To associate a component to a specific application, please visit Sonatype’s “ [Application Health Check (AHC)](https://www.sonatype.com/software-bill-of-materials) ” a no-cost service. To automate this monitoring across all applications, see “Sonatype Lifecycle” above.

In addition to auditing component downloads, Sonatype Repository Firewall is designed to quarantine component download requests based on IQ Server policy configuration. You can configure policy to quarantine new component downloads for known vulnerable versions of any component based on any range of criticality. Check out the blob post, " [How to Keep Vulnerable Versions of Struts Out of Your Nexus Repository](https://blog.sonatype.com/how-to-keep-vulnerable-versions-of-struts-out-of-your-nexus-repository) " for guidance on how this can be achieved.

[Repository Health Check](http://blog.sonatype.com/how-to-use-the-new-repository-health-check-2.0) (RHC) can audit component downloads from a given proxy repository (Java, .NET, npm, Python). Users can view a report that contains all components, which have been previously downloaded to your Nexus Repository through that applicable proxy repository.

This report can be reviewed for any instance of Struts. Users can search for a particular Struts component (E.g. org.apache.struts:struts2-rest-plugin:*). In addition, the RHC report includes links to the associated CVE.

If this component is found, it indicates it was previously downloaded into your Nexus Repository. As a result, the component is available to applications with privileges to access that proxy repository. To associate a component to a specific application, please visit Sonatype’s “ [Application Health Check](https://www.sonatype.com/software-bill-of-materials) (AHC)” a no-cost service. To automate this monitoring across all applications, see “Sonatype Lifecycle” above.

[Enabling RHC](http://blog.sonatype.com/how-to-use-the-new-repository-health-check-2.0) on all supported repository types provides insight into component downloads across your proxy repositories. In addition, the report includes trend analysis determined by month-to-month asset downloads.

**Sonatype Statements**

- [http://blog.sonatype.com/sonatype-statement-struts2-and-equifax-breach](http://blog.sonatype.com/sonatype-statement-struts2-and-equifax-breach)
- [https://blog.sonatype.com/deja-vu-all-over-again-another-new-apache-struts-vulnerability-cve-2018-11776](https://blog.sonatype.com/deja-vu-all-over-again-another-new-apache-struts-vulnerability-cve-2018-11776)
- [http://blog.sonatype.com/alert-three-things-to-know-about-the-newest-struts2-vulnerability](http://blog.sonatype.com/alert-three-things-to-know-about-the-newest-struts2-vulnerability)
- [http://blog.sonatype.com/struts2-vulnerability-cracks-equifax](http://blog.sonatype.com/struts2-vulnerability-cracks-equifax)
- [http://blog.sonatype.com/bracing-for-impact-in-more-ways-than-one-apache-struts2-s2-053](http://blog.sonatype.com/bracing-for-impact-in-more-ways-than-one-apache-struts2-s2-053)

**CVE-2018-11776 Disclosure**

- [https://semmle.com/news/apache-struts-CVE-2018-11776](https://semmle.com/news/apache-struts-CVE-2018-11776)
