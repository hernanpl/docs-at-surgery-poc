---
layout: default
title: "Automated Commit Feedback"
parent: Automated Source Control Feedback
nav_order: 1
---

# Automated Commit Feedback

Sonatype Lifecycle provides policy violation information in your Source Control Management System. This lets developers find out about policy violations during the code development process.

The Automated Commit Feedback feature is enabled by default for all repository types: private, internal, and public.

This feature is configurable at the organization or application level and can either be inherited (default), enabled (default for the root organization), or disabled.

## Managing Policy Evaluation Reports and SCM Commits

### Azure DevOps

In Azure DevOps, a build status can be attached to a commit when an IQ Policy Evaluation highlights violations. This is visible on individual commits, and the commit history.

![126654525.png](/docs-at-surgery-poc/assets/images/uuid-89051ca7-4ffa-36ed-3c37-8ea5afe3ee32.png)

### Bitbucket

In both Bitbucket Server and Bitbucket Cloud, a build status can be attached to commits when an IQ Policy Evaluation highlights violations. This will be visible on individual commits and on any pull requests containing that commit.

![126654526.png](/docs-at-surgery-poc/assets/images/uuid-92b3d7bd-f41d-98a3-0e9e-a307d61b95dd.png)

### GitHub

As a GitHub Status, an IQ Policy Evaluation check runs whenever a Pull Request is created or updated. Like other status checks, it can be configured to just provide feedback or even block a PR from being merged when it detects vulnerable components or policy violations. Each policy evaluation has a link to the full IQ Policy Evaluation via the **Details** link to the right of the components affected summary counts.

![126654530.png](/docs-at-surgery-poc/assets/images/uuid-dffa8e94-8ce9-3575-8add-3a66680bbe4e.png)

The IQ Policy Evaluation report can also be accessed from a commit itself by clicking the status icon then clicking the **Details** link to the right of the IQ Policy Evaluation component summary on the checks popup.

![126654527.png](/docs-at-surgery-poc/assets/images/uuid-256d116d-d124-f26c-871e-2055f3047b14.png)

### GitLab

An IQ Policy Evaluation step can be added to the GitLab pipeline to provide feedback or even block Merge Requests when it detects vulnerable components or policy violations. When violations are detected, the 'IQ Policy Evaluation' will link to the full scan report on IQ Server.

![126654529.png](/docs-at-surgery-poc/assets/images/uuid-8ad4a098-f76e-73ae-df54-14c73aefe521.png)

## Viewing the Full Policy Evaluation Report

Selecting the details link opens the Policy Evaluation report where the developer will see the current version used and other vulnerable and non-vulnerable versions of that component.

This gives developers the information they need to quickly remediate vulnerable components.
