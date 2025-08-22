---
layout: default
title: "Sonatype IQ Server Release Notes"
parent: Sonatype IQ Server
nav_order: 1
---

# Sonatype IQ Server Release Notes

The IQ Server Release Notes cover the full suite of solutions powered by IQ Server. This includes **Sonatype Lifecycle** , **Sonatype Developer** , **Sonatype SBOM Manager** , and **Sonatype Repository Firewall** .

![IQ Server Banner](/docs-at-surgery-poc/assets/images/uuid-84fc4a83-56af-0f9f-d6e8-1f1b918704e4.png)

Explore release-specific details by selecting a release note below. Alternatively, get a quick summary of all releases within a given year on the respective year landing page.

- [IQ Server 2025 Release Notes](#UUID-358dbf93-d21c-da99-fe31-ede3732a0846)

## Download IQ Server

As a best practice, we recommend that you keep your installation up to date (not trailing behind for more than six months) to benefit from the latest features and advancements in component intelligence. You can keep track of versions that are no longer supported in our [IQ Server Version Status section](#UUID-d47113e2-9a13-24c5-b05a-f7e487b88039) .

Download the latest version from our [Download and Compatibility section](#UUID-4e396b62-fd65-1cfc-dd99-2fb0a20e7b36) .

## Upgrading IQ Server

If you are upgrading from an earlier version, please see .

## 2025 Release Notes

This page contains a list of 2025 IQ Server releases, links to each release's release notes, and a brief list of major changes per release.

**Note:** While we strive to fully document new features before releasing them to our Cloud environments, there may be occasional delays. In such instances, we will update this page with links to the relevant help documentation as soon as it becomes available.

### Summary of Major Changes in 2025

The following table lists major changes in 2025 that should be considered when upgrading to a new version.

Features and fixes are added to Sonatype Cloud-based deployments on a **weekly** basis. The same features and fixes are made available to self-hosted deployments on a **monthly** basis.

### Sonatype IQ Server 193 Release Notes

**Released July 9, 2025**

The IQ 193 release includes multiple changes to our IQ-powered solutions. View the details in each solution’s section below.

### Sonatype IQ Server 192 Release Notes

**Released June 11, 2025**

The IQ 192 release includes multiple changes to our IQ-powered solutions. View the details in each solution’s section below.

### Sonatype IQ Server 191 Release Notes

**Released May 6, 2025**

The IQ 191 release includes multiple changes to our IQ-powered solutions. View the details in each solution’s section below.

### Sonatype IQ Server 190 Release Notes

**Released April 2025**

The IQ 190 release is primarily a bug fix release. View the details in the [Bug Fixes section](#UUID-22bef9c3-b772-6045-1512-14d0b8f976c8_id_IQ189ReleaseNotes-BugFixes) .

**Note:** Data Insights Enhancement: Enhanced Security Risk Analysis Dashboard We’ve enhanced the *Security Risk Analysis* dashboard to provide greater insight into security risks. A new *Violations Over Time* table allows users to track the trend of open and waived violations monthly, offering a historical perspective on their security posture. Additionally, you can now filter by *Violation Type* and display only *Legacy Violations* or *Non-Legacy Violations* to help you differentiate between new and pre-existing violations. For full details, see the [Security Risk Analysis Dashboard help documentation](/document/preview/261290#UUID-f1bed07d-8d75-ca7c-47d3-14e360d24901) . Security Risk Analysis

### Sonatype IQ Server 189 Release Notes

**Released April 2025**

The IQ 189 release includes multiple changes to our IQ-powered solutions. View the details in each solution’s section below.

### Sonatype IQ Server 188 Release Notes

**Released March 2025**

The IQ 188 release includes multiple changes to our IQ-powered solutions. View the details in each solution’s section below.

### Sonatype IQ Server 187 Release Notes

**Released February 4, 2025**

The IQ 187 release includes multiple changes to our IQ-powered solutions. View the details in each solution’s section below.

### Sonatype IQ Server 186 Release Notes

**Released January 8, 2025**

The Sonatype IQ Server 186 release includes multiple changes to our IQ-powered solutions. View the details in each solution’s section below. Also be sure to check out our [release-specific upgrade instructions](#UUID-f105bc66-d70f-7a04-17b2-37846a8cdbe5) before upgrading.

## 2024 Release Notes

### Release 185 (December 2024)

**Note:** Upgrade Impact After upgrading a Lifecycle instance using a PostgreSQL database from IQ 182 or earlier to IQ 183 or later, for high data volume installations, you may **temporarily** see an internal error when accessing the Violations dashboard. This is due to an internal job running in the background taking longer to process the large volume of data, and is logged as a NullPointerException (NPE) in the logs. Once the job completes, the dashboard will load as expected, and NPE will no longer be visible in the logs.

### Release 184 (November 2024)

**Note:** Upgrade Impact After upgrading a Lifecycle instance using a PostgreSQL database from IQ 182 or earlier to IQ 183 or later, for high data volume installations, you may **temporarily** see an internal error when accessing the Violations dashboard. This is due to an internal job running in the background taking longer to process the large volume of data, and is logged as a NullPointerException (NPE) in the logs. Once the job completes, the dashboard will load as expected, and NPE will no longer be visible in the logs.

### Release 183 (October 2024)

### Release 182 (September 2024)

### Release 181 (August 2024)

**Note:** Emergency Bug Fix Release This release fixes an issue with versions 179 and 180 that could cause IQ Server instances to shut down when using Source Control Management (SCM) features like Automated Pull Requests and Pull Request Commenting. Users running versions 179 or 180 should upgrade to this version immediately.

### Release 180 (August 2024)

### Release 179 (July 2024)

**Note:** Support for Java 8 and 11 is being phased out for *Sonatype IQ Server* and *Sonatype IQ CLI* from this release onwards. Java 17 is recommended for this release. Java 17 will be **required** from the next release onwards.

### Release 178 (June 2024)

**Note:** This release fixes an upgrade issue with Sonatype IQ Server versions 169 and above, which rendered the upgraded instance in a non-functioning state when the upgrade process was interrupted.

### Release 177 (June 2024)

### Release 176 (May 2024)

### Release 175 (April 2024)

### Release 174 (March 2024)

### Release 173 (February 2024)

### Release 172 (February 2024)

**Note:** Emergency Bug Fix Release This release fixes an issue with versions 170 and 171 that could cause out-of-memory errors on high-volume installations. Users running versions 170 and 171 should upgrade to this version immediately.

### Release 171 (January 2024)

⚠️ **Warning:** This version may cause out-of-memory errors on high-volume installations. We do not recommend upgrading to this version, unless necessary. A fix for this issue will be available soon.

## 2023 Release Notes

### IQ Release 170 (December 2023)

⚠️ **Warning:** IQ release 170 may cause out-of-memory errors on high-volume installations. We do not recommend upgrading to this version.

This release includes several database changes to complete our transition to using the term Legacy Violations. Users may experience longer upgrade times (around an hour.)

### IQ Release 169 (November 2023)

This release fixes a critical issue that affected the command line scanning of SBOMs and containers on installations of release 168 running on the embedded H2 database. Earlier versions (prior to 168) or those running on PostgreSQL (external database) are not affected.

Users facing issues with release 168 installations running on the H2 database should upgrade immediately.

This release includes several database changes to complete our transition to using the term Legacy Violations. Users may experience longer upgrade times (around an hour.)

### IQ Release 168 (October 2023)

The Repository Firewall Guided Setup simplifies onboarding JFrog Artifactory® repositories to enable users to get started with Firewall in a few easy steps. The automated process guides first-time users to maximize supply chain protection by providing configuration recommendations for Firewall based on the host (users') environment.

### IQ Release 167 (September 2023)

The Repository Firewall Guided Setup simplifies onboarding Nexus Repository Manager repositories to enable users to get started with Firewall in a few easy steps. The automated process guides first-time users to maximize the supply chain protection offered by Firewall by providing configuration recommendations.

As part of our inclusive language initiatives stemming from our core values of embracing inclusion, we are renaming the feature previously known as Policy Violation Grandfathering to [Legacy Violations](#UUID-3af5a939-4c70-7dcd-5054-12f1afd559fd) . Starting with this release, Sonatype Lifecycle will use the term Legacy Violations for policy violations that can be deferred during onboarding and prioritized to be remediated later.

There is no change in functionality of this existing feature (previously known as Policy Violation Grandfathering.)

Sonatype is actively working to resolve a distribution issue for the [nexus-jenkins-plugin](https://plugins.jenkins.io/nexus-jenkins-plugin/) . This is a temporary distribution issue and could affect automatic upgrades of the plugin. It does not affect the existing installations or functionalities of the plugin.

The latest version of the nexus-jenkins-plugin will be available from .

### IQ Release 166 (August 2023)

Sonatype IQ Server extends the mission to promote open standards for communicating SBOM information, by introducing the capability to compliant with SPDX® 2.3 standards. Users can also upload SPDX SBOMs (in XML or JSON file formats) directly, using the Third-Party Scan REST API for scan and analysis.

### IQ Release 165 (July 2023)

Sonatype has become aware of a critical issue with Nexus Repository versions 3.57.0 and 3.58.0 impacting deployments using and IQ Server (Repository Firewall). The known issue may allow unintentional download of quarantined components.

If you are on OrientDB and using IQ Server (Repository Firewall), upgrade to Sonatype Nexus Repository versions 3.57.1 or 3.58.1 instead.

### IQ Release 164 (June 2023)

### IQ Release 163 (June 2023)

### IQ Release 162 (June 2023)

### IQ Release 161 (May 2023)

### IQ Release 160 (April 2023)

### IQ Release 159 (April 2023)

### IQ Release 158 (March 2023)

Users will now be able to [override policy notifications](#UUID-99d1c2d2-b1e9-0bbb-6ef7-676b194259b1) for inherited policies. Using this option, it is possible to change the pre-configured policy notification settings for the desired DevSecOps pipeline stage. This improvement also offers the flexibility of changing the recipient type and recipient emails, if applicable, from what was set at the parent level.

We have extended the support for SAML users and groups to allow them to be discoverable via searches in the UI. SAML users and groups are now accessible from the UI to set up access control, assign as application contacts , and receive role notifications.

Note that SAML users and their associated groups must log in to this or later releases at least once before they will be discoverable.

This release allows using the SSH protocol for Automatic Source Control Monitoring (SCM) configuration when cloning a repository. The repository clone URL is now successfully derived and displayed on the SCM UI. This is currently supported for the cloud version of SCMs only.

We have updated our backend to accommodate the increased length of Atlassian API tokens. This will resolve the error related to passwords exceeding 255 characters when setting up Jira configurations.

The IQ Command Line Interface (CLI) scan continues graceful execution with warnings, instead of exceptions, on encountering empty NuGet manifests.

This release handles the null pointer exception that was thrown when attempting to load unknown components that are quarantined.

This release fixes issues with default branch monitoring that affected release 156. Default branch monitoring is now fully functional.

### IQ Release 157 (March 2023)

This release did not meet the critical product acceptance criteria and will not be made available.

### IQ Release 156 (February 2023)

### IQ Release 155 (February 2023)

This release fixes issues in the previous release 154.

Users facing issues with release 154 installations, should upgrade to this version immediately. For users planning an upgrade, we recommend upgrading to release 155 and skipping release 154.

This Release Includes All Features, Improvements, and Notable Bug Fixes of Release 154.

### IQ Release 154 (February 2023)

Starting with this release, users can configure . Currently offered on AWS and on-premises, the HA installations will enable recovery from failures or disruptions with near-zero downtime.

Users can Sorting results in Repository Results Viewow run a multi-column sort in the Repository Results View to retrieve the most relevant repository details.

The SBOM generated from CycloneDX REST API will now include vendor and software name; Sonatype and Sonatype IQ Server version. This additional information will improve the quality of SBOMs generated using this REST API.

We have improved persisting and resetting filter values to match the navigation steps to and from the RepImproved Persistence for Filtersorts view page.

We have added malicious component protection for Java (Maven) All Next-Gen Firewall users might experience blocking of the latest version of Maven artifacts. Blocking of these components will continue until Next-Gen Firewall determines they are safe for your development pipelines.

### IQ Release 153 (January 2023)

### IQ Release 152 (January 2023)

## 2022 Release Notes

**Note:** Sonatype encourages using the most current IQ Server release and not trailing behind for more than six months.

### IQ Release 151 (December 2022)

This release offers improvements to the existing data architecture for IQ Server and HDS. The changes in data organization will prevent database locking issues due to concurrent transactions on shared resources.

This release resolves the internal server error that occurred when using long report template names (>250 chars.) for attribution reports while using the GET method for .

This release handles the null pointer exception that was thrown when attempting to generate an SBOM from an evaluation report that did not show any components.

### IQ Release 150 (November 2022)

Use Experimental Data Insights to view open-source governance behavior for your organization. Click on Data Insights in the left navigation bar, to get started. Analyses from Data Insights uncover open-source component usage patterns across your organization.

Data Insights currently offers:

- Migration Scorecard is a visual representation of component upgrade decisions made by your Java development teams.
- Stack Divergence is an industry-wide comparative analysis of the popularity of components in your technology stack.
- Nudges and Anomalies are key indicators of your platform usage. These indicators reveal patterns and trends used in the remediation processes across your organization.

Scanning local images does not require providing environmental variables. To scan remote images, the user will now have to provide only these variables:

Sonatype IQ Server can now successfully scan files containing the special Unicode character, BYTE ORDER MARK.

This release covers minor UI fixes like typos and the usage of tooltips to display long component names that appeared truncated otherwise.

To maintain and improve stability and security, we continually scan all Sonatype products and applications internally for vulnerabilities. For a strong and most current security posture, components used by our development teams are continually scanned and compared with our proprietary advanced vulnerability detection systems. This section contains information on component upgrades made to mitigate or remediate risks due to our internal policy violations as below:

**CVE-2022-41946 Public on November 23, 2022, Medium risk, Severity 6.3**

Resolution: Upgraded to non-vulnerable component version org.postgresql:postgresql 42.5.1

**SONATYPE-2022-4344, Sonatype Discovered November 22, 2022, Medium risk, Severity 4.7**

Resolution: Upgraded to a non-vulnerable version of the component autolinker :3.16.1 and introduced validations in the code base to verify the trusted source of inputs to the component.

### IQ Release 149 (November 2022)

A modification in release 142 for manifest scans, ignored pom.xml located inside a META-INF directory. In most cases (specifically for uber/shaded archives), pom.xml does not represent the manifest file for the target application to be scanned. This release offers a configurable option to enable [scanning of pom.xml](#UUID-a96629ce-9c35-49b4-7bba-84219d869be4) files, for scan targets that could contain manifest files, in rare situations.

The Advanced Legal Pack (ALP) uses complex automated processes to generate attribution reports. Retrieving data for multiple applications containing hundreds of components can cause high query times. We have optimized our queries and API calls resulting in improved query statistics for attribution reports.

With this release we continue our improvements to the performance of underlying queries for the Dashboard page, to offer a fast and comprehensive risk profile of your applications.

Selecting x days for the Expiration Date filter on the Lifecycle Waivers Dashboard, showed expired waivers, in addition to the waivers meeting the filter criteria i.e. expiring in x days. This release includes a fix for the expiration date filter to show waivers for x days only.

For IQ Server release 132 and higher, idle timeouts affected only native implementation, while users were still able to navigate the UI. With this fix, IQ Server will now force the user to log out after 30 minutes of inactivity.

A tooltip to display the email address of users (from LDAP) on the New Role page under Add a Role, had stopped appearing in IQ Server release 143 and later. This has now been fixed.

To maintain and improve stability and security, we continually scan all Sonatype products and applications internally for vulnerabilities. For a strong and most current security posture, components used by our development teams are continually scanned and compared with our proprietary advanced vulnerability detection systems. This section contains information on component upgrades made to mitigate or remediate risks due to our internal policy violations as below:

**CVE-2022-1415 drools: Public on October 27, 2022, Medium risk, Severity 6.8**

Resolution: Updated drools to 7.73.0.Final

### IQ Release 148 (October 2022)

This release fixes major bugs in the previous release 147.

Users facing issues with release 147 installations, should upgrade to this version immediately. For users planning an upgrade, we recommend upgrading to release 148 and skipping release 147.

Bugs fixed in this release include:

This release includes memory usage optimization to improve the performance of the Lifecycle Dashboard and its related export feature.

### IQ Release 147 (October 2022)

Release 147 contains issues. Upgrading to this version is not recommended. Upgrade to a later release.

This release offers an addition to the Lifecycle Dashboard, the Waivers View. Policy waivers will now be readily available for review on the dashboard. Users can access waivers specific to their needs by creating customized filters for the dashboard. The drill-down capability on each waiver in this list offers a more granular view of the waiver. The Export Waivers Data button generates a .csv file populated with all the waiver data that is retrieved based on the dashboard filter settings.

The Policy Waiver REST API can now retrieve details on a single waiver by passing the policyWaiverID in the GET method.

This release fixes an issue with SAML authentication, that prevented IQ Server from correctly identifying group names containing commas.

We have refactored CycloneDX REST API to include the dependency graph in SBOM, per CycloneDX specification. This is supported for CycloneDX versions 1.2 and higher.

### IQ Release 146 (October 2022)

This release offers minor bug fixes and general UI improvements.

Some of these include:

Experimental feature flags deprecated in config.yml: experimentalFeatures setting in config.yml is no longer referenced. For older versions of IQ server, this configuration setting will have to be deleted from config.yml.

We strongly recommend using Configuration REST API to update the configuration settings for IQ Server 142 and above, instead of config.yml.

### IQ Release 145 (October 2022)

Attribution reports from the Advanced Legal Pack (ALP) provide comprehensive access to more than 90% of OSS obligations. We have streamlined our data retrieval processes to generate these complex and data-intensive reports, faster. This will reduce the possibility of session time-outs that could occur while generating attribution reports for multiple and large applications.

Releases 142 and above fix a bug where a manifest scan processed pom.xml files inside a META-INF directory. Files in this directory, in most cases (specifically for uber/shaded archives), do not represent the manifest file for the target application to be scanned. All pom.xml files inside a META-INF directory from Release 142 and above are now ignored during a manifest scan.

### IQ Release 144 (September 2022)

The Vulnerability Details page contains a section that lists all affected version ranges of the implicated component. This will help users recognize different versions of an implicated component, which could also have security vulnerabilities.

To evaluate a new application that has not been onboarded to IQ Server, using the Sonatype Platform Plugin for Jenkins, users can now provide an additional parameter organization-id for a specific organization. IQ Server will create this application under the specified organization (Org) instead of the parent organization that is set up during the configuration of Automatic Application Creation.

As a result of our code optimization efforts, this release offers significantly faster policy evaluations. We have eliminated performance bottlenecks that occurred in scenarios with hundreds of concurrent users and complex policy evaluations.

### IQ Release 143 (September 2022)

Users can look up vulnerability details by entering any known vulnerability ID from the vulnerability lookup page or Vulnerability Details REST API. The vulnerability ID could be a Sonatype ID (assigned by Sonatype researchers) or just the CVE ID (may also have a Sonatype ID, if discovered first by Sonatype researchers.)

To help users avoid choosing different versions of an implicated component, which could also have security vulnerabilities, we now report all affected version ranges of the implicated component. The affected version range can be retrieved using the Vulnerability Details REST API by passing the component identifier as a query parameter.

Users can now create security policies to evaluate components against the reported CWE IDs. Selecting Security Vulnerability CWE from the dropdown in the conditions section of the policy page now allows defining policy constraint conditions based on the CWE ID.

The upgraded Advanced Legal Pack now provides copyrights, notices, and license text data for the Composer ecosystem.

We have enhanced the response for CycloneDX REST API to include vulnerability details for components in the generated SBOM. This will help get a better understanding of the level of security risk associated with the components and implement remediation.

We have enhanced the Jenkins, Azure DevOps, Bamboo, and Maven plugins to show the total number of evaluated components in the policy evaluation summary. This addition makes eventual misconfigurations easier to spot.

Support for evaluating Java 18 applications and components (first introduced in release 136) has been improved.

To evaluate a new application that has not been onboarded to IQ Server, using Sonatype CLI, users can now provide an additional parameter organization-id for a specific organization. IQ Server will create this application under the specified organization (Org) instead of the parent organization that is set up during the configuration of Automatic Application Creation.

Evaluate a binary action in Lifecycle UI has been modified to Evaluate a file. Using this menu option, users can now also perform manifest scans to analyze source control repositories or software bill of materials (SBOMs) earlier in the development lifecycle, before the applications are built.

Users can apply policy waivers to specific repositories using the new owner types repository and repository_container in the POST request of Policy Waiver REST API.

This release fixes the reported issue (in release 142 only) of blank pages appearing in the web browser, instead of application scan reports. A new scan of the application is recommended for generating the scan report, after installing this release.

Users can now configure the session timeout times for IQ Server using the property sessionTimeout through Configuration REST API.

### IQ Release 142 (July 2022)

The frame-ancestors directive for content security policy (CSP) can be configured using Configuration REST API. This will allow users to control the domains that can frame the current resource and prevent clickjacking. Using the property frameAncestorsAllowlist, users can specify a list of allowed domain URLs as JSON.

Additional IQ Server properties are now exposed through Configuration REST API. These can be configured using the same endpoint /api/v2/config and GET, PUT, and DELETE HTTP methods to read, set, and delete the properties respectively. This process can now be used instead of making changes to the config.yml as in older versions.

Properties added in this release:

We have redesigned the component view in Dashboard, for an enhanced UI:

Users can access the Firewall Dashboard for Repositories if they are granted View IQ Elements and Edit IQ Elements permissions.

Permissions at the global level to access the dashboard are no longer required.

This release fixes a bug where a manifest scan processed pom.xml files inside a META-INF directory. Files in this directory, in most cases (specifically for uber/shaded archives), do not represent the manifest file for the target application to be scanned. All pom.xml files inside a META-INF directory are now ignored.

### IQ Release 141 (June 2022)

This release fixes a critical issue related to the Compare button in the Quarantined Component view in Firewall.

### IQ Release 140 (June 2022)

The Export Results button on the Advanced Search page provides the flexibility of exporting the results into a .csv file, in addition to the existing Advanced Search REST API.

The source control configuration that was controlled through config.yml in older versions must now be configured using .

The feature will allow the policy actions for inherited policies to be overridden. This feature will provide more control in managing the policies and is currently available only for policies configured and inherited for Lifecycle.

The <component name> (all versions) option in the components section of the Add, View, and Remove Waiver page allows the creation of a waiver that will be applied to all versions of a component. NOTE: Unknown components will need to be claimed first.

The JSON payload for Policy Waiver REST API now supports matcherStrategy. It will now be possible to specify the range for components i.e., exact component, all versions of the component, or all components at the specified hierarchy to which the waiver will apply.

As part of this release, the Reference Policy Set v7 now includes a release-integrity policy. For Repository Firewall license installations, the release-integrity policy will not be created automatically.

### IQ Release 139 (June 2022)

The JIRA configuration must now be changed using , instead of making changes in config.yml as in older versions.

This feature adds the flexibility of configuring custom expiration dates for policy waivers from the Add Waivers page. This could previously be done only by using the Policy Waivers API.

### IQ Release 138 (May 2022)

The Reverse Proxy Authentication Configuration must now be changed using , instead of making changes in config.yml as in older versions.

The base URL configuration must now be changed using , instead of making changes in config.yml as in older versions.

NOTE: Configuration of the base URL is required, before configuring email/JIRA notifications and SCM integrations, for events like policy violations.

This release fixed a bug where invalid SBOMs could be generated.

Additionally, from this release, if an SBOM is scanned and it is found to be invalid, then it will be rejected.

### IQ Release 137 (May 2022)

To enhance user experience and make the IQ Server report list page easier to navigate and use, we made the following design improvements:

This release fixes a bug that originated in Release 135. Searches for LDAP static group members now work as expected and return appropriate member information for policy email notifications.

To allow further report customization, the Advanced Legal Pack now includes a filter for Sonatype Special Licenses in the attribution report template. Users can now enable this feature to filter out Sonatype Special Licenses (e.g., Generic-Copyleft-Clause, Generic-Liberal-Clause, See-License-Clause, Identity-Clause, etc.) from their attribution reports.

### IQ Release 136 (April 2022)

A policy condition type for component formats was added.

The application and component evaluation have been updated to support Java 18 bytecode.

A view for remediation advice on quarantined components is available in Firewall. By default, the view is accessible anonymously, using the tokenized link. A unique link is generated for every component quarantine encountered and expires after a certain time. The view contains information on component coordinates, policy violations, recommendations, and other versions that can be used instead.

This feature allows any user with access to the tokenized link to view component vulnerability details. If your IQ Server is publicly accessible to users outside your organization, it is strongly recommended you disable anonymous access to this view using the configuration. Consult with your legal and security teams to determine if you should disable this feature for your organization. If you are using the Repository Firewall for the Nexus Repository, this feature requires the Nexus Repository 3.38.1 release.

We made the following improvements to the release workflow for quarantined components:

The Advanced Legal Pack REST API now supports creating an attribution report for multiple applications with a single call. Users of the UI can now use the legal dashboard filters to generate an attribution report for multiple applications.

The Advanced Legal Pack now automates weak copyleft original source code disclosure obligations for all supported ecosystems. This data will automatically be included in any attribution reports that are generated.

The Application REST API has been updated so that when querying the endpoint of the application, an optional query parameter can be added to include the details of applied application categories.

Atlassian Crowd server provides single sign-on and identity management. Configuration of IQ Atlassian Crowd is through the UI or the REST API. Once enabled, you can use your Atlassian Crowd credentials to log in through the UI or make REST calls.

SAML users may now create User Tokens through the UI.

We have upgraded the Advanced Search feature for component-based searches. The interactive interface gives users the option to choose whether they want to view:

### IQ Release 135 (March 2022)

Organizations and Applications under the Orgs and Policies view in IQ now support configuring InnerSource repositories which enables the Version Explorer for InnerSource components in the component details page.

Refer to the [InnerSource Repository Configuration](#UUID-13c852b6-cc84-d066-b833-16f869780155) documentation for more details on configuring InnerSource repository connections.

### IQ Release 134 (March 2022)

The , , and have been extended to support the CycloneDX schema version 1.4 for XML and JSON formats. In addition to that, the View SBOM option has been updated to produce CycloneDX schema version 1.4 XML.

The Advanced Legal Pack now has a Component Dashboard that provides users with an easy means to view, or search, all components scanned by IQ Server.

Users that have the Advanced Legal Pack can now navigate from the legal tab in the Component Details Page to a component's extended legal details via the 'Review Obligations' button. This makes it much easier to conduct a legal review of a component from a policy report.

We've made a number of improvements to the policy-compliant component selection released first in the Nexus Repository 3.35.0 release. The improvements listed require Nexus Repository 3.38.1 and IQ Release 134 as the minimum recommended versions to use this feature.

- Performance improvements
- New components scanned for resolving version ranges to policy-compliant versions but not downloaded will no longer be visible in the Firewall repository results view

A bug was introduced in 133 that prevented users from being able to select a license on the Component Details Page.

Updated the look and feel to be consistent with our design guidelines.

### IQ Release 133 (March 2022)

Composer data has been improved for both Lifecycle and Firewall.

As of this release, dots are no longer omitted from the application names when importing applications into IQ using easy SCM onboarding. Prior to this release, the dots were removed from the resulting application name.

CycloneDX sbom file scans with dependency-graph data now display dependency information for BOM components (Direct and Transitive).

### IQ Release 132 (January 2022)

This Dependency Tree Page shows a tree-like structure of all the dependencies identified in an application analysis report. This feature is only available for NPM and Maven ecosystems and its full documentation can be found at our .

The Component Details Page is updated with a component-specific Dependency Tree in the Overview Tab.

The addition of ‘Created By’ for Waivers will display and store the information of the individual who created the waiver. This information will also be visible when viewing existing waivers.

False positives that could exist on rare occasions in exported Docker image tar scans are fixed.

## 2021 Release Notes

**Note:** Sonatype encourages using the most current IQ Server release and not trailing behind for more than six months.

### IQ Release 131 (December 2021)

An issue with the SCM onboarding feature has been fixed, where the onboarding process could not load all unarchived repositories if there is a large number of archived repositories in a git organization.

Application dependency tree data for Java & NPM components is now available using the

### IQ Release 130 (December 2021)

Nexus IQ Server does not use log4j versions and uses logback instead. It is therefore not at risk from vulnerabilities impacting log4j. However, because of a low/moderate vulnerability existing in logback", we're taking precautionary measures by updating the logback library version used in Nexus IQ products.

Cran and Cargo data have been improved for both Lifecycle and Firewall.

Conda data has been improved for both Lifecycle and Firewall. Adopt the updated command and file for better results, refer to for more information.

The Application now lists the Effective, Declared, and Observed licenses separately in the Licenses table and indicates if an Effective license is Overridden.

### IQ Release 129 (December 2021)

Added some performance improvements affecting component remediation (both UI and API).

Fixed an issue that could cause the legal tab on the component details page to not load for some components.

### IQ Release 128 (November 2021)

This new Component Details Page is a fully redesigned experience within a singularly dedicated page. This new page provides an improved layout, new comparison functionality to better identify ideal component versions, an increased focus on waiver statuses, and dedicated Security and Legal tabs.

Fixed an issue that caused attribution report generation to fail when a report contained an InnerSource or proprietary component.

### IQ Release 127 (November 2021)

Users can now reset an organization or application source control configuration.

The license tab in the Component Information Panel (CIP) now contains a link from that tab to the component's legal obligation details page in the Advanced Legal Pack. This is useful for legal reviewers who are attempting to remediate legal policy violations from a Firewall report, an IDE integration, or a policy evaluation.

The Advanced Legal Pack (ALP) now allows users to customize their attribution reports. Initial options allow users to add custom headers, footers, titles, and various appendixes. The ability to include standard license text as an appendix can reduce report sizes by as much as 80% and the ability to include generic legal text allows users to include legacy third-party notices or legacy attribution reports with the newer ALP attribution reports.

### IQ Release 126 (October 2021)

**Note:** There is an issue with some IDEs not being able to load data from IQ 126. Customers should upgrade to IQ 127 if experiencing this issue.

The was deprecated in favor of the new , which is 100% backward compatible.

SSH is now supported as a transport protocol for Git operations in IQ for SCM.

### IQ Release 125 (October 2021)

**Note:** There is an issue with the 'Orgs and Policies' view in IQ 125 which can cause errors to appear in the web UI when viewing organizations. Customers should upgrade to IQ 126 if experiencing this issue.

A potential regression in policy evaluation performance introduced in Release 104 has been mitigated. This reduces the chance of lock timeout exceptions especially when using the default embedded H2 database.

Two new options were added to the Source Control Configuration to allow users to enable or disable pull request commenting and IQ-initiated source control evaluations.

The policy evaluation selection for Pull Request Commenting has been optimized.

Conan data and matching have been improved for both Lifecycle and Firewall.

NPM Dependency Information detection has been improved to display more accurate results.

The repository configured under source control has been made more visible in the Organizations and Applications view.

The Easy SCM Onboardingfor Bitbucket Server has received some performance improvements.

The policy result for a scan is now available in the Azure DevOps pull request screen. This enables target branch protection for Azure DevOps.

The application and component evaluation have been updated to support Java 17 bytecode.

### IQ Release 124 (September 2021)

Fixed an issue with the Source Control REST API whereby some fields in the response JSON had been renamed. The previous names have been restored.

### IQ Release 123 (September 2021)

Fixed an issue with some NPM scans that were causing IQ Server 122 evaluations to fail when reading dependency information.

**Note:** There is an issue with the Source Control REST API in IQ 123, customers should upgrade to IQ 124 if using this API.

### IQ Release 122 (September 2021)

NPM project scans with manifests allow the displaying of dependency information for NPM components (Direct and Transitive).

Refer to and for more information.

InnerSource dependency analysis allows a user to visualize NPM InnerSource components and their transitive dependencies in a report with links to any associated applications.

Refer to for more information.

Reports containing InnerSource Insight components will have more and better information about their transitive dependencies and relationships.

Refer to and the for more information.

IQ Server now has the ability to group waive InnerSource transitive policy violations.

IQ report filters now allow filtering by a component's InnerSource status.

Support for Azure DevOps in Automated Pull Requests, Pull Request Commenting, and Automated Commit Feedback.

**Note:** Some NPM scans might fail due to an issue discovered in IQ 122, customers should upgrade to IQ 124 if NPM scans are being used. There is an issue with the Source Control REST API in IQ 122, customers should upgrade to IQ 124 if using this API.

### IQ Release 121 (July 2021)

In this version, we have addressed a few bugs in IQ and made some performance improvements.

### IQ Release 120 (July 2021)

Continuous Risk Profile keeps default branch policy evaluations up to date with fresh source control policy evaluations regularly (configurable). In addition, IQ server will keep feature branch policy evaluations updated with new source control policy evaluations as new commits are made to those feature branches (assuming a pull request exists for that feature branch).

IQ for SCM makes use of 'gradle.properties' files in providing SCM feedback.

### IQ Release 119 (June 2021)

CycloneDX SBOM scans using the and CLI have been improved to display better results in the report and some bugs have been fixed as well.

### IQ Release 118 (June 2021)

IQ Server (through CLI) can now be used to evaluate policies against components from the dependency file of a .

Starting June 30, Nexus Lifecycle and Nexus Firewall users may experience a change in CocoaPods results due to some major improvements to our identity and security data services.

### IQ Release 117 (June 2021)

Fixed an issue where using the could render application reports inaccessible without setting the experimental feature flag componentSearchApiWithInnerSource to false. It is now safe to remove this flag or to set it to true.

The , , and [View SBOM](#UUID-cdab48b3-4098-bf5e-687a-cfe743c4d40e) option have been extended to support the schema version CycloneDX 1.3 for XML format.

### IQ Release 116 (June 2021)

⚠️ **Warning:** Customers should avoid using the without the following setting in their IQ Server configuration file as otherwise it can render application reports inaccessible. experimentalFeatures: componentSearchApiWithInnerSource: false

Fixes a regression for automatic pull requests when using Linux or Mac and the native git support.

Dependency data for Java components is now available using the and .

### IQ Release 115 (May 2021)

in the evaluation report allows you to view the component bill of materials of the report in .

IQ Server (through CLI) now supports evaluating policies against Python components defined in poetry.lock files.

IQ Server now allows the configuration of multiple source code management systems.

### IQ Release 114 (May 2021)

The Third-Party Scan REST API and CycloneDX Application Analysis have been extended to support the schema version CycloneDX 1.2 for XML format.

This add-on to Nexus Lifecycle will help you automatically comply with the components’ terms of use.

This new product from Sonatype helps you stop known risks, novel malware, and 0-day attacks from being downloaded into your repositories.

### IQ Release 113 (April 2021)

Fixed a critical error that prevented attribution report generation for applications that contained an InnerSource component.

The Nexus IQ CLI binaries are now available to be installed as a deb package on Debian/Ubuntu-based Linux systems and as a Homebrew package on Mac OSX.

### IQ Release 112 (April 2021)

As of this release, the navigation has been moved to the left side of the screen and the Dashboard Filter is now accessible via the "Filter" button on the upper right side of the pages.

The application and component evaluation have been updated to support Java 16 bytecode.

### IQ Release 111 (April 2021)

Fixed an error where evaluating a large file could cause an exception if IQ Server is configured to use HTTPS/SSL.

Advanced Remediation Strategies are available in automated pull requests and pull request comments as part of the Advanced Development Pack add-on product license.

### IQ Release 110 (April 2021)

Fixed an error occurring when evaluating a binary file from UI compiled with Java 14 or higher.

### IQ Release 109 (April 2021)

Allows users to quickly create IQ applications for the repositories IQ Server detects in their configured source control management (SCM) system.

Performs an initial IQ Server scan of the contents of source control repositories for new IQ applications created by SCM Easy Onboarding.

As new pull requests are detected for IQ applications IQ Server may perform a one-time source control scan of the feature branch associated with the pull request and comment on the pull request if new vulnerabilities are discovered or if existing ones have been remediated. This source control scan will only be performed if the customer's CI system is not otherwise initiating scans and policy evaluations for the given application.

### IQ Release 108 (March 2021)

Breaking changes information is available in automated pull requests and pull request comments as part of the Advanced Development Pack add-on product license.

Added "Triggered by" information to application reports.

Building on the robust features available in Nexus Lifecycle, the Advanced Legal Pack adds the following capabilities:

- Automation of attribution reports that comply with 90+% of OSS obligations.
- Enhanced legal data pertinent to obligations (e.g. all copyright statements, all notice statements, and all license texts found in a component).
- Legal workflow to resolve license obligations (per component, per license).
- Ability to save attribution and obligation resolutions on a per component, per license basis at the organization or application level.
- Ability to customize and edit attribution reporting as needed.

### IQ Release 107 (March 2021)

IQ Server (through CLI) now supports evaluating policies against Java components in pom.xml and build.gradle files

- Various bug fixes and performance enhancements.

### IQ Release 106 (February 2021)

Nexus users can now automate protection against dependency/namespace conflict at scale by connecting Nexus IQ Server's policy management and component intelligence data with proxy repositories in Nexus Repository Manager.

For more details, check out our [demo video](https://blog.sonatype.com/sonatype-releases-new-nexus-firewall-policy-to-secure-software-supply-chains-from-dependency-confusion-attacks) to see how Nexus users can start protecting against dependency/namespace confusion attacks at scale.

- Updated CLI scanner to exclude development dependencies when scanning package-lock.json files.
- Updated CLI scanner to parse package-lock.json files stored inside an archive.
- Fixed parsing errors when scanning yarn.lock and csproj files.

### IQ Release 105 (February 2021)

- Various bug fixes and performance enhancements.
- Fixed an edge case while using the external database where the application would run into a deadlock and cause the database pool to be exhausted.

Fixed Initialization error in NuGet manifest scanning with CLI.

### IQ Release 104 (January 2021)

Release 86 to 103 (inclusive) of IQ Server suffer from CVE-2020-27218 a security vulnerability that allows an attacker to inject data into the body of the request. We advise you to update your IQ Server to this new release which contains the required fix.

responses now contain additional report URLs to aid navigation.

Automated pull request feedback is now available for Go projects in all supported Source Control Management platforms.

InnerSource Insight was improved and now supports:

- Policy Condition Dependency Type now has the ability to tune policy using the InnerSource dependency type.
- Improved detection of proprietary modules that are not demarcated as InnerSource (instead of marking them as “unknown”).
- Better detection of Direct Dependencies when they are associated with both an InnerSource component and the parent application.

IQ Server (through CLI) now supports evaluating policies against:

- NPM Components are defined in yarn.lock, pnpm-lock.yaml, package-lock.json, and npm-shrinkwrap.json files.
- NuGet Components defined in * .csproj and packages.config files.

## 2020 Release Notes

To ensure accuracy, the API fails if there are any repository evaluations older than release 76, as new waiver information was added as part of that release. Please re-evaluate all repositories to get a successful response.

**Note:** Sonatype encourages using the most current IQ Server release and not trailing behind for more than six months.

### IQ Release 103 (December 2020)

InnerSource dependency analysis allows a user to visualize InnerSource components and their transitive dependencies in a report with links to any associated applications.

The application and component evaluation have been updated to support Java 14 and 15 bytecode.

Automated pull request feedback is now available for Gradle projects in all supported Source Control Management platforms.

Read the SCM documentation to learn more about configuring automated PRs, PR reviews, and code line comments to work with Gradle.

Two additional columns have been added to the exported file from the dashboard's violation tab:

- Reference: contains the CVE or Sonatype code assigned to the vulnerability that caused the policy violation
- Policy Violation ID: contains the policy violation ID that triggered the violation

### IQ Release 102 (November 2020)

The User Token UI allows each user to manage their User Token directly from the IQ Server.

The User Token API has a new endpoint that allows checking if a User Token exists for the current user.

Fixed an XML External Entity (XXE) vulnerability affecting IQ Server parsing of admin-submitted SAML metadata.

See the [CVE-2020-29436](https://support.sonatype.com/hc/en-us/articles/1500000415082-CVE-2020-29436-Nexus-Repository-Manager-3-XML-External-Entities-injection-2020-12-15) advisory for details.

### IQ Release 101 (November 2020)

Nexus IQ CLI no longer supports Lifecycle XC. IQ Server now has native support for all languages that were supported in Lifecycle XC.

PackageUrl for pecoff has a new structure. The namespace is part of the qualifiers with the key "nexusnamespace", older versions will not change. More information can be found in our supported formats.

The Manifest Evaluation REST API provides a way to perform an application policy evaluation on supported manifest files discovered in a source control branch.

The Waivers for Violation page allows viewing, adding, and deleting waivers for a violation.

Now Add Waiver page allows setting an expiration timeframe for the waiver.

**Note:** The nexus-iq-server docker image for IQ version 101 changed the base image from Red Hat UBI (Universal Base Image) to a different Red Hat UBI that includes OpenJDK 1.8. As a result, the UID of the nexus user has changed from uid=998 to uid=997, which will impact access to persistent data. See our [upgrade instructions](#UUID-a6ff9f64-f66d-c9bf-5988-76d176f4cdf9) if you are upgrading to version 101 or later in a docker image.

### IQ Release 100 (October 2020)

Advanced Remediation Strategies, Hygiene Ratings, Breaking Changes, and Release Integrity capabilities are made Generally Available as part of the Advanced Development Pack add-on product license.

Add Waiver API now has the option to apply an expiry time to waivers as a means to better manage and remove waivers. When the timeframe for the expiry time has been met, the waiver will automatically expire.

### IQ Release 99 (September 2020)

GitLab MR reviews now provide MR line comments, noting the exact line of code that caused a policy violation. Supplemented with the summary of policy violations for a specific MR, developers have all the information at their fingertips to innovate with peace of mind.

### IQ Release 98 (September 2020)

IQ Server (through CLI) now supports evaluating policies against Go components defined in a Gopkg.lock file.

Installations that have not yet been created and configured in the Root Organization will automatically be migrated to a Root Organization with no policies defined.

**Note:** If you have not yet migrated and wish to use policies from an existing organization at the Root Organization level, it is recommended to do this before upgrading.

Previously, the search index had to be rebuilt manually to ensure search results reflected the latest policy configuration and application data. This release starts adding an incremental update of the search index that runs automatically when the application data is changed. Automatic indexing currently covers organizations, applications, application categories, component labels, policies, and security vulnerabilities found during policy evaluations.

IQ Server now drops inbound requests containing in-the-path characters known to be used for unsafe purposes (semicolons, backslash, and unescaped non-ASCII characters).

GitLab MR reviews provide an MR comment with a summary of violations, affected components, and a description of violations introduced in that specific MR to help developers resolve policy violations effectively and efficiently.

IQ Server user sessions are now kept when the server is stopped such that they can continue to be used when the server is restarted as long as they have not timed out.

The Applicable Waivers REST API enables retrieval of all the waivers applicable to a given policy violation.

The Add Waiver page provides the ability to apply a waiver against a policy violation from two different workflows. You can access the Add Waiver page either directly from the Application Report or from the Violation Details page.

The SAML implementation in IQ Server has been updated and now requires the "Destination" field to be set if the SAML messages (request/response) are signed. This is in accordance with the SAML specification and if not done you may encounter an authentication error.

### IQ Release 97 (August 2020)

Email notifications for repository policy violations are sent now when the policy violation is detected instead of periodically.

Security Vulnerability Category is now available as a policy condition. See Understanding the Parts of a Policy for details and Policy Management.

The addition of the Security Vulnerability Override API now allows security vulnerability status overrides to be retrieved alongside information about the components where they are currently taking effect.

Policy Waiver REST API allows adding waivers with Application, Organization, or Root Organization scope. The API has the option to apply a waiver to all components with matching policy violations.

Support Automated Pull Requests for GitLab where pull requests are automatically created for policy violations with suggested remediation.

Check the configuration of your source control setup for appropriate permissions for pull requests.

Show recent automated pull request activity in the source control configuration screen.

### IQ Release 96 (July 2020)

Dependency Type is now available as a policy condition. See Understanding the Parts of a Policy for details and Policy Management.

IQ Server (through CLI) now supports evaluating policies against

- C/C++ components are defined in a conaninfo.txt file.
- Go components are defined in a go.list file.

Various performance improvements for accessing LDAP servers

Some PE/COFF component report data (raw/PDF-printed) and Component Information Panel (CIP) data may cause errors in rendering. The application log file would have contained messages such as MalformedPackageURLException: Segments in the namespace and the subpath may not be empty. This rendering problem is now resolved.

### IQ Release 95 (July 2020)

Components found in a manifest that were previously unknown by Sonatype will be shown in the CIP as identified by "Package Manifest" displaying the given coordinates in the scanned file.

Nuget data matching has been enhanced with PE (Portable Executable)/COFF (Common Objective File Format) data:

- The best-fit matching is replaced with DLL pecoff matching.
- Exact matching to the .nupkg archive and for each .dll pecoff signature.

With the enhanced data, the identification of the following extensions is now supported: .acm, .ax, .cpl, .dll, .drv, .efi, .exe, .mui, .ocx, .scr, .sys, .tsp

The Reporting Area in IQ Server's UI is now paged, increasing performance by decreasing load time.

Improved the performance in various areas (UI, REST APIs, etc).

The configuration for LDAP connections now features an additional option to control how LDAP referrals are handled.

PR reviews available in GitHub and BitBucket now provide PR line comments, noting the exact line that introduced a policy violation. Supplemented with the summary of policy violations for a specific PR, developers have all the information at their fingertips to innovate with peace of mind.

The UI for saving, loading, and deleting Dashboard filters is simplified. Now the Save button is accessible directly in the sidebar footer. Saved filters can be loaded and deleted from the single dropdown menu.

### IQ Release 94 (June 2020)

IQ Server (through CLI) can now be used to evaluate policies against components defined in a conanfile.py file.

Policy violations can now be retrieved using the Cross-stage violation API to get information on a particular policy violation across the different stages of the lifecycle.

Centralized access point for policy violation information. It can be accessed from the Dashboard to obtain detailed information on a specific policy violation for an application, including report information across different stages of the lifecycle.

The Advanced Search is still an early access feature but one of its caveats has now been resolved: Search results are now filtered to only include those records the user has "View" permission for.

### IQ Release 93 (June 2020)

An additional recommended version is added to Component Info - Next version with no build failure violations.

### IQ Release 92 (May 2020)

Improved the performance when using an external database for policy evaluations, application reports UI, application reports, and other REST APIs.

The static resources like images that are needed to view email notifications are now retrieved via HTTPS instead of HTTP. Please make sure your network allows outbound connections as detailed in Configuring Outbound Traffic.

Policy Waivers can now be retrieved using the updated Policy Waivers REST API.

### IQ Release 91 (May 2020)

Application Categories can now be managed using the REST API.

Improved the performance of policy evaluations when using an external database.

IQ Server (through CLI) can now be used to evaluate policies against components from dependency files of Yum

Data Source is now available as a policy condition.

Firewall is extended to support packages of the following languages/ecosystems:

- PHP (Composer)
- Swift/Objective-C (Cocoapods)
- Conda
- Alpine (APK)
- Bower
- CRAN (R)
- Debian (APT)
- C/C++ (Conan)

It is recommended to upgrade to the latest Reference Policy Set (reference-policies-v4) with the Component-Unknown policy changes.

### IQ Release 90 (April 2020)

Policy Waivers can now be deleted using the updated Policy Waivers REST API.

Component Labels can now be managed using the updated Component Labels REST API.

IQ Server (through CLI) can now be used to evaluate policies against components from dependency files of:

- Alpine
- Debian
- Drupal

Support for both Bitbucket Server and Bitbucket Cloud has been added to Automated Pull Requests and Build Status.

The storage for Firewall data has been refactored to be faster and to require less disk space. A small performance impact may be noticed after the upgrade (for a few hours) until the existing data is migrated.

### IQ Release 89 (April 2020)

The Component Evaluation REST API now includes data about effective component licenses.

The Report-related REST API now includes data about effective component licenses.

IQ Server (through CLI) can now be used to evaluate policies against components from dependency files of:

- R (CRAN)
- Rust (Cargo)

The look and feel of the PDF Report for the Application Composition Report has been updated and streamlined to align more with the IQ Server's UI. This increases its focus on essential information in addition to improving PDF generation performance.

### IQ Release 88 (March 2020)

Now the Component Info tab in the Component Information Panel adds a Recommended Remediation section for transitive dependencies. It provides links to all direct dependencies that are brought in the selected component. Available for maven components only.

This release includes an Early Access version of Advanced Search. This new search feature provides a flexible way to locate items among your applications. For instance, Advanced Search can help find all applications that are affected by a given security vulnerability.

The Component Details REST API now includes data about effective component licenses.

IQ Server (through CLI) can now be used to evaluate policies against components from dependency files of:

- Swift/Objective-C CocoaPods
- Conda

GitHub PR reviews provide a PR comment to provide a summary of violations, affected components, and a description of violations introduced in a specific PR to help developers resolve policy violations effectively and efficiently.

### IQ Release 87 (March 2020)

User Tokens REST API exposes endpoints to System Administrators for querying tokens by creation date and supports deletion.

This release fixes a regression that prevented IQ Server 86 from loading some reports.

### IQ Release 86 (March 2020)

⚠️ **Warning:** There is an issue with IQ Server 86 failing to load some reports. Customers should avoid upgrading to release 86 and instead upgrade to release 87 or newer.

An application can now be moved from one organization to another using the REST API.

IQ Server (through CLI, Jenkins, and Bamboo plugins) can now be used to evaluate policies against components from dependencies files for:

- C/C++ Conan
- PHP Composer
- RubyGems

### IQ Release 85 (February 2020)

Component Category is now available as a policy condition.

The Component Claim REST API allows you to view, add, update, and delete component claims.

Stale Waivers REST API now returns stale evaluations along with the stale waivers.

### IQ Release 84 (February 2020)

**Note:** Release 83 and Release 84 introduced migration steps in server startup where proxy server and mail server configurations are read from the existing config.yml file and transferred to the database. An issue was discovered that stops IQ Server from successfully starting when the password field for either of these configurations is an empty string. If that is the case for either of your configurations please comment out the password fields entirely instead of having an empty string. Using the proxy server configuration as an example, instead of having a configuration as below: proxy: hostname: "proxy.server" port: 8081 username: "proxy-user" password: "" please configure your configuration as follows where the password is commented out: proxy: hostname: "proxy.server" port: 8081 username: "proxy-user" # password: "" No special action is needed if a non-empty password exists. It will be stored in the database encrypted.

Stale Waivers REST API allows you to retrieve stale application and repository waivers.

**Note:** To ensure accuracy, the API fails if there are any repository evaluations older than release 76, as new waiver information was added as part of that release. Please re-evaluate all repositories to get a successful response.

A sample email can be sent in the Email configuration UI to verify the email server being configured by entering the desired recipient and using the `Send Test Email` button.

The proxy server configuration is now configurable via the HTTP Proxy Server Configuration REST API or via the Proxy Server Configuration View found in System Preferences. Any existing proxy server configuration in config.yml will be migrated and become obsolete.

Nexus IQ for SCM now supports the NPM ecosystem.

### IQ Release 83 (January 2020)

The email server configuration for email notifications is now configurable via the new Mail REST API or via IQ Server's UI. Any existing email server configuration in config.yml will be migrated and become obsolete.

Three new permissions Waive Policy Violations, Change Licenses, and Change Security Vulnerabilities are now available for (un)waiving policy violations, changing component licenses, and changing component security vulnerabilities. Previously, the Edit IQ Elements permission was required for these operations. All roles that have the Edit IQ Elements permission are automatically updated to have these new permissions.

This release includes improvements to our proprietary advanced binary fingerprinting and will increase scan file sizes up to four times.

The Third-Party Scan REST API and CLI have been extended to support identifying components based on SHA-1 value (content hash).

The Policy-centric Application Composition Report no longer contains a banner with a link to the legacy version of the Application Composition Report. Instead, the legacy version may now be accessed via the Policy-centric report's Options menu.

### IQ Release 82 (January 2020)

Application Composition Report now displays Dependency Type Indicators for maven components. Components can be filtered by dependency type using the new Dependency Type filter.

Note: Dependency Type is only supported for maven components. Reports created prior to January 2, 2020, will show all non-maven components as a direct dependency type. Once the application is rescanned, the non-maven components will be shown as unknown dependency types.

A new Edit Access Control permission was added for managing the access control for applications, organizations, and repositories. Previously, the Edit IQ Elements permission was required for access control management. All roles that have the Edit IQ Elements permission are automatically updated to have the new Edit Access Control permission.

## Track Resolved Issues

### Release 193 (July 2025)

### Release 192 (June 2025)

### Release 191 (May 2025)

### Release 190 (April 2025)

### Release 189 (April 2025)

### Release 188 (March 2025)

### Release 187 (February 2025)

### Release 186 (January 2025)

### Release 185 (December 2024)

### Release 184 (November 2024)

### Release 183 (October 2024)

### Release 182 (September 2024)

### Release 181 (August 2024)

### Release 180 (August 2024)

### Release 179 (July 2024)

### Release 178 (June 2024)

### Release 177 (June 2024)

### Release 176 (May 2024)

### Release 175 (April 2024)

### Release 174 (March 2024)

### Release 173 (February 2024)

### Release 171 (January 2024)

### Release 170 (December 2023)

### Release 169 (November 2023)

### Release 168 (October 2023)

### Release 166 (August 2023)

## Release specific upgrade instructions

### Upgrading to release 183 and later release

- For improved stability and performance run the following commands on your PostgreSQL instance.
- Starting release 183 and later, users can download IQ Server installations bundled with JDK. See .

**Note:** Upgrade Impact After upgrading a Lifecycle instance using a PostgreSQL database from IQ 182 or earlier to IQ 183 or later, you may temporarily see an internal error when accessing the violations dashboard and find a NullPointerException (NPE) in the logs. This is due to an internal job running in the background; the dashboard will load as expected after the job completes. We will improve this experience in a future release.

### Upgrading to release 180 and later release

IQ and IQ CLI release 179 were the last to support Java 8 and 11, and are now in [Extended Maintenance](#UUID-a490df78-32b0-60a4-de78-ffa75048d7c1) as defined in our [Sunsetting documentation](#UUID-217b96ec-8a06-93ff-b373-ab40751a5647) . You will need to upgrade to Java 17 before upgrading to release 180+.

Starting Java version 17 the use of SHA-1 based digests and signature algorithms for XML signatures has been forbidden. Users may need to reconfigure the signature algorithm on their identity provider platform.

### Upgrading to release 169 and later release

Release 169 includes several database changes to complete our transition to using the term *Legacy Violations* . Users may experience longer upgrade times (around an hour), regardless of the backend, i.e. H2 or PostgreSQL.

### Upgrading from release 151 and earlier to a later release

This upgrade can initially take much longer to perform. This is due to the schema expansion introduced for enhanced product experience.

### Upgrading from release 118 and earlier to a later release

The IQ Server Docker image for IQ release 119 has fixed the issue with the non-graceful shutdown of the IQ server.

Halting the container before release 119 requires the following command.

```
docker exec -ti $(docker container list -a | grep nexus-iq | head -n 1 | awk '{print$1}') bash -c 'kill -TERM "$(cat /sonatype-work/lock | cut -d"@" -f1)"'
```

Where the portion of the command surrounded by $(docker ...) returns the docker **container_id** of the IQ server. If you have already identified the **container_id** of the running IQ server, you can alternatively run the below command by replacing the **container_id** with the id of the container you have identified:

```
docker exec -ti container_id bash -c 'kill -TERM "$(cat /sonatype-work/lock | cut -d"@" -f1)"'
```

### Upgrading from release 117 and earlier to a later release

The [sonatype/nexus-iq-server docker image](https://hub.docker.com/r/sonatype/nexus-iq-server) for IQ release 118 changed the UID of the nexus user from **997** to 1000, and changed it from a system account to a user account. This is to minimize the chance of a future collision with other UIDs. If you use this image with a persistent data volume you will need to change the owner in order for the new image to start up successfully.

Here is one example of a way to change the peristent storage owner:

```
docker run -it -u=0 -v sonatype-work:/sonatype-work sonatype/nexus-iq-server:1.118.0 chown -R nexus:nexus /sonatype-work
docker run -it -u=0 -v sonatype-logs:/var/log/nexus-iq-server sonatype/nexus-iq-server:1.118.0 chown -R nexus:nexus /var/log/nexus-iq-server
```

This will start up release 118 of an IQ server container with root as the user, allowing it to chown the sonatype-work and other persistent directories and its files to the correct **nexus** user.

### Upgrading from release 100 and earlier to a later release

The [sonatype/nexus-iq-server docker image](https://hub.docker.com/r/sonatype/nexus-iq-server) for IQ release 101 changed the base image from Red Hat UBI (Universal Base Image) to a different Red Hat UBI that includes OpenJDK 1.8. As a result, the UID of the **** user has changed from **uid=998** to **uid=997** . If you use this image with a persistent data volume you will need to change the owner in order for the new image to start up successfully.

Here is one example of a way to change the peristent storage owner:

```
docker run -it -u=0 -v sonatype-work:/sonatype-work sonatype/nexus-iq-server:1.101.0 chown -R nexus:nexus /sonatype-work
```

This will start up release 101 of an IQ server container with root as the user, allowing it to chown the sonatype-work directory and its files to the correct **nexus** user.

### Upgrading from release 97 and earlier to a later release

The SAML implementation in IQ Server was updated in Release 98 and requires the "Destination" field to be set, if the SAML messages (request/response) are signed. This is in accordance with the SAML specification and if not done you may encounter an authentication error. See [Error during SSO login "Authentication failed due to SAML error" after upgrading Nexus Repository 3 or IQ Server](https://support.sonatype.com/hc/en-us/articles/360058028653-Error-during-SSO-login-Authentication-failed-due-to-SAML-error-after-upgrading-Nexus-Repo-3-or-IQ-Server) for more information.

### Upgrading from release 68 and earlier to a later release

The [sonatype/nexus-iq-server docker image](https://hub.docker.com/r/sonatype/nexus-iq-server) for IQ release 69 changed the base image from CentOS to RedHat UBI (Universal Base Image). As a result, the UID of the nexus user has changed from uid=999 to uid=998. If you use this image with a persistent data volume you will need to change the owner in order for the new image to start up successfully.

Here is one example of a way to change the persistent storage owner:

```
docker run -it -u=0 -v sonatype-work:/sonatype-work sonatype/nexus-iq-server:1.69.0 chown -R nexus:nexus /sonatype-work
```

This will start up release 69 of an IQ server container with root as the user, allowing it to chown the sonatype-work directory and its files to the correct nexus user.

### Upgrading from release 64 and earlier to a later release

Release 65 of IQ Server introduces a new policy-centric UI for .

There are some differences that might not be obvious and are worth mentioning:

- The threat level counters in the old Application Composition Report counted the number of violating components, while the similar counters in the new version of the report count violations.
- In Aggregated mode, the "waived" and "grandfathered" indicators in the policy violations table are displayed when all of the violations for the given component are waived or grandfathered. In the Summary mode of the old Application Composition Report, which is analogous to the current Aggregated mode, the "waived" and "grandfathered" indicators never appeared.

### Upgrading from version 1.44 and earlier to a later release

Version 1.45 of IQ Server introduces a more compact format to store the policy violation data of your applications. Upgrading to this version and the new storage format can take notable time. To properly prepare for this upgrade, refer to our detailed instructions on upgrading to version 1.45 below:

### Upgrading from version 1.42 and earlier to a later release

IQ Server version 1.43 uses a more powerful configuration format (config.yml).

To use a configuration file from a prior version, then you must update it.

### Upgrading to version 1.42 or later requires version 1.16 or later

IQ Server version 1.42 or later will no longer perform data migrations for versions before or including 1.16.

This is to streamline future data migrations to improve data storage and its scalability.

### Upgrading from version 1.35 and earlier to a later release

IQ Server version 1.36 replaces the *Security Vulnerability present* policy condition with the *Security Vulnerability Severity greater than or equal to 0* policy condition and removes the *Security Vulnerability absent* policy condition. The upgrade to 1.36 or later will fail if you have any policies relying on the *Security Vulnerability absent* policy condition. Before attempting to upgrade, we highly recommend that you perform a backup. If the upgrade fails, then you can still start the previous version against this backup. In the meantime, you can [contact the support team](https://support.sonatype.com/) or your customer success representative directly for assistance in changing any of your policies that rely on the *Security Vulnerability absent* policy condition.

### Upgrading from version 1.17 and earlier to a later release

IQ Server version 1.18 introduces the Root Organization—a new entity at the top of the system hierarchy that allows you to set policy globally across all organizations and applications. After you update the IQ Server to version 1.18, you should configure and create the Root Organization. It’s a one-time process and occurs when the server is restarted. The process makes a permanent change to the system hierarchy that cannot be undone. It is strongly recommended that you back up the IQ Server and read "Introducing the Root Organization" before proceeding.

In IQ Server version 1.21, the Sonatype CLM for Hudson and Jenkins plugin has been updated and rebranded to Nexus IQ for Hudson/Jenkins 1.x. If you have a prior version of the plugin installed, then you must uninstall the older version before installing the newer rebranded one. For installation instructions, see the Nexus IQ for Hudson/Jenkins 1.x chapter.

IQ Server version 1.26 introduces CSRF protection for all available plugins that use reverse proxy authentication. This new protection is enabled by default. If you want to upgrade to IQ Server version 1.26 and use reverse proxy authentication in your plugins, you should upgrade your plugins to their latest versions first.

**Note:** If you would like to upgrade to IQ Server version 1.26 and use reverse proxy authentication with older plugin versions, you will need to disable CSRF protection for reverse proxy authentication. See the section on Reverse Proxy Authentication for more information.

**Note:** Both Nexus Repository version 2.14.3 and older and Nexus Repository version 3.2.1 and earlier 3.x versions do not support CSRF protection when using reverse proxy authentication. If you want to use reverse proxy authentication with these Nexus Repository versions and IQ Server 1.26 or later, you will need to disable CSRF protection for reverse proxy authentication. See the section on Reverse Proxy Authentication for more information.

### Upgrading from version 1.15 and earlier to a later release

Due to data migrations, you will need to upgrade to version 1.16 first before proceeding to upgrade to version 1.23 or later versions of IQ Server.

### Upgrading from version 1.16 or earlier

In version 1.17 a rebranding of the Sonatype CLM product took place and is now known as Nexus IQ. As part of this rebranding two of the binaries also changed during this release:

Server

- From: sonatype-clm-server
- To: nexus-iq-server

CLI

- From: sonatype-clm-scanner
- To: nexus-iq-cli

If you have any scripts utilizing the previous names, you will want to update these given the change above.

**Note:** In the example above, only the server name is given. The full binary name would look like nexus-iq-server-1.27.0-01.jar

### Upgrading from versions earlier than 1.9.x

While Sonatype only supports the previous two releases, we are happy to help direct any upgrade needs you may have. If you are upgrading from a version before 1.9.x, [contact the support team](https://support.sonatype.com/) .
