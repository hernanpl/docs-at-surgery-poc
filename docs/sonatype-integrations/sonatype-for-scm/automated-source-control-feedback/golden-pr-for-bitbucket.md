---
layout: default
title: "Golden PR for Bitbucket"
parent: Automated Source Control Feedback
nav_order: 8
---

# Golden PR for Bitbucket

Sonatype IQ Server creates a **comment** , if it is able to determine a Golden Version of the component that can remediate the policy violation.

The **Golden Version** of the component is defined as *recommended-non-breaking-with-dependencies* .

Sonatype IQ Server creates a Golden **Pull Request (PR)** automatically, if it is able to determine a Golden Version of the component that can remediate the policy violation. Refer to example 3 below.

**Examples:**

1. A top-level **Golden PR comment** for a Golden Version of a component will be seen as below. The version upgrade information indicates that bumping to a version will resolve all policy violations for this component (including its dependencies) and result in no breaking changes.

![BitBucket_Top_level_comment.png](/docs-at-surgery-poc/assets/images/uuid-2f862e52-29f3-c5a1-b6cb-7a355daeb306.png)

2. A **Golden PR line comment** will be seen as below. The Golden Version of the component is indicated by a gold star.

![BitBucket_line_comment.png](/docs-at-surgery-poc/assets/images/uuid-80246dbe-4138-bc29-a6c1-d36c10df4429.png)

3. A **Golden PR** (indicated by a gold star,) will be created as below, indicating the suggested component version, i.e. Golden Version. This is a safe-to-use version with no breaking changes, no policy violations (including its dependencies) and can be used to remediate the policy violations.

![Bitbucket_Golden_PR.png]({{ "/assets/images/uuid-4c1980db-cb40-c067-6611-2057ffb6492e.png)
