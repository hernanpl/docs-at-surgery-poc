---
layout: default
title: "Automated Pull Requests in Maven"
parent: Automated Pull Requests
nav_order: 2
---

# Automated Pull Requests in Maven

Any `pom.xml` that exists in the repository will be searched. Any pom.xml that is in a `src/test` directory is ignored.

- Component defined inside a `<dependencies>` element with an inline `<version>` element.
- Component defined inside a `<dependencyManagement>` element with an inline `<version>` element.
- Component defined inside either an `<dependencies>` element, or a `<dependencyManagement>` element, with the version defined via a variable in a `<properties>` section.
