---
layout: default
title: "Policy Evaluation with Nexus IQ for SCM"
parent: Sonatype for SCM
nav_order: 4
---

# Policy Evaluation with Nexus IQ for SCM

Assuming you have properly associated IQ Server with your SCM system repository, IQ Server will first look to see if there is a commit hash. If there is, it will add a commit status within the SCM system repository. It will then look to see if there is an existing feature branch in your SCM system repository and, if so, see whether there is at least one pull request for it. If there is such a pull request, it will then determine whether there are any new or resolved policy violations and either create or update pull request comments (or pull request line comments) within your SCM system. If there are new violations to remediate, IQ Server will create a remediation pull request and send it to your SCM system.

![137200131.png](/assets/images/uuid-0578939f-e083-c3f4-e845-bd6efecead7f.png)
