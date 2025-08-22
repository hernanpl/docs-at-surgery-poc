---
layout: default
title: "Easy SCM Onboarding"
parent: Sonatype for SCM
nav_order: 2
has_children: true
---

# Easy SCM Onboarding

Easy SCM Onboarding is a tool whose primary purpose is to import the applications housed in your SCM system repositories and turn them into applications in Lifecycle. This integration enables *Sonatype Lifecycle* to scan and evaluate your organization's applications directly from the source control without modifying any code or continuous integration (CI) build processes.

Once your applications are set up in Lifecycle, Easy SCM Onboarding scans the applications via the [Instant Risk Profile](#UUID-9bc16c19-db96-b9f4-5f20-fb5b970d7075) to give you an immediate, baseline glimpse of your applications' risk. This enables rapid visibility into open-source risks for critical applications and helps your team prioritize remediation efforts. This is done without having to manually scan or add Lifecycle to your build process.

**Note:** It is important to understand that Easy SCM Onboarding is a useful, **initial** tool to help you get started with scanning and accelerate adoption; however, it is just that – *initial* . It **only initially scans what has been committed to your SCM system** (i.e. manifests) and, therefore, **does not provide a full analysis that comes from accessing the advanced binary fingerprinting** .

In fact, performing a full analysis produces noticeably different results for the same project. Therefore, we recommend that you strive toward integrating Lifecycle with your **continuous integration (CI)** and **command line interface (CLI)** **pipeline** for fine-grained scan control and binary analysis, which ensures the highest-quality scan results.

## Prerequisites

To use Easy SCM Onboarding, you'll need to do the following:

- Ensure your SCM system resources are adequate for the new applications.
- Obtain an access token for your SCM system to connect to your IQ organization. We recommend setting the token in the Root Organization.

## Automatically Assign Roles During Application Import

Easy SCM onboarding can also automatically assign roles to your GitHub users if you [configuring user mappings](#UUID-0af5b737-af38-5ec5-ea69-62d8211951d8_section-idm234646010084107) using the Source Control REST API before importing an application.

If user mappings for an organization in *Lifecycle* are available (assigned or inherited), Easy SCM onboarding will attempt to apply them to your GitHub users.

Note this feature currently only supports local and LDAP user accounts in IQ; you cannot use it with SAML or SSO-based IQ user accounts. It also only works with GitHub at this time.

## Using Easy SCM Onboarding

## Instant Risk Profile

Sonatype Lifecycle will scan the default branch for each application created through Easy SCM Onboarding. The results from that scan are your **Instant Risk Profile** . Your results depend on the files stored in your source control repository.

### SCM Scan Details:

Source Control Scans do the following:

- IQ Server performs a Git clone operation to access the files in your repository.
- The files that IQ Server uses several file types to generate results.
- Default branch scans use the 'Source' stage
- Scan/policy evaluation results are available on the Reporting page in the 'Source' stage column

### Instant Risk Profile Results

The Instant Risk Profile is a scan of your Source Control Repository. It is triggered when a Lifecycle Application is created through Easy SCM Onboarding. The purpose of this scan is to give you an overview of the risk and policy violations in your application.

During SCM Onboarding, all new applications without a source scan enter a queue. The Reports page will display a 'pending' indicator for applications that are waiting for their initial onboarding scan. When the scan completes the pending indicator is replaced by a summary of the scan and policy evaluation.

![126654567.png](/docs-at-surgery-poc/assets/images/uuid-13786424-53f9-6e39-f24e-88b07f945541.png)

**Note:** **No relevant files** A report will not be generated if the source control does not contain any relevant files to scan. The CLI tooling will produce a No violations" report.

### Reviewing Results

The scan report will be available on the .

### Next Steps

Lifecycle offers reporting tools in your source control system:

- [Continuous Risk Profile](#UUID-d8b61eb4-8130-3d47-c4c9-881bc5e152cc) - Lifecycle will scan the default branch on an ongoing basis and pull requests.
- [Pull Request Commenting](#UUID-f6241df2-2b87-c01a-2960-b2d8adf661b3) - Lifecycle will provide feedback directly in pull requests. New pull requests can trigger additional scans.

## Continuous Risk Profile

Sonatype for SCM generates a continuous risk profile of the organization's codebase by running automatic application evaluations at the source stage. It uses the following capabilities to create a continuous risk profile:

### Default Branch Monitoring

Default branch monitoring is implemented by running both periodic and event-driven application evaluations. This feature is enabled for all private, internal, and public repository types. The selected repository should be configured for source control as described in .

Periodic application evaluations: Nexus IQ for SCM performs policy evaluations on the default branch once per day. These evaluations are initiated based on the IQ server settings

```
defaultBranchMonitoringstartTime: 00:00
defaultBranchMonitoringIntervalHours:24
```

To change the start time or the time interval between evaluations, use

Event-driven application evaluations:Before performing event-driven application evaluations, Nexus IQ for SCM will check if *external policy evaluations* (run by Nexus CLI or CI jobs) have been performed. If there are no policy evaluations found in the last 7 days, then an application evaluation will be initiated when a PR is detected on the default branch **and** there is no policy evaluation associated with the head commit.

**Note:** If policy evaluations for a default branch have been set to initiate externally for example, via , then Default Branch Monitoring is disabled. The offers better control over the evaluation target (i.e. scan targets) and time. Default Branch Monitoring is automatically re-enabled, if there are no externally initiated policy evaluations in the source stage for the default branch in the last seven days.

### Feature Branch Monitoring

Nexus IQ for SCM periodically detects changes on feature branches that have pull requests, executes policy evaluations on the changed feature branches and updates pull request comments when policy violations are resolved or introduced.

**Note:** Feature branch monitoring only works on repositories that cannot be accessed publicly. Repositories must be private or internal for all supported providers, except GitHub Enterprise, for which all repositories will work.
