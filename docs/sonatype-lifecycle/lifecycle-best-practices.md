---
layout: default
title: "Lifecycle Best Practices"
parent: Sonatype Lifecycle
nav_order: 9
---

# Lifecycle Best Practices

The concepts listed below are common best practices to use when you are planning, deploying, and socializing expectations for the Sonatype Platform. These best practices come from our experience in Customer Success, Sonatype Support, and Engineering Teams. We share how Sonatype Lifecycle is intended to be used and the successful experiences of customers like you.

Each best practice outlines:

- How we've seen others be successful
- A path that avoids most common pitfalls
- Recommendations for good usage

Getting started with Lifecycle Best Practices:

- [Lifecycle Deployment](#UUID-679052c0-688e-9b90-864e-2e6604bbf0c8)
- [Onboarding Applications](#UUID-d82278ed-f86b-0c68-c70b-b53eff49b23c)
- [Software Bill of Materials](#UUID-d470fc35-12c0-13fe-5c15-f2cbb364af64)
- [General Best Practices](#UUID-23307862-bf46-a233-462f-4670c1c92ecb)
- [Reference Policy](#UUID-ddf512c8-427b-ba7d-50c1-bd5020b989d0)
- [Backup and Restore Best Practices](#UUID-d8e98ab5-9485-d67d-65a4-5eded371383e)

Scanning and integrating into other toolsets:

- [Waivers](#UUID-d9ff5788-dd2f-4829-6c51-ab4665827007)
- [Hierarchy and Inheritance](#UUID-f5dab956-b9e9-3742-0183-380dce06b900)
- [Continuous Monitoring](#UUID-aa49127c-116b-6741-aecd-5b1516e735c7)
- [InnerSource](#UUID-355092d2-c0c0-b58d-5e20-671a268aa503)
- [Legacy Violations](#UUID-a997d928-066e-01b7-1be0-018cd252c955)

Maximizing open source governance:

- [Policy Enforcement](#UUID-0511fca1-3377-b8f1-6da7-cecf0afe5e93)
- [0-Day Vulnerability Best Practices](#UUID-b662413e-d541-5868-947b-d86c294d8afc)

## Lifecycle Deployment Best Practices

The following best practices are based on recommendations used in successful deployments. Success comes from the coordinated effort of your developers and open-source governance champions. The Customer Success team can help tailor and plan to meet your organization's needs.

Review the best practices for each phase of your deployment.

- Project Initiation (1st month)
- Project Pilot (first 2 months)
- Project Commencement (1st year)

![137202586.png](/assets/images/uuid-958704a7-05c5-0811-b3df-0c9bbd1a14d1.png)

### Architecture Overview

The Sonatype Lifecycle solution is comprised of the following components:

### Project Initiation (1st month)

### Project Pilot (first 2 months)

### Project Commencement (1st year)

## Onboarding Applications Best Practices

How you onboard applications will depend on a rough idea of your total inventory of applications.

### Manually Onboard

Add applications using the [Organizations and Applications](#UUID-1a7f44f6-c891-1f16-3eac-6ce70461794f) menu of the IQ Server user interface (UI).

- Recommended for a limited (<50) number of applications
- Great for testing and pilot teams
- Not an effective long-term strategy
- Common for third-party software and legacy code
- Application ids and names will need to be unique
- Consider using an onboarding script if you already have a complete list

### Automatic Application Creation

Configure the IQ server to allow applications to automatically be added when using an unused PublicID during a scan.

- Applications are automatically added to a default organization. The default organization may be configured in the UI.
- The default organization may be configured in the UI.
- Recommended for applications that would need to be onboarded over time.
- Application Categories will need to be manually set.

### Onboarding through Source Control Managers

lets you select applications to onboard through a point-and-click menu in the UI.

- Scans are run against the source code.
- Scanners will look for dependency lock files as well as binaries.
- Look for common language-specific patterns.
- Review the [analysis documentation](#UUID-a7f26522-01ae-eca4-b507-f0bffd06e746) for details.

### Onboarding Scripts (REST API)

Using the REST API to configure applications preemptively or in real-time.

- Directly integrate into your application management systems
- Recommended for a large number of applications or self-service growth
- Match to your internal systems using ids, application names, and existing groups

### Config-as-Code Tool

- Config-as-Code is the DevOps principle of treating configuration resources like versioned artifacts.
- Configuration is checked into source control, assigned a version, and associated with versioned builds.
- This [config-as-code tool](https://github.com/sonatype-nexus-community/iq-config-as-code) is a Python script that captures IQ Server’s configuration as a JSON.
- This JSON is applied to other IQ Server instances to set the same configuration.
- The iq-config-as-code/onboarding/templates can help new users prepare their first IQ Server.

**Note:** This tool is not officially supported by Sonatype.

## Legacy Violations Best Practices

### Focus enforcement and remediation on the violations where they matter most

- Configuring enforcement without breaking legacy applications
- Focus reporting on the most important risk
- Giving development time to remediate while alerting to new risk

### Use Legacy Violations to accept application risk for legacy applications

- Enforcement is a challenge when applications are onboarded periodically
- Legacy applications, that are infrequently built, seldom have the bandwidth to remediate technical debt
- Use Legacy Violations to accept the current risk of applications
- Continuous Monitoring to monitor new risk as it is discovered

### Use Legacy Violations to reduce noise when onboarding applications

- The default configuration for Legacy Violations is on policies with a threat level of 7 or lower
- This will effectively waive all risks with a lower threat
- This allows development teams to focus on critical and high-risk violations that present the most risk to the organization
- This configuration can be modified per policy
- The default policy may be configured to accept all risks including policies that are set to fail

### Enable Legacy Violations override for child Organizations and Applications

- Legacy Violations typically should be configured at the root organization level
- Allow Legacy Violations to be overridden at the organization level for teams that do not need it

### Add Legacy Violations to the backlog

- Legacy Violations are still risks that should be remediated
- Add Legacy Violations to the backlog to ensure they still get addressed

### Socialize when Legacy violations will be revoked

- Legacy violations may be hidden in the scan report, however, the risk does not go away
- As a best practice, legacy violations should have a plan for review, and the appropriate remediation actions made
- The risk that will continue to be accepted is replaced with time-based waivers going forward
- Applications may have their legacy violations revoked at any point, but this will have to be done manually through the UI

## Hierarchy and Inheritance Best Practices

Lifecycle uses a hierarchy model of organizations and applications for configuration management. Configuration is set at the highest required level and inherited downwards.

### Lifecycle Hierarchy Model

The following table displays common considerations for organizing your application hierarchy model. The top three (highlighted in yellow) are the most common.

Start with an inventory of your applications

- create a spreadsheet of your applications to align with your hierarchy considerations.
- use existing naming as much as possible to help with automation in your build environment.
- The application PublicID should match your build environment variables.
- Renaming and moving applications after they have been created is very time-consuming.
- Use application categories to flag applications with common policy considerations.

## Waiver Best Practices

Waivers remove the open violations from your scan report by accepting the risk of the violation. While this can be an effective remediation strategy, it still leaves you vulnerable to potential risk.

Here are a number of best practices that will help you use waivers responsibly, reduce friction, and control your overall risk posture.

**Waivers don't eliminate risk.** Prioritize remediating risk by picking better components.

### Scope your waivers narrowly by default

- Limit waivers to the application level for the violating component
- Use the Advanced Search or the Dashboard to understand the impact a waiver will have before broadening the scope

### Use time-based waivers

- Avoid creating waivers with no expiration date
- Scope your waivers to as short of a time frame as makes sense.
- you may wish to adjust the time frame depending on the violation threat level.

### Waive violations that cannot be remediated

- Avoid developers ignoring scan reports by temporarily waiving violations that cannot be remediated in the near term.
- Set an appropriate amount of time for the technical debt to be budgeted into development.

### Review that the waiver validation is still appropriate

- Waiving violations is valid when your application is not at risk.
- Use time-based waivers to periodically review that this is still the case.
- Document both in the waiver and in internal wikis why your application is not at risk and why you should continue to use the component.
- If the project never plans to fix the issue, you will want to consider other projects.
- Your team may also wish to contribute back to the project to remove the issue.

### Document the expected workflow for adding waivers

- At a minimum, the documentation should: List stakeholders Describe how waiver requests should be made Set expectations on how long a waiver request will take Outline default waiver values
- List stakeholders
- Describe how waiver requests should be made
- Set expectations on how long a waiver request will take
- Outline default waiver values

### Document who is responsible for granting waiver requests

- This is typically the project owner, AppSec, or Legal team members. Maybe a lead developer.
- Generally, you do not want to give developers the right to waive their violations.
- The person granting waivers will ultimately holds the responsibility for the risk.

### Set guidelines on the violations allowed to be waived

- Some risks are so severe that they must be remediated, and not be waived.
- Make sure those delineations are clearly documented so that developers are aware.
- Have discussions that include policy creators, risk owners, and developers.
- These sorts of discussions build your organization's DevSecOps maturity.

### Example Waiver Workflows

## InnerSource Best Practices

### Introduction

InnerSource Insight is a feature in Sonatype Lifecycle that identifies proprietary components in your scan results. This tells you when risk in your application is coming from other internal components, saving you time tracking down vulnerabilities that another team is responsible for remediating. Without InnerSource Insight, these proprietary components show up as Unknown Components. Researching the associated open-source dependencies can be challenging. Associating transitive risk with proprietary components can take a lot of time with little reduction in your applications' risk.

## Software Bill of Materials Best Practices

A software bill of materials (SBOM) is a list of all packages and libraries included in your application. It’s the digital equivalent of a manufacturing bill of materials. Just as a bill of materials includes all sub-assemblies, the SBOM also includes transitive dependencies or your components’ dependencies. And like a traditional BOM, the SBOM makes it easy to see if any risky packages are included in an application.

### Generate and store an SBOM for every application

### Include the SBOM in your Lifecycle scans

### Guidelines for Using Lifecycle with SBOMs for Monitoring

Sonatype Lifecyle can be used to analyze SBOMs associated with applications. The following sections provide general guidelines for hardware requirements for an IQ Server instance based on the magnitude of the application workloads.

Assumption: One SBOM per application.

## Policy Enforcement Best Practices

Policy action and enforcement parameters are rules that you set so that Lifecycle knows how to effectively deal with component policy violations occurring in your applications and repositories. Some approaches are better than others, of course. Sonatype has collected a list of the best practices for policy action and enforcement that have proven to be very effective for our most successful customers.

### Enable continuous monitoring to regularly check for violations

- Turn on the continuous monitoring feature to ensure your legacy and highest-priority applications are regularly checked for new violations.
- This is one of the easiest and best things you can do to continually monitor applications that are not in active development or that are not built regularly.

### Have a remediation plan in place to quash vulnerabilities efficiently and effectively

- Create a remediation plan to reduce your organization's risk with open-source components.
- Preparation and proactivity put you one step ahead when there is a vulnerability detected.
- Instead of wasting precious time wondering what to do, your team will already be in action mode thanks to a thoughtful and previously socialized plan.

### Analyze your metrics based on your organization's priorities and goals

- Care about your metrics and use them to your organization's advantage.
- Use your organization's metrics to benchmark continuous improvement and to monitor the value you're returning.
- The degree to which an organization can share and make visible its metrics is a sign of a mature organization that reflects good process alignment.

### Map and align your policy action/enforcement with the software development lifecycle/workflow

- Design your policy action/enforcement so that it follows your software development lifecycle.
- Having enforcement in place that corresponds with your software development workflow places quality gates in and around the flow of artifacts.

### Strive to stop builds for specific threat levels...but only if you can deal with the disruption

- Follow the practice of more mature organizations and stop builds for 9-10 threat levels – or, better yet, for 7-10 threat levels.
- Automatic enforcement of your governance policies during builds should be an organization's ultimate goal.
- However, it must be executed only when the organization's developers are able to handle the ensuing disruption.

## Reference Policy Best Practices

### Baseline your applications using the reference policy that comes with Lifecycle

- Around 90-95% of our customers use the default reference policies out-of-box as they are a solid indicator of open source risk.
- The reference policies are organized into 4 main categories listed below.

### Customize policies to match your existing open-source governance practices

- Around 90-95% of our customers use the default reference policies out-of-box.
- Most variations are to better align with pre-establish governance policies or to prioritize specific architectural risks.
- Rather than deleting the default policies, we recommend scoping them to an unused application category to make them easier to restore later.

### Use application categories to create specific policies for a subset of your applications

- Your applications may have different levels of risk aversion due to regulatory requirements or exposure.
- Create and manage policies at the root organization while using application categories to scope them to these applications.

### Turn on enforcement to block security-malicious components at every lifecycle stage

- Malicious components should never be allowed in your applications.
- Set your policy action to FAIL at all stages of development.
- Do not waive these violations nor allow the components to remain in your application.

### Sign up for Sonatype's policy workshop

- Partner with a Sonatype Customer Success Engineer to design your open-source governance policies.
- Our Customer Success Engineers will get your team up to speed with open-source governance best practices.
- During the workshop, you will amend the reference policy based on your organization's needs and goals.

### Modifying Policies in Production

## Continuous Monitoring Best Practices

Continuous Monitoring (CM) is the capability to automatically check your applications for any new violations every night.

CM needs to be configured to a stage before monitoring will start.

### Overview of the Continuous Monitoring (CM) Process

### Continuous Monitoring Decision Tree

![CM_Decision_Tree.png](/assets/images/uuid-7d8b3be9-aa4a-c0f7-b972-8f456fc46be2.png)

## General Lifecycle Best Practices

### Getting Started

### Integrate Lifecycle into your CI/CD system

### Configure Lifecycle for long-term success

### Enforcement and remediation

### Monitoring your IQ Server

As a critical part of your build pipeline, you will want to monitor the performance and operation of the IQ Server. The following are models common with Lifecycle developments.

### IQ Server data retention and maintenance

The IQ Server UI will display the latest scan for a given stage, however, every scan is retained as a separate report.

## Zero-Day Vulnerability Best Practices

A zero-day event is when a previously unknown vulnerability is discovered in a popular open-source component. This is often before the project has a chance to release a fix; giving the community no time to react and little options to move forward.

Lifecycle customers with Continuous Monitoring enabled will quickly learn where their environment is at risk and using enforcement, halt any builds from automatically deploying. This gives your development team time to respond and fix the issue; limiting the risk to the organization.

The best defense against 0-day events is to analyze your applications through every build to stop them from automatically deploying with newly discovered critical risks

Set notifications for continuous monitoring so new risk is immediately reported when discovered

Use the Dashboard for an organization-wide view of the total impact of the vulnerable component. Use the advanced search to find the component applications that are not continuously monitored nor regularly scanned.

### Create a playbook for handling 0-day vulnerability events

0-Day Vulnerability events are inevitable. Develop a plan now for responding to these events, and review it with your stakeholders.

- Have a designated captain to organize communications and follow up on action items
- The remediation strategy needs to be determined on a per-app basis. Avoid waiving the vulnerability for all applications until the impact is known.
- Focus on confirming the exploitability when the component is found in your most critical public applications
- Share lessons learned with the rest of the organization for a uniform response and reduce double work

## Source Control Integration Best Practices

### Configuration Best Practices

### Easy SCM Onboarding Best Practices

### Source Control Feedback Best Practices

## Backup and Restore Best Practices

Lifecycle is a critical piece of your infrastructure. Mature deployments have a maintenance plan that schedules a regular backup and upgrade plan. The plan should include an annual test of the backup with simulated outages and failovers.

Include step-by-step instructions with methods for password storage and recovery when needed.

### Backing Up

### Restoring

## Data Management and Storage Best Practices

The IQ Server is fairly lightweight, but managing your IQ Server's disk usage is important because:

Follow these best practices to manage your IQ Server's data efficiently.

### Deploy IQ Server into an environment with an appropriate amount of disk space

- Sonatype recommends that you have between 500 GB and 1 TB of storage available for the IQ Server. Your disk usage is largely a product of (the number of apps x the number of scan events). Therefore, scanning lots of apps frequently will fill up disk space fast. Customers who rely heavily on SCM integrations may benefit from more storage. Use sparse checkout file types with your SCM integrations to address this. To maximize your storage space, get the best performance, and for overall ease of management, use the Postgres database option.
- Your disk usage is largely a product of (the number of apps x the number of scan events). Therefore, scanning lots of apps frequently will fill up disk space fast.
- Customers who rely heavily on SCM integrations may benefit from more storage. Use sparse checkout file types with your SCM integrations to address this.
- To maximize your storage space, get the best performance, and for overall ease of management, use the Postgres database option.

### Follow your organization's data retention guidelines

- Your organization may have guidelines for storing assets long-term. Always heed and follow those guidelines.
- If you don't have data retention guidelines, consider putting some in place for IQ Server assets specifically. Reports for internal dev builds typically become irrelevant after a few months. Reports for a release/production version of your app should be kept for longer.
- Reports for internal dev builds typically become irrelevant after a few months.
- Reports for a release/production version of your app should be kept for longer.

### Have a way for stakeholders to protect specific data

- Some stakeholders may require specific data. For example, your Legal team may want to hold on to some key reports forever. Make sure you know what your stakeholders need, and have a way for them to request that some files never get deleted.

### Work with your database administrator

- Large-scale cleanup efforts should include your database administrator. Mismatches between your sonatype-work directory and your database can cause hiccups in the browser UI.

### Have a plan for long-term storage

- If you need to save a report for longer than 5 years, move it out of your work directory.
- Reports can be transformed into SBOMs for more efficient storage.
- Reports may contain sensitive information, including things like application names, component names, file extensions, and vulnerability data.

### Configure Data Retention

- Data Retention handles much of the regular cleanup associated with managing an IQ Server for you. It's on by default—leave it on!
- Data Retention can trigger based on age or based on the total number of reports in a given stage. Consider what stages you generally scan at, and configure accordingly. For example, if you rely heavily on SCM integrations, you'll likely have many scans at the Source stage. In that scenario, make sure the number of maximum reports at the Source stage is high enough that new reports aren't deleting old reports that you still need.
- For example, if you rely heavily on SCM integrations, you'll likely have many scans at the Source stage. In that scenario, make sure the number of maximum reports at the Source stage is high enough that new reports aren't deleting old reports that you still need.
- Purged files are placed into a separate trash folder. By default, this is sonatype-work/clm-server/trash. Files in the trash folder are not deleted automatically – they must be deleted manually. Whenever convenient, check the trash folder and delete the files therein.
- Files in the trash folder are not deleted automatically – they must be deleted manually.
- Whenever convenient, check the trash folder and delete the files therein.
- The contents of your trash directory may contain sensitive data. Compress reports still contain things like application names, component names, file extensions, and vulnerability data.

### Use sparse checkout for your SCM integrations

- Sparse checkouts of your SCM repositories only clone the files that IQ Server requires in order to perform a full scan. This can dramatically decrease the amount of disk space your IQ Server requires.

### Know what to save and what to delete

- Some files can be more safely deleted than others. Success Metrics is a measure of your IQ Server usage over time, so they should not be deleted or moved from the sonatype-work directory. Try to save them at least once a year. Reports may be okay to delete. Follow your organization's data retention rules, but remember that reports are a point-in-time record of your app's contents. Your most recent report is always the most important report. New log files eventually replace old ones. Check the Config YAML file to see how many archived log files are kept, and adjust up or down as needed. The default is 50. SCM files can be deleted safely; if the IQ Server needs them again, it will download them again. However, this could cause issues with your SCM repository's rate limit, if it has one, so exercise caution. Your Advanced Search index (sonatype-work\clm-server\search) is required for Advanced Search and the Advanced Search API. If it's deleted, you can reindex, but this will take some time. New scan files replace old ones, and each app only has one scan file at a time. This means that efforts to clean your scan folder aren't usually worth it.
- Success Metrics is a measure of your IQ Server usage over time, so they should not be deleted or moved from the sonatype-work directory. Try to save them at least once a year.
- Reports may be okay to delete. Follow your organization's data retention rules, but remember that reports are a point-in-time record of your app's contents. Your most recent report is always the most important report.
- New log files eventually replace old ones. Check the Config YAML file to see how many archived log files are kept, and adjust up or down as needed. The default is 50.
- SCM files can be deleted safely; if the IQ Server needs them again, it will download them again. However, this could cause issues with your SCM repository's rate limit, if it has one, so exercise caution.
- Your Advanced Search index (sonatype-work\clm-server\search) is required for Advanced Search and the Advanced Search API. If it's deleted, you can reindex, but this will take some time.
- New scan files replace old ones, and each app only has one scan file at a time. This means that efforts to clean your scan folder aren't usually worth it.

## Creating a Lifecycle Remediation Plan

The Lifecycle solution is most effective when used for automatic discovery and remedation of risk with using open-source components in your application development. Creating a remediation process will help you reduce risk across your organization by resolving policy violations from scan reports and improving the quality of OSS components used by your applications.

This article will help you identify, and put in process, ideal research and remediation guidelines for your organization.

### Audience

Sections of this guide may be more applicable to one role within your organization than another (i.e. analyzing findings is geared toward Project Owners while remediation workflows are more for Developers). However, everything here is informationally relevant to all roles.

### Desired Outcomes

By the end of this guide you’ll be able to:

- Understand the importance and need for remediation.
- Have a plan to get started with remediation.
- View and understand some basic remediation workflow examples.
- Measure your progress with IQ Server reports.

### Prerequisites

Remediation is an essential part of your risk reduction workflow. To get started, you will want to address the following:

- **Define your adoption model** . This is how applications and organizations are added to the IQ Server.
- **Identify application categories pertinent to your organization** . Application categories provide a way to prioritize the risk characteristics of an application and set specific policies for them.
- **Set up your governance policies** . IQ Server comes with a set of predefined policies used by the majority of organizations. These should be evaluated and updated to align with your application security priorities to get an accurate baseline of risk.
- **Evaluate your applications** . In order to remediate risk, you need to know what’s in your applications. We recommended getting a baseline of all your applications by integrating a scan in the build process, or by onboarding through your SCM. You can also run one-off scans in the UI or CLI.

### Importance of Remediation

After Lifecycle is set up and you’ve started scanning, it is easy to be inundated with results. The results of a scan can leave you with a lot of vulnerabilities that you need to deal with. You need to remediate to get the most out of Lifecycle and reduce risk to your organization.

Putting a remediation plan in place helps you accomplish the following:

- **Improved communication.** You’ll have a clear understanding of your organization’s risk posture, remediation workflows, and responsible stakeholders.
- **Better software** . Improved component selection helps you build better, more secure software.
- **More efficiency** . Early identification allows you to continue to work, even when issues arise during development.
- **Reduction of busy work** . Lifecycle delivers expert security information that lets you make informed decisions early, rather than at the end of a dev cycle.

While it’s good to understand the importance and need for remediation, you should also know that it is easy to get started remediating — especially if you have a plan in place.

### Make a Remediation Plan

In this section, you’ll define organizational roles, set remediation goals, determine your risk management process, and then put together a plan to socialize adoption. The Lifecycle project sponsor will drive most of the work described here.

### Review and Analyze Findings

Now that your plans are in place, the next step is for the Lifecycle Project Owner to take the report and prioritize your remediation process. The Lifecycle Project Owner is the one who analyzes scan reports and gets to actionable findings based on the defined organizational goals, the lifecycle of your application, and policy decisions set by the stakeholders. Developers will then apply fixes based on these findings.

In most cases, the remediation path is to upgrade to a patched version of the component. If a fixed version does not exist, or the risk of breaking API changes is too great, the Project Owner will need to manually evaluate the various types of risks that a security issue exposes. For example, the Project Owner may identify several types of security issues:

- **Configuration** : By default, the component is configured to be insecure, and needs determination if there is a case for direct exploitation.
- **Functional** : Requires a specific function to be called.
- **User Input** : Requires specific user-controllable input.
- **Test or Sample Code** : Has sample or test code not normally included in an operational context.
- **Operational** : Effects runtime operational context, often affecting JVM’s, application servers, or runtime configurations.

Once issues are identified, the Project Owner determines the risk and associated remediation effort (i.e. technical debt vs. exploitation in the application) and identifies the immediacy of fixing based on the CVSS score and your risk management threat analysis. It is then up to the developer to follow the applicable workflows and remediate the risk.

### Remediate and Reduce Security Risk

Now it’s time to start remediating based on your goals, review, analysis, and prioritization. Successful risk management is the process of identifying vulnerabilities and threats and then deciding what actions you can take to reduce those risks and reach your goals.

This next section will give you some example developer remediation workflows that can help you focus on how to lower risk. Remediating risk starts with improved component selection based on data. This data is generally found in the Component Information Panel or CIP, which is available from the Lifecycle UI and also in our IDE integrations. Information provided in the CIP helps developers investigate their choices and select better components based on newer available versions, most popular versions, and security and licensing issues.

In general, policy resolution can be achieved by completing one of the following tasks:

- **Upgrade to a non-vulnerable version of the same component** . This option is most recommended because it is generally the easiest path to resolution and reducing your risk.
- **Migrate to a component that does not contain the violation** . If you’re not able to upgrade your component, the next step is to migrate to a similar component without the violation. This option involves research because you’re looking for a replacement component that provides the same functionality while ensuring it’s not exploitable.
- **Request a waiver for the policy violation** . If you can’t upgrade or migrate, the next option is to request a waiver. Send a waiver request to the Project Owner with enough information for a determination to be made. Applying a waiver assumes a certain amount of technical debt, and does not fix the violation. Because of this, it should be used judiciously.

### Measure Your Progress

Sonatype Lifecycle provides many ways that you can measure your remediation success:

- **Success Metrics** are high-level, executive reports that can help you demonstrate the value of the Lifecycle solution. Specifically, the Mean Time to Resolution (MTTR) by Month tile shows the average age of resolved violations for the last year. This information is further broken down by their threat level.
- The **Application Composition Report** represents the health of your application. It serves as a point-in-time report representing security and license risks associated with component usage for a specific application. The report includes information on how the application complies with the policies your team, or business, has established.
- Finally, the **Dashboard** provides the quickest way to review the overall health of the applications you manage. The Dashboard provides filters that let you view results by things like organization, violations found within a specific stage, or policy type.

## Remediation Best Practices

### Introduction

The following best practices are guidelines to consider when starting your remediation efforts.

Empower your developers with these principles to improve outcomes:

### Baselining

Before breaking builds and sending out a wall of notifications, baseline your applications by getting an initial scan of applications in your SDLC. This can be done using the SCM onboarding tool or working through the CI scanners. Writing a shared library of scanning tools for your CI builds will allow you to make changes as your efforts mature.

### Prioritization

When prioritizing violations, it is useful to follow the 80/20 rule. 80% of the violations take 20% of the time with the last 20% taking 80% of the time.

- Focus on quick wins while reducing noise
- Give development teams a chance to review scan reports
- Avoid blocking builds when there are a large number of violations to remediate
- Avoid filling up developer backlogs with OSS violation tickets

### Remediation

### Mitigation

### Reviewing Risk

Waivers help your development teams manage risk by prioritizing what is important and deferring the issues that may be addressed later.
