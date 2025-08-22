---
layout: default
title: "Example Scan Result File"
parent: Sonatype IQ CLI
nav_order: 5
---

# Example Scan Result File

Using the `--result-file` parameter creates a file with evaluation results in the following format.

```
{
    "applicationId" : "...",
    "scanId" : "...",
    "reportHtmlUrl" : "http://...",
    "reportPdfUrl" : "http://.../pdf",
    "reportDataUrl" : "http://.../raw",
    "policyAction" : "None",
    "policyEvaluationResult" : {
        "alerts" : [...detailed list of components which caused the violation...],
        "affectedComponentCount" : 15,
        "criticalComponentCount" : 4,
        "severeComponentCount" : 65,
        "moderateComponentCount" : 36,
        "criticalPolicyViolationCount" : 4,
        "severePolicyViolationCount" : 85,
        "moderatePolicyViolationCount" : 46,
        "grandfatheredPolicyViolationCount" : 0,
        "legacyViolationCount" : 0
     }
}
```

**** - is the application in IQ Server against which you run policy evaluation

**** - can be used in some rest api

** - report with policy evaluation results in different formats

**** - policy evaluation outcome (can be None, Warn, Fail)

**** - contains a summary of the evaluation:

**** - contains information about components that caused a policy violation

**** - number of components that caused a policy violation

**** - number of critical components that caused a policy violation

**** - number of severe components that caused a policy violation

**** - the number of moderate components which caused a policy violation

**** - number of critical policies that were violated

**** - number of severe policies that were violated

**** - number of moderate policies that were violated

**** - number of policies that were violated, but moved to grandfathered

**** - number of legacy policy violations
