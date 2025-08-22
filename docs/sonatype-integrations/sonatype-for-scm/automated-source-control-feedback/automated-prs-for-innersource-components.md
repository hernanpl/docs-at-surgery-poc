---
layout: default
title: "Automated PRs for InnerSource Components"
parent: Automated Source Control Feedback
nav_order: 3
---

# Automated PRs for InnerSource Components

This feature ensures that applications are always current with the latest compatible version of InnerSource components and benefit from the continuous improvements.

When a new non-major version of an InnerSource component is detected during evaluation of an application at the release stage, automated pull requests to update the older version of the InnerSource component are created in the SCM system.

**Note:** No Automated PRs for Policy Violations Automated PRs will not be created for policy violations related to InnerSource Components. They will only be created if a version change is detected.

## Prerequisites

The prerequisites for enabling automated PRs to update InnerSource components are:

- The *Automated InnerSource Updates* feature is enabled in Lifecycle.
- Lifecycle is correctly configured with your SCM system using the *Source Control* settings.

## When is an Automated PR for InnerSource Created

An automated PR to update an InnerSource component will be created when:

- A new version of an InnerSource component is detected at the release stage during evaluation of the application
- The new InnerSource version is **not** a major version upgrade
- The InnerSource component is being used as a direct dependency in the application

The detection of a new version of the InnerSource component will automatically create a PR in the configured SCM system, to update the older version of the component with the new version.

## Steps to Configure Automated PR for InnerSource Updates

- Click on Orgs and Policies in the left navigation bar.
- Select the root org or the organization or application for which you want to configure the automated PRs.
- Set *Automated InnerSource Updates* to **Enabled** .

## Sample of an Automated PR

The example below shows an automated PR for an InnerSource component created in GitHub.

The latest application evaluation detected a new version (0.8.5) of the InnerSource component `com.github.vandeseer:easytable` at the release stage. This automatically created a PR in GitHub to update the older version (0.6.6).

![AutoPr_for_InnerSource.jpg](/assets/images/uuid-76f54cc1-f9b5-9c66-bb4d-96feff9053b0.jpg)
