---
layout: default
title: "Priorities REST API"
parent: REST APIs
nav_order: 1
---

# Priorities REST API

The [Prioritization Algorithm](#UUID-b67217ee-89df-c126-d2ec-6c478b339cb4) determines the priorities of remediation for policy evaluations. Use this REST API to retrieve the Priority Remediations or *Priorities* .

To export the *Priorities* , use the GET method for csv export.

**Methods Supported**

GET

## Retrieve Priorities in JSON format

You can retrieve the prioritized remediations (Priorities) by using the GET method.

**Permissions Required:** View IQ Elements

**Example:**

```
GET /api/v2/developer/priorities/app/3ab22aa306ca481b8823abde3890bdfa?page=1&pageSize=10&includeRemediation=true` 
```

You can retrieve the priorities by providing the application public Id, scanId of the evaluation, number of pages to retrieve, page size (containing number of priorities), and the includeRemedition flag.

Setting includeRemediationflag to `true` will return the remediationType and remediation version for the component.

*remediationType* includes *next no-violations* , *next-non-failing* , *next-no-violations-with-dependencies* , and *next-non-failing-with-dependencies* . Refer to [remediation output types](#UUID-7192ff3e-bf95-c3ee-63a3-47434f032517) for more information.

It may take longer for the request to execute, if retrieving remediationType and remediation version.

**Response:**

The response contains the Priorities for the scanId specified.

The response contains fields indicating the current waiver status and description. The new fields include: `hasExpiredWaiver` , `hasSoonToExpireWaiver` , `isAllViolationsWaived` , `waiverExpirationDetails` , `waivedViolationsCount` , and `hasAutoWaiver` .

```
{
  "priorities": {
    "total": 3,
    "page": 1,
    "pageSize": 10,
    "pageCount": 1,
    "results": [{
        "displayName": "django_make_app (py2.py3-none-any) 0.1.3 (.whl)",
        "componentIdentifier": {
          "format": "pypi",
          "coordinates": {
            "extension": "whl",
            "name": "django_make_app",
            "qualifier": "py2.py3-none-any",
            "version": "0.1.3"
          }
        },
        "componentHash": "14dbd4443110831ec9b2",
        "dependencyType": "Unknown",
        "hasFailActionOnComponent": false,
        "action": "none",
        "highestThreat": 10,
        "highestThreatPolicyName": "Security-Critical",
        "highestThreatPolicyConstraintName": "Critical risk CVSS score",
        "securityReachable": false,
        "priority": 1,
        "remediationType": null,
        "remediationVersion": null,
        "highestReachableThreat": 0,
        "remediationVersion": null,
        "hasExpiredWaiver": false,
        "hasSoonToExpireWaiver": true,
        "isAllViolationsWaived": true,
        "waiverExpirationDetails": “Applied waiver will expire in 3 days”,
        "waivedViolationsCount": 2,
        "hasAutoWaiver": true
      },{
        "displayName": "github.com/Masterminds/vcs v1.13.1",
        "componentIdentifier": {
          "format": "golang",
          "coordinates": {
            "name": "github.com/Masterminds/vcs",
            "version": "v1.13.1"
          }
        },
        "componentHash": "2eb681c8f541daec6ea6",
        "dependencyType": "Unknown",
        "hasFailActionOnComponent": false,
        "action": "none",
        "highestThreat": 10,
        "highestThreatPolicyName": "Security-Critical",
        "highestThreatPolicyConstraintName": "Critical risk CVSS score",
        "securityReachable": false,
        "priority": 2,
        "remediationType": "next-no-violations",
        "remediationVersion": "v1.13.2",
        "highestReachableThreat": 0
      }, {
        "displayName": "log4j : log4j : 1.2.8",
        "componentIdentifier": {
          "format": "maven",
          "coordinates": {
            "artifactId": "log4j",
            "classifier": "",
            "extension": "jar",
            "groupId": "log4j",
            "version": "1.2.8"
          }
        },
        "componentHash": "3640dd71069d7986c9a1",
        "dependencyType": "Direct",
        "hasFailActionOnComponent": false,
        "action": "none",
        "highestThreat": 10,
        "highestThreatPolicyName": "Security-Critical",
        "highestThreatPolicyConstraintName": "Critical risk CVSS score",
        "securityReachable": false,
        "priority": 3,
        "remediationType": null,
        "remediationVersion": null,
        "highestReachableThreat": 0,
        "hasExpiredWaiver": true,
        "hasSoonToExpireWaiver": false,
        "isAllViolationsWaived": false,
        "waiverExpirationDetails": null,
        "waivedViolationsCount": 0,
        "hasAutoWaiver": false
      }
    ]
  }
}

```

### Retrieve Priorities in csv format

Use the GET method as below to retrieve the priorities in a csv format, by providing the application public Id and the scanId for the evaluation.

The Priorities returned in this format do not include remediation type and version information.

The response contains fields indicating the current waiver status and description. It includes fields indicating the current waiver status and description. The new fields include: `hasExpiredWaiver` , `hasSoonToExpireWaiver` , `isAllViolationsWaived` , `waiverExpirationDetails` , `waivedViolationsCount` , and `hasAutoWaiver` .

**Example:**

```
GET /api/v2/developer/priorities/app/3ab22aa306ca481b8823abde3890bdfa/export
```

**Response:**

```
Display Name,Component Identifier,Component Hash,Dependency Type,Has Fail Action On Component,Action,Highest Threat,Highest Threat Policy Name,Highest Threat Policy Constraint Name,Security Reachable,Priority,Remediation Type,Remediation Version,Highest Reachable Threat,Has Expired Waiver,Has Soon To Expire Waiver,Is All Violations Waived,Waiver Expiration Details,Waived Violations Count,Has Auto Waiver
django_make_app (py2.py3-none-any) 0.1.3 (.whl),pypi: {extension=whl, name=django_make_app, qualifier=py2.py3-none-any, version=0.1.3},14dbd4443110831ec9b2,Unknown,false,none,10,Security-Critical,Critical risk CVSS score,false,1,,,0,false,false,false,,8,true
github.com/Masterminds/vcs v1.13.1,golang: {name=github.com/Masterminds/vcs, version=v1.13.1},2eb681c8f541daec6ea6,Unknown,false,none,10,Security-Critical,Critical risk CVSS score,false,2,,,0,false,true,true,Applied waiver will expire in 3 days,3,true
log4j : log4j : 1.2.8,maven: {artifactId=log4j, classifier=, extension=jar, groupId=log4j, version=1.2.8},3640dd71069d7986c9a1,Direct,false,none,10,Security-Critical,Critical risk CVSS score,false,3,,,0,false,false,false,,0,false
django_make_app 0.1.3 (.tar.gz),pypi: {extension=tar.gz, name=django_make_app, qualifier=, version=0.1.3},36fdc0aa5cd420286bfd,Unknown,false,none,10,Security-Critical,Critical risk CVSS score,false,4,,,0,false,false,false,,0,false
commons-collections : commons-collections : 3.1,maven: {artifactId=commons-collections, classifier=, extension=jar, groupId=commons-collections, version=3.1},40fb048097caeacdb11d,Transitive,false,none,10,Security-Critical,Critical risk CVSS score,false,5,,,0,false,false,false,,0,false
com.fasterxml.jackson.core : jackson-databind : 2.9.4,maven: {artifactId=jackson-databind, classifier=, extension=jar, groupId=com.fasterxml.jackson.core, version=2.9.4},498bbc3b94f566982c7f,Unknown,false,none,10,Security-Critical,Critical risk CVSS score,false,6,,,0,false,false,false,,0,false
org.yaml : snakeyaml : 1.29,maven: {artifactId=snakeyaml, classifier=, extension=jar, groupId=org.yaml, version=1.29},6d0cdafb2010f1297e57,Direct,false,none,10,Security-Critical,Critical risk CVSS score,false,7,,,0,false,false,false,,0,false
axis : axis : 1.2,maven: {artifactId=axis, classifier=, extension=jar, groupId=axis, version=1.2},892c772f7c486b3c09d2,Direct,false,none,10,Security-Critical,Critical risk CVSS score,false,8,,,0,false,false,false,,0,false
certifi (py2.py3-none-any) 2018.1.18 (.whl),pypi: {extension=whl, name=certifi, qualifier=py2.py3-none-any, version=2018.1.18},a98e852452156f0ebc8f,Unknown,false,none,10,Security-Critical,Critical risk CVSS score,false,9,,,0,false,false,false,,0,false
Django 1.6 (.tar.gz),pypi: {extension=tar.gz, name=Django, qualifier=, version=1.6},adf539ecb45bed3f1032,Unknown,false,none,10,Security-Critical,Critical risk CVSS score,false,10,,,0,false,false,false,,0,false
confire 0.2.0 (.tar.gz),pypi: {extension=tar.gz, name=confire, qualifier=, version=0.2.0},b19b9bf0c2249860ac9d,Unknown,false,none,10,Security-Critical,Critical risk CVSS score,false,11,,,0,false,false,false,,0,false
Django (py2.py3-none-any) 1.6 (.whl),pypi: {extension=whl, name=Django, qualifier=py2.py3-none-any, version=1.6},d045feb089e591346ad0,Unknown,false,none,10,Security-Critical,Critical risk CVSS score,false,12,,,0,false,false,false,,0,false
com.h2database : h2 : 1.4.196,maven: {artifactId=h2, classifier=, extension=jar, groupId=com.h2database, version=1.4.196},dd0034398d593aa3588c,Direct,false,none,10,Security-Critical,Critical risk CVSS score,false,13,,,0,false,false,false,,0,false

```

### Retrieve Priorities Having Fail/Warn Action

Use the *optionalActionFilter* query parameter to retrieve only those Priorities that have an associated fail or warn action.

**Example:**

When the value for *optionalActionFilter* is set to true, the response contains Priorities containing components with violations that cause a "fail" or "warn" notification/policy action.

```
curl -u admin:admin123 "http://localhost:8070/api/v2/developer/priorities/test/d7bb756b3fe74099b9fbd0c53741d90e?optionalActionFilter=true" 
```

**Response:**

When the value for *optionalActionFilter* is set to false, the response contains Priorities containing components with violations that **do not** cause a "fail" or "warn" notification/policy action.

The response contains Priorities in the descending order, paginated as specified in the request,

The response contains fields indicating the current waiver status and description. It includes fields indicating the current waiver status and description. The new fields include: `hasExpiredWaiver` , `hasSoonToExpireWaiver` , `isAllViolationsWaived` , `waiverExpirationDetails` , `waivedViolationsCount` , and `hasAutoWaiver` .

```
{
  "priorities": {
    "total": 36,
    "page": 1,
    "pageSize": 10,
    "pageCount": 4,
    "results": [{
        "displayName": "ch.qos.logback : logback-core : 1.2.0",
        "componentIdentifier": {
          "format": "maven",
          "coordinates": {
            "artifactId": "logback-core",
            "classifier": "",
            "extension": "jar",
            "groupId": "ch.qos.logback",
            "version": "1.2.0"
          }
        },
        "componentHash": "5a95c8addab9544177c7",
        "dependencyType": "Transitive",
        "hasFailActionOnComponent": false,
        "action": "none",
        "highestThreat": 9,
        "highestThreatPolicyName": "Security-High",
        "highestThreatPolicyConstraintName": "High risk CVSS score",
        "securityReachable": true,
        "priority": 1,
        "remediationType": null,
        "remediationVersion": null,
        "highestReachableThreat": 9,
        "hasExpiredWaiver": true,
        "hasSoonToExpireWaiver": false,
        "isAllViolationsWaived": false,
        "waiverExpirationDetails": "Applied waiver expired 2 days ago",
        "waivedViolationsCount": 0,
        "hasAutoWaiver": false
      }, {
        "displayName": "com.google.guava : guava : 29.0-jre",
        "componentIdentifier": {
          "format": "maven",
          "coordinates": {
            "artifactId": "guava",
            "classifier": "",
            "extension": "jar",
            "groupId": "com.google.guava",
            "version": "29.0-jre"
          }
        },
        "componentHash": "801142b4c3d0f0770dd2",
        "dependencyType": "Direct",
        "hasFailActionOnComponent": false,
        "action": "none",
        "highestThreat": 9,
        "highestThreatPolicyName": "Security-High",
        "highestThreatPolicyConstraintName": "High risk CVSS score",
        "securityReachable": false,
        "priority": 2,
        "remediationType": null,
        "remediationVersion": null,
        "highestReachableThreat": 0,
        "hasExpiredWaiver": false,
        "hasSoonToExpireWaiver": false,
        "isAllViolationsWaived": false,
        "waiverExpirationDetails": "",
        "waivedViolationsCount": 0,
        "hasAutoWaiver": false
      }, {
        "displayName": "com.xenoamess : nashorn : jdk8u265-b01-x1",
        "componentIdentifier": {
          "format": "maven",
          "coordinates": {
            "artifactId": "nashorn",
            "classifier": "",
            "extension": "jar",
            "groupId": "com.xenoamess",
            "version": "jdk8u265-b01-x1"
          }
        },
        "componentHash": "fbe08ca5288808c2d51b",
        "dependencyType": "Direct",
        "hasFailActionOnComponent": false,
        "action": "none",
        "highestThreat": 7,
        "highestThreatPolicyName": "Component-Similar",
        "highestThreatPolicyConstraintName": "Unknown modification to component",
        "securityReachable": false,
        "priority": 3,
        "remediationType": null,
        "remediationVersion": null,
        "highestReachableThreat": 0,
        "hasExpiredWaiver": false,
        "hasSoonToExpireWaiver": false,
        "isAllViolationsWaived": false,
        "waiverExpirationDetails": "",
        "waivedViolationsCount": 0,
        "hasAutoWaiver": false
      }, {
        "displayName": "cn.fossc.jdk : tools : 1.8",
        "componentIdentifier": {
          "format": "maven",
          "coordinates": {
            "artifactId": "tools",
            "classifier": "",
            "extension": "jar",
            "groupId": "cn.fossc.jdk",
            "version": "1.8"
          }
        },
        "componentHash": "4e7ab2a550a6f1e64f4a",
        "dependencyType": "Direct",
        "hasFailActionOnComponent": false,
        "action": "none",
        "highestThreat": 7,
        "highestThreatPolicyName": "Component-Similar",
        "highestThreatPolicyConstraintName": "Unknown modification to component",
        "securityReachable": false,
        "priority": 4,
        "remediationType": null,
        "remediationVersion": null,
        "highestReachableThreat": 0,
        "hasExpiredWaiver": false,
        "hasSoonToExpireWaiver": false,
        "isAllViolationsWaived": false,
        "waiverExpirationDetails": "",
        "waivedViolationsCount": 0,
        "hasAutoWaiver": false
      }, {
        "displayName": "cn.ponfee : jdk-dt : 1.8.0_371",
        "componentIdentifier": {
          "format": "maven",
          "coordinates": {
            "artifactId": "jdk-dt",
            "classifier": "",
            "extension": "jar",
            "groupId": "cn.ponfee",
            "version": "1.8.0_371"
          }
        },
        "componentHash": "845a71d1a430212104f7",
        "dependencyType": "Direct",
        "hasFailActionOnComponent": false,
        "action": "none",
        "highestThreat": 7,
        "highestThreatPolicyName": "Component-Similar",
        "highestThreatPolicyConstraintName": "Unknown modification to component",
        "securityReachable": false,
        "priority": 5,
        "remediationType": null,
        "remediationVersion": null,
        "highestReachableThreat": 0,
        "hasExpiredWaiver": false,
        "hasSoonToExpireWaiver": false,
        "isAllViolationsWaived": false,
        "waiverExpirationDetails": "",
        "waivedViolationsCount": 0,
        "hasAutoWaiver": false
      }, {
        "displayName": "io.github.svarzee : gpsoauth-java : 0.7.0",
        "componentIdentifier": {
          "format": "maven",
          "coordinates": {
            "artifactId": "gpsoauth-java",
            "classifier": "",
            "extension": "jar",
            "groupId": "io.github.svarzee",
            "version": "0.7.0"
          }
        },
        "componentHash": "95fe87433761cca9087b",
        "dependencyType": "Direct",
        "hasFailActionOnComponent": false,
        "action": "none",
        "highestThreat": 7,
        "highestThreatPolicyName": "Component-Similar",
        "highestThreatPolicyConstraintName": "Unknown modification to component",
        "securityReachable": false,
        "priority": 6,
        "remediationType": null,
        "remediationVersion": null,
        "highestReachableThreat": 0,
        "hasExpiredWaiver": false,
        "hasSoonToExpireWaiver": false,
        "isAllViolationsWaived": false,
        "waiverExpirationDetails": "",
        "waivedViolationsCount": 0,
        "hasAutoWaiver": false
      }, {
        "displayName": "insight-scanner-call-flow-analyzer-test.tar",
        "componentIdentifier": null,
        "componentHash": "8c6417f19294ca8b1463",
        "dependencyType": "Unknown",
        "hasFailActionOnComponent": false,
        "action": "none",
        "highestThreat": 2,
        "highestThreatPolicyName": "Component-Unknown",
        "highestThreatPolicyConstraintName": "Unknown 3rd party component",
        "securityReachable": false,
        "priority": 7,
        "remediationType": null,
        "remediationVersion": null,
        "highestReachableThreat": 0,
        "hasExpiredWaiver": false,
        "hasSoonToExpireWaiver": false,
        "isAllViolationsWaived": false,
        "waiverExpirationDetails": "",
        "waivedViolationsCount": 0,
        "hasAutoWaiver": false
      }, {
        "displayName": "layer.tar",
        "componentIdentifier": null,
        "componentHash": "313dfeb123ebec93f672",
        "dependencyType": "Unknown",
        "hasFailActionOnComponent": false,
        "action": "none",
        "highestThreat": 2,
        "highestThreatPolicyName": "Component-Unknown",
        "highestThreatPolicyConstraintName": "Unknown 3rd party component",
        "securityReachable": false,
        "priority": 8,
        "remediationType": null,
        "remediationVersion": null,
        "highestReachableThreat": 0,
        "hasExpiredWaiver": false,
        "hasSoonToExpireWaiver": false,
        "isAllViolationsWaived": false,
        "waiverExpirationDetails": "",
        "waivedViolationsCount": 0,
        "hasAutoWaiver": false
      }, {
        "displayName": "insight-scanner-call-flow-analyzer-test.jar",
        "componentIdentifier": null,
        "componentHash": "b89aa3dc164bcf005f17",
        "dependencyType": "Unknown",
        "hasFailActionOnComponent": false,
        "action": "none",
        "highestThreat": 2,
        "highestThreatPolicyName": "Component-Unknown",
        "highestThreatPolicyConstraintName": "Unknown 3rd party component",
        "securityReachable": false,
        "priority": 9,
        "remediationType": null,
        "remediationVersion": null,
        "highestReachableThreat": 0,
        "hasExpiredWaiver": false,
        "hasSoonToExpireWaiver": false,
        "isAllViolationsWaived": false,
        "waiverExpirationDetails": "",
        "waivedViolationsCount": 0,
        "hasAutoWaiver": false
      }, {
        "displayName": "layer.tar",
        "componentIdentifier": null,
        "componentHash": "e74d03c305441e8b1865",
        "dependencyType": "Unknown",
        "hasFailActionOnComponent": false,
        "action": "none",
        "highestThreat": 2,
        "highestThreatPolicyName": "Component-Unknown",
        "highestThreatPolicyConstraintName": "Unknown 3rd party component",
        "securityReachable": false,
        "priority": 10,
        "remediationType": null,
        "remediationVersion": null,
        "highestReachableThreat": 0,
        "hasExpiredWaiver": false,
        "hasSoonToExpireWaiver": false,
        "isAllViolationsWaived": false,
        "waiverExpirationDetails": "",
        "waivedViolationsCount": 0,
        "hasAutoWaiver": false
      }
    ]
  }
}

```
