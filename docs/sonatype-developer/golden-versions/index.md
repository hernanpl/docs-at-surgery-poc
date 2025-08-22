---
layout: default
title: "Golden Versions"
parent: Sonatype Developer
nav_order: 4
has_children: true
---

# Golden Versions

## The Golden Version

Sonatype's Component Intelligence scores a component version as the **Golden Version** if it falls under the *recommended-non-breaking-with-dependencies* category of recommendation.

This is a safe-to-use version of the component (including its dependencies) with no resulting breaking changes, that can be used for upgrade to remediate the reported policy violation.

NOTE: The Golden Version recommendation is currently available for the Maven ecosystem only.

### Spotting the Golden Version

If Sonatype Component Intelligence finds a Golden Version for a component, the *Recommendation Column* in the Priorities View will show as "Non-breaking upgrade resolving issues for this component and its dependencies"

![Priorities_dashboard_Golden_version.png](/docs-at-surgery-poc/assets/images/uuid-3178bf1d-116a-0c0e-287d-ef23d7214162.png)

Click on the row, to view the Golden Version of the component on the [component details page](#UUID-c348055a-b083-a26c-6dda-b4cfda3cf2ef)

![Golden_ver_component_det.png]({{ /assets/images/uuid-7d2b2b9b-d673-18d1-f04d-db2a2268e0af.png)

## The Golden PR

Sonatype IQ Server plugins for Source Control Management (SCM) can create PRs (pull request) with comments to upgrade dependencies to the recommended Golden Version. These versions are upgrade suggestions that will not cause breaking changes, while remediating the policy violation.

Using Golden Version recommendations you can enhance the fix rate for version upgrades by simplifying

**Prerequisites to view Golden PRs in the SCM system**

- Your SCM environment has been integrated using one of the available Sonatype IQ Server plugins.
- Check the [Sonatype Developer](#UUID-1c5f818f-62e1-8585-4327-62eda2730f7b) dashboard to see if the application has been configured to use automatic SCM Feedback.
- [Automated Pull Requests](#UUID-a84bbc8f-37d5-1031-5835-04972587627f) is enabled for the SCM.

### Spotting Golden PRs Source Control Management Systems

The IQ Server plugins that currently support Golden PRs are:

- [GitHub](#UUID-a94a6186-60ae-10d6-2539-8e7433639d94)
- [GitLab](#UUID-d55598c3-ed13-f8fd-5918-a901d7b0cfdb)
- [Bitbucket](#UUID-0932385f-f121-b85b-4256-fc575259d294)
- [Azure DevOps](#UUID-5a94634b-a3bf-1085-371b-a0bf80e6f114)

## How is the Golden Version Different from Recommended Version?

The *Golden Version* of a component will remediate all policy violations on the current version of the component and its dependencies, without causing any breaking changes.

The recommended version of a component (seen as *Bumping to version xxx* in PR comments) will remediate policy violations on the current version of the component, without causing any breaking changes. It **may not** remediate policy violations for its dependencies.

When a Golden *Version* of a component is not available, the recommended version of the component can be used.
