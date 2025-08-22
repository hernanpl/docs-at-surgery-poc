---
layout: default
title: "Sonatype Integrations"
nav_order: 8
has_children: true
---

# Sonatype Integrations

Our supported integrations cover a variety of systems, including CI Pipelines, IDEs, SCMs, ticketing, platforms, and more. For information about supported plugin versions, refer to the [Integrations Status](#UUID-1747cc1a-0843-6568-7246-e3a46d00fe40) page.

Integrations are available for [Lifecycle](#UUID-612d03d6-3a94-6a1e-b77f-efd3b0684637_section-idm234498867203193) and [Nexus Repository](#UUID-612d03d6-3a94-6a1e-b77f-efd3b0684637_section-idm234498871226859) .

## Lifecycle Integrations

Reduce open source risk early in your development process by integrating Lifecycle with the tools you use.

### CI/CD Systems

When integrated with your Continuous Integration (CI) server, Sonatype Lifecycle allows you to run dynamic scans of your software components to perform a complete security and license analysis.

- [Azure DevOps](#UUID-ddc54863-f606-5018-dfef-4207e5213e78)
- [Bamboo Data Center](#UUID-6737c02e-b17a-00be-be43-2506c487b028)
- [Jenkins](#UUID-0d46c567-a411-72f8-7973-d8f4cf7e00b2)
- [GitLab CI](#UUID-719e3e3a-01ab-3db3-d11b-162d0cf24892)
- [GitHub Actions](#UUID-d91db3ae-9768-f40c-44ed-ab361501df26)

### IDEs

Add Sonatype Lifecycle to your Integrated Developer Environment (IDE) as a plugin or extension to get immediate feedback that guides your component selection.

- [IDEA](#UUID-8bf3a9bb-579a-30b7-5287-dfd6addf453a)
- [VS Code](#UUID-2eba9a13-b1aa-2c9e-73fd-5c73d2fa490f)
- [Visual Studio 2022](#UUID-1fc0d7bd-e256-aa57-6c48-8ef4c6af749b)
- [Eclipse](#UUID-3efc78f7-a31b-beca-db13-a04277de2e10)

### SCM Systems

Streamline your development workflow by integrating with Source Control Management (SCM) systems like GitHub, GitLab, and Bitbucket. Track changes, manage code conflicts, and maintain complete version histories for enhanced code management and security.

[Learn more about SCM integrations](#UUID-32a5d718-bd65-9f34-bba7-704ac47a7a54)

- [GitHub](#UUID-2bbac38c-cecf-51c9-4ceb-3f1e54710012)
- [GitLab](#UUID-c30106a6-d054-ccca-2d4b-efe8470494cc)
- [Bitbucket](#UUID-5b33cb44-e739-a894-035a-0ff992b2f5f5)
- [Bitbucket Cloud](#UUID-3c070929-75b1-8810-9a08-c72408fa8960)
- [Azure DevOps](#UUID-d4a24710-1a36-5280-4dfb-9f615405e6b6)

### Issue Management Systems

Boost your project management by integrating with Jira. Streamline issue tracking and enhance collaboration by connecting your development workflows with real-time ticket updates.

- [Jira Data Center](#UUID-645a3540-3e61-9209-b277-5013ccc1ceb1)
- [Jira Cloud](#UUID-0ac4a6c7-57f1-6bd8-f612-042f3e1cac5a)

### Platforms

Optimize your development processes by integrating with leading platforms. Gain direct insights directly into ServiceNow and Fortify SSC to meet your organization's policies across your projects.

- [ServiceNow](#UUID-0b542de4-365d-b0c4-88c6-874c56411965)
- [Fortify SSC](#UUID-66304bb2-b811-50c1-903d-b2ea35ceaec0)

### Supplemental tools

Expand the Sonatype platform with tools that deliver advanced vulnerability detection, automated policy enforcement for container applications, Lifecycle evaluations via CLI, and specialized templates and Docker images for major cloud platforms.

- [CLI](#UUID-6b69b7b1-858f-e58a-e010-beb4fdff9cdf)
- [Maven](#UUID-433e090b-af9e-c63f-5963-c61a3a5f9729)
- [Container Security](#UUID-256fe272-31f8-babd-fac3-f39c0503cfae)
- [Container Deployment](#UUID-cf3c78f2-6638-5344-09ee-07bc2b645adc)

## Nexus Repository Integrations

Manage your software components by integrating Nexus Repository with your CI/CD tools and other systems.

### CI/CD Systems

Orchestrate your software build and release pipelines with the Sonatype Platform Plugin for Jenkins.

- [Jenkins](#UUID-62502c87-fb04-567c-ba71-0e6a68a66138)

### Supplemental tools

Expand the Sonatype platform with specialized templates and Docker images for major cloud platforms and seamlessly manage your software packages.

- [Maven](#UUID-d6d1134e-fb87-d8ed-31cf-25b62e642d54)
- [Container Deployment](#UUID-9c9ee598-7df7-bef1-40ec-9aeb760e2aff)

## Notable Integrations Changes

This page summarizes the major changes in Sonatype integrations. Note that this is not an exhausted list of all changes across all integrations; detailed change logs are available within each individual integration's main help page. This page focuses only on highlighting major changes.

### July 2025

See below to learn more about exciting changes to our integrations in July 2025.

### June 2025

See below to learn more about exciting changes to our integrations in June 2025.

### May 2025

See below to learn more about exciting changes to our integrations in May 2025.

### April 2025

See below to learn more about exciting changes to our integrations in April 2025.

### March 2025

See below to learn more about exciting changes to our integrations in March 2025.

### February 2025

See below to learn more about exciting changes to our integrations in February 2025.

### January 2025

See below to learn more about changes to our integrations in January 2025.

## Sonatype for Azure DevOps

The Sonatype for Azure DevOps extension integrates with the Azure DevOps pipeline to run policy evaluations in the build workspace. It adds a new step within the build, during which Sonatype IQ Server scans applications to identify any open-source security, license, or quality policy violations. It can be configured to fail the build or generate a warning. This allows the build maintainers to understand the reasons for build failures and plan a remediation strategy.

This extension wraps the [Sonatype IQ CLI](#UUID-6b69b7b1-858f-e58a-e010-beb4fdff9cdf) .

The Sonatype for Azure DevOps extension is available on the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=SonatypeIntegrations.nexus-iq-azure-extension) .

### Main Features

- Perform a Sonatype IQ Server policy evaluation on files in the build workspace.
- Display scan results within Azure DevOps pipeline report.
- Provide a link to a comprehensive Sonatype Lifecycle policy evaluation report indicating violation details and remediation recommendations.

### Release Notes

[https://sonatype.github.io/iq-azure-devops/CHANGELOG](https://sonatype.github.io/iq-azure-devops/CHANGELOG)

### Compatibility

[https://sonatype.github.io/iq-azure-devops/compatibility](https://sonatype.github.io/iq-azure-devops/compatibility)

### Installation and Configuration

Go to the [Installation and Configuration](#UUID-ca9b7cf5-eaeb-4f80-b4ac-43c32cefb0c0) page for steps to install and set up Sonatype IQ in your Azure DevOps pipelines.

### Evaluating Policies

The "SonatypeEvaluate" task appears in the jobs list during a build:

![SonatypeEvaluate.png](/assets/images/uuid-e5d1ac4b-77cf-813b-8b24-26bb512345be.png)

**Note:** `NexusIqPipelineTask` is still supported, but it has been deprecated and may be removed in a future version.

### Add dashboard widgets for Sonatype IQ

For ease of use, the following widgets for Sonatype IQ can be added to the Azure DevOps dashboard.

- Sonatype IQ Policy Evaluation widget: shows the policy evaluation results for the latest build.
- Trends for Sonatype IQ Policy Evaluation: shows a historical trend of Sonatype IQ Policy evaluations of the last 5 builds.

**How to add Sonatype IQ widgets to the Azure DevOps Dashboard:**

### Running Sonatype IQ in Azure Self-Hosted Agents

If you’re using an HTTP proxy within your infrastructure and Azure self-hosted build agents, you can specify the Azure DevOps agent’s proxy settings. These settings will then be automatically applied when connecting to IQ. For more information, refer to [Microsoft’s documentation](https://docs.microsoft.com/en-us/azure/devops/pipelines/agents/proxy?view=azure-devops&tabs=windows) .

In the Azure-provided sample command:

```
./config.sh --proxyurl http://127.0.0.1:8888 --proxyusername "myuser" --proxypassword "mypass"
```

This would appear in the scan output as it is passed through to the IQ scan client:

```
...
-p
127.0.0.1:8888
-U
myuser:***
...
```

### Fetch SBOM Task Properties

Fetch SBOM is a task for retrieving an SBOM (Software Bill of Materials) file associated with a previous Lifecycle evaluation. It supports both the [CycloneDX](https://cyclonedx.org/) and [SPDX](https://spdx.dev/) standards. For configuration steps, see the [Installation and Configuration](urn:resource:component:343122/section-idm183496732361458) page.

**Note:** The reference name you assign to each task (e.g., `sonatypePolicyEvaluation` , `sonatypeFetchSbomTask` ) becomes the prefix for its output variables. Adjust the variable references accordingly.

### Git/jgit Configuration and Permissions

The Azure DevOps extension uses the Sonatype IQ CLI to perform scans.

During the scanning process, the CLI uses Git to detect the repository URL, commit hash, and branch name.

If native Git is available on the build agent, the CLI will use it; otherwise, it falls back to jgit (Java-based Git). When jgit is used, it attempts to create configuration files in the current user’s `$HOME` directory. If it doesn’t have permission to do so, you may see ERROR-level log messages—these are not critical to the scan and can be safely ignored. To avoid them, make sure native Git is installed on the build agent, or set the `XDG_CONFIG_HOME` environment variable to a directory that the build agent user can write to.

### Installation and Configuration - Sonatype for Azure DevOps

## Sonatype for Bamboo Data Center

Sonatype for Bamboo Data Center integrates with Atlassian Bamboo to run policy evaluations in the build workspace. It provides instant analysis of open-source components used in every Bamboo build and generates alerts for policy violations related to quality, license, or security. This allows development teams to address open-source policy violations earlier in the development cycle and avoid unplanned rework.

The Sonatype for Bamboo Data Center integration is available on the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1229508/nexus-iq-for-bamboo) .

**Note:** Sonatype for Bamboo Data Center plugin is verified by Sonatype to work on the Bamboo Data Center.

### Main Features

### Release Notes

[https://sonatype.github.io/clm-bamboo-plugin/CHANGELOG](https://sonatype.github.io/clm-bamboo-plugin/CHANGELOG)

### Compatibility

[https://sonatype.github.io/clm-bamboo-plugin/compatibility](https://sonatype.github.io/clm-bamboo-plugin/compatibility)

### Requirements

- Install and start IQ Server.
- Create an organization and at least one application in IQ Server.
- Evaluate the application at least once (see [Manual Application Evaluation.](#UUID-c364f118-bb5b-8f05-7421-1c09086ed38a) )

### Installation and Configuration

Go to the [Installation and Configuration](#UUID-9ff30eb6-505b-bc32-28ce-9cd02fd63891) page for steps to install and set up Sonatype for Bamboo Data Center.

### Variables and credentials

Starting from version **3.1.0** , you can configure variables and credentials at the global, project, or plan level from the Bamboo administration page.

To add a variable, click on the *Global variables* option on the left-hand navigation menu, and enter a variable name and value.

![bamboo_variables.png](/assets/images/uuid-9d9c80eb-76fb-3af5-cb34-f76650390196.png)

To add a credential, click on the *Shared credentials* option on the left-hand navigation menu, and enter the a *Credential name* , *Username* , and *Password* .

The *Credential name* field is the value that will be used by the Sonatype for Bamboo Data Center plugin; make sure it's one of the supported values listed below. The *Username* field can be set to match the *Credential Name* .

![bamboo_credentials.png](/assets/images/uuid-04be4abe-f072-7108-80cd-3c557bdeb09d.png)

Sonatype for Bamboo Data Center currently supports the following credentials:

```
NEXUS_CONTAINER_IMAGE_REGISTRY_USER
```

```
NEXUS_CONTAINER_IMAGE_REGISTRY_PASSWORD
```

```
NEXUS_CONTAINER_SCANNING_REGISTRY_USER
```

```
NEXUS_CONTAINER_SCANNING_REGISTRY_PASSWORD
```

### Add Sonatype Lifecycle analysis task

### Evaluate Policies and View Results

Your application will be evaluated as a task during Bamboo job execution. The Job Summary page shows the results of the evaluation.

The summary results give a breakdown and count of violations for each of the 3 threat level categories:

- Critical (threat level 8-10)
- Severe (threat level 4-7)
- Moderate (threat level 2-3)

The overall evaluation status is indicated by Passed, Failed, Passed with Warnings.

Click on Full Report to view a detailed report in the IQ Server.

![126655782.png](/assets/images/uuid-15553f7f-2747-e355-d3f5-1c6c654d15c0.png)

### Installation and Configuration - Sonatype for Bamboo Data Center

## Sonatype Container Security

Sonatype Container Security is a comprehensive security solution for the entire container build time pipeline; safeguarding your containerized applications by protecting them with unmatched vulnerability detection and automatic policy enforcement during build time.

- Integrates within CI/CD pipelines to scan and report CVE vulnerabilities within container images
- Scan early in the development process to prevent vulnerable images from deploying

### Prerequisites for Sonatype Container Security

- macOS or Linux.
- A running instance of the Docker client. [Podman](https://podman.io/) provides wrapper commands ("docker") that mimic the behavior of Docker commands and is also supported.
- [Podman](https://podman.io/) provides wrapper commands ("docker") that mimic the behavior of Docker commands and is also supported.
- Set the environment variables as needed.

**Note:** Container scanning using Windows OS is not supported. The Azure DevOps plugin supports container security build time container: scanning, provided the agent uses macOS or Linux and the other prerequisites are met. Windows users should refer to [Docker Container Analysis](#UUID-6fc284d2-4d0b-409f-5e27-81abfa103f0e) .

### Scanning with Sonatype Container Security

Sonatype Container Security uses the Docker client to analyze the container as a scan target when using the CLI scanner. Environment variables are configured depending on where the image is located.

**Note:** When using IQ CLI version 1.183.0 or earlier, use unique mount paths for each scan target when performing container scans in parallel.

### Running a scan from Jenkins

Requirements are a running instance of Jenkins with the Sonatype Platform plugin installed and configured to run policy evaluations in Jenkins.

Consult the [Jenkins documentation](https://www.jenkins.io/doc/pipeline/tour/environment/) for examples of setting environment variables.

For this example, the `scanPattern` of `container:` is used to target the container.

```
pipeline {
  agent any

  environment {
    NEXUS_CONTAINER_IMAGE_REGISTRY_USER = {anyuser}
    NEXUS_CONTAINER_IMAGE_REGISTRY_PASSWORD = {password}
  }

  stages {
    stage('Policy') {
      steps {
        nexusPolicyEvaluation (
          advancedProperties: '', 
          enableDebugLogging: false,
          failBuildOnNetworkError: false,
          iqApplication: selectedApplication('test-app'),
          iqScanPatterns: [
            [scanPattern: 'container:http://registry.hub.docker.com/library/alpine:3.4'],
            [scanPattern: '**/my_application.war']
          ], 
          iqStage: 'build',
          jobCredentialsId: ''
        )
      }
    }
  }
}

```

### Running a scan on Podman without Docker

If you don't have Docker, you may use Podman as an alternative container runtime. [Podman](https://podman.io/) is a daemonless container engine for developing, managing, and running OCI (Open Containers Initiative) Containers and Container Images.

Follow the steps below to scan with Sonatype Container Security using Podman instead of Docker:

### Sonatype Container Security environment variables

These environment variables are to set the authentication to remote servers.

These environment variables may be set to override the default configuration.

### FAQs

## Sonatype for Eclipse

The Eclipse IDE is an open-sourced software application for software development managed by the Eclipse Foundation. It's used for development in many ecosystems and is the most widely used IDE for Java development.

The Sonatype for Eclipse integration is available on the [Eclipse Marketplace](https://marketplace.eclipse.org/content/sonatype-nexus-iq) .

**Note:** Maven-based Java projects are fully supported. Gradle-based Java projects are supported with limited functionality. "Migrate to Selected" and "Locate Declarations" features are not available for Gradle-based projects.

### Release Notes

[https://sonatype.github.io/insight-eclipse/CHANGELOG](https://sonatype.github.io/insight-eclipse/CHANGELOG)

### Compatibility

[https://sonatype.github.io/insight-eclipse/compatibility](https://sonatype.github.io/insight-eclipse/compatibility)

### Installing the Integration

Check the [integration requirements](https://help.sonatype.com/en/download-and-compatibility.html#sonatype-lifecycle-for-eclipse) for Eclipse before starting the installation process.

Sonatype IQ for Eclipse can be installed by adding a new software repository.

### Configuring the Integration

After the successful installation of Sonatype IQ for Eclipse, you will be able to choose to show the Sonatype IQ for Eclipse view. To access this view:

### Using the Component Info View

Once the integration has been configured and the component analysis is completed, a component view will look similar to the examples shown below. The list of components will reflect an analysis of the build path.

If a **Golden Version** of the component is available, the suggestion will be marked with a star icon:

![golden-version.png](/assets/images/uuid-ec45388d-3fb5-46a3-8408-8ecc05a3afa4.png)

If there is no **Golden Version** available, but other remediations exist, they will be shown as **Available Fix Version(s)** :

![available-fix-versions.png](/assets/images/uuid-bd1e49b6-de9d-e59c-3f6d-85f2080d48ba.png)

**Note:** For Maven projects we include the compile and runtime scopes in the component evaluation. If you wish to include additional dependencies found in provided, test, and system scope, these can be configured.

The top left-hand corner of the *Sonatype IQ for Eclipse Component Info* view displays either the number of projects currently being examined in the view, or the name of the specific project. Next to that, the number of components found, and the number of components shown in the list is displayed.

The top right-hand corner provides a number of buttons to access the following features of Sonatype IQ for Eclipse:

The left-hand side of the view contains the list of components found in the project and identified by their artifact identifier and version number. A color indicator beside the components signals potential policy violations. The right-hand side of the view displays the details of the selected component from the list on the left.

By clicking on the list header on the left, the list can be ordered by the threat level of the policy a component has violated. In cases where there is no violation, the threat is simply light blue.

When you select a specific component in the list, the details, various properties, and a visualization of the different versions is displayed to the right of the list.

### Filtering the Component List

The list of components found in the analysis and displayed in the component info view can be configured by pressing the **Filter** button . The filter dialog, displayed below, allows you to narrow down the components shown.

![126656304.png](/assets/images/uuid-beefbc62-4629-73d9-0b14-19f1ea478a49.png)

The Scope setting determines which projects' components are displayed in the list:

### Searching for Component Usages

Once you have selected a specific component in the list on the left of the component info view, Sonatype IQ Server can determine in which projects the component is used. After pressing the **Locate Declarations** button , and once the search has been completed, you will see the results in a tree view of projects and project pom.xml files, all displayed in the *Search* window.

Inspecting this list can help you assess the impact of a potential upgrade to a new component version. Looking at the found projects, you can potentially remove wrong declarations, determine side effects from transitive dependencies, or find out why this component shows up as a dependency at all.

**Note:** **Locate Declarations** is only available for Maven-based Java projects.

### Inspecting Component Details

Press the **Open Component Details** button to access the details about policy violations, license analysis and security issues for a specific component selected in the list. An example details view is shown below:

![137203956.png](/assets/images/uuid-61f4dd95-36ef-f4ce-25bc-403ee1b9e31e.png)

The *Policy Violations* section in the top contains a list of all the policies that have been violated by the component.

The *License Analysis* section contains the threat levels posed by the licenses declared for each component, as well as those that have been observed in the source code.

The *Security Issues* section below contains the list of issues found. They are sorted from higher to lower risk, with each issue detailed by a threat level ranging from 0 to 10, or potentially with the value unscored and a descriptive text in the *Summary* column. In addition, links to the security vulnerability database entry are added as links in the *Problem Code* column.

### Migrating to Different Component Versions

**Note:** **Migrate to Selected** is only available for Maven-based Java projects.

If you determine that a component upgrade is required to avoid a security or license issue or a policy violation, after reviewing your component usage, Sonatype IQ for Eclipse can be used to assist you in the necessary refactoring.

The first step to start the migration is to select a newer version for the component in the visualization chart, or by selecting the recommended version. An example is displayed in the image below:

![migrate-button-enabled.png](/assets/images/uuid-6b02712a-f521-a01a-bf14-480802c36224.png)

Once you have selected a different version than the one currently used, the **Migrate to Selected** button will become active. Pressing the button opens a dialog that assists you in the migration to the newer component. The complexity of this task varies considerably from project setup to project setup. The migration wizard is able to detect circumstances such as the component being a transitive dependency or versions managed in a property.

The simplest flow is when a dependency version can be applied and the result is a single dialog like the one displayed below.

![126656307.png](/assets/images/uuid-8d3cd652-8ebd-a0b6-b3df-f7031437aca3.png)

If the version is managed in a property, the initial screen in the following example allows you to select if you want to continue with a property upgrade, or perform a replacing version upgrade.

![126656308.png](/assets/images/uuid-7d7c78a9-d01b-e698-74fa-c05ee563bd12.png)

Once you have selected to perform a property upgrade, you will be able to apply it in the next screen, as shown below:

![126656309.png](/assets/images/uuid-1dfacea0-342e-b6e5-758d-83c0ba3a732d.png)

The *Refactoring* screen features navigation tools allowing you to view all potential changes in the dialog, and step through them one-by-one before deciding to continue.

After you have completed the refactoring of your project files, you should perform a full build, as well as a thorough test, to determine that you can proceed with the new version in your development.

Typically, smaller version changes will have a higher chance of working without any major refactorings, or adaptations, of your code base and projects, while larger version changes potentially give you more new features or bug fixes.

Your release cycle, customer demands, production issues, and other influencing factors will determine your version upgrade choices. You might decide a multi-step approach, where you do a small version upgrade immediately to resolve current issues and then work on the larger upgrade subsequently to get the benefits of using a newer version. Or, you might be okay with doing an upgrade to the latest available version straight away. Potentially, a combination of approaches in different branches of your source code management system is used to figure out the best way of going forward with the upgrade.

Sonatype IQ for Eclipse and other tools of the IQ Server suite can assist you through the process of upgrading, as well as monitoring, the applications after upgrade completion.

## Sonatype for Fortify SSC

**Note:** Get the [Sonatype Lifecycle integration with SSC](https://marketplace.opentext.com/cybersecurity/content/sonatype-for-fortify-ssc) on the Fortify Marketplace.

### Release Notes

[https://sonatype.github.io/nexus-iq-fortify/CHANGELOG](https://sonatype.github.io/nexus-iq-fortify/CHANGELOG)

### Compatibility

For IQ Server Java compatibility, refer to the [Java Compatibility Matrix](#UUID-2b4bbc56-9eda-57ec-11cb-958bea327407) .

[https://sonatype.github.io/nexus-iq-fortify/compatibility](https://sonatype.github.io/nexus-iq-fortify/compatibility)

### Architecture Overview

![126657005.png](/assets/images/uuid-5b47a503-22e4-0fd1-21c5-5b23a4b166d8.png)

The integration has two main parts. Both of them are included in the installation bundle

- IQ - Fortify parser plugin
- IQ - Fortify integration service

### IQ - Fortify Parser Plugin Installation

The Sonatype parser plugin should be installed and enabled.

![126657007.png](/assets/images/uuid-8dc8d08c-2383-a5a6-acf0-3c63275922b2.png)

### IQ - Fortify Integration Service Configuration and Execution

Both servers must be up and running in order to successfully export data from Lifecycle to Fortify SSC. Other versions of the servers may work, but they are not officially supported.

### Integrating IQ Webhook with Fortify SSC Sync Service

Refer to [Integration of IQ Webhook with Fortify SSC Sync Service](#UUID-1fcc8087-34f4-2ab6-e7b8-9b9fadddcb9b) for details.

### About the Scan Report

### Integration of IQ Webhook with Fortify SSC Sync Service

The Fortify SSC synchronization service supports data synchronization with the IQ server in two ways:

- Scheduled polling (cron jobs) using the Synchronization Scheduler Refer to details on [Synchronization Scheduler](https://help.sonatype.com/en/sonatype-fortify-ssc.html#synchronization-scheduler) .
- Using IQ webhooks The following sections describe the integration of Fortify SSC Sync service with IQ webhook event.

## Sonatype GitHub Actions

This integration provides a set of [GitHub Actions](https://github.com/features/actions) for interacting with different Sonatype products directly within your GitHub workflows.

Sonatype GitHub Actions also support integration with GitHub Code Scanning, part of the [GitHub Advanced Security feature](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) , which displays detected vulnerabilities on the GitHub Security tab. As you'll find in the documentation below, you can use the `evaluate` or `run-iq-cli` actions in combination with the `upload-sarif-file` parameter to take advantage of this functionality. GitHub Advanced Security is available for GitHub Enterprise customers and public repositories.

The Sonatype GitHub Actions integration is available on the [GitHub Marketplace](https://github.com/marketplace/actions/sonatype-github-actions) .

### Release Notes

[https://sonatype.github.io/github-actions/CHANGELOG](https://sonatype.github.io/github-actions/CHANGELOG)

### Compatibility

[https://sonatype.github.io/github-actions/compatibility](https://sonatype.github.io/github-actions/compatibility)

### Sonatype Evaluate Action

An action for evaluations against a Sonatype Lifecycle instance in GitHub workflows. It sets up [Sonatype CLI](#UUID-6b69b7b1-858f-e58a-e010-beb4fdff9cdf) and runs it to execute the evaluation. This convenient composite action enables developers to start running Lifecycle evaluations quickly.

Internally, it uses 3 actions with some predefined parameters: **Setup Java** (which makes Java available for GitHub runners by selecting an appropriate version for the Sonatype CLI) and the following 2 actions which you can configure for more fine-grained control:

### Fetch SBOM Action

An action for retrieving an SBOM (Software Bill of Materials) file associated with a previous Lifecycle evaluation. It supports both the [CycloneDX](https://cyclonedx.org/) and [SPDX](https://spdx.dev/) standards.

### GitHub Enterprise Server

If you're using GitHub Enterprise Server (GHES) and encounter a warning message such as `Fail to upload artifact from Github Enterprise server` , it's because GHES doesn't currently support `@actions/upload-artifact@v4` .

To resolve this, add the following step to your workflow to use `@actions/upload-artifact@v3` instead:

```
- name: Upload Result File as an artifact
  if: ${{ !cancelled() && steps.run-iq-cli.outputs.result-file-path }}
  uses: actions/upload-artifact@v3
  env:
    NODE_TLS_REJECT_UNAUTHORIZED: 0 
  with:
    name: result-file
    path: ${{ steps.run-iq-cli.outputs.result-file-path }}
```

Possible outputs for `run-iq-cli` that can be used with this artifact upload step:

- `result-file-path`
- `sarif-file-path`
- `scan-file-path`

Possible outputs for `fetch-sbom` :

- `sbom-file-path`

### Usage Example - Sonatype GitHub Actions

Here's a typical usage example that evaluates an npm project against a Sonatype Lifecycle instance and retrieves the associated SBOM (Software Bill of Materials) file:

```
name: Sonatype Workflow
on: push
jobs:
  sonatype-cli:
    runs-on: ubuntu-latest
    steps:
      # Check out your code
      - name: Checkout
        id: checkout
        uses: actions/checkout@v4
      # Perform an evaluation 
      - name: Run evaluate action
        id: evaluate
        uses: sonatype/actions/evaluate@v1
        with:
          iq-server-url: https://your.lifecycle.server
          username: ${{ secrets.LIFECYCLE_USERNAME }}
          password: ${{ secrets.LIFECYCLE_PASSWORD }}
          application-id: lifecycle-app
          scan-targets: package.json package-lock.json
      # Fetch the SBOM file associated with the evaluation
      - name: Fetch SBOM
        uses: sonatype/actions/fetch-sbom@v1
        if: ( success() || failure() ) && steps.evaluate.outputs.scan-id 
        with:
          iq-server-url: https://your.lifecycle.server
          username: ${{ secrets.LIFECYCLE_USERNAME }}
          password: ${{ secrets.LIFECYCLE_PASSWORD }}
          application-id: lifecycle-app
          scan-id: ${{ steps.evaluate.outputs.scan-id }}
          sbom-standard: cyclonedx
          sbom-version: 1.5
          sbom-format: json
          artifact-name: lifecycle-app-sbom.json
```

## Sonatype for GitLab CI

Sonatype for GitLab CI allows you to perform policy evaluations against one or more build artifacts during a GitLab CI/CD pipeline run.

For GitLab Ultimate customers, Sonatype for GitLab CI can populate the Vulnerability Report and the Dependency List under the GitLab Ultimate Security feature.

![sonatype-gitlab.png](/assets/images/uuid-06a4a1fc-35b5-bf19-bcfc-7a0c99e41a04.png)

### Release Notes

[https://sonatype.github.io/gitlab-nexus-platform-plugin/CHANGELOG](https://sonatype.github.io/gitlab-nexus-platform-plugin/CHANGELOG)

### Compatibility

[https://sonatype.github.io/gitlab-nexus-platform-plugin/compatibility](https://sonatype.github.io/gitlab-nexus-platform-plugin/compatibility)

There are two options for integrating Sonatype with GitLab CI:

### CI Components

Available on the [GitLab CI/CD Catalog](https://gitlab.com/explore/catalog/sonatype-integrations/components) .

Sonatype CI Components are designed to integrate Sonatype solutions into your GitLab CI/CD pipelines. These components allow you to automate tasks like policy evaluation against your code, generating vulnerability reports, and fetching Software Bill of Materials (SBOMs) directly within your CI/CD workflow.

Refer to [GitLab Docs](https://docs.gitlab.com/ee/ci/components/) for more information about CI Components.

****

### CI/CD Pipelines

Available as a Docker image on the [Docker Hub](https://hub.docker.com/r/sonatype/gitlab-nexus-iq-pipeline) .

With Sonatype in your CI/CD pipeline, you can perform policy evaluations against one or more build artifacts, generate reports, scan containers, and fetch and store SBOM files.

GitLab Ultimate users can also create and update the GitLab's Vulnerability Report. See the corresponding course on [Sonatype Learn](https://learn.sonatype.com/learn/courses/108/sonatypes-gitlab-ultimate-integration/lessons) for a video about this feature.

**Note:** You can also scan Docker containers using the [Sonatype Container Security](#UUID-256fe272-31f8-babd-fac3-f39c0503cfae) integration.

### CI Components - Sonatype for GitLab CI

The component set currently contains several top-level, single-purpose components:

- [Run a policy evaluation](#UUID-780d8212-0eb2-ecfd-0dd8-1b7eba4d49bf_section-idm234656672134897) against a Sonatype IQ Server instance.
- [Create a vulnerability report](#UUID-780d8212-0eb2-ecfd-0dd8-1b7eba4d49bf_section-idm234657855429687) based on a previous policy evaluation.
- [Fetch a Software Bill of Materials (SBOM)](#UUID-780d8212-0eb2-ecfd-0dd8-1b7eba4d49bf_section-idm234657914381812) from a Sonatype IQ Server instance.

Additionally, two convenience components are also provided, which wrap the above components:

- [Run a policy evaluation](#UUID-780d8212-0eb2-ecfd-0dd8-1b7eba4d49bf_section-idm234658037523814) against a Sonatype IQ Server instance, and also get a vulnerability report and the SBOM in a single step (GitLab Ultimate users only).
- [Run a policy evaluation](#UUID-780d8212-0eb2-ecfd-0dd8-1b7eba4d49bf_section-idm234658049072407) against a Sonatype IQ Server instance, and also get the SBOM in a single step.

### CI/CD Pipelines - Sonatype for GitLab CI

Sonatype for GitLab CI is packaged as a Docker image to perform policy evaluations against one or more build artifacts during a GitLab CI/CD pipeline run.

## Sonatype for IDEA

IntelliJ IDEA is a fully-featured integrated development environment (IDE) used for Java development. WebStorm is an IDE for the JavaScript ecosystem.

The Sonatype for IDEA integration is available on the [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/14692-sonatype-nexus-iq) .

### Supported JetBrains IDEs for Lifecycle Component Analysis

### Release Notes

[https://sonatype.github.io/nexus-iq-idea-plugin/CHANGELOG](https://sonatype.github.io/nexus-iq-idea-plugin/CHANGELOG)

### Compatibility

[https://sonatype.github.io/nexus-iq-idea-plugin/compatibility](https://sonatype.github.io/nexus-iq-idea-plugin/compatibility)

### Installing Sonatype for IDEA

**Download latest version** :

Sonatype for IDEA supports installation via a zip file. Installation is performed using the Settings/Preferences dialog. Select Plugins from the left-hand pane to open the option to install the plugin from disk. From there, browse to the plugin zip file and select it.

![126656232.png](/assets/images/uuid-56327bf5-ed79-2095-7bb0-c3ad223ebc08.png)

### Configuring Sonatype for IDEA

After the installation, the plugin needs to be configured to connect to your Lifecycle server. From a project view, click the Nexus IQ icon on the Tool Windows menu, and then click on the gear icon to configure the integration with your Sonatype Lifecycle credentials.

- Server URL: Enter the base URL of your IQ Server including a trailing slash. Eg. https://iq.cloud.sonatype.com/
- Authentication Method: PKI Authentication: Delegate authentication to the JVM. User Authentication: Enter your credentials or user token for the Lifecycle server. You will be prompted for your IDEA Master Password when saving the Preferences/Settings. This allows IDEA to store your Lifecycle credentials securely.
- PKI Authentication: Delegate authentication to the JVM.
- User Authentication: Enter your credentials or user token for the Lifecycle server. You will be prompted for your IDEA Master Password when saving the Preferences/Settings. This allows IDEA to store your Lifecycle credentials securely.

Once the connection information is provided, select Connect to verify the connection to the Lifecycle server. When connected, select an application from the dropdown. The policies scoped to this application are used when evaluating your IDE project.

When the test **Connect** reports an HTTP error:

- Check your [HTTP Proxy Server configuration](https://www.jetbrains.com/help/idea/settings-http-proxy.html) . When the URL is for an internal hostname, the host may need to be added to the **No proxy for** the list of patterns.
- Have your administrator verify the server request.log shows that your **Connect** requests have reached the server. The log files may contain more information to debug the issue.

### Using the Component Info View

The Sonatype for IDEA tool window can be accessed by clicking the IQ Tab on the bottom tool strip of IDEA. This is also available in View > Tool Windows.

Once configured and the component analysis is completed, a component view is populated with all open source components and their metadata. The list of components reflect an analysis of the project’s dependencies. For Java projects, that include all project libraries. For JavaScript projects, it includes all dependent Node modules. For Python projects, it includes all Python packages installed in the virtual environment associated with the project. Mixed projects, contain a mix of Java, JavaScript, and Python dependencies.

![137206016.png](/assets/images/uuid-e8e9d4f7-f679-5eab-d634-44ea33c52a47.png)

By default, all project dependencies are included in the component list. Scope filters can be applied to adjust which components are visible.

The following scopes are available:

- Java components: Compile, Test, Runtime, and Provided;
- JavaScript/Node components: Production, and Development;
- Python components: All (the IDE does not provide enough information to distinguish between production and development packages).

Right-clicking on any component will bring up a menu of actions. All components allow for the following actions: View Details and Find Usages. Maven-based Java components show an extra action: Open Maven POM.

- View Details will open the details screen providing more context to the component.
- Find Usages will bring up a list of every module the component is used in. Clicking on a module will display the location where the component is declared, which is either a Maven POM file or a package.json file.
- Open Maven POM will open the Maven POM of the component selected.

### Multi-Language Projects

The Sonatype for IDEA plugin detects and analyzes components written in different programming languages, within a single project. The project is organized to follow the JetBrains recommended project structure.

IntelliJ IDEA project structure consists of projects and modules. A [project](https://www.jetbrains.com/help/idea/creating-and-managing-projects.html) can contain source code, tests, libraries in use, build instructions, and configuration files. It may contain one or more [modules](https://www.jetbrains.com/help/idea/creating-and-managing-modules.html) . When no modules are defined for the project, the project itself is considered a module.

### Troubleshooting Load Components

### Migrating to Different Component Versions

**Note:** For Java projects, this feature relies on the project being Maven-based. For JavaScript projects, this feature expects that the project is properly set up in the IDE as a Node project and that a package manager is available (i.e. npm, yarn, or pnpm).

If you determine that a component upgrade is required to avoid a security or license issue or a policy violation, after reviewing your component usage, the plugin can be used to assist you in the necessary refactoring.

The first step to start the migration is to select a newer version for the component in the visualization chart, or by selecting the recommended version.

A version of a dependency with no policy violations and no breaking changes for the same component and its dependencies will be presented as a **Golden Version** , which means that the migration can be done with minimal effort.

Alternate versions might also be available so you can migrate to them in case there is no Golden Version available.

![137206019.png](/assets/images/uuid-8ccf8aff-217a-6a47-1a85-101557b341e4.png)

Once you have selected a different version than the one currently used, the **Migrate to Selected** button will become active. Selecting the button migrates from the current component version to the selected component version, by updating the component version in the manifest file.

For Maven-based Java projects, the migration process is able to detect circumstances such as the component being a transitive dependency or versions managed in a property. For JavaScript projects, only direct dependencies can be migrated.

After the migration is completed, the component list will be updated and a component scan will be initiated. You should perform a full build, as well as a thorough test, to determine that you can proceed with the new version in your development.

Typically, smaller version changes will have a higher chance of working without any major refactorings, or adaptations, of your codebase and projects, while larger version changes potentially give you more new features or bug fixes.

Your release cycle, customer demands, production issues, and other influencing factors will determine your version upgrade choices. You might decide on a multi-step approach, where you do a small version upgrade immediately to resolve current issues and then work on the larger upgrade subsequently to get the benefits of using a newer version. Or, you might be okay with doing an upgrade to the latest available version straight away. Potentially, a combination of approaches in different branches of your source code management system is used to figure out the best way of going forward with the upgrade.

### Code Inspections

New in version 4.3.0, custom code inspections are provided for **pom.xml** and **package.json** files. If a component, declared in those files, has critical, severe or moderate policy violations, it gets a code inspection maker attached to it, describing the severity of the violation and providing a link to its corresponding entry in the Component Info view.

![126656231.png](/assets/images/uuid-38f409f5-7d97-7ae5-4a13-f0220a6d504f.png)

### Upgrading to IntelliJ IDEA 2020.2

When upgrading to a newer version of IntelliJ IDEA from version 2020.1.x and below, you will need to install the latest version of the plugin. The Sonatype for IDEA plugin does not automatically upgrade itself when upgrading IntelliJ. We recommend uninstalling the plugin and reinstalling the latest plugin once the upgrade is complete.

You might see a message like this when you start the IntelliJ IDEA 2020.2.x upgrade:

![126656243.png](/assets/images/uuid-1858b96a-bf27-0114-8a56-81683917df66.png)

## Sonatype Platform Plugin for Jenkins - Lifecycle

Sonatype Platform Plugin for Jenkins (previously known as the Nexus Platform Plugin for Jenkins) integrates Jenkins with Lifecycle to perform SCA open-source evaluations during the application build and to push the CI analysis back to CSM pull request.

This integration also works with [Nexus Repository](#UUID-62502c87-fb04-567c-ba71-0e6a68a66138) .

### Release Notes

[https://sonatype.github.io/jenkins-plugin/CHANGELOG](https://sonatype.github.io/jenkins-plugin/CHANGELOG)

### Compatibility

[https://sonatype.github.io/jenkins-plugin/compatibility](https://sonatype.github.io/jenkins-plugin/compatibility)

### Prerequisites

The Sonatype Platform Plugin for Jenkins uses the HTTP proxy settings defined in *Manage Jenkins > Manage Plugins > Advanced* . These settings take precedence over any JVM proxy settings and are applied consistently by both Nexus Repository and IQ Server. If no Jenkins proxy settings are configured in the UI, the plugin falls back to the JVM proxy settings, for example:

```
-Dhttp.proxyHost=127.0.0.1 
-Dhttp.proxyPort=8080
-Dhttp.nonProxyHosts="*.demo"
```

To bypass the HTTP proxy server you must update the non-proxy host to include the IQ Server.

### Installation and Configuration

Go to the [Installation and Configuration](#UUID-b7da653d-f50a-8861-8330-28b74786cdf5) page for steps to install and set up Sonatype Platform Plugin for Jenkins.

### Adding an Evaluation to a Build

*Pipeline* refers to both [Declarative and Scripted Jenkins Pipelines](https://jenkins.io/doc/book/pipeline/) .

*Project (or Job)* refers to [a Jenkins item](https://www.jenkins.io/doc/book/glossary/#item-1) , such as a Freestyle project, Multi-configuration project, or Maven project, that allows selecting an explicit *build* *step* from a drop-down menu and filling in form field values inside the build configuration.

The scan patterns applied by default are `**/*.jar, **/*.war, **/*.ear, **/*.zip, **/*.tar.gz` .

To use other patterns, a manual override of `iqScanPatterns` is required, as described in the pipeline build step below.

**Note:** Scan patterns are file-oriented; they must match files, not directories. For example, to include all files in the `my-folder` directory, use the pattern `**/my-folder/**.` The pattern `**/my-folder` is insufficient for proper file matching as it targets a directory name.

### Reviewing Evaluation Results

Once the build is complete, a summary is shown on the project page. The three boxes (red, orange, and yellow) located below the link give you counts for policy violations and are based on the associated severity (critical, severe, and moderate).

A historical graph is also shown to indicate policy health over time.

Additionally, a build report is available within Jenkins by clicking the *IQ Build Report* in the left-hand navigation. This build report shows which components caused a 'warn' or 'fail' action on a particular build.

![126655796.png](/assets/images/uuid-e4f95af0-f05b-8481-2f50-9608519acc44.png)

If you are looking for previous report results, navigate to a specific build report in the Build History. Click on the link *View Application Report* to view the build report in IQ Server. Alternatively, you can use the *View Developer Priorities* link to navigate to the Developer priorities page.

![178717520.png](/assets/images/uuid-d8b40889-7c7f-3f64-2ab8-fc468a48675e.png)

### Reachability Analysis

Reachability Analysis detects method signatures in the application code that contain components (belonging to the Maven ecosystem) with potentially exploitable security vulnerabilities and are in the execution path. The policy violations occurring due to such components, will be assigned the status of `Reachable` on the application report. Clicking on the policy violation gives the details of the implicated component.

This helps developers prioritize the remediation of such policy violations by replacing the vulnerable components that are reachable by executing the application.

For more details refer to [Reachability Analysis](#UUID-bffb3d6e-1a0b-5607-518a-3dcdc88508c2) .

This configuration is suitable for *Pipeline* , *Multi-branch Pipeline* , or any other build types that make use of the [Jenkins pipeline](https://www.jenkins.io/doc/book/pipeline/) (including using Jenkinsfile).

### Installation and Configuration - Sonatype Platform Plugin for Jenkins

## Sonatype Platform Plugin for Jenkins - Nexus Repository

The Sonatype Platform Plugin for Jenkins provides the powerful abilities needed to orchestrate your organization's build and release pipelines while also enabling integration and orchestration of the staging functionality in Nexus Repository Pro.

Features include:

- Publishing tagged build outputs to the Nexus Repository.
- Creating and associating tags to components.
- Moving/promoting tagged components through a series of staging repositories (e.g. dev, test, qa).
- Deleting tagged components as needed during post-release cleanup activities.

This integration also works with [Sonatype Lifecycle](#UUID-0d46c567-a411-72f8-7973-d8f4cf7e00b2) .

### Connecting Jenkins to Nexus Repository

Connect Jenkins to connect to Nexus Repository:

Repeat the above process for each Nexus Repository server instance.

### Publish / Deploy Components

The following repository formats are supported by the publisher:

- Maven 2 release repositories

### Tagging Components

Tagging components is available when using a Nexus Repository Pro instance.

### Staging Workflow

Staging is available for Nexus Repository Pro instances.

## Sonatype for Jira Cloud

Sonatype for Jira Cloud automatically creates issues in response to new violations as they occur during your policy evaluation. Prioritize and track the remediation of open-source component risk directly in your development workflow.

The Sonatype for Jira Cloud integration is available on the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1232875/sonatype-for-jira-cloud-preview?hosting=cloud&tab=overview) .

### Release Notes

[https://sonatype.github.io/lifecycle-jira-cloud-integration/CHANGELOG](https://sonatype.github.io/lifecycle-jira-cloud-integration/CHANGELOG)

### Compatibility

[https://sonatype.github.io/lifecycle-jira-cloud-integration/compatibility](https://sonatype.github.io/lifecycle-jira-cloud-integration/compatibility)

### Steps for Configuration

To perform as a Jira Cloud site admin:

- Install Sonatype for Jira Cloud
- Configure the integration in Jira Cloud
- Configure the integration per project to receive tickets

To perform as IQ Server and Policy administrator:

- Add webhook to the Jira Cloud in IQ Server
- Set up notifications on the Lifecycle policy

### Install Sonatype for Jira Cloud

Install the integration directly from the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1232875/sonatype-for-jira-cloud-preview?hosting=cloud&tab=overview)

![iq-integration-Jira-cloud-site.png](/assets/images/uuid-c3b09f4c-1197-6a1b-b7da-24756e63d257.png)

### Configuration Requirements

- A Sonatype Lifecycle license with IQ Server version 168 or higher.
- The latest Sonatype for Jira Cloud integration installed.
- A webhook endpoint from Jira with a secured secret key.

⚠️ **Warning:** The secret key will be created by your team to encrypt requests. Keep the key secret as it will have permission to send requests to add issues in your Jira instance.

### Configure Sonatype for Jira Cloud

After installing the plugin we need the webhook to send requests to Jira:

![Integrations_-_Jira_Cloud_-_Configuration.png](/assets/images/uuid-b05f0629-15a5-b266-a453-3139e6796200.png)

### Assign Sonatype Lifecycle Applications to Jira Projects

You must assign Sonatype Lifecycle applications to your Jira projects before new violations are created as issues.

### Create a webhook in the Lifecycle server

The Lifecycle server webhooks are used to communicate with the plugin

**Note:** The `Organization and Application Summary` webhook event may result in slow performance and potential security concerns for Lifecycle servers with hundreds of applications. The assigning applications dropdown is only present when this webhook is configured. Instead, you will need to provide a comma-separated list of organizations and application Ids.

### Configure Notifications on Policies

Not all policy violations require a Jira ticket to be created whenever it is found. Notifications in Lifecycle are set on each policy for the stages you wish tickets to be created. For example, creating tickets on all security-critical and security-high violations at the build stage. The following steps will need to be performed for each policy violation you will want to configure a Jira notification for.

![126655373.png](/assets/images/uuid-a363eb00-ae03-8017-bf95-6d8bbc57dd4a.png)

### Review violation tickets within the plugin

When Lifecycle detects violations, new issues are created on the project board with the `New` status.

Example of issue aggregation of `By IQ Evaluation`

![Lifecycle_notification.png](/assets/images/uuid-0fa9eaf5-02cd-f6ba-5ce7-35fa28ca153c.png)

A subtask is created for each of the components attached to the primary report scan ticket for the issue aggregation of `By Component`

![iq-integration-jira-child-issues](/assets/images/uuid-c42cd3bd-29bb-a5c7-82ef-01c696b8ba40.png)

The following fields are populated as follows:

- **Type** : Corresponds to the selected issue type on the mapping page.
- **Labels** : Corresponds to a selected label on the mapping page.
- **Reporter** : Corresponds to a selected reporter on the mapping page.
- **Priority** : Lifecycle threat level 10 is mapped to the highest Jira priority with the threat of 0 is mapped to the lowest priority. Additional priorities are assigned using a linear function. Threat Level Jira Priority 9-10 Highest 7-8 High 4-6 Medium 2-3 Low 0-1 Lowest

**Note:** Priority names for your organization can be different if they've been customized in Jira settings by a Jira admin.

### Supported and unsupported field types

Default values are required for mandatory fields in Jira. The plugin will ignore the unsupported fields if they are marked optional in Jira.

The supported fields are: `Number, Paragraph, Short text, Select list (single choice), Select list (multiple choices), URL, Radio, Labels`

### Logging Details

In Sonatype for Jira Cloud's logs, we only record the IQ payload from webhook events, including whether they were processed successfully and any error messages. We do not capture or store any data from Jira itself; our logging is strictly limited to IQ content and metadata automatically provided by Jira.

### Jira Integration troubleshooting tips

- Check that policy notifications are sent to the Jira webhook. Jira issues are only created for new violations. `No Action` is taken when the violation has already been sent to Jira.
- Jira issues are only created for new violations.
- `No Action` is taken when the violation has already been sent to Jira.
- Verify the webhook URL matches between the Lifecycle server and Jira.
- Check the Sonatype for Jira Cloud configuration page on Jira for error messages. The message box will display the status of the last webhook received from the Lifecycle server.
- At least one application or organization needs to be mapped to the project.
- Check that the violation alerts are mapped to the correct Jira project.
- Check that the evaluation stage matches the configured webhook notification.

## Sonatype for Jira Data Center

Sonatype for Jira Data Center is an Atlassian Jira plugin that automates the creation of Jira issues for new policy violations.

- Prioritize remediation of open-source policy violations from the Lifecycle server inside the Jira Data Center
- Automatically create Jira issues when new violations occur
- Transition project issues once they have been remediated in the application code

The Sonatype for Jira Data Center integration is available on the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1220548/nexus-iq-for-jira) .

### Workflow overview

### Release Notes

[https://sonatype.github.io/iq-jira-plugin/CHANGELOG](https://sonatype.github.io/iq-jira-plugin/CHANGELOG)

### Compatibility

[https://sonatype.github.io/iq-jira-plugin/compatibility](https://sonatype.github.io/iq-jira-plugin/compatibility)

### Requirements

- Sonatype Lifecycle license and configured IQ Server
- IQ Server account with the *Policy Administrator* role
- Jira Administrator account to install and configure the plugin

For details on the Jira Data Center versions supported, please check the plugin's [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1220548/nexus-iq-for-jira) listing.

**Note:** The Sonatype for Jira plugin is verified by Sonatype to work on the Jira Data Center

### Installation

The initial installation is only required once and will apply to all Jira projects. This configuration enables the integration between Jira and Sonatype IQ Server.

- Install the [Sonatype for Jira Data Center](https://marketplace.atlassian.com/apps/1220548/nexus-iq-for-jira?hosting=datacenter&tab=installation) from the Atlassian Marketplace

### Configure the plugin

Configuration of the Sonatype for Jira Data Center plugin is done at the global Jira instance level.

![Integrations_-_Jira_Data_Center.png](/assets/images/uuid-273a90d4-b4e7-752c-b15f-a1cba5b1ce3d.png)

### Jira project to Lifecycle server associations

Sonatype Lifecycle organizations/applications are associated with a specific Jira project. Follow the steps below for each Jira project intended to receive policy violation notifications from the Sonatype IQ Server.

### Supported and unsupported field types

Default values are required for mandatory fields in Jira. The plugin will ignore the unsupported fields if they are marked optional in Jira.

The supported fields are: `Number, Paragraph, Short text, Select list (single choice), Select list (multiple choices), URL, Radio, Labels`

### Supported Custom Field Types

- Date Picker
- Date Time Picker
- Labels
- Number Field
- Paragraph Field
- Short Text
- URL Field
- User Picker

### Jira Integration troubleshooting tips

- Check that policy notifications are sent to the Jira webhook. Jira issues are only created for new violations. `No Action` is taken when the violation has already been sent to Jira.
- Jira issues are only created for new violations.
- `No Action` is taken when the violation has already been sent to Jira.
- Verify the webhook URL matches between the Lifecycle server and Jira.
- Check the Sonatype for Jira Cloud configuration page on Jira for error messages. The message box will display the status of the last webhook received from the Lifecycle server.
- At least one application or organization needs to be mapped to the project.
- Check that the violation alerts are mapped to the correct Jira project.
- Check that the evaluation stage matches the configured webhook notification.

### Jira logging

Error messages are sent to Jira's default log4j logger of levels `WARN` or higher. Log levels can be temporarily changed by navigating to the `System` → `Logging and Profiling` tab on the Jira administration page.

To make log changes permanent or for advanced log4j settings, edit 'WEB-INF/classes/log4j.properties'.

The logging of the Jira plugin can be customized using the following log levels:

## Sonatype CLM for Maven

Sonatype CLM for Maven is a Maven plugin that allows users to evaluate any Maven-based software project (e.g. Nexus Repository 3 Pro, Eclipse, Hudson/Jenkins). Run Sonatype CLM for Maven from a command line interface to integrate with any continuous integration server or IDE.

**Note:** When using the plugin on a multi-module project, only configure an execution for the modules that produce components deployed as an application. For example: EAR or WAR files for deployment on application servers. tar.gz archives distributed to users. Any modules of a project.

### Release Notes

[https://sonatype.github.io/clm-maven-plugin/CHANGELOG](https://sonatype.github.io/clm-maven-plugin/CHANGELOG)

### Compatibility

### Integration Goals

### Evaluating Project Components with Sonatype Lifecycle

The evaluate goal scans the dependencies and build artifacts of a project and directly submits the information to Sonatype Lifecycle for policy evaluation.

- The Maven build will fail when the analysis results trigger the failing action on the provided stage.
- Dependencies of all child modules will be considered when invoked for a multi-module / aggregator project.
- The evaluate goal cannot be bound to a Lifecycle phase.
- The results can be accessed in Lifecycle under the application's lastest report or through the provided link.

The command line arguments are:

### Creating a Component Index

The index goal of Sonatype CLM for Maven allows you to identify component dependencies and makes this information available to IQ CI integrations. Invoke an execution of the index goal after the package phase.

- The generated `module.xml` file will be included by Lifecycle during the CI evaluation
- To manually configure the lifecycle phase to execute the plugin, you have to choose a phase after package
- The default location where the module information files are stored is `${project.build.directory}/sonatype-clm/module.xml` To ensure a successful IQ scan, the generated `module.xml` files must remain in their default locations.

```
mvn clean install com.sonatype.clm:clm-maven-plugin:index
```

Alternatively, configure the execution in the **** files build section or in a **** 's build section.

```
<build>
   <plugins>
      <plugin>
         <groupId>com.sonatype.clm</groupId>
         <artifactId>clm-maven-plugin</artifactId>
         <version>2.51.1-01</version>
         <executions>
            <execution>
               <goals>
                  <goal>index</goal>
               </goals>
            </execution>
         </executions>
      </plugin>
   </plugins>
</build>
```

With the above configuration, a normal Maven build execution will trigger the plugin to be executed in the **** phase.

```
[INFO] --- clm-maven-plugin:2.51.1-01:index (default) @ test-app ---
[INFO] Saved module information to /opt/test-app/target/sonatype-clm/module.xml
```

**Excluding Modules in Continuous Integration Integrations**

Use the Module Excludes property in the CI configuration to exclude modules from being evaluated during an CI evaluation.

A comma-separated list of Apache Ant styled patterns relative to the workspace root will denote the module information files to be ignored.

Here’s an example of the pattern described above:

```
**/my-module/target/**, **/another-module/target/**
```

If unspecified, all modules will contribute dependency information (if any) to the evaluation.

### Including a Bill of Materials in Nexus Repository 3 Pro

The attach goal scans the dependencies and build artifacts of a project and attaches the results to the project as another artifact in the form of a scan.xml.gz file. It contains all the checksums for the dependencies and their classes and further meta information and can be found in the target/sonatype-clm directory. A separate scan.xml.gz file is generated for each maven module in an aggregator project in which the plugin is executed.

This attachment causes the file to be part of any Maven install and deploy invocation. When the deployment is executed against a Nexus Repository 3 Pro server the artifact is used to evaluate policies against the components included in the evaluation.

To use this goal, add an execution for it in the POM, e.g. as part of a profile used during releases:

```
<build>
   <plugins>
      <plugin>
         <groupId>com.sonatype.clm</groupId>
         <artifactId>clm-maven-plugin</artifactId>
         <version>2.51.1-01</version>
         <executions>
            <execution>
               <goals>
                  <goal>attach</goal>
               </goals>
            </execution>
         </executions>
      </plugin>
   </plugins>
</build>
```

Once configured in your project, the build log will contain messages similar to

```
[INFO] --- clm-maven-plugin:2.51.1-01:attach (default) @ test-app ---
[INFO] Starting scan...
[INFO] Scanning ...plexus-utils-3.0.jar
[INFO] Scanning ...maven-settings-3.0.jar...
[INFO] Scanning target/test-app-1.0-SNAPSHOT.jar...
[INFO] Saved module scan to /opt/test-app/target/sonatype-clm/scan.xml.gz
```

The attachment of the scan.xml.gz file as a build artifact causes it to be stored in the local repository as well as deployed to Nexus Repository 3 Pro.

### Using Sonatype CLM for Maven with IDEs

All common Java IDEs have integrations with Apache Maven and therefore can be used together with Sonatype CLM for Maven to evaluate projects against Sonatype Lifecycle.

This section showcases the integration with IntelliJ IDEA from JetBrains and NetBeans IDE from Oracle.

## Nexus Repository Maven Plugin

You can use the Nexus Repository Maven plugin for deploying, moving, and deleting packages as part of Nexus Repository's [staging](#UUID-7bc63556-9690-e797-782e-538b2ec719cc) functionality. To use this plugin, you will need to modify your project build configuration as described in this section.

### Configuration

The Nexus Repository Maven plugin replaces the Maven Deploy plugin in your build configuration and specifically enables staging actions for Nexus Repository 3.

You can configure the plugin by adding it to the project build plugins section of your project's `pom.xml` file as an extension:

```
<plugin>
  <groupId>org.sonatype.plugins</groupId>
  <artifactId>nxrm3-maven-plugin</artifactId>
  <!-- replace plugin version with the latest available -->
  <!-- https://search.maven.org/search?q=a:nxrm3-maven-plugin -->
  <version>1.0.3</version>
  <extensions>true</extensions>
  <configuration>
    <nexusUrl>http://localhost:8081</nexusUrl>
     
    <!-- The server "id" element from settings to use authentication from settings.xml-->
    <serverId>local-nexus</serverId>
    
    <!-- Which repository to deploy to -->
    <repository>maven-releases</repository>
     
    <!-- Skip the staging deploy mojo -->
    <skipNexusStagingDeployMojo>true</skipNexusStagingDeployMojo>
  </configuration>
</plugin>
```

### nxrm3:staging-deploy

Deploying packages using the plugin relies on assigning a tag. A tag can be generated by the plugin, assigned in the projects `pom.xml,` or assigned from the command line.

**Note:** **staging.properties** When a package is sent to staging, a `staging.properties` file is created under `./target/nexus-staging/staging` for tracking purposes. The file's contents include the name of the plugin, the date the package was staged, and the tag the package was given when staged. You can also use this file if you accidentally staged something to perform a rollback by doing a `nxrm3:staging-delete` without a tag defined. The tag will be drawn from this file. See nxrm3:staging-delete for more about staging-delete. Similarly, this file will be used to define the tag when you perform a staging-move without a defined tag. If you do not specify a tag in your move command, the plugin will use the last tag deployed.

### nxrm3:staging-move

Your Continuous Integration requirements may involve promoting packages. For example, this could involve moving packages from a testing repository to a production repository. The Nexus Repository Maven plugin provides this functionality.

### nxrm3:staging-delete

You can also use the Nexus Repository Maven plugin to delete deployed packages. For example, if a deployment fails part-way through, requiring a rollback, you can use the plugin to delete any currently deployed packages by tag.

⚠️ **Warning:** The delete operation will delete packages associated with the given tag across all repositories and all formats.

### Customizing Tag Value Format

If you do not prefer the default tag format of `${project.artifactId}-${project.version}-${timestamp}` , you can build it dynamically instead using a consistent format in POM configuration.

For example, in the [POM <properties> section](https://maven.apache.org/pom.html#Properties) , define the [Maven build time stamp format](http://maven.apache.org/guides/introduction/introduction-to-the-pom.html#Available_Variables) you want:

```
<!--
Build timestamp.
-->
<maven.build.timestamp.format>yyyyMMddHHmm</maven.build.timestamp.format>
```

Define a POM property that defines the complete format of the staging tag name to keep it consistent for all projects:

Perhaps [re-use the project name from the pom](https://maven.apache.org/pom.html#Quick_Overview) as well:

```
<name>staging-test</name>
```

Then, define the tag name in a consistent manner in the project POM or global parent POM plugin configuration.

```
    <plugin>
      <groupId>org.sonatype.plugins</groupId>
      <artifactId>nxrm3-maven-plugin</artifactId>
      <version>1.0.2</version>
      <extensions>true</extensions>
      <executions>
        <execution>
          <id>default-deploy</id>
          <phase>deploy</phase>
          <goals>
            <goal>deploy</goal>
          </goals>
        </execution>
      </executions>
      <configuration>
        <nexusUrl>${nexusUrl}</nexusUrl>
        <tag>${nxrm3.staging.tag}</tag>
      </configuration>
    </plugin>
```

### Nexus Repository 2 Users

This plugin is distinct from the [Nexus Staging Maven Plugin](https://github.com/sonatype/nexus-maven-plugins/tree/master/staging/maven-plugin) , which only enables staging actions in Nexus Repository 2. Due to underlying architectural differences of staging between Nexus Repository 2 and Nexus Repository 3, there is no backward compatibility.

## Sonatype for ServiceNow

This guide walks through the functionality of the Sonatype for ServiceNow integration, including where the data can be found within ServiceNow’s Application Vulnerability Response. This guide will include detailed instructions for how to install and configure the integration as well as how to begin tailoring the application to the user’s ServiceNow environment.

**Note:** The Sonatype Application Vulnerability Response integration currently only imports violations where the Sonatype policy type is “Security”, since those correspond most closely to the functions of Application VR in ServiceNow.

The purpose of this document is primarily to familiarize the reader with the software and integration itself, not to provide an all-encompassing review of ServiceNow’s Application Vulnerability Response modules and how to use them. The guide does attempt to provide best practice recommendations for utilizing the Sonatype data in concert with Application Vulnerability Response where possible/applicable; however, where decisions must be made and tailored to the customer environment, those decisions will be highlighted.

If you have questions regarding details of the integration not covered in this document, contact Sonatype’s customer support through your normal support channels.

### Prerequisites

- An active license for Sonatype Lifecycle (SaaS, Private Cloud, or Self-Hosted) version 173 or later is required to utilize the integration
- The target ServiceNow environment requires the Application Vulnerability Response (AVR) version 20.0.2 or newer to be installed (now bundled as part of “Vulnerability Response”)

**Note:** The integration is certified and fully compatible with ServiceNow Washington DC and ServiceNow Vancouver, as well as with Application Vulnerability Response (AVR) 20.0.2 and newer. While previous versions of the AVR modules may work, we recommend updating to the latest version for optimal integration.

Users should be familiar with the basic administration and usage of the ServiceNow platform (e.g. Creating report, tailoring list views, etc.)

For help with the ServiceNow platform, consult the [ServiceNow documentation](https://docs.servicenow.com/) or raise a ticket with the ServiceNow support team.

It is recommended to utilize ServiceNow’s NVD integration to populate the CVE and CWE tables. This provides contextual data on any vulnerable items created by the integration.

### Installation and Configuration

**Note:** Obtaining API Access Before configuring the integration we recommend generating an API User Code and Passcode from within the Lifecycle server. Look for the option `Manage User Token` in the user menu in the upper right corner within Lifecycle, and then choose `Generate User Token` on the display popup. See the documentation on for more information.

### Use Cases

This section outlines the use cases for the Application Vulnerability Response (AVR) ServiceNow Store App. The app integrates Software Composition Analysis (SCA) vulnerability data from Sonatype into ServiceNow, enhancing the capability to manage and mitigate vulnerabilities in software applications.

The AVR app processes SCA vulnerabilities to identify weaknesses in open-source software components used within applications, providing a structured response and remediation framework. The AVR app is designed to streamline the vulnerability management process by providing automated tools and workflows that integrate directly with ServiceNow’s existing infrastructure.

### Integration Architecture

This diagram describes the integration functionality at a high level:

![image7.png](/assets/images/uuid-77a380f4-ff40-176c-3d41-f9cc9c7b4972.png)

## Sonatype for Visual Studio 2022

Sonatype’s Integrated Development Environments (IDE) extensions provide development teams with direct access to Sonatype's comprehensive component intelligence. The Visual Studio 2022 extension enables a true Shift-Left in application security for development teams by putting security into the development workflow, allowing developers to build secure applications quickly.

Sonatype for Visual Studio 2022 Extension provides component analysis for both the Community, Professional, and Enterprise versions of Visual Studio.

The Sonatype for Visual Studio 2022 extension is available on the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=SonatypeIntegrations.SONADEV-VS2022) .

### New functionality in Visual Studio 2022

The Sonatype for Visual Studio 2022 extension has complete parity with the previous IQ for Visual Studio 2019 plugin. Expanded and new features found only in this version are listed in the [Supported Features](#UUID-1fc0d7bd-e256-aa57-6c48-8ef4c6af749b_id_SonatypeforVisualStudio2022-SupportedFeatures) section.

### Release Notes

[https://sonatype.github.io/visual-studio-2022-extension/CHANGELOG](https://sonatype.github.io/visual-studio-2022-extension/CHANGELOG)

### Compatibility

[https://sonatype.github.io/visual-studio-2022-extension/compatibility](https://sonatype.github.io/visual-studio-2022-extension/compatibility)

### Requirements

### Installing Sonatype for Visual Studio 2022

IQ for Visual Studio 2022 can be installed from within Visual Studio using the Extensions Manager or [via the Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=SonatypeIntegrations.SONADEV-VS2022) .

### Opening Sonatype for Visual Studio 2022

You can access the extension by navigating the menu for *View -> Other Windows -> Sonatype*

### Configuring Sonatype for Visual Studio 2022

The Sonatype IQ options are available from within the Visual Studio options dialog.

### Using Sonatype for Visual Studio 2022

The Sonatype for Visual Studio tool window is accessed by clicking the Sonatype Developer tab on the bottom tool strip of Visual Studio. It is also available in View under Other Windows.

Once configured and the component analysis is completed, a component view will be displayed. Component versions and details are available by clicking on the component name in the Component list.

![181764261.png](/assets/images/uuid-f0a4f240-1eb3-7f14-0deb-bd97af1a28f7.png)

Review the Component Info View for details on the returned Policy Threat levels.

## Sonatype for VS Code

Sonatype for VS Code extension allows you to surface and remediate issues in your workspace dependencies, a true Shift Left in application security for development teams.

The Sonatype for VS Code extension is available on the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=SonatypeIntegrations.iq-vscode-plugin) .

### Supported Languages and Ecosystems

- Java (Maven and Gradle)
- JavaScript (npm, pnpm, and Yarn)
- Go (Go modules)
- Python (Poetry, pip)
- Rust (Cargo)
- PHP (Composer)
- C (Conan (1.x only))
- CycloneDX (SBOM standard)

### Release Notes

[https://sonatype.github.io/iq-vscode-plugin/CHANGELOG](https://sonatype.github.io/iq-vscode-plugin/CHANGELOG)

### Compatibility

[https://sonatype.github.io/iq-vscode-plugin/compatibility](https://sonatype.github.io/iq-vscode-plugin/compatibility)

### Installing Sonatype for VS Code

Sonatype for VS Code can be installed from within VS Code using the Extensions Manager or via the [Microsoft Marketplace](https://marketplace.visualstudio.com/items?itemName=SonatypeIntegrations.iq-vscode-plugin) . The extension can be run in local VS Code, VS Code hosted in GitHub Codespaces, and supports Visual Studio Code Dev Containers as well as WSL2.

### Configuring Sonatype for VS Code

At a minimum, the extension requires the IQ Server URL and the credentials to be set.

You can set up the URL and username by opening the extension settings in VS Code: *Settings > Extensions > Sonatype for VS Code*

The password can be entered in two ways:

- Open the command palette by pressing `Command + Shift + P` on Mac or `Control + Shift + P` on Windows, and then enter the `Sonatype: Set IQ Server Password` command after the `>` prefix. If you want to clear the stored password, you can use the `Sonatype: Clear IQ Server Password` command.
- You can also use the SONATYPE_IQ_PASSWORD environmental variable. This method requires the "Use Environment Variable for Password" checkbox to be selected in the extension settings. You might need to restart VS Code for the changes to be recognized.

![vscode-configuration.png](/assets/images/uuid-f5919b85-b574-8d45-5fc3-2256d3e10617.png)

In the extension settings, enter the Default Application ID before running the component analysis. This is required to use the appropriately scoped policy set for your application.

You can configure additional settings such as:

- Including or excluding development dependencies from the overall analysis.
- Parallelization - higher values mean the component analysis will be faster, but it requires more resources from VS Code; lower values mean the component analysis will be slower, but it will have less impact on VS Code's performance.
- Starting the Analysis on VS Code Startup for the opened workspace.
- Restricting the number of versions shown in the Version History view that are older than the version in use. Default is 10, but you can change it based on your preferences.

### Using Sonatype for VS Code

## Sonatype IQ CLI

The Sonatype IQ Command Line Interface (CLI) is the multi-tool for performing a Lifecycle Analysis. Evaluations of your applications are either run manually or automatically using the CLI in many environments.

### Release Notes

[https://sonatype.github.io/iq-cli/CHANGELOG](https://sonatype.github.io/iq-cli/CHANGELOG)

### Compatibility

[https://sonatype.github.io/iq-cli/compatibility](https://sonatype.github.io/iq-cli/compatibility)

**Note:** For detailed information on feature availability in each CLI version, please review the [IQ CLI Release Notes](#UUID-6b69b7b1-858f-e58a-e010-beb4fdff9cdf_section-idm234473287734977) . This will help you determine the precise CLI version required for your desired functionality.

### Getting started with the Sonatype IQ CLI

You will need to perform a few tasks to run a Lifecycle analysis using the CLI.

### CLI parameters

The path to the Sonatype CLI jar file or native binary.

Provide credentials in the following format: `username:password`

Delegate authentication to the JVM environment.

The PublicId for the application. When is enabled and the PublicId has not yet been used, a new application will be created.

The ID for the organization to which the application belongs. When automatic application creation is enabled and the application does not exist, it will be created under the organization having the provided organization ID.

See

The location of your Lifecycle server (e.g. [http://localhost:8070](http://localhost:8070) ).

Path to specific files, directory, or Docker image. Include one or more scan targets at the end of the command. See supported file formats in .

If present, Sonatype CLM for Maven-generated `module.xml` files are automatically evaluated only when they are located in the default directories (i.e., directly under either the `sonatype-clm` or `nexus-iq` directory). To ensure a successful scan, the Maven plugin’s generated `module.xml` files must remain in their default locations.

### Evaluation results

When the Sonatype CLI evaluation succeeds, the output includes a summary and a link to the scan report. If the target IQ server supports priorities URLs (with both `developmentDashboardEnabled` and `prioritizedFindingsReportEnabled` set), a link to the priorities URL is also provided.

```
[INFO] Policy Action: Warning
[INFO] Summary of policy violations: 4 critical, 85 severe, 46 moderate
[INFO] The detailed report can be viewed online at http://localhost:8070/ui/links/application/my-app/report/95c4c14e
[INFO] The application priorities can be viewed online at http://localhost:8070/ui/links/developer/priorities/my-app/95c4c14e/cli
```

### Reachability Analysis with Sonatype CLI

You can configure Sonatype CLI to perform [Reachability Analysis](#UUID-bffb3d6e-1a0b-5607-518a-3dcdc88508c2) , which can detect method signatures in your application code that contain components with potentially exploitable security vulnerabilities. Policy violations occurring due to these vulnerable components are labeled as `Reachable` and can be viewed on the application report.

**Note:** Supported Languages [Reachability Analysis](#UUID-bffb3d6e-1a0b-5607-518a-3dcdc88508c2) currently supports Java only.

By including [an additional parameter in the CLI command](#UUID-6b69b7b1-858f-e58a-e010-beb4fdff9cdf_section-idm4591846617011234159137652215) you can enable the Reachability Analysis feature. The scan process will then analyze all application and dependency Java (or any JVM language) binaries located in the scan target. This allows you to detect reachable vulnerabilities, even in proprietary components within your application.

Reachability Analysis requires a JVM CLI and does not work with native CLI installations.

### Sonatype IQ CLI Binaries

The CLI binary versions are a drop-in replacement for the Java version without the Java runtime environment (JRE) requirements. The parameters are the same as the Java CLI versions with the addition of Secure Sockets Layer (SSL) customizations.

**Note:** The native Mac OSX CLI has been sunset and will receive only critical bug and security fixes until June 10th, 2025. After this date, it will no longer be supported. The native Linux and Windows CLI have been sunset and will receive only critical bug and security fixes until September 14, 2025. After this date, they will no longer be supported. For the latest features and full support, [switch to our cross-platform Java CLI with bundled JDK](#UUID-4e396b62-fd65-1cfc-dd99-2fb0a20e7b36_section-idm234690697763901) .

### Sonatype IQ CLI With Bundled JDK

### Passing CLI parameters from a file

One or more text files may be used to pass some or all the parameters to the CLI. The `@` prefix is used followed by the name of the file in the command. The file uses the JVM's default character encoding however file matching or globbing is not supported.

- Add parameters and values as separate lines.
- Both short and long parameter names are supported.
- File paths are relative to the current process. Absolute file paths are supported. Include multiple paths as separate lines.

Example command

```
java -jar ./nexus-iq-cli*.jar @cli-params.txt
```

Example cli-params.txt

```
-i 
Test123 
-a 
username:password 
-s
http://localhost:8070 
-t 
build 
./sample-application.zip
```

### Example Scan Result File

Using the `--result-file` parameter creates a file with evaluation results in the following format.

```
{
    "applicationId" : "...",
    "scanId" : "...",
    "reportHtmlUrl" : "http://...",
    "reportPdfUrl" : "http://.../pdf",
    "reportDataUrl" : "http://.../raw",
    "policyAction" : "None",
    "policyEvaluationResult" : {
        "alerts" : [...detailed list of components which caused the violation...],
        "affectedComponentCount" : 15,
        "criticalComponentCount" : 4,
        "severeComponentCount" : 65,
        "moderateComponentCount" : 36,
        "criticalPolicyViolationCount" : 4,
        "severePolicyViolationCount" : 85,
        "moderatePolicyViolationCount" : 46,
        "grandfatheredPolicyViolationCount" : 0,
        "legacyViolationCount" : 0
     }
}
```

**** - is the application in IQ Server against which you run policy evaluation

**** - can be used in some rest api

** - report with policy evaluation results in different formats

**** - policy evaluation outcome (can be None, Warn, Fail)

**** - contains a summary of the evaluation:

**** - contains information about components that caused a policy violation

**** - number of components that caused a policy violation

**** - number of critical components that caused a policy violation

**** - number of severe components that caused a policy violation

**** - the number of moderate components which caused a policy violation

**** - number of critical policies that were violated

**** - number of severe policies that were violated

**** - number of moderate policies that were violated

**** - number of policies that were violated, but moved to grandfathered

**** - number of legacy policy violations

### Using Automatic application creation with the CLI

When automatic application creation is enabled, Lifecycle creates new applications when the passed applicationId is not found. This is recommended for first-time evaluation of new applications.

The automatic application creation feature creates a new application under the organization that is configured. To create an application under a different organization, you can specify the `organization-id` as an input parameter.

**Note:** The CLI evaluation will error when providing an organization ID that does not match the organization the application belongs to in the Lifecycle server. This prevents accidental misconfigurations where scans are made to the wrong application; corrupting the evaluation history.

### Using the Sonatype CLI with a CI Server

In your continuous integration (CI) server, identify the location for adding a build step that includes processing a simple shell script during the build stage.

Execute a script call to the Sonatype CLI using the following syntax, from that location:

```
java -jar [ScannerJar] \
  -i [AppID] \
  -e [IgnoreSystemErrors] \
  -w [FailOnPolicyWarning] \
  -s [ServerURL] \
  -a [username:password] \
  [Target]
```

Given a typical setup, your syntax, including all available options, will likely look similar to the following:

```
java -jar nexus-iq-cli*.jar \
  -a username:password \
  -i tester123 \
  -s http://localhost:8070 \
  ./target/sample-app.war
```

When your application is built, the build step you have added will call the Sonatype CLI, evaluate your application, and upload the results of the evaluation to the IQ Server. By default, this will be placed below the build column in the Reports and Application area on the IQ Server, for your application.

**Note:** We recommend using a separate application identifier for each of your applications. Using the same application identifier will result in report results being overwritten each time an application is built.

### CLI error messages

The resulting file contains a log of errors that occurred during the policy evaluation in the following format:

```
{
    "errorMessage" : "<some error message>",
    "isSystemError" : <true or false>
}
```

errorMessage - a test of the error message that happened during the CLI run

isSystemError - an indicator of whether it is a system or configuration error

Error examples:

1. User has provided the wrong application ID (this is a configuration error, i.e. "isSystemError" is false)

```
{
    "errorMessage" : "The application ID testapp02 is invalid.",
    "isSystemError" : false
}
```

2. IQ Server is down (this is a system error, i.e. "isSystemError" is true)

```
{
    "errorMessage" : "The IQ Server http://localhost:8070 could not be contacted: Unknown host: localhost: nodename nor servname provided, or not known",
    "isSystemError" : true
}
```

## Sonatype Container Deployment - Lifecycle

Sonatype provides templates and Docker images for the following cloud providers and tools.

### Docker Hub

Docker images are available on Docker Hub and are delivered from an associated GitHub repository.

- [Docker Hub sonatype/nexus-iq-server](https://hub.docker.com/r/sonatype/nexus-iq-server/)
- [GitHub sonatype/docker-nexus-iq-server](https://github.com/sonatype/docker-nexus-iq-server)

### Helm Charts for Kubernetes

Helm charts are available at Helm Hub.

- [Helm Chart for Sonatype IQ Server](https://hub.helm.sh/charts/sonatype/nexus-iq-server)

### Red Hat OpenShift

Certified containers are available through the Red Hat Container Catalog.

- [RHCC for Sonatype IQ Server](https://catalog.redhat.com/software/containers/sonatype/nexus-iq-server/5e5d8063ac3db90370816c66)

Kubernetes Operators are available in the OpenShift OperatorHub for installing servers into OpenShift. Search inside your running OpenShift cluster's Operator Hub to find them.

- [Operator for Sonatype IQ Server](https://catalog.redhat.com/software/containers/sonatype/nxiq-operator-certified/5ea31b80ecb5246c0903c602)

New operators are released quarterly.

### Iron Bank

Hardened containers are available through Iron Bank, a central repository of digitally signed container images accredited by the US Department of Defense (DoD).

- [Iron Bank for Sonatype IQ Server](https://repo1.dso.mil/dsop/sonatype/nexus-iq-server/nexus-iq-server)

## Sonatype Container Deployment - Nexus Repository

Sonatype provides templates and Docker images for the following cloud providers and tools.

### Docker Hub

Docker images are available on Docker Hub and are delivered from an associated GitHub repository.

Nexus Repository Manager

- [Docker Hub sonatype/nexus3](https://hub.docker.com/r/sonatype/nexus3/)
- [GitHub sonatype/docker-nexus3](https://github.com/sonatype/docker-nexus3)

### Helm Charts for Kubernetes

**Note:** A Helm Chart ( [GitHub](https://github.com/sonatype/nxrm3-ha-repository/tree/main/nxrm-ha) , [ArtifactHub](https://artifacthub.io/packages/helm/sonatype/nxrm-ha) ) is available for our resiliency and high-availability deployment options. Be sure to read the deployment instructions in the [associated README file](https://github.com/sonatype/nxrm3-ha-repository/blob/main/nxrm-ha/README.md) before using the chart.

### Red Hat OpenShift

**Note:** As explained in our [Feature Sunsetting documentation](#UUID-910de0dd-dc88-616d-2d71-ef2843018cc9) , Sonatype does not recommend using the OrientDB container/operator due to data corruption risks when running the embedded OrientDB database inside container orchestration (Kubernetes, OpenShift). The container/operator for OrientDB deployments will be officially sunset on December 15, 2023. At the links below, the OrientDB container/operator is called "Nexus Repository Certified Operator" and "Nexus Repository Certified Operator Bundle." This notice and the official sunset only apply to these two items. **The "Nexus Repository HA Certified Operator" and "Nexus Repository HA Certified Operator Bundle" are new, work with a PostgreSQL database, and will continue to be supported and maintained.**

Certified containers are available through the Red Hat Container Catalog.

- [RHCC for Sonatype Nexus Repository](https://catalog.redhat.com/software/container-stacks/detail/62f4199c2eb63f74c2bff1cc)

Kubernetes Operators are available in the OpenShift OperatorHub for installing servers into OpenShift. Search inside your running OpenShift cluster's Operator Hub to find them.

- [Operator for Sonatype Nexus Repository](https://catalog.redhat.com/software/container-stacks/detail/62fe81a9059b5d754ae0198b)

### Mesosphere DC/OS

Sonatype Nexus Repository is offered through the Mesosphere DC/OS Universe

This offering is available through the DC/OS user interface. The templates are available via [mesosphere/universe](https://github.com/mesosphere/universe/tree/version-3.x/repo/packages/N/nexus) .

### Iron Bank

Hardened containers are available through Iron Bank, a central repository of digitally signed container images accredited by the US Department of Defense (DoD).

- [Iron Bank for Nexus Repository](https://repo1.dso.mil/dsop/sonatype/nexus/nexus)

## Sonatype for SCM

Source Control Management (SCM) systems are no strangers to development teams. Platforms such as GitHub, GitLab, and Bitbucket store and manage organizations' code repositories. As members of development teams make changes to code, the SCM system tracks the resulting iterations, reports any conflicts between those iterations, and maintains a complete history of the code, which is helpful in case any previous version needs to be reinstated. This makes SCM systems a vital part of the software development process.

Sonatype for SCM is a tool the provides early insight into an application's security and licensing risk by analyzing the open source referenced in the code. It is designed to work *directly within* your SCM. This is essentially like posting a security guard inside the bank vault rather than outside the bank building. Our Source Control Integration works with in tandem with our Continuous Integration system integrations to give you policy information in the tools your team uses every day. If a component violates a policy that the organization has set, Lifecycle takes action not only to communicate its findings but also to generate suggested remediation directly into the source code repository by initiating such things as automated commit feedback, automated pull requests, and pull request commenting with the changes to an application's component manifest. Sonatype IQ Server interacts with Git-based systems primarily through an API. The APIs enable the creation of pull requests, commenting on pull requests, creation of commit statuses, etc.

### Sonatype for SCM's two main features

- **Easy SCM Onboarding** – A tool to help you import the repositories housed in your SCM systems that you wish to integrate with Sonatype IQ so that they can be recreated as Lifecycle applications. Once this step is complete, Sonatype IQ scans the newly imported applications via the **Instant Risk Profile** to offer a one-time, initial glimpse of your applications' risk based on what has been committed to your SCM system up to that point. This helps your development team know what applications to prioritize when subsequently establishing your remediation plan.
- **Automated source control feedback** – This aspect of Sonatype for SCM, in essence, is the ways in which Sonatype IQ communicates what it has found and what it suggests in terms of action taken to remediate any concerns in the SCM system repositories. To achieve this, Sonatype IQ Server uses automated commit feedback, automated pull requests, and pull request commenting to report its scan results. The specific features available to you depend upon which SCM system you use since each system has different configuration capabilities with Sonatype integration.

### Getting Started

To use Sonatype for SCM, your IQ Server must be configured to allow access to your company's SCM platform. To begin, you'll need to connect Sonatype IQ to your SCM system repositories, which is best done by following the steps in [Easy SCM Onboarding](#UUID-152e68ac-3e1e-2038-45a3-f8fbc16ab7e4) . Following that, you will need to set up your source control configuration.

### End Goal

By the end of this documentation, you will be able to connect and configure your SCM system to work with Sonatype IQ so that it can begin monitoring your code for anything suspicious and communicate with you accordingly.

### Source Control Configuration

### Easy SCM Onboarding

### Automated Source Control Feedback

### Policy Evaluation with Nexus IQ for SCM

Assuming you have properly associated IQ Server with your SCM system repository, IQ Server will first look to see if there is a commit hash. If there is, it will add a commit status within the SCM system repository. It will then look to see if there is an existing feature branch in your SCM system repository and, if so, see whether there is at least one pull request for it. If there is such a pull request, it will then determine whether there are any new or resolved policy violations and either create or update pull request comments (or pull request line comments) within your SCM system. If there are new violations to remediate, IQ Server will create a remediation pull request and send it to your SCM system.

![137200131.png](/assets/images/uuid-0578939f-e083-c3f4-e845-bd6efecead7f.png)

### CI and CLI Integrations

Sonatype Lifecycle supports several CLI and CI integrations with its [SCM Integration](#UUID-32a5d718-bd65-9f34-bba7-704ac47a7a54) .

### Bitbucket Code Insights

Lifecycle creates code insight reports in Bitbucket based on the evaluation of your configured default branch and a feature branch with an open Pull Request. This is accomplished by comparing the policy evaluation report of the pull request's source branch with:

- the latest policy evaluation report for the common ancestor commit between the pull request's source and target branches, if such report exists, or
- the latest policy evaluation report for the pull request's base commit, which is the head commit of the pull request's target branch at the moment the pull request was created, if such report exists, or
- the latest available policy evaluation report for the source control configured default branch.

Learn about [Bitbucket's Code Insights](https://confluence.atlassian.com/bitbucketserver/code-insights-966660485.html) from the Atlassian support site.

### Policy Evaluation in Source Control Management

Lifecycle for Source Control Management (SCM) is a set of features that lets developers gain early insight into code changes by working in tandem with continuous integration to push policy information about an application’s components directly into their SCM.

Lifecycle for SCM has the following features:

- **Automated commit feedback** : Lifecycle for SCM puts the information needed to quickly remediate vulnerabilities in software solutions at the fingertips of developers by pushing policy evaluation information into SCM commits and pull requests (PRs), where developers work.
- **Automated pull requests** : Lifecycle for SCM will automatically create pull requests for policy violations on components that have an available version that remediates those violations.
- **Pull request commenting** : Lifecycle for SCM adds a comment to pull requests for repositories configured for source control when the PR introduces a new policy violation.

## Java Runtime Agent (Experimental)

The **Java Runtime Agent** detects vulnerable Java methods or classes loaded during runtime to enhance the priority of policy remediation.

Vulnerable components are labeled when the vulnerable classes are loaded and when the vulnerable methods are called during your integration test coverage as part of your build.

Lifecycle policy uses the labels to prioritize the risk found in open-source components by lowering the threat level when not directly referenced by your application during runtime.

Developers better manage their open-source workload with fewer false critical violations and broken builds.

⚠️ **Warning:** This is an experimental feature that will change in the future. We do not know the performance impact of running this tool against the Lifecycle at any scale. We insist that this is not run on production environments until this functionality has been hardened. For assistance or to provide feedback with this experimental feature, contact our [data-insights-pm@sonatype.com](mailto:data-insights-pm@sonatype.com)

### How it works

The Java Runtime Agent detects class loading and calls to vulnerable methods then notifies the Lifecycle server using components labels.

- The agent detects the loading of a vulnerable method and notifies Lifecycle
- The agent also detects and labels when the classes are loaded
- The agent labels all components in the application bill of material with a runtime-enabled label
- Lifecycle policy constraints will make judgments on these labels in combination with other risk data

For applications with thorough test coverage, every method and class from the open-source components are labeled as being loaded and/or called. Vulnerable methods or classes that are not referenced in the application are deprioritized as less risk.

Learn more about [Java Instrumentation and Java Agents](https://www.baeldung.com/java-instrumentation)

### Prerequisites for using Java Runtime Agent

- Run the Java Runtime Agent on a non-production server. The agent injects bytecode to intercept calls to vulnerable methods, with minimal impact.
- The Lifecycle server must be accessible to the system where the Java Runtime Agent is running
- The runtime agent depends on Java 17
- The application ID and user access will need to be in the Lifecycle server
- Component labels and policy constraints should be configured before running the agent
- User tokens and token passwords are recommended

### Steps to use the Java Runtime Agent

- Download the Java Runtime Agent: [runtime-agent-1.0.10.jar](https://github.com/sonatype-nexus-community/iq-api-examples/blob/main/iq-reference-policy/java-runtime-example/runtime-agent-1.0.10.jar)
- Create component labels and update policies with the runtime prioritization The Java Runtime Agent uses component labels to trigger custom policies depending on when methods and classes are loaded from vulnerable components.
- Add the agent at the root of the project to run during your test coverage build The jar must be placed in the classpath of the client’s application and run with the Java agent JVM option. The agent is configured using either JVM system properties or environment variables.
- View the Report Go to the application report in Lifecycle. Components found by the agent have labels indicating if the classes are loaded and if the vulnerable method signatures are loaded and/or called.

### Runtime Java Agent custom policy configuration

The runtime agent uses a custom set of policies to prioritize security vulnerabilities based on the component labels applied to the components during the evaluation. These policies may be loaded using a sample policy set or manually created using the tables below as a reference.

Once you configure the policies and labels, the runtime agent uses them in the following workflow.

- The runtime agent applies the `Runtime-Enabled` label to components. The standard security policies are modified to not trigger when the component has this label. The standard security policies are used when the application is not scanned with the runtime agent.
- The `Runtime-Method-Called` label is added when the vulnerable method is called during runtime. This triggers the security policies that the vulnerability has been `Security-Confirmed` . The vulnerability keeps the designated threat level.
- The `Runtime-Class-Loaded` label is added when the vulnerable class is loaded during runtime. If the `Runtime-Method-Loaded` label is not added, then the `Security-Partial-Confirmed` policies is triggered to identify potential risk. This happens when the vulnerable method is not known at the time.
- When either the class is not loaded or both the class and methods are loaded but the method is not called, then the violation triggers the `Security-Downgrade` policy to indicate that the application is not at risk do to the vulnerability.

### Runtime Java Agent with Spring’s Pet Clinic

This demo simulates vulnerable method calls to show what the runtime agent can do. This example uses a public folk of the maven project [spring pet clinic](https://github.com/spring-projects/spring-petclinic) to include the agent during integration tests. The steps may be duplicated for other Java projects.

Follow the prerequisites and steps above to prepare your Lifecycle server.

- Clone the demo repository for [spring-petclinic-runtime-agent](https://github.com/navaneeth-mysore-sonatype/spring-petclinic-runtime-agent)
- Copy the runtime agent to the level up of the path of the project or adjust the agent config below
- Update the project `pom.xml` Set the [maven plugin](#UUID-433e090b-af9e-c63f-5963-c61a3a5f9729) configuration in the pom `<properties>` section Add/update the following from [lines 19-22](https://github.com/navaneeth-mysore-sonatype/spring-petclinic-runtime-agent/blob/main/pom.xml#L19) in the pom.xml The maven plugin is added to the plugins section starting at [line 157](https://github.com/navaneeth-mysore-sonatype/spring-petclinic-runtime-agent/blob/main/pom.xml#L157) . This project uses the artifactId `spring-petclinic-runtime-agent` as the applicationId to use in the Lifecycle analysis. This application should be added before running the demo. The runtime agent is added to the configuration at [line 190](https://github.com/navaneeth-mysore-sonatype/spring-petclinic-runtime-agent/blob/main/pom.xml#L190) for the `maven-surefire-plugin` which is used for unit tests in this project. Update the plugin version and Lifecycle server in this section. Credentials should be passed as environment variables. NOTE: the `-Dsonatype.runtime.agent.runtimeEnabledLabel=true` may need to be added to the configuration if not present. This is used to set the `Runtime-Enabled` label on all components.
- Set the [maven plugin](#UUID-433e090b-af9e-c63f-5963-c61a3a5f9729) configuration in the pom `<properties>` section Add/update the following from [lines 19-22](https://github.com/navaneeth-mysore-sonatype/spring-petclinic-runtime-agent/blob/main/pom.xml#L19) in the pom.xml The maven plugin is added to the plugins section starting at [line 157](https://github.com/navaneeth-mysore-sonatype/spring-petclinic-runtime-agent/blob/main/pom.xml#L157) . This project uses the artifactId `spring-petclinic-runtime-agent` as the applicationId to use in the Lifecycle analysis. This application should be added before running the demo.
- The runtime agent is added to the configuration at [line 190](https://github.com/navaneeth-mysore-sonatype/spring-petclinic-runtime-agent/blob/main/pom.xml#L190) for the `maven-surefire-plugin` which is used for unit tests in this project. Update the plugin version and Lifecycle server in this section. Credentials should be passed as environment variables. NOTE: the `-Dsonatype.runtime.agent.runtimeEnabledLabel=true` may need to be added to the configuration if not present. This is used to set the `Runtime-Enabled` label on all components.
- Update your local maven `${HOME}/.m2/settings.xml` with the clm.serverId property.
- Set environment variable for Lifecycle server authentication
- Run the agent with integration tests
- Confirm components have been labeled in the Lifecycle report The following components should have been discovered as part of the test coverage and labeled by the runtime agent.

### Samples for Running the Agent

### Reference JVM system properties

### Reference Environment Variables

### Reference Component Labels

The following Component Labels are used to flag components loaded and called by the runtime agent. See [Component Labels](#UUID-d2a72712-e91d-bd83-a78c-b89fdeab64ae) to add component labels to the Lifecycle instance.

### Reference Policies

The following Policies are used to prioritize the security risk found by the runtime agent.

## Integrations Capability Matrix

Our developers are continuously improving and adding new capabilities to Lifecycle integrations. As they develop new capabilities, they are rolled out to the various platforms and deployment options. This document maps which features are currently available with which deployment. If you do not see the supported feature you expect, please submit your request through the [ideas.sonatype.com](https://ideas.sonatype.com) portal.

Integrations to Lifecycle require a license, while Lifecycle integrations with Nexus Repository require a Sonatype Lifecycle or Repository Firewall license and a Nexus Repository Pro license.

The following summarizes our current integration offerings with leading DevOps toolchain applications and technology stacks.

### CI/CD Systems

**Legend:** = Supported, = Not Tested, = Community

### Source Control Management (SCM)

**Legend:** = Supported, = Not Tested

### IDE Integration

**Legend:** = Supported

### Package / Build Tools

**Legend:** = Supported, = Community

### Ticketing Systems

**Legend:** = Supported

-- Icons made by [Alfredo Hernandez](https://www.flaticon.com/authors/alfredo-hernandez) from [Flaticon](https://www.flaticon.com/)

## IQ for Visual Studio 2019

**Note:** **You're looking at a page for an extension that has been sunset.** For the latest supported Visual Studio integration, see [Sonatype for Visual Studio 2022](#UUID-1fc0d7bd-e256-aa57-6c48-8ef4c6af749b) .

### Compatibility

This extension works with VS 2015, VS 2017, and VS 2019 on Windows and Linux (if your Visual Studio can run on Linux using other extensions or plugins.)

It is not supported for Visual Studio on macOS.

### Installing IQ for Visual Studio

IQ for Visual Studio can be installed from within Visual Studio using the Extensions Manager or [via the Microsoft Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=SonatypeIntegrations.NexusIQforVisualStudio) .

### Configuring IQ for Visual Studio

### Using IQ for Visual Studio

The IQ for Visual Studio tool window can be accessed by clicking the Nexus IQ tab on the bottom tool strip of Visual Studio. If not accessible from there, it should also be available in View under Other Windows. Once configured and the component analysis is completed, a component view will look similar to the example displayed below. Component details are available by double-clicking on the component name in the Component list or via the View Details button in the component view once you have selected a component.

![180813912.png](/assets/images/uuid-f872a1ab-bcc4-a174-5661-11f9d75cf8a0.png)

If you have selected a component with some threats (as above), you can select other versions in the Version Graph and then the View Details to find remediation options. Alternatively, IQ may present a recommended version that you can select and which will update the version graph.

![180813913.png](/assets/images/uuid-bbcc192c-aa09-8419-d00d-fb9aac38446b.png)

When you select one of the recommended version links, or if you click on any of the versions in the Version Graph, the "Migrate to Selected" button will become enabled.

![180813914.png](/assets/images/uuid-6063f6d5-0f3f-17b6-1598-ea8dcf3a5562.png)

Clicking this button will update all projects where this component was present and migrate to the version you selected.
