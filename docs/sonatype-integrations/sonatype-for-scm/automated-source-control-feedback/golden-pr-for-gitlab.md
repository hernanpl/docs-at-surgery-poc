---
layout: default
title: "Golden PR for GitLab"
parent: Automated Source Control Feedback
nav_order: 6
---

# Golden PR for GitLab

Sonatype IQ Server creates a **comment** if it is able to determine a **Golden Version** of the component that can remediate the policy violation.

The **Golden Version** of the component is defined as *recommended-non-breaking-with-dependencies* .

Sonatype IQ Server creates a Golden **Pull Request (PR)** automatically, if it is able to determine a Golden Version of the component that can remediate the policy violation. Refer to example 3 below.

**Examples:**

1. A top-level **Golden PR comment** for a Golden Version of a component will be seen as below. The version upgrade information indicates that bumping to a version will resolve all policy violations for this component (including its dependencies) and result in no breaking changes.

![Top_level_GitLab_comment.png](/docs-at-surgery-poc/assets/images/uuid-e032029b-41b7-d4aa-4aec-55d08603b4e4.png)

2. A **Golden PR line comment** will be seen as below. The Golden Version of the component is indicated by a gold star.

![GitLab_Golden_line_comment.png]({{ /assets/images/uuid-39004e5a-f9bb-cb99-30f8-41d08d0e5879.png)

3. A **Golden PR** (indicated by a gold star,) will be created as below, indicating the suggested component version, i.e. Golden Version. This is a safe-to-use version with no breaking changes, no policy violations (including its dependencies) and can be used to remediate the policy violations.

![GitLab_Folden_PR.png]({{ "/assets/images/uuid-7f3874c6-1665-3627-a999-b7b6c521b487.png)
