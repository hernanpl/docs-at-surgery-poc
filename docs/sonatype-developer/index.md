---
layout: default
title: "Sonatype Developer"
nav_order: 7
has_children: true
---

# Sonatype Developer

This release includes the following changes for Sonatype Developer:

## InnerSource Proactive Dependency Management

Sonatype Developer now supports proactive dependency management for InnerSource components through automated pull requests. When a new, compatible (non-major) version of an InnerSource component is detected during application evaluation at the release stage, Sonatype Lifecycle will automatically generate a pull request in your source control system to update the older version. Note that automated pull requests are only created for version updates and not for policy violations.

This feature helps teams stay current with the latest improvements to InnerSource libraries without manual tracking, reducing technical debt and improving development velocity.

To take advantage of this improvement, enable the *Automated InnerSource Updates* feature under *Orgs and Policies* as described in our [Automated PRs for InnerSource help documentation](#UUID-8ebdbbf8-503b-b36e-378e-4cc9725f216c) .
