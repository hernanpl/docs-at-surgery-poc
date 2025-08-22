---
layout: default
title: "Reporting"
parent: Sonatype Lifecycle
nav_order: 6
---

# Reporting

The Reporting section is where you'll learn everything you need to know about the Application Composition Report and our Success Metrics reports. The Application Composition Report serves as a point-in-time report representing risk associated with component usage for a specific application. Success Metrics demonstrate the value of IQ Server and should be used as high-level executive reports.

This [eLearning course](https://learn.sonatype.com/courses/iq-103/) provides a great overview of component remediation.

## Lifecycle Dashboard

Lifecycle’s dashboard is the fastest way to baseline and monitor the health of your applications. The dashboard provides insights into your organization's open-source consumption and helps you prioritize the highest risk.

Users need the `View IQ Elements` permission for at least one application to view the dashboard.

### Dashboard Results

The dashboard results display information based on the applied filters. The same filters continue across the different views with the results differing depending on the selected view.

Features common across tabs on the dashboard.

- **Filters** - Focus on specific violations. Save your custom views to match your workflow. Research the highest risk across each development team. See for details.
- **Sort** - Select the column headers to change how the data is organized. For example, you may prioritize the highest risk or the latest violations.
- **Export Data** - Save the content of any view to a spreadsheet for a point-in-time review or to generate custom reports.
- **Total Risk** - is the aggregated policy threat scores for the scoped violations on a component across the scoped application reports. Use the filters to update the scoped violations and applications.

### Violations View

The Violations view displays the policy violations found in applications you have permission to view.

Selecting a violation opens the showing the violating policy and the stages where the violation has been identified. Security violations include a detailed explanation of the vulnerability.

see

**Prioritize and Remediate**

- Filter results to newly discovered critical violations that have occurred in the last few days to coordinate a response with your development teams on the best path forward.
- See the latest breaking violations across your build pipeline; review the violation details while requesting a waiver without having to navigate to individual scan reports.

**Audit Risk throughout the Organization**

- Generate a detailed view of risk across business units. Export the view to deliver reports to stakeholders and business intelligence tooling.

### Components View

The Components view organizes components based on their total risk to the enterprise. The threat scores assigned to policy violations are aggregated by component and anywhere the component is found in the filter's application scope. The risk is also calculated across the threat ranges; critical, severe, moderate, and low to apply additional meaning to the total score.

Selecting a component opens the component risk overview page which displays the applications the component is found as well as a breakdown of the violations.

see

**Prioritize and Remediate**

- Select the components with the most risk and provide remediation instructions to the team members of each of those applications.

**Audit Risk throughout the Organization**

- Export a list of all the components used in your organization.

### Applications View

The Applications view provides a high-level baseline of your total organization risk and which applications have the greatest risk. Access the latest reports for each stage that have been evaluated for the application

The threat scores are assigned to policy violations from the application scan report and aggregated based on the current filters. The risk is also calculated across the threat ranges; critical, severe, moderate, and low to apply additional meaning to the total score.

see

**Prioritize and Remediate**

- Identify applications’ aggregated risk to prioritize remediation

**Audit Risk throughout the Organization**

- Generate a baseline report of total risk to track over time. Use these totals to estimate the effectiveness of your SCA program and the value the tool is generating.

### Waivers View

The waiver view shows waivers based on your filter selections. Click on a waiver to navigate to see the waiver's details.

The Upgrade column indicates when an upgrade is available for a waived component. This configuration is not set by default.

Learn more about .

**Note:** For accurate results, we recommend checking the *Upgrade* column for available upgrades after 24 hours of configuring the *Waived Component Upgrades* feature or applying a waiver.

see

**Prioritize and Remediate**

- Use the expiration date filter to review soon-to-expire waivers for build-failing violations to proactively remediate or renew the waiver.
- See which components have a non-violating version so development has a clear path forward.

**Audit Risk throughout the Organization**

- Revoke permanent waivers that do not have an exploration date
- Review waivers that are overly broad potentially hiding critical risk
- Audit existing waivers for quality and compliance

### Use the Solution Switcher

Need to switch to another Sonatype solution, seamlessly?

Click on the [Solution Switcher](#UUID-f6cc2b00-f036-2711-ba56-621efcd473a5) icon in the top right navigation bar to experience other licensed Sonatype solutions, including Sonatype Lifecycle, Sonatype Developer, Sonatype SBOM Manager, and Sonatype Repository Firewall.

### Dashboard Filters

The filters menu is accessible from the "Filter" button on the upper right side of the Dashboard as seen in the screenshot above.

You can create a customized filter to fine-tune the results displayed in the Dashboard to analyze them better.

Use the Apply button to view the updated results of the filter.

To save an applied filter selection, click the Save button. Saved filters can be reused from the dropdown at the top of the sidebar.

### Export Violation Data

### Export Component Data

For the components tab, all Risk columns are calculated by taking the associated Threat Level of the policy violation and multiplying it by the number of affected applications.

The columns exported into the file are:

### Export Applications Data

For the applications tab, all Risk columns are calculated by taking the sum of the associated Threat Level of the policy violations of all affected components in the application.

The columns exported into the file are:

### Exporting Waiver Data

Select Export Waivers Data to download the waiver data to a CSV file. The table below lists the information included in the waiver export.

## Waivers

Waivers are used to temporarily accept a specific risk when depending on an open-source component in your application to resolve the associated policy violation. Waiving a violation does not make your application more secure nor will it remediate the violation. Waiving will resolve the violation in the application report and keep the violation from triggering policy actions.

Waiving the violation meets the following use cases:

### Waivers and Repository Firewall Quarantine

Using Repository Firewall, components with policy violations set to fail are put into a quarantine to keep them from being downloaded during an application build. Waivers are used to release components by waiving all the failing violations against the component. Once the component has been allowed into the repository, failing violations will not put the component back into quarantine.

In some use-cases, you may want to release a component from quarantine but still trigger policy violations where they are found in applications during a Lifecycle analysis. The waivers used to release the component should be scoped to either only the repository from which they were quarantined or using a short lived time-based waiver. Once the waiver expires, the component will again trigger the violation. However, since it is already in the repository, it will not be quarantined.

To quarantine the component again, delete it from the proxy after the waivers have expired or remove the waiver before attempting to download it again.

### Waivers and Legacy Violations

Legacy Violations are an effective way to accept a base level of risk without a detailed review of the violations. They are configured at the policy level and apply directly to all violations in an application as a single configuration. This feature is useful for legacy applications not in active development to only prioritize newly discovered risks. Violations that are hidden by legacy violations may be reviewed and addressed without disabling legacy violations for the application.

Waivers are applied to the specific metadata associated with component violations. They are intended to provide granular control and violation management. Consider using legacy violations instead of applying bulk waivers to all violations especially when they have not been reviewed by the development team.

### Waiver Properties

### Waiver Management

Manage waivers from the violations details on the Dashboard or tab, or directly from the waiver dashboard.

- Violation Details page - click on any violation in the dashboard violation view.
- Policy Violations view - click on a violation in the application composition report.

### Automated Waivers

**Automated Waivers** allow you to automatically manage waivers for low-risk security policy violations that have no upgrade path (i.e., no safe component version available) and/or if the violating component is not reachable. Once configured, automated waivers will be applied and removed dynamically, based on the upgrade path and reachability, at the time of application evaluations.

Violations that are *auto-waived* will not trigger policy actions, saving time and effort otherwise spent requesting and creating waivers. The *auto-waived* policy violations will be excluded from subsequent application evaluations, allowing the development teams to focus on the policy violations that are more actionable.

Automated waivers are not permanent; they are automatically removed if there is a change in the condition that justified the waiver. For example, if an auto-waiver was applied to a policy violation for a vulnerability that was not reachable, now becomes reachable, the auto-waiver will be removed because it no longer satisfies the *Vulnerability is Not Reachable* condition. Similarly, if a safe version of the component is now available, the auto-waiver will be removed from the policy violation because it no longer satisfies the *Upgrade Path is Not Available* condition.

Automated waivers are context-aware, leveraging Reachability Analysis to make intelligent, application-specific decisions. Rather than applying waivers based on conditions that are relevant to context of the root or parent parent organization, the system evaluates each violation in the context of the specific application’s usage and risk exposure, and applies automated waivers if relevant to the application context.

### Examples of Waiver Scoping

Imagine that your application has a component called 'example' which has a reported vulnerability CVE-20XX-1000 with a CVS of 10. There's a policy called Security-Critical with one constraint, and that constraint has one condition that reads "Security Vulnerability Severity greater than or equals 9."

Review the table below to see how the various scoping options would affect a waiver.

### Similar Waivers

The Similar Waivers feature offers users the convenience of looking up *similar* waivers for a specific policy violation. The waiver details displayed in the *Violation Details* pane can be useful in determining if the selected policy violation can be waived for similar reasons.

A waiver is considered "similar" if it meets all of the following conditions:

- The user has *View* permission for the waiver, i.e. View permission on the organization or application that the waiver is scoped to.
- The waiver is created for the same policy.
- The waiver is applicable to the current component, either by being an exact waiver, applicable to any version of the same component or by being applicable to “All components”.
- The expiration date of the waiver is later than the current date.
- The waiver is not already applicable to the policy violation.

For **security violations** only, a waiver is considered "similar" if the vulnerabilityId (CVE or Sonatype Id) matches the vulnerabilityId of the security violation.

### Requested Waivers

The *Requested Waivers* tab on the Waivers dashboard provides a quick reference to all requests that have been made to waive policy violations. Users with permissions to waive policy violations (reviewer) for the organization or application can review each waiver request in detail and choose to apply or reject it.

![Requested_waivers.png](/docs-at-surgery-poc/assets/images/uuid-f57ee13b-b70d-32e6-8fea-b9d86b16022c.png)

Use the filter to retrieve *Requested Waivers* for a specific organization or application, repository, application category, policy type, expiration date, policy threat level, and the waiver reason.

### Transitive Violation Waivers for InnerSource

Waiving violations for components that are both transitive and Innersource can be a challenge. The Transitive Violations Page lets you view all the transitive violations brought in by an Innersource component and quickly view, manage, and apply waivers.

## Application Composition Report

The Application Composition Report is a point-in-time report detailing the policy violations affecting the use of open-source components found in your application. The report includes information on how the application complies with the policies your team, or business, has established.

![178716743.png](/docs-at-surgery-poc/assets/images/uuid-8d4b557d-f0fe-45e1-e540-06f02a81b31b.png)

### Accessing the Report

Access the Application Composition Report from either the Reports Area, the Organizations and Applications area, or via direct URLs.

### Reviewing a Report

### Component Details Page

The Component Details Page is where you can drill down on individual components that appear in your scanned applications, along with the policy violations associated with them.

### Component Information Panel

⚠️ **Warning:** Lifecycle customers with IQ Server version 128 or above will see the [Component Details Page](#UUID-c348055a-b083-a26c-6dda-b4cfda3cf2ef) instead of the CIP. However, the CIP may still appear in IDE integrations or as part of Repository Firewall.

### Dependency Tree

### Reviewing Security Vulnerabilities

Our proprietary Sonatype vulnerability data powers your evaluations and flags all policy violations that are associated with component vulnerabilities. We recommend remediating these vulnerabilities to maintain a strong security posture. Use the recommended version information under the Risk Remediation Section (on the [Component Details Page](#UUID-c348055a-b083-a26c-6dda-b4cfda3cf2ef) .)

However, based on the context of your application or your organizational security policies, some of these violations may not be applicable to you. You can review these violations and determine the next steps for resolving them.

To prevent the violations from blocking your development workflow, you can:

### Component License Information

Just like IQ Server can have policies about security vulnerabilities, it can also have policies for the licenses associated with open-source components it might find in your applications.

### Component Identification

### Assigning Component Labels

Component labels allow you to tag individual components to target them in policy constraints. Policies are configured with a constraint against that label. You are free to assign the label to any components that should be targeted or avoided by the policy without having to modify the policy.

![iq-policy-constraint-component-label](/docs-at-surgery-poc/assets/images/uuid-5df7a4fe-0e84-e900-d8e2-a22ccb7494a4.png)

Component label creation and management are performed in Organization & Policies. For more information on creating or managing component labels, see [Component Labels](#UUID-d2a72712-e91d-bd83-a78c-b89fdeab64ae) .

Assign labels to a component using the Component Information Panel.

### Scan Reports

### View Latest Evaluations

This option is available from the [Options dropdown](#UUID-cdab48b3-4098-bf5e-687a-cfe743c4d40e) on the Application Evaluation Reports page.

The *Latest Evaluations* page contains a list of the last twenty evaluation reports for the selected stage.

![Latest_Evaluations_189.png](/docs-at-surgery-poc/assets/images/uuid-a1863fa9-0734-272a-ccc0-eeb2bb2c97bb.png)

**Note:** Cannot Find a Report? If an application evaluation report has been purged, it will not be accessible under the *Latest Evaluations* . Refer to [Data Retention Configuration](#UUID-2b3cfee1-89f1-01d1-3054-80b82081877c) for details on purging and retrieving the purged reports from the trash directory.

### PDF Report

Not everyone will have access to the IQ Server or any of the integrated enforcement points, and in turn, any of the associated reports. However, certain individuals or teams would likely still benefit from the information the Application Composition Report provides. Even if that’s not your particular situation, you may reach a point where you would like to produce an archive of an Application Composition Report for historical and audit purposes. Given this need, a PDF can be generated for every report you produce.

### Options Dropdown

The Options dropdown button, located in the top-right corner gives you the options available to export the Application Composition Report.

![Options_dropdown.png](/docs-at-surgery-poc/assets/images/uuid-1494ef7e-a66e-e6d9-2ae1-7a4d25175d3c.png)

### InnerSource Insight

### Re-evaluating a Report

## Success Metrics

Sonatype Lifecycle automatically tracks statistics about its usage called Success Metrics. These statistics reflect policy evaluation, violation, and remediation, which are aggregated monthly or weekly. By following the trends in policy evaluation data, you can monitor progress toward your organization’s goals with Lifecycle. For example, an organization using Lifecycle to select safer open-source components can measure its success with the newly discovered violations' statistics. Success Metrics are available in the Lifecycle UI and through the API. The data in the UI provides visualizations out of the box while the API allows you to use your own tools to analyze data or automate data collection.

The Success Metrics data is designed to demonstrate progress toward your organization’s goal with Lifecycle. This is not designed to audit the health of an application or organization. As a result, it only includes aggregated counts of violations and general risk categories for violation counts.

### Calculating Success Metrics

Success Metrics are aggregated from historical data across all stages. Sonatype Lifecycle can tell if a violation was previously identified in an earlier scan, even if that scan was in a different stage. For example, if a violation appears in both the Build stage and Release stage, Success Metrics will only count that violation one time.

The REST API returns these aggregated counts for each application over a specified time period. Sonatype Lifecycle tracks exactly when each violation is first found and when it is resolved. This is used to calculate how long the violation was opened. An average of all violation resolution times is returned as the Mean Time To Resolution (MTTR). Like with other tallies, this statistic is aggregated across all stages.

The Success Metrics UI can display data for multiple applications. To handle this, Lifecycle will total or average statistics across all applications as appropriate.

Note that as of version 189, a user must have CONFIGURE_SYSTEM permissions to create and view success metrics reports.

### Risk Categories

Success Metrics groups violations into categories corresponding to their Threat Level, a subjective value placed on the perceived risk of a policy violation.

Additionally, the API groups violations into several categories. These categories are defined below.

### Success Metrics in the UI

Sonatype Lifecycle can generate Success Metrics reports through the user interface. These reports are standardized and provide visualizations and derived metrics based on the Success Metrics Data. The data charts and graphs in these reports are designed to show trends in application policy violations over time allowing you to monitor progress toward your goals. The reports created through the UI can be customized to show specific applications or all organizations.

### Success Metrics via API

Sonatype Lifecycle also provides data through a REST API. The Success Metrics API lets you retrieve data about your applications. Using the returned data, you can create custom reports or data visualizations to better measure your organization’s use of Lifecycle. The API allows you to automate data collection and quickly receive Lifecycle data. This is the same raw data used in the UI and can be fetched as either a JSON or CSV format.

### Making an API Request

The Success Metrics Data API can be accessed using a POST request. The API can return data as either a JSON or CSV. The returned format is specified in the request headers along with authentication information and time period. The start and stop dates for the request accept the [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601) . In this format, the first week of the year is the week with the first Thursday in January. The annotated API request below has information about the specific values the Success Metrics API accepts.

### API Value Reference

The tables below define the individual values returned by the Success Metrics API. The values are grouped into categories based on the kind of data returned.

### Limiting Success Metrics to a Stage

By default, the violation data for all eligible states is used to generate Success Metrics. You can limit Success Metrics to a single stage, by specifying the stageId.

Using the [Configuration REST API](#UUID-0fa6ca2c-1237-6aca-a4e6-ad4d074fd63f) , set the value of the property *successMetricsStageId* to the desired stage. Allowed stages are:

- source
- build
- stage-release
- release
- operate

- Success metrics data will be retrieved only for those stages which the IQ instance is licensed for.
- Limiting the Success Metrics to a single stage will only apply to future aggregations, from the time the change was made. It will not be applicable for success metrics aggregations generated previously.

### Disabling Success Metrics

Success Metrics can be disabled by an administrator in the Lifecycle UI:

![Screenshot of window to enable success metrics](/docs-at-surgery-poc/assets/images/uuid-67a1a189-91b9-b514-d635-568e69d4ef0c.png)

### Additional Resources

Success Metrics is a powerful tool to track progress toward goals with Sonatype Lifecycle. The UI provides visualizations and reports while the API provides customizable data and allows you to retrieve data for use with your own tools.

Additionally, the [Success Metrics Community Project](https://github.com/sonatype-nexus-community/nexusiq-successmetrics) provides a simple web application for viewing Success Metrics and creating PDF reports. This tool is not supported by Sonatype. The following are Sonatype resources for Success Metrics:

- [Success Metrics Data REST API Documentation](#UUID-001207f2-3e23-3558-ea07-d70a4ea4b004)
- [Rest APIs Documentation](#UUID-2e8bede8-1587-8455-0658-e63ba0f39cab)

## Vulnerability Lookup

The vulnerability lookup view allows the user to search for Sonatype-proprietary and CVE vulnerabilities.

There are two ways to access this page: directly from the navigation bar or by clicking on the vulnerabilities identified .

The Vulnerability List Report will show the result of searching for that particular vulnerability.

The page is comprised of two sections: the search box and the vulnerability details.

![126654411.png](/docs-at-surgery-poc/assets/images/uuid-7e1d0728-4beb-24f6-4066-3242bc291799.png)

Vulnerability lookup is an exact match search using vulnerability ID as an input.

Find will send a request to our data services and return the latest information we have about a vulnerability. The vulnerability need not have been already identified in any of your applications or repositories scanned by IQ Server.

**Note:** CVEs not found in Sonatype data Our vulnerability search feature is used to search for vulnerabilities that exist in components we have ingested into our data. It is not a general lookup for all CVEs reported on the [National Vulnerability Database (NVD)](https://nvd.nist.gov/) . The search will not show vulnerabilities for components we have not ingested.

### The Vulnerability Details

Once a lookup is performed with a valid vulnerability ID, or if coming directly from a link in the Vulnerability List Report, the page will show the details corresponding to that particular vulnerability.

![153060747.png](/docs-at-surgery-poc/assets/images/uuid-03ae4a42-9eec-0f5a-9d46-671382410e11.png)

Within these results, the user can find detailed information about a vulnerability, such as an explanation of what comprises the vulnerability, relevant links to more information, severity scores, detection, recommendations, and whether or not the entry has gone through Fast Track or Deep Dive research.

### Anonymous Vulnerability Lookup

You can look up a vulnerability without logging in.

A link to the vulnerability lookup page is now provided in the Login dialog:

![137206046.png](/docs-at-surgery-poc/assets/images/uuid-2a7f2329-4db2-fb66-3faa-974d224821ba.png)

When a lookup is performed anonymously, the provided vulnerability information is limited to the following vulnerability details:

- Issue
- Severity
- Source
- Explanation
- CVSS Details

![153060299.png](/docs-at-surgery-poc/assets/images/uuid-161e813b-1a90-d6d2-b820-88e369a48a74.png)

## Advanced Search

The Advanced Search feature allows you to search the configuration and component details from the UI.

This feature is enabled by default and the search index is created automatically. System Administrators may manually recreate a search index from the Advanced Search configuration. This page is accessible from the System Preferences menu. The enabled checkbox needs to be checked before recreating the index. The last indexed time will display once the index has successfully been created.

The Advanced Search does not return policy violations.

- Use the for searching policy violations.
- Use the to search for quarantined components.
- To script advanced searches, use .

The Advanced Search automatically re-indexes when changes are made to the data. Automatic indexing only applies to data changes made while the feature is enabled.

Advanced Search feature retrieves results from large data sets. To limit risk to the performance of the server by consuming too much of the service resources, limits to the query results are in place. You will see an error message asking you to narrow down the search when this occurs.

You may export the results of an advanced search by selecting the Export Results button from the Advanced Search page. The search results are downloaded in a CSV file.

Results may also be exported using the Advanced Search REST API.

![123404564.png](/docs-at-surgery-poc/assets/images/uuid-d2294c03-fd72-00e4-ba1e-94ff8ecb445f.png)

**Note:** Limitations with the Advance Search The Advance Search does not list all vulnerabilities known to Sonatype. The complete list of vulnerabilities are stored in Sonatype's proprietary Hosted Data Services (HDS) database and is used during the application analysis.

### Performing a Search

Fine-tune the search query by combining multiple search terms/item types with the supported search syntax. Such queries are used to find specific organizations, applications, components, and policies by names, IDs, etc.

Steps to use Advanced Search:

Selecting any search item type from the Component category will give an option to retrieve:

You can search for components or vulnerabilities in applications that belong to a specific organization by including the organization name or organization ID in the search query.

The search retrieves components and vulnerabilities from applications directly managed by the organization specified in the search query.

Searching into the organization hierarchy is not supported by the Advanced Search. Including an organization in the search query will not retrieve results for its child organizations.

### Search Examples

The following are examples using the Advanced Search.

### Reference- search item types and field names

Refer to the tables below for search item types and examples when building a search query.

## Enterprise Reporting

*Enterprise Reporting* (known as *Data Insights* until release 191) is your one-stop access to understand your organization's open-source consumption patterns including AI/ML components, risk and remediation patterns, and factors affecting the overall security posture. It summarizes how Sonatype Lifecycle impacts the security profile of the development pipelines within your organization.

**Note:** We have implemented the dashboards using the Looker™ platform for versatility. The visualizations will continue to evolve in functionality or scope, based on future improvements and user feedback.

### Data Handling Processes for Enterprise Reporting

To address the concerns due to data processing with our third-party reporting tool, Looker™, we have implemented a 4-way protection methodology:

- Data Storage No data is stored in any third-party tool. We use the third-party tooling's streaming capability to receive the query results directly from the Sonatype environment in a dedicated instance. The data is transmitted without being stored.
- Data Anonymization The information for these visualizations and reports is restricted for an organization from the anonymized telemetry during application analysis performed via Sonatype Data Services.
- Data Authentication and Authorization To ensure that the data in these visualizations is accessible to authorized users only, the system programmatically creates obfuscated, unique one-way hash identifiers for the user and the organization's instance.
- Data Encryption We implement encryption for data in flight from the Lifecycle environment to the third-party reporting tool.

For added security, the vulnerability data for a specific application or component is not included in any of the dashboards.

### Prerequisites

- Your browser has no restrictions on accessing “*. [looker.com](http://looker.com/) ” URLs
- For the Safari browser, “ *Prevent cross-site tracking* “ in the *Settings* menu → Privacy is **disabled.**

### Accessing

Click on *Enterprise Reporting* from the left navigation bar.

![ER-sidebar.png](/docs-at-surgery-poc/assets/images/uuid-49600a69-e788-6b39-17bf-470c8e3c64fa.png)

### Get to know your Enterprise Reporting Landing Page

![Landing_page.png](/docs-at-surgery-poc/assets/images/uuid-b6049fdd-4a74-a968-f93f-a4c1fe2d3bb4.png)

The Enterprise Reporting landing page displays the following information:

- **Enterprise Dashboards** Enterprise dashboards offer a set of logically related visualizations or charts to provide a complete picture of key aspects that impact the organization security and compliance risks. The individual visualizations in an enterprise dashboard are curated and compiled to empower users to make data-driven informed decisions and maximize on the capabilities value delivered by using Sonatype Lifecycle to improve the program efficacy.
- **Data Insights** Data Insights are standalone visualizations that enable focused analytics and data exploration. Based on the data generated as a result of using Sonatype Lifecycle, these visualizations answer specific task-oriented questions like reporting applications containing End-of-Life (EOL) components or AI/ML components, applications on-boarding rate, scan rates, component upgrades (Upgrade Posture) etc.

### AI Models Usage

### Component End-of-Life

Sonatype captures the declared End-of-Life (EOL) for open-source software (OSS) projects. Components that are end-of-life are declared either in project metadata, readme files, or in other official locations that they are no longer supported and have reached end-of-life". For components that have multiple versions, the EOL is tracked only for the latest version of the component.

EOL components do not receive enhancements, security issues may go unreported and unpatched while bug fixes are ignored. A lack of updates to EOL components may present a sense stability and of false security; leaving consumers open to the risk of being exploited.

This dashboard displays a list of applications and the corresponding EOL components detected by *Lifecycle* . Based on this data, you can strategically plan to retire old OSS components and migrate to the latest supported ones.

**Note:** The EOL dashboard currently displays components of npm, Maven, NuGet, and PyPI format/ecosystems.

### Machine Learning AI

### Rolling Recap Dashboard

### Supply Chain Monitoring

### Dependency Scorecard

**Note:** Retiring August 31, 2025 To enhance your Enterprise Reporting experience, we're continuously evolving our *Data Insights* . As part of this, the Dependency Scorecard's data refresh will end on **July 31, 2025** , with it formally being retired **August 31, 2025** . We're excited to bring you new and improved insights soon, so keep an eye on this space for updates!

### Stack Divergence

**Note:** Stack Divergence is under active development; views and functionality are subject to change.

### Upgrade Posture

### Security Risk Trends

### Security Risk Breakdown

### Success Metrics Enterprise Dashboard

### Waivers Explorer
