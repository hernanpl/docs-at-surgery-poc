---
layout: default
title: "Automated Source Control Feedback"
parent: Sonatype for SCM
nav_order: 3
has_children: true
---

# Automated Source Control Feedback

Sonatype Lifecycle provides policy violation information directly in your Source Control Management System. This lets developers find out about policy violations during the code development process.

The policy violation information includes policy evaluation summaries on new pull requests, comments on your pull requests, and opening new pull requests. Learn more about each feature below:

## Prerequisites

All features require the Lifecycle Application is [configured with an Access token and repository URL.](#UUID-161243f0-61ce-a164-d457-2bff696761b4)

The table below identifies where features can be enabled and disabled:

## Automated Commit Feedback

Sonatype Lifecycle provides policy violation information in your Source Control Management System. This lets developers find out about policy violations during the code development process.

The Automated Commit Feedback feature is enabled by default for all repository types: private, internal, and public.

This feature is configurable at the organization or application level and can either be inherited (default), enabled (default for the root organization), or disabled.

### Managing Policy Evaluation Reports and SCM Commits

### Viewing the Full Policy Evaluation Report

Selecting the details link opens the Policy Evaluation report where the developer will see the current version used and other vulnerable and non-vulnerable versions of that component.

This gives developers the information they need to quickly remediate vulnerable components.

## Automated Pull Requests

Sonatype Lifecycle can create new pull requests (PRs) to update dependencies to versions without policy violations. Whenever a scan of your SCM repository’s default branch finds a component with a policy violation that hasn't already been identified, and a newer version without the violation is available, Lifecycle will try to update the component to that newer version. This approach is the preferred way to remediate a policy violation. The pull request contains links to the full Lifecycle report that triggered it, as well as links to any security vulnerability details.

**Supported platforms** : Azure DevOps, Bitbucket Cloud, Bitbucket Server, GitHub, GitLab

**Supported ecosystems** : Maven, npm, Gradle, Go

### Prerequisites

To use Automatic Pull Requests:

Also, note that the repository URL is configured at the Application level, but the other attributes can be at the Application, Organization, or Root Organization level.

The following diagram illustrates the ways that the creation of an automated remediation pull request can be triggered.

![137203329.png](/assets/images/uuid-8c47bb70-6798-2330-8783-d19c4bca8e69.png)

### IQ Server Clone Directory Configuration

For each configured application, the repository will be cloned on the host that the IQ Server runs on. The default location is:

```
<sonatypeWork>/source-control
```

Note that the default for sonatypeWork is ./sonatype-work/clm-server.

To change the location of the repository clone for IQ Server Release 140 and later, use the .

For release 139 and earlier, use the config.yml

```
sourceControl:
  cloneDirectory: /your/path/here
```

Note that if the `cloneDirectory` does not have a leading "/", then the path will be relative to `<sonatypeWork>` .

### Understanding Automated Pull Requests

The Automated Pull Request functionality behaves in a specific, predictable way:

- The automated pull request workflow is triggered whenever your SCM repository's base branch is scanned.
- Automated Pull Requests only work on components. It does not find or fix other vulnerabilities in your code.
- Automated Pull Requests only bumps components to non-violating versions. It does not take any other remediation action. Review the pull requests and the linked Lifecycle report thoroughly to see other remediation options.
- A manifest file with component version information must be included in the repository. E.G. a pom.xml file
- The Automated Pull Request follows a hierarchy when selecting a new component version: If a version resolves violations for the target component *and* violations for that component's transitive dependencies, that version is used. Otherwise, a version that resolves all violations for the target component is used. If neither of the above is true, then no pull request is generated.
- If a version resolves violations for the target component *and* violations for that component's transitive dependencies, that version is used.
- Otherwise, a version that resolves all violations for the target component is used.
- If neither of the above is true, then no pull request is generated.
- Solving transitive dependencies alone is not currently supported. This means that no pull request is created when bumping versions would only remediate a violation in a transitive dependency.
- This means that no pull request is created when bumping versions would only remediate a violation in a transitive dependency.

**Note:** Component Versions Recommended by Automated PRs The Automated PR only bumps to component versions that are free from all violations. It will not bump to a version with fewer violations or less severe violations. The Automated PR will not recommend or bump to any pre-release versions of a component. For example, component versions like canary, ea, nightly, milestone, alpha, beta, pre, preview, dev, snapshot etc. will be excluded.

### Reading an Automated Pull Request

Pull requests generated by the Automated Pull Request feature look like the example below, and contain useful information that helps developers evaluate the pull request for appropriateness.

![126658069.png](/assets/images/uuid-30cd34ee-1666-89cd-c5ca-0cf24d85c921.png)

### Automated Pull Request Daily Activity

The Source Control Configuration Overview screen displays recent activity related to automated pull request creation.

![126654535.png](/assets/images/uuid-f7a96f0f-35f4-d64f-de37-bd9a27205e63.png)

Summary information for each attempt to create a pull request will be shown in a table. This information is purged on a daily rotating basis determined by when the server was last started, so at any time a maximum of 24 hours of results is shown.

The *Daily Automated Pull Requests* table displays the daily automated PR activity. Hover on the icons in the *Status* column for a description of the reasons indicating a successful/unsuccessful PR creation.

![Auto_PR_Daily_Activity.png](/assets/images/uuid-44df16ff-34b2-02d6-c1d7-222066e400cb.png)

The *Time Spent* shows the total time taken in milliseconds, to checkout, remediate, push, and create the PR.

The *Start Time* shows the timestamp and time zone when the process to create the automated PR was initiated.

### Breaking Changes

If a pull request bumps a component to a different version that is likely to break the application, the pull request will inform the developer of these breaking changes, as in the image below.

![example of a breaking changes notification in a pull request](/assets/images/uuid-2c1c87f5-0d82-c583-3c3a-548c04f5c2c4.png)

Breaking Changes alerts the developer that this remediation path will require some extra effort. For more information about the violation and other potential remediation paths or strategies, users can click View Full Report at the bottom of the Pull Request.

### Automated Pull Requests in Go

### Automated Pull Requests in Maven

Any `pom.xml` that exists in the repository will be searched. Any pom.xml that is in a `src/test` directory is ignored.

- Component defined inside a `<dependencies>` element with an inline `<version>` element.
- Component defined inside a `<dependencyManagement>` element with an inline `<version>` element.
- Component defined inside either an `<dependencies>` element, or a `<dependencyManagement>` element, with the version defined via a variable in a `<properties>` section.

### Automated Pull Requests in npm

### Automated Pull Requests with Gradle

## Automated PRs for InnerSource Components

This feature ensures that applications are always current with the latest compatible version of InnerSource components and benefit from the continuous improvements.

When a new non-major version of an InnerSource component is detected during evaluation of an application at the release stage, automated pull requests to update the older version of the InnerSource component are created in the SCM system.

**Note:** No Automated PRs for Policy Violations Automated PRs will not be created for policy violations related to InnerSource Components. They will only be created if a version change is detected.

### Prerequisites

The prerequisites for enabling automated PRs to update InnerSource components are:

- The *Automated InnerSource Updates* feature is enabled in Lifecycle.
- Lifecycle is correctly configured with your SCM system using the *Source Control* settings.

### When is an Automated PR for InnerSource Created

An automated PR to update an InnerSource component will be created when:

- A new version of an InnerSource component is detected at the release stage during evaluation of the application
- The new InnerSource version is **not** a major version upgrade
- The InnerSource component is being used as a direct dependency in the application

The detection of a new version of the InnerSource component will automatically create a PR in the configured SCM system, to update the older version of the component with the new version.

### Steps to Configure Automated PR for InnerSource Updates

- Click on Orgs and Policies in the left navigation bar.
- Select the root org or the organization or application for which you want to configure the automated PRs.
- Set *Automated InnerSource Updates* to **Enabled** .

### Sample of an Automated PR

The example below shows an automated PR for an InnerSource component created in GitHub.

The latest application evaluation detected a new version (0.8.5) of the InnerSource component `com.github.vandeseer:easytable` at the release stage. This automatically created a PR in GitHub to update the older version (0.6.6).

![AutoPr_for_InnerSource.jpg](/assets/images/uuid-76f54cc1-f9b5-9c66-bb4d-96feff9053b0.jpg)

## Pull Request Commenting

**Note:** This page uses the phrase "Pull Request," but in GitLab, the terminology is "Merge Request."

Lifecycle can add comments to pull requests in repositories configured for source control if the pull request introduces a new policy violation. This is accomplished by comparing the policy evaluation report of the pull request's source branch with:

- the latest policy evaluation report for the common ancestor commit between the pull request's source and target branches, if such a report exists, or
- the latest policy evaluation report for the pull request's base commit, which is the head commit of the pull request's target branch at the moment the pull request was created, if such a report exists, or
- the latest available policy evaluation report for the source control configured default branch.

**Note:** The PR comment reports Threat Level Low, Medium, and High (2-10) and excludes the Informational level (0 and 1) to keep development focus on policy violations that require most attention.

There are several ways that pull request comments can be triggered:

- In direct response to a policy evaluation.
- Via a polling mechanism when a pull request is created after the policy evaluation occurs.
- When a new commit is detected on the pull request feature branch (pull request monitoring).

The diagram below illustrates a branch-on-branch scenario to explain the full selection process of selecting the commits used to find the evaluation reports. However, pull requests are often for a feature branch stemming from the default branch.

![137200606.png](/assets/images/uuid-965f19c2-98dd-69d2-c90e-5c4c2796df83.png)

### Prerequisites

### PR Summary Comment

IQ Server supports two approaches to PR commenting:

- Base comments on customer-initiated policy evaluations via their CI system or other automation processes. This is the preferred approach and allows the customer to specify exactly what they want to be evaluated, including build artifacts, and they want them evaluated.
- In cases where the customer has not set up CI/automation yet on a given repository, IQ Server will still detect pull requests and, noticing that these CI-initiated policy evaluations are not occurring, will initiate evaluations based on the contents of the repository. This will produce the necessary policy evaluations on which to base comments.

The diagram below illustrates these approaches to PR commenting in more detail. Please note the use of IQ Server stages.

![137200607.png](/assets/images/uuid-bc1b3e29-0772-6010-1577-7488e5fdff83.png)

The PR summary comment contains the summary of policy violations, affected components, and a description of the policy violations that were introduced by the PR. Suggested remediation for policy violations is included when available.

The and icons that can be seen next to the affected components are used to indicate whether a component is a direct or transitive dependency of the project. For Bitbucket, these are shown as text instead of icons.

If PR line comments are created (more details in the next section), links are added to the associated components for convenience. See an example below (for GitHub):

![PR_Summary.png](/assets/images/uuid-41774c22-e8d6-9d51-ddf7-b19091256d82.png)

The policy violation details are collapsed by default for GitHub and GitLab. Developers can expand them as needed. For Bitbucket the policy violation details are fully expanded, by default.

There is also a section for fixed policy violations if the PR fixes preexisting policy violations.

PR comments are generated when:

- Policy evaluation reports are run against new commits for an open PR and new policy violations have been detected or existing policy violations have been fixed
- Newly detected PRs satisfy the prerequisites for PR commenting

The PR comment is designed to appear on the PR within a few moments after either of these conditions are satisfied.

Nexus IQ for SCM will update existing PR comments with the latest available information if a new policy evaluation is run against the head commit for the PR.

**Note:** The pull request (PR) comment only reports policy violations introduced or fixed by the specific PR. These policy violations are determined by comparing two policy evaluation reports as described above in the Overview section. Note that the Summary and Application Report shown in the status check section includes all policy violations present in the latest policy evaluation for a given **commit** .

### PR Line Comments

An attempt is made to create a line comment for each change that introduces new policy violations. That is not always possible due to the fact that line comments can be only created on lines available in the pull request's file diff. Additionally, sometimes there are multiple potential locations to comment on for a particular component. In those cases, the most relevant location is chosen for each component in order to keep the number of line comments to a minimum.

Identifying changes that introduce policy violations is ecosystem-specific. Currently, the PR line commenting feature is enabled for direct dependencies in Maven, Gradle, NPM, and Go projects. The strategy used to identify the location for the line comments is similar to the one used by the Automated Pull Request feature for version bumping.

Similar to the PR summary comment, PR line comments contain the affected component, the summary, and the description of the policy violations that were introduced by the change at the line of code to which the comment is attached. A component version that would remediate all policy violations is also included, if available. The policy violation details are expanded by default. An example is shown below (for GitHub):

![126654548.png](/assets/images/uuid-79e3ef34-e8f0-2635-22e0-5778702fe151.png)

### Breaking Changes

Breaking changes information will inform the developer about the amount of work required to perform the version upgrade whenever suggested remediations for policy violations are included.

In the screenshot below the line starting with a red square and "Multiple breaking changes" was added to the PR comment, based on the breaking changes information available for the suggested remediation.

![126658993.png](/assets/images/uuid-fd66a5f3-cb20-a6dc-a133-d84ee9e68a02.png)

### Transitive Solver

**Note:** If you experience challenges with seeing Transitive Solver recommendations, please refer to this [Knowledgebase article](https://support.sonatype.com/hc/en-us/articles/5932871948691-Remediation-recommendations-don-t-load-consistently) .

Remediations that fix policy violations for the target component and its dependencies are preferred, if available, over remediations that fix policy violations for just the target component.

In the example shown below, upgrading to the suggested remediation will fix all policy violations for 'jackson-databind' and its dependencies:

![126654540.png](/assets/images/uuid-45d19b67-65a7-0b11-5a57-a9e1184d60a2.png)

### Running Policy Evaluations on Different Branches

We recommend that policy evaluations against the default branch use the ‘build' stage in the Sonatype Lifecycle and that all other branches' evaluations are performed against the ‘develop’ stage. The ‘develop’ stage is intended for policy evaluation snapshots, where changes to application dependencies and any associated policy violations are not tracked linearly. Because feature/development branches are volatile and vary across the features developed, using the ‘develop’ stage helps reduce noise by not showing these evaluations on the dashboard or your reports.

Enabling policy evaluations on feature branches will also increase the amount of disk space consumed by stored application composition reports. Sonatype IQ Server can be configured to automatically purge outdated reports.

Please review the actions in the Sonatype Lifecycle policy configuration if the feature branch policy evaluation is configured to use the 'develop' stage. By default, using the 'develop' stage will not result in a 'fail' action for any of the defined policies. Status checks and the associated branch protection only report failure if the policy evaluation triggers a 'fail' action.

## Golden PR for GitHub

Sonatype IQ Server creates a **Pull Request (PR) comment** , if it is able to determine a Golden Version of the component that can remediate the policy violation.

The **Golden Version** of the component is defined as *recommended-non-breaking-with-dependencies* .

Sonatype IQ Server creates a Golden **Pull Request (PR)** automatically, if it is able to determine a Golden Version of the component that can remediate the policy violation. Refer to example 3 below.

**Examples:**

1. A top-level **Golden PR comment** for a Golden Version of a component will be seen as below. The version upgrade information indicates that bumping to a version will resolve all policy violations for this component (including its dependencies) and result in no breaking changes.

![Top_level_Github_comment.png](/assets/images/uuid-5ed70928-43ce-e902-6441-cfdab32ae287.png)

2. A **Golden PR line comment** will be seen as below. The Golden Version of the component is indicated by a gold star.

![Line_comment_golden.png](/assets/images/uuid-64295316-facb-d828-f09d-4b9056fd480a.png)

3. A **Golden PR** (indicated by a gold star,) will be created as below, indicating the suggested component version, i.e. Golden Version. This is a safe-to-use version with no breaking changes, no policy violations (including its dependencies) and can be used to remediate the policy violations.

![Github_Golden_PR.png](/assets/images/uuid-df8b0d0d-6b32-e3fd-871f-780df9cad923.png)

## Golden PR for GitLab

Sonatype IQ Server creates a **comment** if it is able to determine a **Golden Version** of the component that can remediate the policy violation.

The **Golden Version** of the component is defined as *recommended-non-breaking-with-dependencies* .

Sonatype IQ Server creates a Golden **Pull Request (PR)** automatically, if it is able to determine a Golden Version of the component that can remediate the policy violation. Refer to example 3 below.

**Examples:**

1. A top-level **Golden PR comment** for a Golden Version of a component will be seen as below. The version upgrade information indicates that bumping to a version will resolve all policy violations for this component (including its dependencies) and result in no breaking changes.

![Top_level_GitLab_comment.png](/assets/images/uuid-e032029b-41b7-d4aa-4aec-55d08603b4e4.png)

2. A **Golden PR line comment** will be seen as below. The Golden Version of the component is indicated by a gold star.

![GitLab_Golden_line_comment.png](/assets/images/uuid-39004e5a-f9bb-cb99-30f8-41d08d0e5879.png)

3. A **Golden PR** (indicated by a gold star,) will be created as below, indicating the suggested component version, i.e. Golden Version. This is a safe-to-use version with no breaking changes, no policy violations (including its dependencies) and can be used to remediate the policy violations.

![GitLab_Folden_PR.png](/assets/images/uuid-7f3874c6-1665-3627-a999-b7b6c521b487.png)

## Golden PR for Azure DevOps

Sonatype IQ Server creates a **Pull Request (PR) comment** , if it is able to determine a Golden Version of the component that can remediate the policy violation.

The **Golden Version** of the component is defined as *recommended-non-breaking-with-dependencies* .

Sonatype IQ Server creates a Golden **Pull Request (PR)** automatically, if it is able to determine a Golden Version of the component that can remediate the policy violation. Refer to example 3 below.

**Examples:**

1. A top-level **Golden PR comment** for a Golden Version of a component will be seen as below. The version upgrade information indicates that bumping to a version will resolve all policy violations for this component (including its dependencies) and result in no breaking changes.

![Azure_top_level_comment.png](/assets/images/uuid-8a483b90-55f8-5123-9416-46360878892e.png)

2. A **Golden PR line comment** will be seen as below. The Golden Version of the component is indicated by a gold star.

![Azure_line_comment.png](/assets/images/uuid-8793d199-dee3-415c-3482-5eccae4f62c7.png)

3. A **Golden PR** (indicated by a gold star,) will be created as below, indicating the suggested component version, i.e. Golden Version. This is a safe-to-use version with no breaking changes, no policy violations (including its dependencies) and can be used to remediate the policy violations.

![Azure_Golden_PR.png](/assets/images/uuid-df0a7ae4-9d99-ce1e-0659-907acf1d6e36.png)

## Golden PR for Bitbucket

Sonatype IQ Server creates a **comment** , if it is able to determine a Golden Version of the component that can remediate the policy violation.

The **Golden Version** of the component is defined as *recommended-non-breaking-with-dependencies* .

Sonatype IQ Server creates a Golden **Pull Request (PR)** automatically, if it is able to determine a Golden Version of the component that can remediate the policy violation. Refer to example 3 below.

**Examples:**

1. A top-level **Golden PR comment** for a Golden Version of a component will be seen as below. The version upgrade information indicates that bumping to a version will resolve all policy violations for this component (including its dependencies) and result in no breaking changes.

![BitBucket_Top_level_comment.png](/assets/images/uuid-2f862e52-29f3-c5a1-b6cb-7a355daeb306.png)

2. A **Golden PR line comment** will be seen as below. The Golden Version of the component is indicated by a gold star.

![BitBucket_line_comment.png](/assets/images/uuid-80246dbe-4138-bc29-a6c1-d36c10df4429.png)

3. A **Golden PR** (indicated by a gold star,) will be created as below, indicating the suggested component version, i.e. Golden Version. This is a safe-to-use version with no breaking changes, no policy violations (including its dependencies) and can be used to remediate the policy violations.

![Bitbucket_Golden_PR.png](/assets/images/uuid-4c1980db-cb40-c067-6611-2057ffb6492e.png)
