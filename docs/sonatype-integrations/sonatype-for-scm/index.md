---
layout: default
title: "Sonatype for SCM"
parent: Sonatype Integrations
nav_order: 22
has_children: true
---

# Sonatype for SCM

Source Control Management (SCM) systems are no strangers to development teams. Platforms such as GitHub, GitLab, and Bitbucket store and manage organizations' code repositories. As members of development teams make changes to code, the SCM system tracks the resulting iterations, reports any conflicts between those iterations, and maintains a complete history of the code, which is helpful in case any previous version needs to be reinstated. This makes SCM systems a vital part of the software development process.

Sonatype for SCM is a tool the provides early insight into an application's security and licensing risk by analyzing the open source referenced in the code. It is designed to work *directly within* your SCM. This is essentially like posting a security guard inside the bank vault rather than outside the bank building. Our Source Control Integration works with in tandem with our Continuous Integration system integrations to give you policy information in the tools your team uses every day. If a component violates a policy that the organization has set, Lifecycle takes action not only to communicate its findings but also to generate suggested remediation directly into the source code repository by initiating such things as automated commit feedback, automated pull requests, and pull request commenting with the changes to an application's component manifest. Sonatype IQ Server interacts with Git-based systems primarily through an API. The APIs enable the creation of pull requests, commenting on pull requests, creation of commit statuses, etc.

## Sonatype for SCM's two main features

- **Easy SCM Onboarding** – A tool to help you import the repositories housed in your SCM systems that you wish to integrate with Sonatype IQ so that they can be recreated as Lifecycle applications. Once this step is complete, Sonatype IQ scans the newly imported applications via the **Instant Risk Profile** to offer a one-time, initial glimpse of your applications' risk based on what has been committed to your SCM system up to that point. This helps your development team know what applications to prioritize when subsequently establishing your remediation plan.
- **Automated source control feedback** – This aspect of Sonatype for SCM, in essence, is the ways in which Sonatype IQ communicates what it has found and what it suggests in terms of action taken to remediate any concerns in the SCM system repositories. To achieve this, Sonatype IQ Server uses automated commit feedback, automated pull requests, and pull request commenting to report its scan results. The specific features available to you depend upon which SCM system you use since each system has different configuration capabilities with Sonatype integration.

## Getting Started

To use Sonatype for SCM, your IQ Server must be configured to allow access to your company's SCM platform. To begin, you'll need to connect Sonatype IQ to your SCM system repositories, which is best done by following the steps in [Easy SCM Onboarding](#UUID-152e68ac-3e1e-2038-45a3-f8fbc16ab7e4) . Following that, you will need to set up your source control configuration.

## End Goal

By the end of this documentation, you will be able to connect and configure your SCM system to work with Sonatype IQ so that it can begin monitoring your code for anything suspicious and communicate with you accordingly.

## Source Control Configuration

Sonatype Lifecycle can connect to your Source Control Management (SCM) system with an access token to scan your projects during the development phase. The access token can be set at the Root Organization level. This page provides the configuration steps for SCM.

**Note:** The must be configured for Source Control Features to function.

### SCM Feature Configuration

The table below shows where the SCM feature is configured.

### Create Access Token

Select your SCM provider below for information on creating an access token and configuring your SCM System for use with Sonatype Lifecycle.

### SCM Features Technical Overview

### GitHub Configuration

### GitLab Configuration

### Bitbucket Configuration

### Bitbucket Cloud Configuration

### Azure DevOps Configuration

### IQ Server Configuration

The IQ Server configuration options allow you to enable and disable the SCM Integration features. This setup consists of the following parts:

- Base URL Configuration
- Git Client Configuration (optional)
- Connect IQ Server to SCM system
- Testing Your Configuration

You can use Secure Shell (SSH) for Git operations such as clone, fetch, and push.

Note that the term "pull request" is equivalent to "merge request" used in GitLab terminology.

### Sparse Checkout File Types

The following file types are checked out when sparse checkout is enabled in your SCM for IQ settings.

**Note:** Sparse checkout is only available when the native git client is enabled. See [Nexus IQ Server Configuration](#UUID-f3b4500c-ca79-40f7-37ec-428d70e9d8a7) for more information.

```
alpine.txt
bom.xml
bower.json
Cargo.lock
clair-scanner-output.json
Podfile.lock
conanfile.txt
conaninfo.txt
conanfile.py
conda.txt
cran-installed.packages
debian-packages.txt
drupal-components.csv
go.list
Gopkg.lock
go.sum
package.json
package-lock.json
npm-shrinkwrap.json
pom.xml
build.gradle
composer.lock
pnpm-lock.yaml
requirements.txt
poetry.lock
Gemfile.lock
yarn.lock
packages.config
yum-packages.txt
Package.resolved
*.csproj
*.tfplan
*.aar
*.ear
*.har
*.hpi
*.jar
*.mar
*.nbm
*.nupkg
*.rar
*.sar
*.tar
*.tar.bz2
*.tar.gz
*.tar.xz
*.tb2
*.tbz
*.tgz
*.txz
*.war
*.whl
*.wsr
*.zip
*.dll
*.gem
*.js
*.rpm
gradle.properties
go.mod
```

## Easy SCM Onboarding

Easy SCM Onboarding is a tool whose primary purpose is to import the applications housed in your SCM system repositories and turn them into applications in Lifecycle. This integration enables *Sonatype Lifecycle* to scan and evaluate your organization's applications directly from the source control without modifying any code or continuous integration (CI) build processes.

Once your applications are set up in Lifecycle, Easy SCM Onboarding scans the applications via the [Instant Risk Profile](#UUID-9bc16c19-db96-b9f4-5f20-fb5b970d7075) to give you an immediate, baseline glimpse of your applications' risk. This enables rapid visibility into open-source risks for critical applications and helps your team prioritize remediation efforts. This is done without having to manually scan or add Lifecycle to your build process.

**Note:** It is important to understand that Easy SCM Onboarding is a useful, **initial** tool to help you get started with scanning and accelerate adoption; however, it is just that – *initial* . It **only initially scans what has been committed to your SCM system** (i.e. manifests) and, therefore, **does not provide a full analysis that comes from accessing the advanced binary fingerprinting** .

In fact, performing a full analysis produces noticeably different results for the same project. Therefore, we recommend that you strive toward integrating Lifecycle with your **continuous integration (CI)** and **command line interface (CLI)** **pipeline** for fine-grained scan control and binary analysis, which ensures the highest-quality scan results.

### Prerequisites

To use Easy SCM Onboarding, you'll need to do the following:

- Ensure your SCM system resources are adequate for the new applications.
- Obtain an access token for your SCM system to connect to your IQ organization. We recommend setting the token in the Root Organization.

### Automatically Assign Roles During Application Import

Easy SCM onboarding can also automatically assign roles to your GitHub users if you [configuring user mappings](#UUID-0af5b737-af38-5ec5-ea69-62d8211951d8_section-idm234646010084107) using the Source Control REST API before importing an application.

If user mappings for an organization in *Lifecycle* are available (assigned or inherited), Easy SCM onboarding will attempt to apply them to your GitHub users.

Note this feature currently only supports local and LDAP user accounts in IQ; you cannot use it with SAML or SSO-based IQ user accounts. It also only works with GitHub at this time.

### Using Easy SCM Onboarding

### Instant Risk Profile

### Continuous Risk Profile

Sonatype for SCM generates a continuous risk profile of the organization's codebase by running automatic application evaluations at the source stage. It uses the following capabilities to create a continuous risk profile:

## Automated Source Control Feedback

Sonatype Lifecycle provides policy violation information directly in your Source Control Management System. This lets developers find out about policy violations during the code development process.

The policy violation information includes policy evaluation summaries on new pull requests, comments on your pull requests, and opening new pull requests. Learn more about each feature below:

### Prerequisites

All features require the Lifecycle Application is [configured with an Access token and repository URL.](#UUID-161243f0-61ce-a164-d457-2bff696761b4)

The table below identifies where features can be enabled and disabled:

### Automated Commit Feedback

### Automated Pull Requests

### Automated PRs for InnerSource Components

This feature ensures that applications are always current with the latest compatible version of InnerSource components and benefit from the continuous improvements.

When a new non-major version of an InnerSource component is detected during evaluation of an application at the release stage, automated pull requests to update the older version of the InnerSource component are created in the SCM system.

**Note:** No Automated PRs for Policy Violations Automated PRs will not be created for policy violations related to InnerSource Components. They will only be created if a version change is detected.

### Pull Request Commenting

**Note:** This page uses the phrase "Pull Request," but in GitLab, the terminology is "Merge Request."

### Golden PR for GitHub

Sonatype IQ Server creates a **Pull Request (PR) comment** , if it is able to determine a Golden Version of the component that can remediate the policy violation.

The **Golden Version** of the component is defined as *recommended-non-breaking-with-dependencies* .

Sonatype IQ Server creates a Golden **Pull Request (PR)** automatically, if it is able to determine a Golden Version of the component that can remediate the policy violation. Refer to example 3 below.

**Examples:**

1. A top-level **Golden PR comment** for a Golden Version of a component will be seen as below. The version upgrade information indicates that bumping to a version will resolve all policy violations for this component (including its dependencies) and result in no breaking changes.

![Top_level_Github_comment.png](/docs-at-surgery-poc/assets/images/uuid-5ed70928-43ce-e902-6441-cfdab32ae287.png)

2. A **Golden PR line comment** will be seen as below. The Golden Version of the component is indicated by a gold star.

![Line_comment_golden.png](/docs-at-surgery-poc/assets/images/uuid-64295316-facb-d828-f09d-4b9056fd480a.png)

3. A **Golden PR** (indicated by a gold star,) will be created as below, indicating the suggested component version, i.e. Golden Version. This is a safe-to-use version with no breaking changes, no policy violations (including its dependencies) and can be used to remediate the policy violations.

![Github_Golden_PR.png](/docs-at-surgery-poc/assets/images/uuid-df8b0d0d-6b32-e3fd-871f-780df9cad923.png)

### Golden PR for GitLab

Sonatype IQ Server creates a **comment** if it is able to determine a **Golden Version** of the component that can remediate the policy violation.

The **Golden Version** of the component is defined as *recommended-non-breaking-with-dependencies* .

Sonatype IQ Server creates a Golden **Pull Request (PR)** automatically, if it is able to determine a Golden Version of the component that can remediate the policy violation. Refer to example 3 below.

**Examples:**

1. A top-level **Golden PR comment** for a Golden Version of a component will be seen as below. The version upgrade information indicates that bumping to a version will resolve all policy violations for this component (including its dependencies) and result in no breaking changes.

![Top_level_GitLab_comment.png](/docs-at-surgery-poc/assets/images/uuid-e032029b-41b7-d4aa-4aec-55d08603b4e4.png)

2. A **Golden PR line comment** will be seen as below. The Golden Version of the component is indicated by a gold star.

![GitLab_Golden_line_comment.png](/docs-at-surgery-poc/assets/images/uuid-39004e5a-f9bb-cb99-30f8-41d08d0e5879.png)

3. A **Golden PR** (indicated by a gold star,) will be created as below, indicating the suggested component version, i.e. Golden Version. This is a safe-to-use version with no breaking changes, no policy violations (including its dependencies) and can be used to remediate the policy violations.

![GitLab_Folden_PR.png](/docs-at-surgery-poc/assets/images/uuid-7f3874c6-1665-3627-a999-b7b6c521b487.png)

### Golden PR for Azure DevOps

Sonatype IQ Server creates a **Pull Request (PR) comment** , if it is able to determine a Golden Version of the component that can remediate the policy violation.

The **Golden Version** of the component is defined as *recommended-non-breaking-with-dependencies* .

Sonatype IQ Server creates a Golden **Pull Request (PR)** automatically, if it is able to determine a Golden Version of the component that can remediate the policy violation. Refer to example 3 below.

**Examples:**

1. A top-level **Golden PR comment** for a Golden Version of a component will be seen as below. The version upgrade information indicates that bumping to a version will resolve all policy violations for this component (including its dependencies) and result in no breaking changes.

![Azure_top_level_comment.png](/docs-at-surgery-poc/assets/images/uuid-8a483b90-55f8-5123-9416-46360878892e.png)

2. A **Golden PR line comment** will be seen as below. The Golden Version of the component is indicated by a gold star.

![Azure_line_comment.png](/docs-at-surgery-poc/assets/images/uuid-8793d199-dee3-415c-3482-5eccae4f62c7.png)

3. A **Golden PR** (indicated by a gold star,) will be created as below, indicating the suggested component version, i.e. Golden Version. This is a safe-to-use version with no breaking changes, no policy violations (including its dependencies) and can be used to remediate the policy violations.

![Azure_Golden_PR.png](/docs-at-surgery-poc/assets/images/uuid-df0a7ae4-9d99-ce1e-0659-907acf1d6e36.png)

### Golden PR for Bitbucket

Sonatype IQ Server creates a **comment** , if it is able to determine a Golden Version of the component that can remediate the policy violation.

The **Golden Version** of the component is defined as *recommended-non-breaking-with-dependencies* .

Sonatype IQ Server creates a Golden **Pull Request (PR)** automatically, if it is able to determine a Golden Version of the component that can remediate the policy violation. Refer to example 3 below.

**Examples:**

1. A top-level **Golden PR comment** for a Golden Version of a component will be seen as below. The version upgrade information indicates that bumping to a version will resolve all policy violations for this component (including its dependencies) and result in no breaking changes.

![BitBucket_Top_level_comment.png](/docs-at-surgery-poc/assets/images/uuid-2f862e52-29f3-c5a1-b6cb-7a355daeb306.png)

2. A **Golden PR line comment** will be seen as below. The Golden Version of the component is indicated by a gold star.

![BitBucket_line_comment.png](/docs-at-surgery-poc/assets/images/uuid-80246dbe-4138-bc29-a6c1-d36c10df4429.png)

3. A **Golden PR** (indicated by a gold star,) will be created as below, indicating the suggested component version, i.e. Golden Version. This is a safe-to-use version with no breaking changes, no policy violations (including its dependencies) and can be used to remediate the policy violations.

![Bitbucket_Golden_PR.png](/docs-at-surgery-poc/assets/images/uuid-4c1980db-cb40-c067-6611-2057ffb6492e.png)

## Policy Evaluation with Nexus IQ for SCM

Assuming you have properly associated IQ Server with your SCM system repository, IQ Server will first look to see if there is a commit hash. If there is, it will add a commit status within the SCM system repository. It will then look to see if there is an existing feature branch in your SCM system repository and, if so, see whether there is at least one pull request for it. If there is such a pull request, it will then determine whether there are any new or resolved policy violations and either create or update pull request comments (or pull request line comments) within your SCM system. If there are new violations to remediate, IQ Server will create a remediation pull request and send it to your SCM system.

![137200131.png](/docs-at-surgery-poc/assets/images/uuid-0578939f-e083-c3f4-e845-bd6efecead7f.png)

## CI and CLI Integrations

Sonatype Lifecycle supports several CLI and CI integrations with its [SCM Integration](#UUID-32a5d718-bd65-9f34-bba7-704ac47a7a54) .

### Sonatype CLI

Any application can be evaluated against your policies using the Sonatype CLI.

### Sonatype CLI Docker Image

The Sonatype CLI is also available as a docker image at [https://hub.docker.com/r/sonatype/nexus-iq-cli](https://hub.docker.com/r/sonatype/nexus-iq-cli) . The documentation there details how to use the image to perform an evaluation.

### Sonatype Platform Plugin for Jenkins

Sonatype Platform Plugin for Jenkins scans a build workspace for components, creates a summary file about all the components found, and then submits that file to the IQ Server for a detailed policy evaluation. Lifecycle generates a detailed analysis of security information, license information, and other policy details. A summary of that report is sent to the Jenkins server to include in the build results.

### Sonatype for GitLab CI

CI/CD pipeline jobs in GitLab use custom docker images to perform actions in GitLab project's build workspace. The GitLab Sonatype docker image provides the ability to run policy evaluations against build artifacts in GitLab. This produces a summary report with policy violation counts and a link to a detailed report on the IQ Server.

### Sonatype CLM for Maven

Any application can be evaluated against your policies using the Sonatype CLM for Maven Plugin.

### Sonatype for Bamboo

The Sonatype for Bamboo plugin lets you run policy evaluations against building artifacts in Bamboo. This produces a summary report with policy violation counts and a link to a detailed report on the IQ Server.

## Bitbucket Code Insights

Lifecycle creates code insight reports in Bitbucket based on the evaluation of your configured default branch and a feature branch with an open Pull Request. This is accomplished by comparing the policy evaluation report of the pull request's source branch with:

- the latest policy evaluation report for the common ancestor commit between the pull request's source and target branches, if such report exists, or
- the latest policy evaluation report for the pull request's base commit, which is the head commit of the pull request's target branch at the moment the pull request was created, if such report exists, or
- the latest available policy evaluation report for the source control configured default branch.

Learn about [Bitbucket's Code Insights](https://confluence.atlassian.com/bitbucketserver/code-insights-966660485.html) from the Atlassian support site.

### Prerequisites

Integrating Lifecycle with the Bitbucket Code Insights has prerequisites.

- Your IQ Server instance must be configured for Bitbucket SCM
- Bitbucket repo must have a default branch and a feature/development branch

### Code Insight Report Content

- A summary of the policy violation information generated by comparing the Pull Request branch with the default branch configured for a given Application.
- A link to the full report in your IQ Server.
- Each component that led to a policy violation and a synopsis of which policy has been violated and how.
- A link to the file and line number for violations which were introduced as a part of this Pull Request
- Annotations in the build file indicating the line which is causing the policy violation

## Policy Evaluation in Source Control Management

Lifecycle for Source Control Management (SCM) is a set of features that lets developers gain early insight into code changes by working in tandem with continuous integration to push policy information about an application’s components directly into their SCM.

Lifecycle for SCM has the following features:

- **Automated commit feedback** : Lifecycle for SCM puts the information needed to quickly remediate vulnerabilities in software solutions at the fingertips of developers by pushing policy evaluation information into SCM commits and pull requests (PRs), where developers work.
- **Automated pull requests** : Lifecycle for SCM will automatically create pull requests for policy violations on components that have an available version that remediates those violations.
- **Pull request commenting** : Lifecycle for SCM adds a comment to pull requests for repositories configured for source control when the PR introduces a new policy violation.

### Early Feedback and Automation

In today’s software development lifecycle (SDLC), developers are asked to release complex software at an increasingly faster pace. Because of this, devs are relying more and more on OSS, utilizing openly available, popular components rather than writing unique code. Consequently, [Sonatype’s State of the Software Supply Chain](https://www.sonatype.com/resources/state-of-the-software-supply-chain-2021) found that open-source software (OSS) components make up more than 80% of most modern applications. With this, the traditional capacity of a developer simply writing code has shifted to a holistic role that includes assembling and integrating code that supports both your software and business operations.

While assembling code, developers often use source control management systems, like GitHub, GitLab, and Bitbucket. SCMs are often the first place where a piece of code gets shared and reviewed by both humans and machines. Lifecycle for SCM uses Lifecycle to establish a relevant policy configuration. Scan evaluations in SCM are run against that policy configuration so that as developers build applications, they receive accurate and timely information to take action on reported violations.

The main value of SCM systems is their ease of collaboration. Developers are able to push quality control of their application development to a source control platform, where this collaboration exists in code reviews that contain both commits and pull requests.

Building on this, Lifecycle for SCM provides suggested remediations for policy violations directly into the source control repository. We do this by automatically creating pull requests with the changes to an application’s component manifest. Using this type of early feedback and automation, we reduce rework and keep development teams focused on contributing business value rather than managing application component risk.

### How Lifecycle for SCM Works

To use Lifecycle for SCM, you first need to configure the IQ Server to allow access to your company’s Source Control Management platform. For large organizations, we recommend enabling automatic source control which lets CI and CLI integrations configure application source control connections when running from a locally cloned repository (a common practice in CI systems).

Once configured, commits will immediately receive automated commit feedback. If enabled and appropriately configured, applications will also start seeing automated pull requests for any new policy violation with suggested remediation, and pull request comments that detail the summary of violations, affected components, and a description of the violations that were introduced in the PR.

A Continuous Integration system or build agent is required for these features to work. For example, if Jenkins is pulling and running the scan, Lifecycle can pick up the source control context and use that as a source. This eases control and gets policy information closer to developers.

We suggest using CI against all feature branches in your SCM, letting you see early feedback on the quality of your code as it’s written. For Lifecycle to provide feedback to feature branches during development, CI must be configured to run a policy evaluation against these branches. We recommend that evaluations against the main branch use the ‘build’ stage in Lifecycle, and that feature branch evaluations are performed against the ‘develop’ stage. The ‘develop’ stage is intended for policy evaluation snapshots where changes to application dependencies and any associated policy violations are not tracked linearly. Because feature branches are volatile and vary across the features developed, using the ‘develop’ stage helps reduce noise by not showing these evaluations on the dashboard or your reports.

When deploying Lifecycle for SCM, you should authorize Lifecycle at the Root Organization level to communicate with your SCM tool (example: GitHub). Then, when you do any evaluation, we will look at the context in modern CI systems—meaning your Git repo gets cloned, then we run an evaluation in that directory, and we can get that information and see what was cloned. This lets us associate GitHub projects to applications in Lifecycle.

### Example Use Case: Automatic Pull Requests for npm

Using this example, you will be able to:

- Regularly scan an npm project for violations of your organization’s stated policy for the Software Supply Chain.
- Create GitHub pull requests and update project component dependencies to available versions that comply with organization policy.
- Automatically verify and integrate Lifecycle remediation suggestions in your Continuous Integration pipeline.

### Measuring Success

Success can be measured by a reduction in mean time to resolution (MTTR) which can be seen in our success metrics. Lifecycle for SCM provides the ability to prevent new violations from entering your main branch by informing development teams of risk as soon as they introduce it. We use automation to fix any violations as they occur by providing pull requests with the version change, and both of these practices should reduce MTTR.

If you’re ready to start using Lifecycle for SCM features, reach out to your customer success representative for guidance.
