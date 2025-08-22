---
layout: default
title: "Automated Pull Requests in Go"
parent: Automated Pull Requests
nav_order: 1
---

# Automated Pull Requests in Go

## Go

Any `go.mod` file that exists in the repository will be searched for dependencies. Remediation PRs are created for the following scenarios:

- Required modules declared in single or block `require` directives
- Replaced modules declared in single or block `replace` directives, having a full version specified on the right side of the `replace` directive
