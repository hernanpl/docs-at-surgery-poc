---
layout: default
title: "ServiceNow"
parent: Sonatype Integrations
nav_order: 16
---

# Sonatype for ServiceNow

This guide walks through the functionality of the Sonatype for ServiceNow integration, including where the data can be found within ServiceNow’s Application Vulnerability Response. This guide will include detailed instructions for how to install and configure the integration as well as how to begin tailoring the application to the user’s ServiceNow environment.

**Note:** The Sonatype Application Vulnerability Response integration currently only imports violations where the Sonatype policy type is “Security”, since those correspond most closely to the functions of Application VR in ServiceNow.

The purpose of this document is primarily to familiarize the reader with the software and integration itself, not to provide an all-encompassing review of ServiceNow’s Application Vulnerability Response modules and how to use them. The guide does attempt to provide best practice recommendations for utilizing the Sonatype data in concert with Application Vulnerability Response where possible/applicable; however, where decisions must be made and tailored to the customer environment, those decisions will be highlighted.

If you have questions regarding details of the integration not covered in this document, contact Sonatype’s customer support through your normal support channels.

## Prerequisites

- An active license for Sonatype Lifecycle (SaaS, Private Cloud, or Self-Hosted) version 173 or later is required to utilize the integration
- The target ServiceNow environment requires the Application Vulnerability Response (AVR) version 20.0.2 or newer to be installed (now bundled as part of “Vulnerability Response”)

**Note:** The integration is certified and fully compatible with ServiceNow Washington DC and ServiceNow Vancouver, as well as with Application Vulnerability Response (AVR) 20.0.2 and newer. While previous versions of the AVR modules may work, we recommend updating to the latest version for optimal integration.

Users should be familiar with the basic administration and usage of the ServiceNow platform (e.g. Creating report, tailoring list views, etc.)

For help with the ServiceNow platform, consult the [ServiceNow documentation](https://docs.servicenow.com/) or raise a ticket with the ServiceNow support team.

It is recommended to utilize ServiceNow’s NVD integration to populate the CVE and CWE tables. This provides contextual data on any vulnerable items created by the integration.

## Installation and Configuration

**Note:** Obtaining API Access Before configuring the integration we recommend generating an API User Code and Passcode from within the Lifecycle server. Look for the option `Manage User Token` in the user menu in the upper right corner within Lifecycle, and then choose `Generate User Token` on the display popup. See the documentation on for more information.

### Setting the Integration Frequency

All of the components within the Sonatype integration can be scheduled as desired in your environment as well as triggered manually. To review the standard configuration, open the ServiceNow application navigator menu and locate `Sonatype App VR Integration > Admin > Integrations` .

Here you will find five integrations:

By default, the integrations are chained together such that they will automatically run when the previous run completes:

*Sonatype Organizations Integration -> Sonatype Applications Integration -> Sonatype Scan Summary Integration -> Sonatype Application Vulnerable Item Integration -> Sonatype Remediations Integration* .

It is recommended to maintain this sequence as it ensures dependent data from earlier integrations is available for those that follow.

Adjust the timing of the integration by opening the Organizations integration and then setting the `Run` field to the desired frequency. It is recommended to set the frequency of imports according to the frequency of reports in your Sonatype environment. This has been set to `Daily` by default.

### Execute the Integration Manually (optional)

It is also possible to execute an integration manually. Open any given integration and select the “Execute Now” button. A new row will appear in the “Integration Runs” related list on the integration, which will be dynamically updated with the status as the integration runs.

### CI Lookup Rules

Basic Configuration Item (CI) Lookup Rules are provided to match the CMDB based on the name of the application as well as the less likely (but more reliable scenario) where the Application IDs from Sonatype are mapped to CIs and can be used for matching.

These rules can be found under `Security Operations > CMDB > Lookup Rules` .

![image5.png](/assets/images/uuid-65c49a2a-376b-0aa2-6458-ae4a6c92210e.png)

These rules will help to identify the attributes coming from Sonatype and how they can be used in other more complicated rules that may match your organization’s CMDB structure and Discovery tools.

![image6.png](/assets/images/uuid-8442f493-a8bd-de95-925f-bd3460ea3058.png)

### Security Roles

The integration includes two roles to help govern access to the base integration features. Importantly, these roles don’t grant specific privileges within Vulnerability Response, so these roles are only meant to supplement users’ existing App VR roles.

### Reports

Several reports are included to give statistics and trends around the information imported from the Sonatype integration. These reports are also available on a dashboard included in the Sonatype application menu.

## Use Cases

This section outlines the use cases for the Application Vulnerability Response (AVR) ServiceNow Store App. The app integrates Software Composition Analysis (SCA) vulnerability data from Sonatype into ServiceNow, enhancing the capability to manage and mitigate vulnerabilities in software applications.

The AVR app processes SCA vulnerabilities to identify weaknesses in open-source software components used within applications, providing a structured response and remediation framework. The AVR app is designed to streamline the vulnerability management process by providing automated tools and workflows that integrate directly with ServiceNow’s existing infrastructure.

### Key Features

- **CI Lookup Rules** : Automatically search and match application data within the Configuration Management Database (CMDB), linking vulnerabilities to the appropriate application components. [Learn more in the ServiceNow docs](https://docs.servicenow.com/bundle/washingtondc-security-management/page/product/vulnerability-app-vuln-mgmt/concept/avm-ci-lookup-rules.html) .
- **Assignment Rules** : Dynamically assign vulnerabilities to responsible user groups based on predefined criteria, ensuring that the right team addresses each issue. [Learn more in the ServiceNow docs](https://docs.servicenow.com/bundle/washingtondc-security-management/page/product/vulnerability-app-vuln-mgmt/concept/avm-assignment-rules.html) .
- **Risk Calculators** : Evaluate and prioritize vulnerabilities using customizable risk calculators that apply condition filters to assess the impact and urgency of each identified vulnerability. [Learn more in the ServiceNow docs](https://docs.servicenow.com/bundle/washingtondc-security-management/page/product/vulnerability-app-vuln-mgmt/concept/avm-calculators-rules.html) .
- **Severity Mapping** : Translate and normalize severity ratings from Sonatype, utilizing the normalized severity in ServiceNow to maintain consistency across reported vulnerabilities. [Learn more in the ServiceNow docs](https://docs.servicenow.com/bundle/washingtondc-security-management/page/product/vulnerability-app-vuln-mgmt/task/avm-create-severity-map.html) .
- **Reporting** : Generate detailed reports to gain insights into the security posture, track remediation trends, and highlight the most vulnerable applications or business units. [Learn more in the ServiceNow docs](https://docs.servicenow.com/bundle/washingtondc-security-management/page/use/dashboards/application-content-packs/app-vuln-mgmnt-content-pack.html) .

### Scanned Applications

Manage and track application releases, which serve as key reference points for grouping vulnerability assessments within the AVR framework. This component leverages a dedicated child table (`sn_vul_app_scanned_application`) within the CMDB to store relevant data.

### Application Vulnerable Items (AVIs)

Link vulnerabilities to specific applications to create AVIs, which are managed until they are resolved or mitigated. AVIs are maintained based on the most recent scan and updated when vulnerabilities are fixed or no longer detected.

### User Roles and Groups

- **App-Sec Manager** : Manages security processes and oversees vulnerability assessments.
- **Security Champion** : Facilitates communication between development and security teams, ensuring compliance and security best practices.
- **Developer** : Implements solutions and patches to address vulnerabilities.
- **Ethical Hacker** (v15.0 onwards): Conducts penetration testing to proactively identify security weaknesses.

[Learn more about the latest definitions of roles in Application Vulnerability Response in the ServiceNow documentation](https://docs.servicenow.com/bundle/washingtondc-security-management/page/product/vulnerability-app-vuln-mgmt/concept/avm-manage-roles.html) .

### AVI State Transitions

AVRs progress through defined states from detection to resolution, guiding users on when and how to address each item based on its current status. Keep in mind that the remediation/exception process in ServiceNow currently does not sync back to Sonatype. [Learn more in the ServiceNow docs](https://docs.servicenow.com/bundle/washingtondc-security-management/page/product/vulnerability-app-vuln-mgmt/concept/avm-states.html) .

### Integration Components

There are five scheduled integrations that will run as part of the Sonatype for ServiceNow integration. Open *Sonatype App VR Integration -> Admin -> Integrations* to see these components.

![Integrations_-_ServiceNow_-_Components.png](/assets/images/uuid-bfaf53f8-6b75-9a81-636b-55c40c17a389.png)

The following is a brief summary of the data imported by each integration component:

- **Applications Integration** : This integration imports a list of applications that have been scanned by Sonatype into ServiceNow. It serves as the primary data input that matches with the CMDB application information, which includes all applications currently in use that may be susceptible to vulnerabilities. This integration is crucial for maintaining an up-to-date repository of application data, which the AVR system uses to map vulnerabilities to specific Configuration Items (CIs) based on the scans conducted.
- **Organizations Integration** : This integration imports a list of organizations maintained within Sonatype, which can be used to tag each application. This feature allows for better categorization and association of applications within the broader organizational structure, enabling targeted vulnerability management and response strategies based on organizational units, departments, or specific business lines.
- **Scan Summary Integration** : This integration imports summaries of all scans performed by Sonatype, including key statistics about each scan. These summaries provide a snapshot of the scan results, highlighting critical vulnerabilities, the number of components assessed, breakdowns of vulnerabilities by severity within each scan, and the overall security status of the scanned assets. This data is essential for tracking the effectiveness of your security measures over time and identifying trends in vulnerability exposure.
- **Application Vulnerable Item Integration** : This integration imports records that combine specific vulnerabilities with the applications they affect, creating Application Vulnerable Items (AVIs) in ServiceNow. Each AVI undergoes the Application Vulnerable Item lifecycle within ServiceNow, which manages the process from detection to potential remediation of the vulnerability. This integration is the core of the AVR's operational functionality, leveraging data from the previous three integrations to produce the assignable AVI tasks and thus facilitate the management, tracking, and resolution of vulnerabilities.
- **Remediations Integration** : This integration reaches out to the Sonatype platform for additional version details about affected application/package versions, specifically importing the next available version of a package with no associated violations. These recommendations will be pulled to the “Recommendation” field on Application Vulnerable Items when available. This integration will run after the Application Vulnerable Item integration and update new AVITs with the remediation information. If a recommended update version is not available, it is likely that the update has not been released yet or that the security vulnerability still exists in the updated versions.

### Integration Runs

Each of the above integrations can be reviewed to determine when integrations have run, how many items were imported or updated by each run, and also to understand any errors or failures that may have taken place during integration runs. Scroll to the bottom of any integration definition to see a related list titled “Integration Runs”:

![Integrations_-_ServiceNow_-_Evaluation.png](/assets/images/uuid-93f06f7e-1772-611e-9434-d3510f0a38f5.png)

The columns in this list include:

- **Start datetime / End datetime** : The recorded times when the integration started and finished running.
- **New Items / Updated Items** : The number of records (App Vulnerable Items, Scan Summaries, etc.) that were either created or updated when this particular run executed.
- **State / Substate** : The current state of a run (e.g. Running, Completed) as well as whether the run was successful or encountered a failure.
- **Fatal Error Message / Notes** : When there are errors or other debugging produced by a run, that information will be displayed here.

Further information can also be found by opening a run to look at different “Integration Processes” that were generated during the run. This may provide additional context around which process encountered an issue in a failure investigation.

## Integration Architecture

This diagram describes the integration functionality at a high level:

![image7.png](/assets/images/uuid-77a380f4-ff40-176c-3d41-f9cc9c7b4972.png)
