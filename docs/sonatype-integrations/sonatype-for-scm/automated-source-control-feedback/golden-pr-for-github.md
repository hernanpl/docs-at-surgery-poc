---
layout: default
title: "Golden PR for GitHub"
parent: Automated Source Control Feedback
nav_order: 5
---

# Golden PR for GitHub

Sonatype IQ Server creates a **Pull Request (PR) comment** , if it is able to determine a Golden Version of the component that can remediate the policy violation.

The **Golden Version** of the component is defined as *recommended-non-breaking-with-dependencies* .

Sonatype IQ Server creates a Golden **Pull Request (PR)** automatically, if it is able to determine a Golden Version of the component that can remediate the policy violation. Refer to example 3 below.

**Examples:**

1. A top-level **Golden PR comment** for a Golden Version of a component will be seen as below. The version upgrade information indicates that bumping to a version will resolve all policy violations for this component (including its dependencies) and result in no breaking changes.

![Top_level_Github_comment.png](/docs-at-surgery-poc/assets/images/uuid-5ed70928-43ce-e902-6441-cfdab32ae287.png)

2. A **Golden PR line comment** will be seen as below. The Golden Version of the component is indicated by a gold star.

![Line_comment_golden.png](/docs-at-surgery-poc/assets/images/uuid-64295316-facb-d828-f09d-4b9056fd480a.png)

3. A **Golden PR** (indicated by a gold star,) will be created as below, indicating the suggested component version, i.e. Golden Version. This is a safe-to-use version with no breaking changes, no policy violations (including its dependencies) and can be used to remediate the policy violations.

![Github_Golden_PR.png]({{ "/assets/images/uuid-df8b0d0d-6b32-e3fd-871f-780df9cad923.png)
