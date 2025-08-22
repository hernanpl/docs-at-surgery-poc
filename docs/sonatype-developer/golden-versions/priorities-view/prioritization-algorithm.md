---
layout: default
title: "Prioritization Algorithm"
parent: Priorities View
nav_order: 1
---

# Prioritization Algorithm

The priority of remediation is determined by the Sonatype Prioritization Algorithm.

The Prioritization Algorithm is designed to analyze the following factors:

- Policy Actions (fail/warn/none)
- Reachability of the policy violation
- Threat level of the violation

The weight applied to each factor above depends upon the policy action (highest), reachability of the policy violation and the threat level associated with the violation.

## How Prioritization Algorithm Works

Review the [Policy Action](#UUID-2edc9f20-6766-eb4b-2a06-786cd5985f0c) and the stage in the your devOps cycle, that is designated to trigger when violations occur. Setting the policy action to *fail* ranks the violation higher than *warn* . Since the *build* stage is considered to be most crucial and optimized for addressing remediation issues, policy actions set to trigger at the build stage will be ranked higher than other stages.

The [Reachability](#UUID-bffb3d6e-1a0b-5607-518a-3dcdc88508c2) of the component determines the relevance of addressing the policy violation. If the vulnerable component is not found to be *reachable* , it will be ranked lower in priority. This ensures targeting remediation efforts towards vulnerabilities that are in the execution paths and exploitable.

The threat level associated with the policy violation reflects the actual threat level of vulnerability. Higher threat levels will be ranked higher in priority, to ensure quick remediation.
