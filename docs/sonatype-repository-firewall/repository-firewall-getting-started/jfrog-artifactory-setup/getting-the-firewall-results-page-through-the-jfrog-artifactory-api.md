---
layout: default
title: "Getting the Firewall results page through the JFrog Artifactory API"
parent: JFrog Artifactory Setup
nav_order: 1
---

# Getting the Firewall results page through the JFrog Artifactory API

Every repository protected by Repository Firewall has a results page detailing all of the evaluations made as components are requested through the repository. You may find this URL by making the following call to the JFrog Artifactory server.

```
curl -u {username}:{password} https://{artifactory.example.com}/api/plugins/execute/firewallEvaluationSummary?params=repo={virtual-repo-name}
```

In the example above, substitute your: `username` , `password` , `JFrog Artifactory URL` , and `virtual-repository-name` .

This is an example of the response:

```
{
  "moderateComponentCount" : 0,
  "quarantinedComponentCount" : 0,
  "reportUrl" : "https://myiqserver:8070/ui/links/repository/0396e6d401d143399d53493e57c106e8/result"
  "severeComponentCount" : 0,
  "criticalComponentCount" : 0,
  "affectedComponentCount" : 0
}
```

The `reportUrl` may be opened in a browser. This directs you to the static policy report URL.

The property `firewall.iqRepositoryUrl` links to the same Repository Results URL and is unique to each repository.

IQ Repository URL property for a repository with Firewall enabled:

![120521688.png](/docs-at-surgery-poc/assets/images/uuid-fad235f0-0d82-459c-222d-0f20b953ee25.png)
