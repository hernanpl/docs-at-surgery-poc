---
layout: default
title: "Sonatype Lifecycle"
nav_order: 4
has_children: true
---

# Sonatype Lifecycle

The following information helps Sonatype Lifecycle users find and fix Springshell vulnerabilities.

## How do I know if my applications are affected by the Springshell vulnerability (CVE-2022-22965)?

I have scanned my application(s) since March 30, 2022

Your Dashboard results will show the most recent violations. The Dashboard is displayed by default when you log into Lifecycle. You can also access it by clicking the Dashboard icon on the left navbar.

Click the Filter button to adjust your results. For example, you can filter by security threat severity. Large organizations with lots of scanned apps should set the Age filter to *Past 7 Days* or *Past 24 hours* to reduce potential slowdowns.

Click Apply in the Filter menu to view your results:

Click the Export Violations Data button to save a CSV of the results.

I scanned my application(s) prior to March 30, 2022

If you scanned your application before the vulnerability was known, you can manually search applications for this vulnerability using the following REST endpoint to find the impacted spring-beans versions.

**NOTE:** Update the following with your IQ Server address, password, and target stage (e.g.,stageId=release).

```
http://localhost:8070/api/v2/search/component?stageId=release&componentIdentifier=%7B%22format%22%3A%22maven%22%2C%22coordinates%22%3A%7B%22groupId%22%3A%22org.springframework%22%2C%22artifactId%22%3A%22spring-beans%22%2C%22version%22%3A%22*%22%2C%22extension%22%3A%22*%22%2C%22classifier%22%3A%22*%22%7D%7D%E2%80%9D
```

An example REST API call to the IQ Server follows. Note that the REST endpoint in the Sonatype blog post is equivalent to below.

```
curl -u admin:password -X GET "http://localhost:8070/api/v2/search/component?stageId=release&componentIdentifier=%7B%22format%22%3A%22maven%22%2C%22coordinates%22%3A%7B%22groupId%22%3A%22org.springframework%22%2C%22artifactId%22%3A%22spring-beans%22%2C%22version%22%3A%22*%22%2C%22extension%22%3A%22*%22%2C%22classifier%22%3A%22*%22%7D%7D%E2%80%9D"
```

Alternatively, the Advanced Search feature is available in Sonatype Lifecycle. A search term you can use is: `componentCoordinateArtifactId:spring-beans`

**Note:** The best practice for identifyingSpringshellcomponents in your application is to run a full, new scan. Avoid using re-evaluate in this situation. Clicking the *Re-evaluate Report* button on an existing report only applies policies to the scan data, and the vulnerabilities do not change.

I have never scanned my application(s)

You can then run a scan via the CLI to get results.

The following example shows the command line. Replace <version> with your version of the CLI.

```
java -jar ./nexus-iq-cli-<version>.jar -i Test123 -s http://localhost:8070 -a username:password -t release sample-application.zip
```

## Springshell is in my application. How do I fix it?

I can upgrade my component

We recommend upgrading to a version of this component that is not vulnerable to this specific issue. The best option is to upgrade Springshell to a newly released, non-vulnerable version immediately.

Spring has released patched versions 5.3.18 and 5.2.20 available on Maven Central. We recommend an immediate upgrade.

I cannot upgrade my component

We strongly recommend upgrading to a non-vulnerable version of Springshell. If that is not possible, Spring has suggested workarounds.

Reference: [https://spring.io/blog/2022/03/31/spring-framework-rce-early-announcement#suggested-workarounds](https://spring.io/blog/2022/03/31/spring-framework-rce-early-announcement#suggested-workarounds)

## How do I protect my applications going forward?

**Enable Continuous Monitoring**

The best practice is to turn on the Continuous Monitoring feature. Continuous Monitoring lets you use existing policies with notifications to constantly watch (once a day, based on your configuration) for new violations at a specific development stage (such as Release). Configure Continuous Monitoring in two steps: (1.) turn it on for an application or organization, and then (2.) turn it on at the policy level and set your notifications.

To turn on Continuous Monitoring for an application or organization:

The next step is turning on Continuous Monitoring at the policy level. This lets you identify who should receive an email message when a violation of the current policy occurs.

To turn on Continuous Monitoring in a policy:

Turn on email notifications

Sonatype Lifecycle can be configured to send email notifications for events such as policy violation notifications. Email is a simple way to start getting notifications to the application security team, and eventually developers once they have been notified to expect them.

This functionality requires an SMTP server, which is configured along with a number of other options in the Mail Configuration section of the `config.yml` file.

Email notifications from the IQ Server are automatically sent to recipients when a policy alert occurs. The email contains information about the application and violation and provides a link to the full results for further investigation.
