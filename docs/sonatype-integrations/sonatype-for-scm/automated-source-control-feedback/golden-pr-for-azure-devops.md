---
layout: default
title: "Golden PR for Azure DevOps"
parent: Automated Source Control Feedback
nav_order: 7
---

# Golden PR for Azure DevOps

Sonatype IQ Server creates a **Pull Request (PR) comment** , if it is able to determine a Golden Version of the component that can remediate the policy violation.

The **Golden Version** of the component is defined as *recommended-non-breaking-with-dependencies* .

Sonatype IQ Server creates a Golden **Pull Request (PR)** automatically, if it is able to determine a Golden Version of the component that can remediate the policy violation. Refer to example 3 below.

**Examples:**

1. A top-level **Golden PR comment** for a Golden Version of a component will be seen as below. The version upgrade information indicates that bumping to a version will resolve all policy violations for this component (including its dependencies) and result in no breaking changes.

![Azure_top_level_comment.png](/docs-at-surgery-poc/assets/images/uuid-8a483b90-55f8-5123-9416-46360878892e.png)

2. A **Golden PR line comment** will be seen as below. The Golden Version of the component is indicated by a gold star.

![Azure_line_comment.png](/docs-at-surgery-poc/assets/images/uuid-8793d199-dee3-415c-3482-5eccae4f62c7.png)

3. A **Golden PR** (indicated by a gold star,) will be created as below, indicating the suggested component version, i.e. Golden Version. This is a safe-to-use version with no breaking changes, no policy violations (including its dependencies) and can be used to remediate the policy violations.

![Azure_Golden_PR.png]({{ "/assets/images/uuid-df0a7ae4-9d99-ce1e-0659-907acf1d6e36.png)
