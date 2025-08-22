---
layout: default
title: "Developer Dashboard"
parent: Sonatype Developer
nav_order: 3
---

# Developer Dashboard

Sonatype Developer Dashboard provides insights into the extent of application adoption, risk remediation timelines, and the current state of application evaluations.

Click on the *Developer* option in the left navigation section to view the Developer Dashboard.

![New_Developer_dashboard.png](/assets/images/uuid-2ed1f1bf-2375-d5f4-c7e3-57f866196439.png)

## Overview tab

**Adoption Profile**

The adoption profile indicates the percentage of applications in your organization that use the Sonatype integration plug-ins for SCM and CI/CD each month.

The trend line can help decide whether the use of Sonatype integration plug-ins should be ramped up, to maintain the security posture.

**Risk and Remediation**

The Count (y-axis) represents the number of active waivers and the number of applications with failing violations.

The trend lines can help determine the corrective actions needed to remediate the risks.

**Mean Time to Remediate**

The *Mean Time to Remediate* represents the average age of the violations that were remediated each month in your applications.

The trend line gives an insight into the priority given to remediation tasks on a monthly basis.

### Build Stage Risk Monitoring Summary

![Build_stage_risk_monitoring_summary.png](/assets/images/uuid-9459e7bd-f6f8-9dcf-222d-36651ffd821c.png)

This section summarizes the risks to your build pipeline and displays the IQ Server scan findings for each application. It contains:

- Applications that are currently configured or not configured with CI/CD plugins. Click on the *Configure* button to find out more about configuration details.
- Applications that have or do not have automated source control feedback enabled. Click on the *Configure* button to find out more about configuration details.
- The date of the last commit.
- The date of the last evaluation.
- The *Priorities* column with a link to [view the suggested priority](#UUID-1c4c14be-340a-dadb-6d0c-3da2dc62833f) of the violations that need to be remediated for the application.

**Using the Filter**

![New_filter.png](/assets/images/uuid-c7bbf428-1bce-e6fa-a572-412d6f57ee2e.png)

Use the filter to limit the scope of your focus to target applications that are configured/non-configured for CI/CD or SCM feedback.

**Using the Search**

To navigate to a specific application, enter the name of the application in the *Search* box at the top of the applications list.

**Review the Application Configuration**

Click on an application name to view the existing IQ Server settings for the application, including the assigned application categories, policies applied, enabled/disabled legacy violations, continuous monitoring settings, proprietary component configuration, component labels assigned, applicable license threat groups, existing source control integration, InnerSource repository configuration, and user roles and access,

## Available Plugins

![Available_integrations.png](/assets/images/uuid-9c4c296b-4895-fbf8-afb1-e2a038fb800c.png)

Click on any of the tabs to view the Sonatype IQ Server plugins currently available for integration with CI/CD pipelines, SCM, issue-tracking systems, and IDE integrations.

The plugins are updated regularly, corresponding to every release of the Sonatype IQ Server. We suggest checking these periodically to ensure that you are using the most recent version of the plugin.

## Use the Solution Switcher

Need to switch to another Sonatype solution, seamlessly?

Click on the [Solution Switcher](#UUID-f6cc2b00-f036-2711-ba56-621efcd473a5) icon in the top right navigation bar to experience other licensed Sonatype solutions, including Sonatype Lifecycle, Sonatype Developer, Sonatype SBOM Manager, and Sonatype Repository Firewall.
