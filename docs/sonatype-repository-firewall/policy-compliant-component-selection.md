---
layout: default
title: "Policy Compliant Component Selection"
parent: Sonatype Repository Firewall
nav_order: 8
---

# Policy Compliant Component Selection

The DevSecOps best practice for build reliability is to specify exact versions of open source dependencies in the build manifest. A common norm for some projects is to leave the dependency versions undefined or defined as a range of versions. When the latest version has violations blocked by Repository Firewall the npm client errors without a clear path forward.

Policy-compliant component selection filters requests to prevent clients from selecting versions that violate your policies. This feature runs automatically when components are requested from quarantine-enabled proxy repositories.

## Configuration for Nexus Repository 3 Pro

### Prerequisites

- IQ Server 167+ and Nexus Repository 3.61+ Pro
- Nexus Repository 3 Pro and Repository Firewall license configured with IQ Server
- Quarantine enabled on the npm and PyPi proxy repositories

### Enable Policy Compliant Component Selection

![fw-pccs-configuration.png]({{ "/assets/images/uuid-16d5cea7-f1e2-af79-6853-830e671ac1a9.png)

### Configure Cache Settings

The Policy Compliant Component Selection cache may be modified in Nexus Repository to one hour or less. Here's how to set the cache:

## Configuration for JFrog Artifactory

### Prerequisites

- Next-Gen Repository Firewall license
- Firewall for Artifactory plugin installed
- Quarantine enabled on the proxy repository in JFrog Artifactory npm proxy repositories supported Pypi proxy is not supported
- npm proxy repositories supported
- Pypi proxy is not supported

### Enable Policy Compliant Component Selection

In the *firewall.properties* configuration file for Firewall for JFrog Artifactory, add a line for each repository you want to enable Policy Compliant Component Selection:

```
firewall.repo.my-remote-repo=policyCompliantComponentSelection
```

### Configure Cache Settings

Performance for Policy Compliant Component Selection can be improved by reducing the [Metadata Retrieval Cache Period](https://www.jfrog.com/confluence/display/JFROG/Advanced+Settings) configuration setting in Artifactory to one hour or less.

## General Info
